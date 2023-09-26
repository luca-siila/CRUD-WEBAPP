$(document).ready(function () {
    var table = new Tabulator("#contact-table", { // Change ID to match the contact table
        ajaxURL:"/get_contact_data", // Update the URL to fetch contact data
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
            {column:"CONTACT_ID", dir:"desc"}, // Sort by CONTACT_ID
        ],
        columns:[
            {title:"CONTACT_ID", field:"CONTACT_ID", editor:false},
            {title:"CONTACT_NAME", field:"CONTACT_NAME", editor:"input"}, // Editable input for CONTACT_NAME
            {title:"CONTACT_EMAIL", field:"CONTACT_EMAIL", editor:"input"}, // Editable input for CONTACT_EMAIL
            {title:"CONTACT_PHONE", field:"CONTACT_PHONE", editor:"input"}, // Editable input for CONTACT_PHONE
        ],
        cellEdited:function(cell){
            var columnName = cell.getColumn().getField();
            var tableId = cell.getRow().getData().CONTACT_ID; // Use CONTACT_ID
            var newValue = cell.getValue();

            $.post('/update_contact_table', { // Update URL to match contact table update route
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
        table.setData("/get_contact_data"); // Update the URL to fetch contact data again
    }, 1000);

    document.getElementById("search").addEventListener("input", function(e){
        table.setFilter([
            [
                {field:"CONTACT_ID", type:"like", value:e.target.value},
                {field:"CONTACT_NAME", type:"like", value:e.target.value},
                {field:"CONTACT_EMAIL", type:"like", value:e.target.value},
                {field:"CONTACT_PHONE", type:"like", value:e.target.value},
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
