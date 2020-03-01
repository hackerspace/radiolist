{ stdenv, buildPythonPackage, fetchPypi, beautifulsoup4 }:

buildPythonPackage rec {
  pname = "radiolist";
  version = "0.1";

  src = ./.;
  propagatedBuildInputs = [ beautifulsoup4 ];

  meta = with stdenv.lib; {
    homepage = https://github.com/hackerspace/radiolist;
    description = "Internet radio directory";
    license = licenses.wtfpl;
    maintainers = with maintainers; [ b42 sorki ];
  };
}
