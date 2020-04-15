import { Component } from '@angular/core';
import { FrontApiService } from './front-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'front';
  students = [{snumber: ''}, {name: ''}]

  constructor(private api:FrontApiService) {
    this.getStudents();

  }
  getStudents = () => {
    this.api.getAllStudents().subscribe(
      data => {
        this.students = data;
      },
      error => {
        console.log(error)
      }

    )
  }

}
