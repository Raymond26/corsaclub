class UserProfile {
    constructor(userProfileID) {
        this.userProfileID = userProfileID;
    }
}

function getCookieName() {
     return 'cc-user-profile-id=';
}

function setCCCookie(value) {
    if (value == null) {
        document.cookie = getCookieName() + "; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        return;
    }
    document.cookie = getCookieName() + value + ';path=/';
}

function getCCCookie() {
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while(c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(getCookieName()) == 0) {
            return c.substring(getCookieName().length, c.length);
        }
    }
    return "";
}

function sendOnload() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("received " + this.status);
            console.log(xhttp.response);
            var obj = JSON.parse(xhttp.response);
            setCCCookie("" + obj.id);
        }
    };
    var reqData = {
        location : window.location.pathname
    };
    var existingCookie = getCCCookie();
    if (existingCookie != "") {
        reqData['user_profile_id'] = existingCookie;
    }
    xhttp.open("POST", "/profiles/sync/", true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify(reqData));
}

function CC() {
    var cc = new UserProfile(null);
    window.addEventListener('load', sendOnload);
    return cc;
};

function syncID() {
    var profileID = getCCCookie();
    if (profileID == "") {
        profileID = null;
    }
    cc.userProfileID = profileID;
}