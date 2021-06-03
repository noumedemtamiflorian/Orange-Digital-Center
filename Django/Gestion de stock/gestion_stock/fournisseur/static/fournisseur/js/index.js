$(document).ready(function () {
    $('#myTable').DataTable();
    $("table").click(function () {
        $.ajax({
            url: 'http://127.0.0.1:8000/fournisseur/3'
        }).then((res) => {
            console.log(res.response);
            console.log(res.response['id']);
            // $("tbody").append(`
            // <tr>
            // 	<td> ${res.response['id']}	</td>
            // 	<td> ${res.response['email']}	</td>
            // 	<td> ${res.response['name']}	</td>
            // 	<td> ${res.response['addresse']}	</td>
            // 	<td> ${res.response['addresse']}	</td>
            // </tr>

            // `)
        });
    });
});

