<?php

namespace App\Http\Controllers;
namespace App\Voice_evals;

use Illuminate\Http\Request;

class voice_evalsController extends Controller
{
    public function index()
    {
        $evals = Voice_evals::all(); 
        $response=$evals;

        return response()->json($response,200);
        
    }
    
    public function show($id)
    {   
        $evals = Voice_evals::find($id);
        if(isset($evals))
        {
          $response=$evals;

          return response()->json($response,200);
        }
        else
        {
          $response=$evals;

          return response()->json($response,404);
        }
    }

    public function store(Request $request)
    {

        $voice = new Voice_evals;
        $voice->sound_speed=$request->sound_speed;
        $voice->sound_laudness=$request->sound_laudness;
        $voice->sound_stress=$request->sound_stress;

        $voice->save();
        return $voice;
    }

    public function update(Request $request,$id)
    {   $voice = Voice_evals::where('id',$id)->first(); 
        if(isset($voice))
        {
           
            $voice->sound_speed=$request->sound_speed;
            $voice->sound_laudness=$request->sound_laudness;
            $voice->sound_stress=$request->sound_stress;
          

        $voice->save();
        }
        return $voice;
    }

    public function delete($id)
    {
        $voice = Voice_evals::where('id',$id)->first(); 
        if(isset($voice))
            {
                
             $voice->delete();
             return "deleted";
                
            }

    }
}
