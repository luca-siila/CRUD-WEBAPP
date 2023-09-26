$(document).ready(function () {
    var table = new Tabulator("#siila2-table", { // Change 1: Updated the table ID to "siila2-table"
        ajaxURL:"/get_siila2_data", // Change 2: Updated the URL to fetch siila2_data
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
            {column:"SIILA2_ID", dir:"desc"}, // Change 3: Updated the sorting column to "SIILA2_ID"
        ],
        columns:[
            {title:"SIILA2_ID", field:"SIILA2_ID", editor:false}, // Change 4: Updated column definition for siila2_table
            {title:"SIILA1_NAME", field:"SIILA1_NAME", editor:false}, // Change 5: Added SIILA1_NAME (read-only)
            {title:"SIILA2_NAME", field:"SIILA2_NAME", editor:"input"}, // Change 6: Added SIILA2_NAME (editable)
        ],
        cellEdited:function(cell){
            var columnName = cell.getColumn().getField();
            var tableId = cell.getRow().getData().SIILA2_ID; // Change 7: Updated to SIILA2_ID
            var newValue = cell.getValue();

            $.post('/update_siila2_table', { // Change 8: Updated the URL for updating siila2_table
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

    setTimeout(function(){
        table.setData("/get_siila2_data"); // Change 9: Updated the URL to fetch siila2_data again
    }, 1000);

    document.getElementById("search").addEventListener("input", function(e){
        table.setFilter([
            [
                {field:"SIILA2_ID", type:"like", value:e.target.value}, // Change 10: Updated to filter SIILA2_ID
                {field:"SIILA1_NAME", type:"like", value:e.target.value}, // Change 11: Added filter for SIILA1_NAME
                {field:"SIILA2_NAME", type:"like", value:e.target.value}, // Change 12: Added filter for SIILA2_NAME
            ]
        ]);
    });
});

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
