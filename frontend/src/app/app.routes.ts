import { Routes } from '@angular/router';
import {LoginPageComponent} from './pages/login-page/login-page.component';
import {ResetPasswordPageComponent} from './pages/reset-password-page/reset-password-page.component';
import {StartPageComponent} from './pages/start-page/start-page.component';
import {BookingPageComponent} from './pages/booking-page/booking-page.component';

export const routes: Routes = [
  {
    path: 'login',
    component: LoginPageComponent,
  },
  {
    path: 'reset-password',
    component: ResetPasswordPageComponent,
  },
  {
    path: 'booking',
    component: BookingPageComponent,
  },
  {
    path: '',
    component: StartPageComponent,
  },
  {
    path: '',
    redirectTo: '',
    pathMatch: 'full',
  }
];
