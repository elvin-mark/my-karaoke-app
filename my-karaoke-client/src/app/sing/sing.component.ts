import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-sing',
  templateUrl: './sing.component.html',
  styleUrls: ['./sing.component.scss'],
})
export class SingComponent {
  lyrics: string[] = [
    // Sample lyrics data, this will eventually come from your backend
    'Line 1 of the song',
    'Line 2 of the song',
    'Line 3 of the song',
  ];

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    const songId = this.route.snapshot.paramMap.get('id');
    // Fetch song details using songId
  }

  startSinging(): void {
    // Logic to start singing with pitch guide
  }
}
