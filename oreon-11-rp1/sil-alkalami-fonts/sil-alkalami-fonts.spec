%global source0_hash 632747ad5ebb9a9b9e91d1bc810e2a0314709edeb035dc5931812b74327fef17

# SPDX-License-Identifier: MIT
Version: 1.200
Release: 20%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Alkalami
%global fontsummary       A font family for the Arabic scripts of the Kano region of Nigeria and Niger
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Alkalami is a font family for Arabic-based writing systems in the Kano region
of Nigeria and in Niger. This style of writing African Ajami has sometimes been
called Sudani Kufi or Rubutun Kano.

Alkǎlami (pronounced al-KA-la-mi) is the local word for the Arabic “qalam”, a
type of sharpened stick used for writing on wooden boards in the Kano region of
Nigeria and in Niger, and what gives the style its distinct appearance. The
baseline stroke is very thick and solid. The ascenders and other vertical
strokes including the teeth are very narrow when compared to the baseline. A
generous line height is necessary to allow for deep swashes and descenders, and
the overall look of the page is a very black, solid rectangle. Diacritics are
much smaller in scale, with very little distance from the main letters.

The Alkalami font supports the characters known to be used by languages written
with the Kano style of Arabic script, but may not have the characters needed
for other languages.}

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 66-%{fontpkgname}.xml

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
