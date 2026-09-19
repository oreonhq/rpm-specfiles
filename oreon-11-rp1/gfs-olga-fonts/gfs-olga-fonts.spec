%global source0_hash 4d76616227130ac0f93e9ac33385ec4ba34d988315af1476b07f721d460fdb84

# SPDX-License-Identifier: MIT
Version: 20160509
Release: 20%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Olga
%global fontsummary       GFS Olga, a 20th century oblique Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
In Greece the terms italic and oblique have the same meaning since they are
borrowed from the Latin typographic practice without any real historical
equivalent in Greek history. Until the end of the 19th century Greek typefaces
were cut and cast independently, not as members of a font family. The
mechanization of type cutting allowed the transformation of upright Greek
typefaces to oblique designs. Nonetheless, the typesetting practice of a
cursive Greek font to complement an upright one did not survive the 19th
century.

The experimental font GFS Olga (1995) attempts to revive this lost tradition.
The typeface was designed and digitized by George Matthiopoulos, based on the
historical Porson Greek type (1803) with the intention to be the companion of
the upright GFS Didot font whenever there is a need for an italic alternative.}

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
