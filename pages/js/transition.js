const main = document.querySelector("#main");
const userName = document.querySelector("#userName");
const userUniv = document.querySelector("#userUniv");

//좀 많이 멍청한 코딩이긴 한데 실력이 딸려서 무식하게 일단 함.
//false true 값 왔다리갔다리 하면 한 코드에 끝낼 수 있을 것 같긴 한데 그걸 못하겠음
function create(){
    main.style.webkitANimation = "fadeOut 1s";
    main.style.animation = "fadeOut 1s";
    setTimeout(() => {
        userName.style.webkitANimation = "fadeIn 1s";
        userName.style.animation = "fadeIn 1s";
    
        setTimeout(() => {
            main.style.display = "none";
            userName.style.display = "block";
            userUniv.style.display = "none"; 

        }, 450);

    }, 450)
}

function create2(){
    userName.style.webkitANimation = "fadeOut 1s";
    userName.style.animation = "fadeOut 1s";
    setTimeout(() => {
        userUniv.style.webkitANimation = "fadeIn 1s";
        userUniv.style.animation = "fadeIn 1s";
    
        setTimeout(() => {
            main.style.display = "none";
            userName.style.display = "none";
            userUniv.style.display = "block"; 

        }, 450);

    }, 450)
}
