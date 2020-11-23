$(document).ready(function () {
    $('#id_table').DataTable({
        "language": {
            "lengthMenu": " _MENU_ ",
            "zeroRecords": "Nothing found - sorry",
            "info": " ",
            "infoEmpty": "Não há dados",
            "infoFiltered": "(filtered from _MAX_ total records)"
        }
    });
  });