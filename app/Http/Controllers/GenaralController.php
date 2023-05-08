<?php

namespace App\Http\Controllers;

use App\User;
use Illuminate\Http\Request;

class GenaralController extends Controller
{
    public function regester(Request $request)
    {
       $user =new User;
           $user->name = $request->name;
           $user->email = $request->email;
           $user->password = bcrypt("$request->password");
           $user->save();

            $response['data'] = $user;

            return response()->json($response,200) ;

    }



}
