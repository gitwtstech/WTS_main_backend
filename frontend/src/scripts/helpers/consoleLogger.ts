import type { AxiosResponse } from 'axios';

export function logAxiosResponse(message:AxiosResponse):AxiosResponse{
    const {data, status} = message;
    console.log(JSON.stringify(data, null, 4));
    console.log(status);
    return message;
}