$(document).ready(function () {
    var table = new Tabulator("#prices-table", { // Change ID to match the prices table
        ajaxURL:"/get_prices_data", // Update the URL to fetch prices data
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
            {column:"SIILA1_NAME", dir:"desc"}, // Sort by SIILA1_NAME
        ],
        columns:[
            {title:"SIILA1_NAME", field:"SIILA1_NAME", editor:false},
            {title:"PERIOD", field:"PERIOD", editor:false},
            {title:"PRICE", field:"PRICE", editor:"input"},
            {title:"PRICE_BOMA", field:"PRICE_BOMA", editor:"input"},
            {title:"PRICE_TEXT", field:"PRICE_TEXT", editor:"input"},
            {title:"COND", field:"COND", editor:"input"},
            {title:"COND_BOMA", field:"COND_BOMA", editor:"input"},
            {title:"COND_TEXT", field:"COND_TEXT", editor:"input"},
            {title:"TAX", field:"TAX", editor:"input"},
            {title:"TAX_BOMA", field:"TAX_BOMA", editor:"input"},
            {title:"TAX_TEXT", field:"TAX_TEXT", editor:"input"},
        ],
		cellEdited:function(cell){
			var columnName = cell.getColumn().getField();
			var tableId = cell.getRow().getData().ID_PRICE; // Use ID_PRICE
			var newValue = cell.getValue();

			$.post('/update_prices_table', {
				column_name: columnName,
				table_id: tableId, // Send ID_PRICE as table_id
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
        table.setData("/get_prices_data"); // Update the URL to fetch prices data again
    }, 1000);

    document.getElementById("search").addEventListener("input", function(e){
        table.setFilter([
            [
                {field:"SIILA1_NAME", type:"like", value:e.target.value},
                {field:"PERIOD", type:"like", value:e.target.value},
                {field:"PRICE", type:"like", value:e.target.value},
                {field:"PRICE_TEXT", type:"like", value:e.target.value},
                {field:"COND", type:"like", value:e.target.value},
                {field:"COND_TEXT", type:"like", value:e.target.value},
                {field:"TAX", type:"like", value:e.target.value},
                {field:"TAX_TEXT", type:"like", value:e.target.value},
            ]
        ]);
    });
});

// Toggle menu function remains the same
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
