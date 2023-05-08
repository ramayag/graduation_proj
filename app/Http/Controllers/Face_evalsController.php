<?php

namespace App\Http\Controllers;
namespace App\Head_evals;

use Illuminate\Http\Request;

class Face_evalsController extends Controller
{  

    public function index()
    {
        $evals = Head_evals::all(); 
        $response=$evals;

        return response()->json($response,200);
        
    }
    
    public function show($id)
    {   
        $evals = Head_evals::find($id);
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
        $head = new Head_evals;
        $head->eye_contact=$request->eye_contact;
        $head->smile_count=$request->smile_count;
        $head->head_movement=$request->head_movement;
        $head->clear_view=$request->clear_view;

        $head->save();
        return $head;
    }

    public function update(Request $request,$id)
    {   $head = Head_evals::where('id',$id)->first(); 
        if(isset($categories))
        {
        $head->eye_contact=$request->eye_contact;
        $head->smile_count=$request->smile_count;
        $head->head_movement=$request->head_movement;
        $head->clear_view=$request->clear_view;

        $head->save();
        }
        return $head;
    }

    public function delete($id)
    {
        $head = Head_evals::where('id',$id)->first(); 
        if(isset($head))
            {
                
             $head->delete();
             return "deleted";
                
            }

    }
    //
}
