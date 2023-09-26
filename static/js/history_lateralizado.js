// Declare the table variable at the top of your JS file
var table;

// AJAX call to fetch cadastre names
var cadastreNames = [];
$.get('/get_cadastre_names', function(data) {
    cadastreNames = data;
});

	// Initialize the Tabulator table
	$(document).ready(function () {
		console.log("Initializing Tabulator..."); 
		table = new Tabulator("#history-lateralizado-table", {
			layout: "fitData",  // Columns will resize to fit the data
			ajaxURL: "/get_history_lateralizado_data",
			ajaxResponse: function(url, params, response) {
				return response.data;
			},
			responsiveLayout: false,  // Hide columns that don't fit
			tooltips:true,  // Enable tooltips
			addRowPos:"top",  // Add new rows at the top
			history:true,  // Enable undo/redo history
			pagination:"local",  // Enable local pagination
			paginationSize:25,  // Rows per page
			paginationSizeSelector:[25, 50, 100, 200],  // Rows per page selector
			movableColumns:true,  // Enable column reordering
			resizableRows:true,  // Enable row resizing
			virtualDomHoz: false,  // Disable horizontal virtual DOM
			initialSort:[
				{column:"SIILA3_ID", dir:"desc"},
			],
			columns: [
				{title:"SIILA3 ID", field:"SIILA3_ID", frozen: false},
				{title:"Market", field:"MARKET_NAME", frozen: false},
				{title:"Property Type", field:"PROPERTY_TYPE", frozen: false},
				{title:"SiiLA ID", field:"SIILA1_ID", frozen: false},
				{title:"NOME", field:"SIILA1_NAME", frozen: false},
				{title:"REGIÃO SiiLA", field:"REGION_NAME", frozen: false},
				{title:"CLASSE", field:"CLASS", frozen: false},
				{title:"DATA DE ENTREGA", field:"DELIVERY_DATE", frozen: false},
				{title:"STATUS", field:"STATUS", frozen: false},
				{title:"ANDAR", field:"SIILA2_NAME", frozen: false},
				{title:"CONJUNTO", field:"SIILA3_NAME", frozen: false},
				{title:"AREA CONJ./ANDAR", field:"AREA", frozen: false},
				{
					title: "201504", field: "201504",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201601", field: "201601",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201602", field: "201602",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201604", field: "201604",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201701", field: "201701",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201702", field: "201702",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201703", field: "201703",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201704", field: "201704",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201801", field: "201801",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201802", field: "201802",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201803", field: "201803",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201804", field: "201804",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201901", field: "201901",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201902", field: "201902",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201903", field: "201903",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "201904", field: "201904",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202001", field: "202001",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202002", field: "202002",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202003", field: "202003",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202004", field: "202004",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202101", field: "202101",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202102", field: "202102",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202103", field: "202103",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202104", field: "202104",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202201", field: "202201",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202202", field: "202202",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202203", field: "202203",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202204", field: "202204",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202301", field: "202301",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202302", field: "202302",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},
				{
					title: "202303", field: "202303",
					editor: "autocomplete",
					editorParams: {
						allowEmpty: true,
						showListOnEmpty: true,
						values: cadastreNames
					}
				},

				{title:"Industry", field:"202303_INDUSTRY_NAME"},
				{title:"Registry", field:"REGISTRY"},
				{
					title:"Tenant Contact",
					field:"202303_CONTACT_NAME",
					cellClick: function (e, cell) {
						showPopup(cell.getRow().getData().SIILA3_ID, cell.getColumn().getDefinition().field);
					}
				},
				{
					title:"Tenant Contact Phone",
					field:"202303_CONTACT_PHONE",
					cellClick: function (e, cell) {
						showPopup(cell.getRow().getData().SIILA3_ID, cell.getColumn().getDefinition().field);
					}
				},
				{
					title:"Tenant Contact Email",
					field:"202303_CONTACT_EMAIL",
					cellClick: function (e, cell) {
						showPopup(cell.getRow().getData().SIILA3_ID, cell.getColumn().getDefinition().field);
					}
				},
				{title:"DELIVERY PERIOD", field:"DELIVERY_PERIOD"},
			],
			cellEdited:function(cell) {
				// Get the new and old values
				var newValue = cell.getValue();
				var oldValue = cell.getOldValue();

				// Get the row and column data
				var row = cell.getRow().getData();
				var column = cell.getColumn().getDefinition();

				// Calculate the ID_UNIQUE
				var ID_UNIQUE;
				if (column.field === 'ID_CONT_TENANT') {
					ID_UNIQUE = row.SIILA3_ID + "_202303";
				} else {
					ID_UNIQUE = row.SIILA3_ID + "_" + column.field;
				}

				// Send an AJAX POST request to update the database
				$.post("/update_history_lateralizado_table", {
					tablename: "history_lateralizado",
					tableid: ID_UNIQUE,
					columnname: column.field,
					newvalue: newValue,
					oldvalue: oldValue
				}, function (data, status) {
					if (status !== 'success' || data.status !== 'success') {
						cell.setValue(oldValue);
					}
				});
			},
		});

		table.redraw(true);
		document.getElementById("history-lateralizado-table").scrollLeft = 500; 
		document.getElementById("search").addEventListener("input", function(e){
			table.setFilter([
				{field:"SIILA3_ID", type:"like", value:e.target.value},
				{field:"MARKET_NAME", type:"like", value:e.target.value},
				{field:"PROPERTY_TYPE", type:"like", value:e.target.value},
				{field:"SiiLA_ID", type:"like", value:e.target.value},
				{field:"SIILA1_NAME", type:"like", value:e.target.value},
				{field:"REGION_NAME", type:"like", value:e.target.value},
				{field:"CLASSE", type:"like", value:e.target.value},
				{field:"DELIVERY_DATE", type:"like", value:e.target.value},
				{field:"STATUS", type:"like", value:e.target.value},
				{field:"SIILA2_NAME", type:"like", value:e.target.value},
				{field:"SIILA3_NAME", type:"like", value:e.target.value},
				{field:"AREA", type:"like", value:e.target.value},
				{field:"201504", type:"like", value:e.target.value},
				{field:"201601", type:"like", value:e.target.value},
				{field:"201602", type:"like", value:e.target.value},
				{field:"201603", type:"like", value:e.target.value},
				{field:"201604", type:"like", value:e.target.value},
				{field:"201701", type:"like", value:e.target.value},
				{field:"201702", type:"like", value:e.target.value},
				{field:"201703", type:"like", value:e.target.value},
				{field:"201704", type:"like", value:e.target.value},
				{field:"201801", type:"like", value:e.target.value},
				{field:"201802", type:"like", value:e.target.value},
				{field:"201803", type:"like", value:e.target.value},
				{field:"201804", type:"like", value:e.target.value},
				{field:"201901", type:"like", value:e.target.value},
				{field:"201902", type:"like", value:e.target.value},
				{field:"201903", type:"like", value:e.target.value},
				{field:"201904", type:"like", value:e.target.value},
				{field:"202001", type:"like", value:e.target.value},
				{field:"202002", type:"like", value:e.target.value},
				{field:"202003", type:"like", value:e.target.value},
				{field:"202004", type:"like", value:e.target.value},
				{field:"202101", type:"like", value:e.target.value},
				{field:"202102", type:"like", value:e.target.value},
				{field:"202103", type:"like", value:e.target.value},
				{field:"202104", type:"like", value:e.target.value},
				{field:"202201", type:"like", value:e.target.value},
				{field:"202202", type:"like", value:e.target.value},
				{field:"202203", type:"like", value:e.target.value},
				{field:"202204", type:"like", value:e.target.value},
				{field:"202301", type:"like", value:e.target.value},
				{field:"202302", type:"like", value:e.target.value},
				{field:"202303", type:"like", value:e.target.value},
				{field:"202303_INDUSTRY_NAME", type:"like", value:e.target.value},
				{field:"Registry", type:"like", value:e.target.value},
				{field:"202303_CONTACT_NAME", type:"like", value:e.target.value},
				{field:"202303_CONTACT_PHONE", type:"like", value:e.target.value},
				{field:"202303_CONTACT_EMAIL", type:"like", value:e.target.value},
				{field:"DELIVERY_PERIOD", type:"like", value:e.target.value},
			]);
		});
	});


	function showPopup(historyId, columnName) {
		$.get(`/get_data_from_table?table=contact_table`, function(data) {
			// Clear the existing table
			document.querySelector(".modal-body table").innerHTML = "";

			// Create a new table row for each data row
			data.forEach(function (row) {
				var tr = document.createElement("tr");

				// Create a new table cell for each column in the row
				for (var column in row) {
					var td = document.createElement("td");
					td.textContent = row[column];
					tr.appendChild(td);
				}

				// Add a click event listener to each row
				tr.addEventListener("click", function () {
					// Set the selectedId attribute of the modal selection button
					document.querySelector('.modal-footer .modal-button').setAttribute('data-selected-id', row.contact_id);

					// Set the historyId and columnName attributes of the modal
					document.getElementById('dataModal').setAttribute('data-history-id', historyId);
					document.getElementById('dataModal').setAttribute('data-column-name', columnName);
				});

				// Add the row to the table
				document.querySelector(".modal-body table").appendChild(tr);
			});

			// Display the modal
			document.getElementById('dataModal').style.display = 'block';
		});
	}

	function handleModalSelection() {
		var selectedId = document.querySelector('.modal-footer .modal-button').getAttribute('data-selected-id');
		var historyId = document.getElementById('dataModal').getAttribute('data-history-id');
		var columnName = document.getElementById('dataModal').getAttribute('data-column-name');
		if (!selectedId || selectedId === 'undefined') {
			alert("Please select a valid entry.");
			return;
		}

		var ID_UNIQUE = historyId + "_" + columnName;

		updateOriginalTable(ID_UNIQUE, selectedId);
	}

	function updateOriginalTable(ID_UNIQUE, selectedId) {
		var data = {
			tablename: "history_lateralizado",
			tableid: ID_UNIQUE,
			columnname: "ID_CONT_TENANT",
			newvalue: selectedId
		};

		$.post('/update_history_lateralizado_table', data, function(response) {
			if (response.status === 'success') {
				console.log("Update successful");
				document.getElementById('dataModal').style.display = 'none';
			} else {
				console.error("Update failed:", response.message);
			}
		});
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

	document.querySelector('.modal-footer .modal-button').addEventListener('click', function() {
		var selectedId = this.getAttribute('data-selected-id');
		if (!selectedId || selectedId === 'undefined') {
			alert("Please select a valid entry.");
			return;
		}
		updateOriginalTable(selectedId);
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

	function closeDataModal() {
		document.getElementById('dataModal').style.display = 'none';
	}


	function updateFrozenColumns() {
		// Get all checked checkboxes
		const checkedBoxes = $("#freezeColumnOptions input[type='checkbox']:checked");
		const columnsToFreeze = [];
	
		// Loop through each checked checkbox and add its value to the columnsToFreeze array
		checkedBoxes.each(function() {
			columnsToFreeze.push($(this).val());
		});
	
		// Update the frozen columns in your table
		table.updateConfig({
			columns: table.getColumns().map(col => {
				if (columnsToFreeze.includes(col.getField())) {
					col.update({frozen: true});
				} else {
					col.update({frozen: false});
				}
				return col;
			})
		});
	}
	

$('#updateFrozenColumns').click(updateFrozenColumns);