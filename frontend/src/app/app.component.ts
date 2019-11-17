import {Component, OnInit} from '@angular/core';
import {FlaskApiService} from "./services/flask-api.service";
import {Subscription} from "rxjs";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'frontend';
  dataSub: Subscription;
  data: string;

  constructor(private _apiService:FlaskApiService){
  }

  ngOnInit(): void {

    this.dataSub = this._apiService.getSomeData().subscribe(data => {
        console.log(data);
          this.data = data;
        },
        console.error
      );
  }


}
