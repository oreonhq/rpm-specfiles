%global source0_hash b9c31d4259f5579d8ce677ea161d761b1abc13c220b798a73e9d5d22710237d5

# SPDX-License-Identifier: MIT
Version: 1.204
Release: 20%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Annapurna SIL
%global fontsummary       Annapurna SIL, a Devanagari font family
%global projectname       annapurna
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Annapurna SIL is a Unicode-based font family with broad support for writing
systems that use the Devanagari script. Inspired by traditional calligraphic
forms, the design is intended to be highly readable, reasonably compact, and
visually attractive.

The Devanagari script is used to write over 170 languages in South Asia.
Annapurna SIL supports a full range of these writing systems.}

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}
%linuxtext *.txt documentation/*.txt
chmod 644 %{fontdocs} %{fontlicenses} documentation/*

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%license OFL.txt
%doc documentation/*.pdf

%changelog
%autochangelog
