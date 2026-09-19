%global source0_hash 7bfe591a3d31d13edfe82f6ba968ad1b0fcd2ee5ecb579b9837181949679752c

# SPDX-License-Identifier: MIT
Version: 20161102
Release: 19%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Orpheus
%global fontsummary       GFS Orpheus, a 21st century Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
GFS Orpheus is a variation of GFS Orpheus Classic. It was based on the text
found in a school textbook entitled Στοιχειώδης Φυσική Ιστορία, published by
the publisher Anestis Konstantinidis in Athens on 1887. The x-height is shorter
(longer descenders), while the uppercase characters and the numbers were
designed from scratch, following more closely the style of the lowercase
characters.

GFS Orpheus was designed by George Triantafyllakos.}

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
