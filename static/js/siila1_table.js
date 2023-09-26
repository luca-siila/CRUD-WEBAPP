$(document).ready(function () {
    // Display the modal to the user
    const modal = document.getElementById("filterModal");
    modal.style.display = "block";

    // Add event listener for the modal's "Apply Filters" button
    document.getElementById("applyFiltersBtn").addEventListener("click", function() {
        const propertyType = document.getElementById("propertyType").value;
        const marketName = document.getElementById("marketName").value;

        // Close the modal
        modal.style.display = "none";

        // Fetch data and initialize the table
        fetchDataAndInitTable(propertyType, marketName);
    });
});

function fetchDataAndInitTable(propertyType, marketName) {
    const ajaxURL = `/get_siila1_data?propertyType=${propertyType}&marketName=${marketName}`;

    $.get(ajaxURL, function(data) {
        initTable(data, ajaxURL);
    });
}

function initTable(data, ajaxURL) {
    var table = new Tabulator("#history-table", {
        ajaxURL: ajaxURL,
        layout:"fitDataStretch",
        responsiveLayout:"hide",
        tooltips:true,
        addRowPos:"top",
        history:true,
        pagination:"local",
        paginationSize:25,
        paginationSizeSelector:[25, 50, 100, 200],
        movableColumns:true,
        resizableRows:true,
        initialSort:[
            {column:"SIILA1_ID", dir:"desc"},
        ],
        columns:[
            {title:"SIILA1_ID", field:"SIILA1_ID", editor:false},
            {title:"PROPERTY_TYPE", field:"PROPERTY_TYPE", editor:"select", editorParams:{values:["Industrial", "Escritório"]}},
            {title:"SIILA1_NAME", field:"SIILA1_NAME", editor:"input"},
            {title:"CLASS", field:"CLASS", editor:"select", editorParams:{values:["C", "C+", "B-", "B", "B+", "A-", "A", "A+"]}},
            {title:"REGION_NAME", field:"REGION_NAME", editor:"select", editorParams:{
                values:true,
                ajaxURL:"/get_region_names",
                ajaxResponse:function(url, params, response){
                    return response.region_names;
                }
            }},
            {title:"MARKET_NAME", field:"MARKET_NAME", editor:false},
        ],
        cellEdited:function(cell){
            var columnName = cell.getColumn().getField();
            var tableId = cell.getRow().getData().SIILA1_ID;
            var newValue = cell.getValue();

            $.post('/update_siila1_table', {  // Updated endpoint name
                column_name: columnName,
                table_id: tableId,
                new_value: newValue
            }, function(data) {
                if (!data.success) {
                    alert('Update failed: ' + data.message);
                    cell.setValue(cell.getOldValue());
                }
            });
        },
        rowMouseEnter:function(e, row){
            row.getElement().style.backgroundColor = "#D3961C";
        },
        rowMouseLeave:function(e, row){
            row.getElement().style.backgroundColor = "";
        },
    });

    table.setData(data);

    document.getElementById("search").addEventListener("input", function(e){
        table.setFilter([
            [
                {field:"SIILA1_ID", type:"like", value:e.target.value},
                {field:"PROPERTY_TYPE", type:"like", value:e.target.value},
                {field:"SIILA1_NAME", type:"like", value:e.target.value},
                {field:"CLASS", type:"like", value:e.target.value},
                {field:"REGION_NAME", type:"like", value:e.target.value},
                {field:"MARKET_NAME", type:"like", value:e.target.value},
            ]
        ]);
    });
}

function toggleMenu() {
    var menuBar = document.getElementById("menu-bar");
    var menuToggle = document.getElementById("menu-toggle");

    if (menuBar.style.width == "0px" || menuBar.style.width == "") {
        menuBar.style.width = "200px";
        menuToggle.innerHTML = "&#8592;";
        $(".content").css("margin-left", "260px");
    } else {
        menuBar.style.width = "0";
        menuToggle.innerHTML = "&#8594;";
        $(".content").css("margin-left", "60px");
    }
}
