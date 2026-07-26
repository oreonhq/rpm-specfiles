%global source0_hash 77cef2fdf15dc3e4ca4b469e84a507f1ba1c0cbf4685d0662ae42c72e409664a

# SPDX-License-Identifier: MIT
Version: 20090618
Release: 39%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Decker
%global fontsummary       GFS Decker, a 19th century Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
This typeface is a product of Deckersche Schriftgießere type foundry owned by
Rudolf Ludwig Decker (1804-1877) in Berlin, but it was frequently used in
Greek editions by both Oxford and Cambridge University Press during the last
decades of the 19th century. It was designed and cut before 1864, according to
John Bowman, when a set of matrices was bought by OUP, although the type was
not cast and used in England until 1882.

The typeface is an uncial design containing a case of capitals, and small
capitals, too. The letters lack any serifs although they retain their thick
and thin strokes. It appeared as an alternate type of Byzantine tradition in
mostly Patristic texts.

The font was digitally designed by George D. Matthiopoulos and is freely
available by GFS.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc *.pdf

%changelog
%autochangelog
