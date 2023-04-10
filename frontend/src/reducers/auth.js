import {
    SIGNIN_SUCCESS,
    SIGNIN_FAILD,
    SIGNUP_SUCCESS,
    SIGNUP_FAILD,
    LOGOUT,
} from '../actions/types'

const initialState = {
    token : localStorage.getItem('token'),
    isAuthenticated: null, 
    loading : false
};

export default function auth (state = initialState, action) {
    const {type, payload} = action;
    switch(type) {
        case SIGNIN_SUCCESS:
            localStorage.setItem('token', payload.access);
            return {
                ...state,
                isAuthenticated: true,
                loading: false,
                token: payload.access

            }

        case SIGNUP_SUCCESS:
            return {
                    ...state,
                    isAuthenticated: false,
                    loading: true,
                }
        case SIGNUP_FAILD:
            return {
                ...state,
                isAuthenticated: false,
                loading: true,
            }
        case SIGNIN_FAILD:
            return {
                    ...state,
                    isAuthenticated: false,
                    loading: true,
            }
        case LOGOUT:
            localStorage.removeItem('token')
            return {
                ...state,
                token: null,
                isAuthenticated: false,
                loading: false
            }

        default: 
            return state
    }
}