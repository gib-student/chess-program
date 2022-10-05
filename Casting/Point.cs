using System;

namespace chess_program
{
    public class Point{
        private int _x;
        private int _y;
        
        public Point(int x, int y)
        {
            _x = x;
            _y = y;
        }

        public int GetX()
        {
            return x;
        }

        public int GetY()
        {
            return _y;
        }

        public Point Add(Point other)
        {
            int new X = _x + other._x;
            int newY = _y + other._y;
        }

        
    }
}