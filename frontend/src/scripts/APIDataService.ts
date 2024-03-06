import http from './http-common'
import { logAxiosResponse } from './helpers/consoleLogger'

export type User = {
    username: string,
    password: string,
    email: string
}

export type Users = {
    users: User[]
}

class UserAPI {
    
    async get(){
        const response = await http.get<Users>("users/",{
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        })
        return logAxiosResponse(response)
    };

    async getById(id: number){
        const response = await http.get<Users>(`users/${id}`,{
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        })
        return logAxiosResponse(response)
    };

    async post(user: User){
        const response = await http.post<User>("users/", 
        user,  
        {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });
        return logAxiosResponse(response)
    };

    async put(id: number, user: User){
        const response = await http.put<User>(`users/${id}`, 
        user,  
        {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });
        return logAxiosResponse(response)
    };
}

export const userAPI = new UserAPI();
