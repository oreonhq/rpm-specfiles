%global source0_hash none

Version:        0.954
Release:        26%{?dist}
## Note that upstream is dead and there is no download link available at this minute
## so please don't report FTBFS bugs for this package.
URL:            http://www.ctan.org/tex-archive/fonts/Asana-Math/

%global foundry           oflb
%global fontlicense       OFL-1.1
%global fontlicenses      License.txt
%global fontdocs          *.txt README.license
%global fontdocsex        %{fontlicenses}

%global fontfamily        Asana Math
%global fontsummary       An OpenType font with a MATH table
%global fonts             Asana-Math.otf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
An OpenType font with a MATH table that can be used with XeTeX to typeset math
content.}

Source0:        http://mirrors.ctan.org/fonts/Asana-Math/Asana-Math.otf
Source1:        63-%{fontpkgname}.conf
Source2:        README.license
#license text extracted from font file
Source3:        License.txt

%fontpkg

%prep
%setup -q -c -T
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
