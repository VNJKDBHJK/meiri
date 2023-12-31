using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class SocketClient : MonoBehaviour
{
    private Socket _clientSocket;
    public int answer = 0;

    void Start()
    {
        // 建立TCP连接
        _clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

        // 连接Python服务器
        string address = "127.0.0.1";  // Python服务器地址
        int port = 8888;  // Python服务器端口号
        _clientSocket.Connect(address, port);
    }

    void Update()
    {
        // 向Python服务器发送数据
        string message = "Hello Python!";
        byte[] data = Encoding.UTF8.GetBytes(message);
        _clientSocket.Send(data);

        // 接收Python服务器传来的数据
        byte[] recvData = new byte[1024];
        int count = _clientSocket.Receive(recvData);
        string recvMessage = Encoding.UTF8.GetString(recvData, 0, count);
        Debug.Log(recvMessage);
        if (recvMessage == "Open Hand")
        {
            answer = 1;
        }
        else if (recvMessage == "Fist")
        {
            answer = 0;
        }
    }

    void OnDestroy()
    {
        // 关闭TCP连接
        _clientSocket.Shutdown(SocketShutdown.Both);
        _clientSocket.Close();
    }
}