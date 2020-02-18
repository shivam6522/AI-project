
#include <iostream>
#include <queue> 
using namespace std;

class State{
    public:
    int cost;
    int arr[8][8];
    bool isVisited;
    int nextRow;
    State(){
        cost = 0;
        isVisited = false;
        nextRow = 0;
    }
};

bool isValid(int board[8][8], int row, int column)
{
    int count = 0;
    for (int i = 0; i < 8; i++)
    {
        if (board[i][column] == 1)
        {
            count++;
        }
    }
    if (count > 1)
    {
        return false;
    }
    count = 0;
    for (int i = 0; i < 8; i++)
    {
        if (board[row][i] == 1)
        {
            count++;
        }
    }
    if (count > 1)
    {
        return false;
    }
    count = 0;

    int c1 = column;
    int r1 = row;
    int c2 = column - 1;
    int r2 = row - 1;
    count = 0;
    for (; c1 < 8 && r1 < 8; c1++, r1++)
    {
        if (board[r1][c1] == 1)
        {
            count++;
        }
    }
    for (; c2 >= 0 && r2 >= 0; c2--, r2--)
    {
        if (board[r2][c2] == 1)
        {
            count++;
        }
    }
    if (count > 1)
    {
        return false;
    }

    c1 = column;
    r1 = row;
    c2 = column + 1;
    r2 = row - 1;
    count = 0;
    for (; c1 >= 0 && r1 < 8; c1--, r1++)
    {
        if (board[r1][c1] == 1)
        {
            count++;
        }
    }
    for (; c2 < 8 && r2 >= 0; c2++, r2--)
    {
        if (board[r2][c2] == 1)
        {
            count++;
        }
    }
    if (count > 1)
    {
        return false;
    }

    return true;
}

bool isGoalState(State temp){
    return temp.nextRow == 8;
}

priority_queue<State> applyAction(State temp, priority_queue<State>open){
    int row = temp.nextRow;
    int cost = temp.cost;
    int board[8][8];
    for(int i=0;i<8;i++){
        for(int j=0;j<8;j++){
            board[i][j]=temp.arr[i][j];
        }
    }

    for (int i = 0; i < 8; i++)
    {
        board[row][i] = 1;
        if (isValid(board, row, i))
        {
            State nextState;
            for(int k=0;k<8;k++){
                for(int l=0;l<8;l++){
                    nextState.arr[k][l] = board[k][l];
                }
            }
            nextState.cost = cost+1;
            nextState.nextRow = row+1;
            open.push(nextState);
        }
        board[row][i] = 0;
    }
    return open;
}

bool operator<(const State& p1, const State& p2) 
{ 
    return p1.cost < p2.cost; 
} 

int main(){
    priority_queue <State> open;
    State s;

    for(int i=0;i<8;i++){
        for(int j=0;j<8;j++){
            s.arr[i][j]=0;
        }
    }
    bool hasReachedGoalState = false;
    open.push(s);
    while(!open.empty()){
        State temp = open.top();
        open.pop();
        if(isGoalState(temp)){
            hasReachedGoalState = true;
            cout<<"Cost = "<<temp.cost<<endl;
            for(int i=0; i<8; i++)
            {
                for (int j=0; j<8; j++)
                {
                    cout<<temp.arr[i][j]<<" ";
                }
                cout<<"\n";
            }
            break;
        }
        open = applyAction(temp,open);
    }
    if(!hasReachedGoalState){
        cout<<"No Solution Exits"<<endl;
    }

    return 0;
}