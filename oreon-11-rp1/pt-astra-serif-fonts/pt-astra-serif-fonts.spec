%global source0_hash 7922cc0bedd3308be652b33c528f2d2152ec6503375764eb2cfecc989a476799

Version: 1.003
Release: 10%{?dist}

URL: https://astralinux.ru/en/information/#section-fonts-astra

%global foundry PT 
%global fontlicense  OFL-1.1
%global fontlicenses  LICENSE.txt

%global fontfamily  PT Astra Serif
%global fontsummary  Serif fonts that are metric analogs of Times New Roman
%global fontdescription  %{expand:Russian free-for-all fonts that are 
metric analogs of the Times New Roman font. The use of these fonts 
instead of Times New Roman doesn’t lead to document distortion, and 
freeware distribution and cross-platform combined with modern design make
them suitable and user-friendly in the any operating system and office 
program.}

%global fonts  %{name}-%{version}/*.ttf
%global fontconfs  %{SOURCE10}

Source0: https://astralinux.ru/information/fonts-astra/font-ptastra-serif-ver1003.zip 

Source10: 60-%{fontpkgname}.xml
# https://astralinux.ru/en/ofl
Source11: LICENSE.txt

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
unzip -n %{SOURCE0} -d %{name}-%{version}

%build
%fontbuild
install -p -m 0644 %{SOURCE11} .

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
