<?php

namespace App\Http\Controllers;


use App\Evaluations;
use Illuminate\Http\Request;
// use App\Traits\GeneralTrait;

class EvalsController extends Controller
{

    // use GeneralTrait;
    public function add(Request $request)
    {
           $evaluations =new Evaluations;
           $evaluations->vedio_num = $request->vedio_num;
           $evaluations->hands_eval = $request->hands_eval;
           $evaluations->face_eval = $request->face_eval;
           $evaluations->movement_eval = $request->movement_eval;
           $evaluations->total_eval = $request->total_eval;
           $evaluations->user_id = $request->user_id;
           $evaluations->save();

            $response['data'] = $evaluations;

            return response()->json($response,200) ;

    }

    public function Evaluations_ID(Request $request)
    {

        $evaluations = Evaluations::selection()->find($request->id);
        if (!$evaluations)
            return $this->returnError('001', 'هذا  الفيديو غير موجد');

        return $this->returnData('categroy', $evaluations);
    }


}
