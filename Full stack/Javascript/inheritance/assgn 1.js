class vehicle{
    setname(name){
	  this .name=name;
	  document.write("This is "+this name);
	 }
	sp(speed){
	     this .speed=speed;
		document.write("Speed is "+ this speed"kmph.");
	 }
}
 class bike extends vehicle{
     seats(st){
	     this .st=st;
		 document.write("Available seats are"+this st);
	 } 
}

let myvehicle=new bike();
myvehicle.setname(car);
myvehicle.sp(60);
myvehicle.seats(55);
