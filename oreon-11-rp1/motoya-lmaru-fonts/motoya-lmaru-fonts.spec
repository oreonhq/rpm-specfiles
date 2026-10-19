%global source0_hash none
%global        archivedate     20110406
%global        download_root   http://android.git.kernel.org/?p=platform/frameworks/base.git;a=blob_plain;f=data/fonts/
Version: 1.00
Release:        1%{?dist}
URL:     http://android.git.kernel.org/?p=platform/frameworks/base.git;a=tree;f=data/fonts
%global foundry           Motoya
%global fontlicense       Apache-2.0
%global fontlicenses      NOTICE
%global fontdocs          README.txt
%global fontdocsex        %{fontlicenses}
%global fontfamily        MotoyaLMaru
%global fontsummary       Japanese Round Gothic-typeface TrueType fonts by MOTOYA Co,LTD
%global fonts             MTLmr3m.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Motoya font was created in 1950s, it aims beauty and readability.
"MotoyaLMaru W3 mono", Round Gothic-typeface font was contributed by
MOTOYA Co,LTD. for Android platform.
}
Source0:        %{download_root}%{fonts}
Source10: 70-motoya-lmaru-fonts.conf
Source20: %{download_root}NOTICE
Source21: %{download_root}README.txt
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE20} .
cp %{SOURCE21} .

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
