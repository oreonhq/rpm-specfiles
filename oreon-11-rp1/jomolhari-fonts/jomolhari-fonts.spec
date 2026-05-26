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

Source0: http://chris.fynn.googlepages.com/%{archivename}.zip
Source1:        65-0-%{fontpkgname}.conf 
# oreon url source checksums begin
%global source0_sha256 03877d8c31ab4b85e344f3e53c8465afb7acd6a13111354514556eca4aad9172
%global source0_file jomolhari-alpha003c.zip
# oreon url source checksums end

%fontpkg

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jomolhari-alpha003c.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "03877d8c31ab4b85e344f3e53c8465afb7acd6a13111354514556eca4aad9172" || { echo "oreon: Source0 SHA256 mismatch for jomolhari-alpha003c.zip" >&2; exit 1; })
# oreon verify url source checksums end
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
