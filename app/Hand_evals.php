<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Hand_evals extends Model
{
    use Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
  


    protected $fillable = [
        'CLOSED_U_HANDS', 'HAND_CROSSED','HAND_ON_HIP',
        'HAND_ON_HEAD','STRAIGHT_DOWN','CLOSED_D_HANDS',
        'evaluation_id'
    ];


    public function getJWTIdentifier()
    {
        return $this->getKey();
    }

    /**
     * Return a key value array, containing any custom claims to be added to the JWT.
     *
     * @return array
     */
    public function getJWTCustomClaims()
    {
        return [];
    }
}
