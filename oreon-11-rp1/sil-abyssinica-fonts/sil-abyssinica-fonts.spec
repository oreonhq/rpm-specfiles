Version:        1.200
Release:        32%{?dist}

%global foundry           SIL
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Abyssinica SIL
%global fontsummary       SIL Abyssinica fonts
%global projectname       AbyssinicaSIL
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
SIL Abyssinica is a Unicode typeface family containing glyphs for the
Ethiopic script.

The Ethiopic script is used for writing many of the languages of Ethiopia and
Eritrea. Abyssinica SIL supports all Ethiopic characters which are in Unicode
including the Unicode 4.1 extensions. Some languages of Ethiopia are not yet
able to be fully represented in Unicode and, where necessary, we have included
non-Unicode characters in the Private Use Area (see Private-use (PUA)
characters supported by Abyssinica SIL).

Abyssinica SIL is based on Ethiopic calligraphic traditions. This release is
a regular typeface, with no bold or italic version available or planned.}


# download from http://scripts.sil.org/cms/scripts/render_download.php?site_id=nrsi&format=file&media_id=AbyssinicaSIL1.200.zip&filename=AbyssinicaSIL1.200.zip
Source0:        %{archivename}.zip
Source1:        66-%{fontpkgname}.conf

%fontpkg

%prep
%setup -q -n %{projectname}-%{version}
%linuxtext FONTLOG.txt OFL.txt OFL-FAQ.txt README.txt documentation/DOCUMENTATION.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.200-32
- Prepare for Oreon 11 (RP1)
