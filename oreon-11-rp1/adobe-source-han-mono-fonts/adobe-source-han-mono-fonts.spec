%global source21_hash de4e853428588b67499b2ad66cf261846497e8cea4f3eca5ae1067685cd9897c
%global source20_hash 0983abed9371adc8958c321bf8d8036324b4a2e8cc324682b0fe0c699e63a009
%global source0_hash 0c192448de90848f11eb8336876883a9a36dc65b8965e489600cfcc7a67358c1
Version: 1.002
Release:        1%{?dist}
URL:     https://github.com/adobe-fonts/source-han-mono/
%global foundry           adobe
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.md
%global fontdocs          README.md
%global fontdocsex        %{fontlicenses}
%global fontfamily        Source Han Mono
%global fontsummary       Adobe OpenType monospaced font for mixed Latin and CJK text
%global fonts             SourceHanMono.ttc
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Source Han Mono, which is derived from Source Han Sans and Source Code Pro,
is an OpenType/CFF Collection (OTC) that includes 70 font instances—consisting
of seven weights, five languages, and two styles—and is a Pan-CJK version
of Source Han Code JP.
}
Source0:        https://github.com/adobe-fonts/source-han-mono/releases/download/%{version}/SourceHanMono.ttc
Source10: 68-adobe-source-han-mono-fonts.conf
Source20: https://raw.githubusercontent.com/adobe-fonts/source-han-mono/%{version}/LICENSE.md
Source21: https://raw.githubusercontent.com/adobe-fonts/source-han-mono/%{version}/README.md
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
