import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent {
  songs = [
    // Sample data, this will eventually come from your backend
    { id: 1, title: 'Song 1' },
    { id: 2, title: 'Song 2' },
  ];

  constructor(private router: Router) {}

  ngOnInit(): void {}

  navigateToUpload(): void {
    this.router.navigate(['/upload']);
  }

  navigateToSing(id: number): void {
    this.router.navigate(['/sing', id]);
  }
}
