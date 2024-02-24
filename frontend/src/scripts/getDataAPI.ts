import http from '../scripts/http-common'

type User = {
    username: string,
    password: string,
    email: string
}

type Users = {
    users: User[]
}

export class userAPI {
    

    async get(){
        const {data, status} = await http.get<Users>("users/",{
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        })
        console.log(JSON.stringify(data, null, 4));
    
        console.log(status);
    };

    async post(email:string, username: string, password: string){
        const {data, status} = await http.post<User>("users/", 
        {   email: email, username: username, password: password},  
        {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });
    
        console.log(JSON.stringify(data, null, 4));
    
        console.log(status);
    };

    async put(email:string, username: string, password: string){
        const {data, status} = await http.put<User>("users/", 
        {   email: email, username: username, password: password},  
        {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });
    
        console.log(JSON.stringify(data, null, 4));
    
        console.log(status);
    };
}
