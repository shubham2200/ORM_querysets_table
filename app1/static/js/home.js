
$(document).on('click', function () {
    var select = $('#level').val();
    dropdown = { select: select }
    console.log(select)
    // $('#tbody').emty();
    $('#tbody').empty();
    $.ajax({
        url: "/show_data/",
        method: "POST",
        data: dropdown,
        success: function (data) {
            console.log(data)
            if(data.status){

                var all = data.status
                console.log(all)
                for (i in all) {
                    console.log(all[i])
                    console.log(i)
                    output = `<tr>
                    <td> ${all[i].id}  </td>
                    <td> ${all[i].name} </td>
                    <td> ${all[i].subject} </td>
                    <td> ${all[i].marks} </td>
                </tr>`
                    $('#tbody').append(output);
                }
                $('form')[0].reset();
                
                
            }
            // if(data.django){

            //     var django = data.django
            //     console.log('django table')
            //     console.log(django)
            // }

        }
        



    })

})