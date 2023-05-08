<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Head_evals extends Model
{
    use Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
  

    protected $fillable = [
        'eye_contact', 'smile_count','head_movement',
        'clear_view'
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
