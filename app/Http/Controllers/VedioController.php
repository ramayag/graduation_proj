<?php

namespace App\Http\Controllers;
namespace App\Vedios;

use Illuminate\Http\Request;

class VedioController extends Controller
{


    public function index()
    {
        $evals = Vedios::all(); 
        $response=$evals;

        return response()->json($response,200);
        
    }
    
    public function show($id)
    {   
        $evals = Vedios::find($id);
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

        $vedio = new Vedios;
        $vedio->size=$request->size;
        $vedio->time=$request->time;
        $vedio->title=$request->title;
        $vedio->date=$request->date;
        $vedio->user_id=$request->user_id;

        $vedio->save();
        return $vedio;
    }

    public function update(Request $request,$id)
    {   $vedio = Vedios::where('id',$id)->first(); 
        if(isset($vedio))
        {
           
        $vedio->size=$request->size;
        $vedio->time=$request->time;
        $vedio->title=$request->title;
        $vedio->date=$request->date;
        $vedio->user_id=$request->user_id;

        $vedio->save();

        }
        return $vedio;
    }

    public function delete($id)
    {
        $vedio = Vedios::where('id',$id)->first(); 
        if(isset($vedio))
            {
                
             $vedio->delete();
             return "deleted";
                
            }

    }
}
