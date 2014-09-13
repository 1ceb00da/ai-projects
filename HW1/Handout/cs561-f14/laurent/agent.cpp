#include <fstream>

int main(int argc, char const * argv[])
{
  std::ofstream out("output.txt");
  out << "CSCI-561 rocks!" << std::endl;
  out.close();

  return 0;
}
