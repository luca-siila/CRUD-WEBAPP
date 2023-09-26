$(document).ready(function () {
    var table = new Tabulator("#cadastre-table", {
        ajaxURL:"/get_cadastre_data",
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
            {column:"CADASTRE_ID", dir:"desc"},
        ],
        columns:[
            {title:"CADASTRE_ID", field:"CADASTRE_ID", editor:false},
            {title:"CADASTRE_NAME", field:"CADASTRE_NAME", editor:"input"},
            {title:"CAD_GROUP", field:"CAD_GROUP", editor:"input"},
            {title:"INDUSTRY_NAME", field:"INDUSTRY_NAME", editor:"select", editorParams:{
                values:true,
                ajaxURL:"/get_industry_names",
                ajaxResponse:function(url, params, response){
                    return response.industry_names;
                }
            }},
        ],
        cellEdited:function(cell){
            var columnName = cell.getColumn().getField();
            var tableId = cell.getRow().getData().CADASTRE_ID;
            var newValue = cell.getValue();

            $.post('/update_cadastre_table', {
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
        table.setData("/get_cadastre_data");
    }, 1000);

    document.getElementById("search").addEventListener("input", function(e){
        table.setFilter([
            [
                {field:"CADASTRE_ID", type:"like", value:e.target.value},
                {field:"CADASTRE_NAME", type:"like", value:e.target.value},
                {field:"CAD_GROUP", type:"like", value:e.target.value},
                {field:"INDUSTRY_NAME", type:"like", value:e.target.value},
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
