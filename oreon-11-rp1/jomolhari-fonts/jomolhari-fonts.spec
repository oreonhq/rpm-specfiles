%global source0_hash f188cfd2e1e4120e28cdf6a94da9b51be7c1adc678baa2c1aa55127bb5ac72ee

Version:        0.003
Release:        45%{?dist}

URL: https://fonts.google.com/specimen/Jomolhari

%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Jomolhari
%global fontsummary       Jomolhari a Bhutanese style font for Tibetan and Dzongkha
%global archivename       jomolhari-alpha003c
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
Jomolhari is an TrueType OpenType Bhutanese style font for Dzongkha and
Tibetan text. It is based on Bhutanese manuscript examples, supports the
Unicode and the Chinese encoding for Tibetan.
The font supports the standard combinations used in most texts.}

Source0:        https://chris.fynn.googlepages.com/jomolhari-alpha003c.zip
Source1:        65-0-jomolhari-fonts.conf 

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c
%linuxtext FONTLOG.txt OFL-FAQ.txt OFL.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.003-45
- Import
