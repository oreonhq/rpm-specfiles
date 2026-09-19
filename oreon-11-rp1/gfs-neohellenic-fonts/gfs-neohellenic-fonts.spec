%global source0_hash 9b3f63c792823e7d2cb7859432c40d008b7bc67cd4ef0d1424dc4565745ae999

# SPDX-License-Identifier: MIT
Version: 20090918
Release: 37%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        NeoHellenic
%global fontsummary       GFS NeoHellenic, a 20th century round Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The design of new Greek typefaces always followed the growing needs of the
Classical Studies in the major European Universities. Furthermore, by the end
of the 19th century bibliology had become an established section of Historical
Studies, and, as John Bowman commented, the prevailing attitude was that Greek
types should adhere to a lost idealized, yet undefined, Greekness of yore.
Especially in Great Britain this tendency remained unchallenged in the first
decades of the 20th century, both by Richard Proctor, curator of the incunabula
section in the British Museum Library and his successor Victor Scholderer.

In 1927, Scholderer, on behalf of the Society for the Promotion of Greek
Studies, got involved in choosing and consulting the design and production of a
Greek type called New Hellenic cut by the Lanston Monotype Corporation. He
chose the revival of a round, and almost mono-line type which had first appeared
in 1492 in the edition of Macrobius, ascribable to the printing shop of
Giovanni Rosso (Joannes Rubeus) in Venice. New Hellenic was the only successful
typeface in Great Britain after the introduction of Porson Greek well over a
century before. The type, since to 1930’s, was also well received in Greece,
albeit with a different design for Ksi and Omega.

GFS digitized the typeface (1993-1994) funded by the Athens Archeological
Society with the addition of a new set of epigraphical symbols. Later (2000)
more weights were added (italic, bold and bold italic) as well as a Latin
version.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 60-%{fontpkgname}.xml

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
