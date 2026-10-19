%global source0_hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
Version:        1.000
Release:        1%{?dist}
URL:            http://www.astigmatic.com/
%global foundry           Astigmatic
%global fontlicense       OFL-1.1
%global fontlicenses      "SIL Open Font License.txt"
%global fontfamily        Grand Hotel
%global fontsummary       Script retro style fonts
%global fonts             *.otf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
Grand Hotel finds its inspiration from the title screen of the 1937 film “Cafe 
Metropole” starring Tyrone Power. This condensed upright connecting script has 
a classic vibe to it.
It has a wonderful weight to it that feels subtly tied to Holiday and Bakery 
themed designs, even though it can work outside that genre.}
Source0:        https://www.fontsquirrel.com/fonts/download/grand-hotel/grand-hotel.zip
Source1:        61-%{fontpkgname}.conf
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%fontbuild
%install
%fontinstall
%oreon_autofiles main

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
