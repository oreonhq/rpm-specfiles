%global source0_hash 866855b0296579451c233fc78bec82918996a8df7341ee2f1c09d7bc94440680
Version: 20070616
Release:        48%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century
%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}
%global fontfamily        Didot
%global fontsummary       GFS Didot, a 20th century Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Didot’s type was the base for a new font, GFS Didot (1994) which was designed
by Takis Katsoulidis, and digitized by George Matthiopoulos. The typeface is
accompanied by a matching Latin alphabet based on Hermann Zapf’s PaLatino.}
%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}
Source0:        http://www.greekfontsociety-gfs.gr/_assets/fonts/%{foundry}_%{fontfamily}.zip
Source10: 60-%{fontpkgname}.xml
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list
%files -n adf-gillius-fonts-doc -f %{oreon_filedir}/adf-gillius-fonts-doc.list

%changelog

%autochangelog
