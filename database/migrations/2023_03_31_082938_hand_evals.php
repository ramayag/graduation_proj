<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class HandEvals extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('hand_evals', function (Blueprint $table) {
            $table->id();
            $table->Integer('CLOSED_U_HANDS');
            $table->Integer('HAND_CROSSED');
            $table->Integer('HAND_ON_HIP'); 
            $table->Integer('HAND_ON_HEAD');
            $table->Integer('STRAIGHT_DOWN');
            $table->Integer('CLOSED_D_HANDS'); 
            $table->unsignedBigInteger('evaluation_id');
            $table->foreign('evaluation_id')
            ->references('id')->on('evaluations')
            ->onDelete('cascade'); 


            $table->rememberToken();
            $table->timestamps();
        }); 
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        //
    }
}
