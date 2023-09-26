
var historyTable;

// Column Definitions
var columns = [
    {title:"SIILA1 ID", field:"SIILA1_ID"},
    {title:"SIILA1 NAME", field:"SIILA1_NAME"},
    {title:"SIILA2 NAME", field:"SIILA2_NAME"},
    {title:"SIILA3 NAME", field:"SIILA3_NAME"},
    {title:"REGION NAME", field:"REGION_NAME"},
    {title:"PERIOD", field:"PERIOD"},
    {
        title:"OWNER NAME", 
        field:"OWNER_NAME",
        formatter:"link",
        formatterParams:{
            labelField:"OWNER_NAME", 
            url:"#", 
            target:"_self"
        },
        cellClick:function(e, cell) {
            e.preventDefault();  
            e.stopPropagation();
            showPopup("cadastre_table", "ID_OWNER", cell.getRow().getData().ID_UNIQUE);
        }
    },
    {
        title:"OWNER GROUP", 
        field:"OWNER_GROUP",
        formatter:"link",
        formatterParams:{
            labelField:"OWNER_GROUP",
            url:"#", 
            target:"_self"
        },
        cellClick:function(e, cell) {
            e.preventDefault();  
            e.stopPropagation();
            showPopup("cadastre_table", "ID_OWNER", cell.getRow().getData().ID_UNIQUE);
        }
    },
    {
        title:"CONTACT NAME", 
        field:"CONTACT_NAME",
        formatter:"link",
        formatterParams:{
            labelField:"CONTACT_NAME",
            url:"#", 
            target:"_self"
        },
        cellClick:function(e, cell) {
            e.preventDefault();  
            e.stopPropagation();
            showPopup("contact_table", "ID_CONT_OWNER", cell.getRow().getData().ID_UNIQUE);
        }
    },
    {
        title:"CONTACT PHONE", 
        field:"CONTACT_PHONE",
        formatter:"link",
        formatterParams:{
            labelField:"CONTACT_PHONE",
            url:"#", 
            target:"_self"
        },
        cellClick:function(e, cell) {
            e.preventDefault();  
            e.stopPropagation();
            showPopup("contact_table", "ID_CONT_OWNER", cell.getRow().getData().ID_UNIQUE);
        }
    },
    {
        title:"CONTACT MAIL", 
        field:"CONTACT_EMAIL",
        formatter:"link",
        formatterParams:{
            labelField:"CONTACT_EMAIL",
            url:"#", 
            target:"_self"
        },
        cellClick:function(e, cell) {
            e.preventDefault();  
            e.stopPropagation();
            showPopup("contact_table", "ID_CONT_OWNER", cell.getRow().getData().ID_UNIQUE);
        }
    }
];

function showPopup(tableType, columnName, historyId) {
    $.get(`/get_data_from_table?table=${tableType}`, function(data) {
        var tableHtml = "<table>";
        
        // Table headers
        tableHtml += "<tr>";
        for (const key in data[0]) {
            tableHtml += `<th>${key.replace('_', ' ')}</th>`;
        }
        tableHtml += "</tr>";
        
        // Table data
        data.forEach(function(row, index) {
            tableHtml += "<tr data-row-index='" + index + "'>";
            for (const key in row) {
                tableHtml += `<td>${row[key]}</td>`;
            }
            tableHtml += "</tr>";
        });
        tableHtml += "</table>";
        
        // Populate the modal's content and show the modal
        document.querySelector('.modal-body').innerHTML = tableHtml;
        var modal = document.getElementById('dataModal');
        modal.setAttribute('data-table-type', tableType); 
        modal.setAttribute('data-history-id', historyId);        
        modal.style.display = 'block';
        
        // Add click event to each row to highlight it when clicked
        document.querySelectorAll('.modal-body tr').forEach(function(row) {
            row.addEventListener('click', function() {
                document.querySelectorAll('.modal-body tr.selected').forEach(function(selectedRow) {
                    selectedRow.classList.remove('selected');
                });
                
                row.classList.add('selected');
                
                var rowIndex = row.getAttribute('data-row-index');
                var selectedRowId = data[rowIndex]['CADASTRE_ID'] || data[rowIndex]['CONTACT_ID'];
                if (!selectedRowId) {
                    console.error("Error: Unexpected row data structure. Neither CADASTRE_ID nor CONTACT_ID found.");
                    return;
                }
                document.querySelector('.modal-footer .modal-button').setAttribute('data-selected-id', selectedRowId);
            });
        });
    });
}

