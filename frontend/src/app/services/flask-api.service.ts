import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class FlaskApiService {

  API_URL:string  = environment.FLASK_API_URL;

  constructor(private http: HttpClient) { }

  getSomeData(): Observable<string> {
    return this.http
      .get<string>(this.API_URL + "/somedata")
  }
}
