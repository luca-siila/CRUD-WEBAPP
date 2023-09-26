$(document).ready(function () {
    var table = new Tabulator("#siila3-table", {
        ajaxURL:"/get_siila3_data",
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
            {column:"SIILA3_ID", dir:"desc"},
        ],
        columns:[
            {title:"SIILA3_ID", field:"SIILA3_ID", editor:false},
            {title:"SIILA1_NAME", field:"SIILA1_NAME", editor:false},
            {title:"SIILA2_NAME", field:"SIILA2_NAME", editor:false},
            {title:"SIILA3_NAME", field:"SIILA3_NAME", editor:"input"},
            {title:"STATUS", field:"STATUS", editor:false},
            {title:"DELIVERY_DATE", field:"DELIVERY_DATE", editor:"input"},
            {title:"AREA_BOMA", field:"AREA_BOMA", editor:"input"},
            {title:"AREA", field:"AREA", editor:"input"},
            {title:"REGISTRY", field:"REGISTRY", editor:"input"},
            {title:"MODULE_EFFICIENCY", field:"MODULE_EFFICIENCY", editor:"input"},
            {title:"DOCKS_MODULE", field:"DOCKS_MODULE", editor:"input"},
        ],
        cellEdited:function(cell){
            var columnName = cell.getColumn().getField();
            var tableId = cell.getRow().getData().SIILA3_ID;
            var newValue = cell.getValue();

            $.post('/update_siila3_table', {
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
        table.setData("/get_siila3_data");
    }, 1000);

    document.getElementById("search").addEventListener("input", function(e){
        table.setFilter([
            [
                {field:"SIILA3_ID", type:"like", value:e.target.value},
                {field:"SIILA1_NAME", type:"like", value:e.target.value},
                {field:"SIILA2_NAME", type:"like", value:e.target.value},
                {field:"SIILA3_NAME", type:"like", value:e.target.value},
                {field:"STATUS", type:"like", value:e.target.value},
                {field:"DELIVERY_DATE", type:"like", value:e.target.value},
                {field:"AREA_BOMA", type:"like", value:e.target.value},
                {field:"AREA", type:"like", value:e.target.value},
                {field:"REGISTRY", type:"like", value:e.target.value},
                {field:"MODULE_EFFICIENCY", type:"like", value:e.target.value},
                {field:"DOCKS_MODULE", type:"like", value:e.target.value},
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
