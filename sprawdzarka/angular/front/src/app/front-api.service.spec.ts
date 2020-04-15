import { TestBed } from '@angular/core/testing';

import { FrontApiService } from './front-api.service';

describe('FrontApiService', () => {
  let service: FrontApiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FrontApiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
