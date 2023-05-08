<?php

namespace App\Http\Controllers;
namespace App\Hand_evals;

use Illuminate\Http\Request;

class Hand_evalsController extends Controller
{


        public function index()
        {
            $evals = Hand_evals::all(); 
            $response=$evals;
    
            return response()->json($response,200);
            
        }
        
        public function show($id)
        {   
            $evals = Hand_evals::find($id);
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
            $hand = new Hand_evals;
            $hand->arm_closed=$request->arm_closed;
            $hand->hand_crossed=$request->hand_crossed;
            $hand->hand_opend=$request->hand_opend;
            $hand->sholder=$request->sholder;
    
            $hand->save();
            return $hand;
        }
    
        public function update(Request $request,$id)
        {   $hand = Hand_evals::where('id',$id)->first(); 
            if(isset($hand))
            {
                $hand->arm_closed=$request->arm_closed;
                $hand->hand_crossed=$request->hand_crossed;
                $hand->hand_opend=$request->hand_opend;
                $hand->sholder=$request->sholder;
    
            $hand->save();
            }
            return $hand;
        }
    
        public function delete($id)
        {
            $hand = Hand_evals::where('id',$id)->first(); 
            if(isset($hand))
                {
                    
                 $hand->delete();
                 return "deleted";
                    
                }
    
        }
}
