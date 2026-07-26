%global source0_hash 750ecb0310ee4e1cb62336a2f078be776b42cd8f7ddf62368351c3aedb0fefd9

# SPDX-License-Identifier: MIT
Version: 20091008
Release: 36%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/18th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Gazis
%global fontsummary       GFS Gazis, an 18th century oblique Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
During the whole of the 18th century the old tradition of using Greek types
designed to conform to the Byzantine cursive hand with many ligatures and
abbreviations — as it was originated by Aldus Manutius in Venice and
consolidated by Claude Garamont (Grecs du Roy) — was still much in practice,
although clearly on the wane.

GFS Gazis is a typical German example of this practice as it appeared at the
end of that era in the 1790’s. Its name pays tribute to Anthimos Gazis
(1758-1828), one of the most prolific Greek thinkers of the period, who was
responsible for writing, translating and editing numerous books, including the
editorship of the important Greek periodical Ερμής ο Λόγιος (Litterary Hermes)
in Wien.

GFS Gazis has been digitally designed by George D. Matthiopoulos.}

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
