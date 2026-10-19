%global source0_hash c17855d4d95290266f6a10f76d6168a75d8b6eb486b6ab3b72f1c1694e3da977
Version: 20070415
Release:        48%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century
%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.rtf
%global fontdocsex        %{fontlicenses}
%global fontfamily        Artemisia
%global fontsummary       GFS Artemisia, a Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The type family GFS Artemisia was designed by the painter-engraver Takis
Katsoulidis and reflects his style and typographic acumen. It is largely his
effort to offer, from a different perspective, a type face which, like Times
Greek, would be applicable to a wide spectrum of uses and equally agreeable and
legible.
The typeface has been digitized by George D. Matthiopoulos.}
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
chmod 644 %{fontdocs} %{fontlicenses}

%build

%fontbuild
%install
%fontinstall
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list
%files -n bitmap-ecolier-court-fonts-doc -f %{oreon_filedir}/bitmap-ecolier-court-fonts-doc.list

%changelog

%autochangelog
