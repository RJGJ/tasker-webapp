jQuery(document).ready(() => {
    /*
    look for refresh token, if there is none go to login
    */
    const refreshToken = Cookies.get('refresh_token');
    if (refreshToken === undefined || refreshToken === null) {
        alert('An error occured, Please login again');
        location.href = 'login.html';
    }
});