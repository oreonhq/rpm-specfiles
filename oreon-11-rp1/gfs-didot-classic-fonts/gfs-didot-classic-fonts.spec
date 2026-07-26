%global source0_hash 5b01ef4783db75327fb90165a243e0bd467cc5329623d769f6a3aaec7b6cf80b

# SPDX-License-Identifier: MIT
Version: 20080702
Release: 43%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Didot Classic
%global fontsummary       GFS Didot Classic, a 19th century Greek font family
%global fontpkgheader     %{expand:
Suggests: font(gfsdidot)
}
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Under the influence of the neoclassical ideals of the late 18th century, the
famous French type cutter Firmin Didot in Paris designed a new Greek typeface
(1805) which was immediately used in the publishing program of Adamantios
Korai, the prominent intellectual figure of the Greek diaspora and leading
scholar of the Greek Enlightenment. The typeface eventually arrived in Greece,
with the field press which came with Didot’s grandson Ambroise Firmin Didot,
during the Greek Revolution in 1821. Since then the typeface has enjoyed an
unrivaled success as the type of choice for almost every kind of publication
until the last decades of the 20th century.

Didot’s original type design, as it is documented in publications during the
first decades of the 19th century, was digitized and revived by George D.
Matthiopoulos in 2006 for a project of the Department of Literature in the
School of Philosophy at the University of Thessaloniki, and is now available
for general use.}

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
