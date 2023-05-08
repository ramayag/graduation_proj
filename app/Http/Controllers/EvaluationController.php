<?php

namespace App\Http\Controllers;
namespace App\Evaluation;

use Illuminate\Http\Request;

class EvaluationController extends Controller
{
    public function index()
    {
        $evals = Evaluation::all(); 
        $response=$evals;

        return response()->json($response,200);
        
    }
    
    public function show($id)
    {   
        $evals = Evaluation::find($id);
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
        $categories = new Category;
        $categories->name=$request->name;
        if (isset($request->image)) {
            $image_name = rand() . "." . $request->image->getClientOriginalExtension();
            $categories->image =  $image_name;
            $request->image->move('categories', $image_name);
          }
        $categories->save();
        return $categories;
    }

    public function update(Request $request,$id)
    {   $categories = Category::where('id',$id)->first(); 
        if(isset($categories))
        {
        $categories->name=$request->name;
        $categories->save();
        }
        return $categories;
    }

    public function delete($id)
    {
        $categories = Category::where('id',$id)->first(); 
        if(isset($categories))
            {
                
             $categories->delete();
             return "deleted";
                
            }

    }
}
