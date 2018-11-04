function changeVisibility(lecture_tuple) {
    if (lecture_tuple.getAttribute('data-series') === 'true' && lecture_tuple.getAttribute('data-opening_department') === 'true') {
        lecture_tuple.classList.add('d-flex');
        lecture_tuple.classList.remove('d-none');
    } else {
        lecture_tuple.classList.add('d-none');
        lecture_tuple.classList.remove('d-flex');
    }
}

function checkboxListener(_id, data_type) {
    var rows = document.getElementsByClassName(_id);

    var value = (document.getElementById(_id).checked) ? 'true' : 'false';
    for (var row of rows) {
        row.setAttribute(data_type, value);
        changeVisibility(row);
    }
}

function changeAllCheckboxes(className, bool_value) {
    var checkboxes = document.getElementsByName(className);

    for (var checkbox of checkboxes) {
        checkbox.checked = bool_value;
    }
    var rows = document.getElementById('tbody-lecture').getElementsByTagName('tr');

    var data_value = (bool_value) ? 'true' : 'false';
    var data_type = 'data-' + className;
    for (var row of rows) {
        row.setAttribute(data_type, data_value);
        changeVisibility(row);
    }
}