function searchTable(query) {
    if (query) {
        historyTable.setFilter([
            [
                {field:"SIILA1_NAME", type:"like", value:query},
                {field:"SIILA2_NAME", type:"like", value:query},
                {field:"SIILA3_NAME", type:"like", value:query},
                {field:"REGION_NAME", type:"like", value:query},
                {field:"OWNER_NAME", type:"like", value:query},
                {field:"OWNER_GROUP", type:"like", value:query},
                {field:"CONTACT_NAME", type:"like", value:query},
                {field:"CONTACT_PHONE", type:"like", value:query},
                {field:"CONTACT_EMAIL", type:"like", value:query}
            ]
        ]);
    } else {
        historyTable.clearFilter();
    }
}

$(document).ready(function() {
    // Load filters from localStorage (if they exist)
    currentPropertyType = localStorage.getItem('currentPropertyType');
    currentMarketName = localStorage.getItem('currentMarketName');

    console.log('Retrieved Filters:', {
        propertyType: currentPropertyType,
        marketName: currentMarketName
    });

    // If filters are not set, show the modal
    if (!currentPropertyType || !currentMarketName) {
        document.getElementById('filterModal').style.display = 'block';
    }
    initTable();
});

function initTable() {
    var ajaxURL = "/get_history_data";
    historyTable = new Tabulator("#history-table", {
        ajaxURL: ajaxURL,
        columns: columns,
        pagination: "local",
        paginationSize: 50,
        paginationSizeSelector: [25, 50, 100, 200],
        layout: "fitColumns",
        responsiveLayout: "collapse",
    });
}

function applyFilters() {
    currentPropertyType = document.getElementById('propertyType').value;
    currentMarketName = document.getElementById('marketName').value;

    // Save the filters to localStorage
    localStorage.setItem('currentPropertyType', currentPropertyType);
    localStorage.setItem('currentMarketName', currentMarketName);

    // Log the values to ensure they're set correctly
    console.log('Set Filters:', {
        propertyType: localStorage.getItem('currentPropertyType'),
        marketName: localStorage.getItem('currentMarketName')
    });

    // Hide the modal
    document.getElementById('filterModal').style.display = 'none';

    // Fetch data using the selected filters
    refreshTableData(currentPropertyType, currentMarketName);
}

function refreshTableData(propertyType, marketName) {
    console.log('Using Filters:', {
        propertyType: propertyType,
        marketName: marketName
    });

    // If filters are not set, show the modal
    if (!propertyType || !marketName) {
        document.getElementById('filterModal').style.display = 'block';
    } else {
        const ajaxURL = `/get_history_data?propertyType=${propertyType}&marketName=${marketName}`;
        historyTable.setData(ajaxURL);
    }
}

function handleModalSelection() {
    var selectedId = document.querySelector('.modal-footer .modal-button').getAttribute('data-selected-id');
    if (!selectedId || selectedId === 'undefined') {
        alert("Please select a valid entry.");
        return;
    }
    updateOriginalTable(selectedId);
}

function filterTable() {
    var input, filter, table, tr, td, i, j, visible;
    input = document.getElementById("tableSearch");
    filter = input.value.toUpperCase();
    table = document.querySelector(".modal-body table");
    tr = table.getElementsByTagName("tr");

    if (input.value.length < 3) {
        for (i = 1; i < tr.length; i++) {
            tr[i].style.display = "";
        }
        return;
    }

    for (i = 1; i < tr.length; i++) {
        visible = false;
        td = tr[i].getElementsByTagName("td");
        for (j = 0; j < td.length; j++) {
            if (td[j]) {
                if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
                    visible = true;
                } 
            }
        }
        if (visible === true) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
    }
}

function updateOriginalTable(selectedId) {
    if (!selectedId || selectedId === 'undefined') {
        console.error("Invalid selectedId:", selectedId);
        return;
    }

    var modal = document.getElementById('dataModal');
    var tableType = modal.getAttribute('data-table-type');
    var historyId = modal.getAttribute('data-history-id'); 

    var data = {
        tableType: tableType,
        selectedId: selectedId,
        ID_UNIQUE: historyId
    };

    $.post('/update_original_table', data, function(response) {
        if (response.success) {
            console.log("Update successful");
            modal.style.display = 'none';
        } else {
            console.error("Update failed:", response.message);
        }
    });
}

document.querySelector('.modal-footer .modal-button').addEventListener('click', function() {
    var selectedId = this.getAttribute('data-selected-id');
    if (!selectedId || selectedId === 'undefined') {
        alert("Please select a valid entry.");
        return;
    }
    updateOriginalTable(selectedId);
});
