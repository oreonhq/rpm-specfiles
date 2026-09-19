%global source0_hash fd2894531aab32ff7d6845e3d0b4c0401c91f64ba637d13624dfc17a3e815831

# SPDX-License-Identifier: MIT
Version: 2.51
Release: 19%{?dist}
URL:     https://scripts.sil.org/ezrasil_home

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      Licenses.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
The Ezra SIL font families are fashioned after the square letter forms of the
typography of the Biblia Hebraica Stuttgartensia (BHS), a beautiful Old
Testament volume familiar to Biblical Hebrew scholars.

The different font families are available to provide two different styles of
cantillation marks. They were developed together, but there are some
differences in how they display markings. This was done intentionally.}

%global fontfamily0       Ezra SIL
%global fontsummary0      Ezra SIL, an Hebrew font family
%global fonts0            *.ttf
%global fontsex0          %{fonts1}
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

The Ezra SIL font family is supposed to render text identically to the printed BHS.}

%global fontfamily1       Ezra SIL SR
%global fontsummary1      Ezra SIL SR, an Hebrew font family
%global fonts1            *SR.ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

The Ezra SIL SR font has a different style of cantillation marks which may be
more familiar to users working with other editions.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{fontfamily}%{version}"), "[%p%s]+", "");print(t)}

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=%{archivename}.zip&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 65-%{fontpkgname0}.xml
Source11: 65-%{fontpkgname1}.xml

%fontpkg -a

%fontmetapkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
unzip -j -q %{SOURCE0}
%linuxtext *.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
