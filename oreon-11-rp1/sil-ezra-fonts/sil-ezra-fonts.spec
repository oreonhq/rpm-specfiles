%global source0_hash fd2894531aab32ff7d6845e3d0b4c0401c91f64ba637d13624dfc17a3e815831
Version: 2.51
Release:        1%{?dist}
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
Source0:        https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=Ezra%{foundry}251.zip&filename=Ezra%{foundry}251.zip#/Ezra%{foundry}251.zip
Source10: 65-%{fontpkgname0}.xml
Source11: 65-%{fontpkgname1}.xml
%fontpkg -a
%fontmetapkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
unzip -j -q %{SOURCE0}
%linuxtext *.txt

%build

%fontbuild -a
%install
%fontinstall -a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck -a
%fontfiles -a
%files -f %{oreon_filedir}/main.list
%files -n bitmap-lucida-typewriter-fonts -f %{oreon_filedir}/bitmap-lucida-typewriter-fonts.list
%files -n bitmap-lucida-typewriter-opentype-fonts -f %{oreon_filedir}/bitmap-lucida-typewriter-opentype-fonts.list
%files -n bitmap-fangsongti-fonts -f %{oreon_filedir}/bitmap-fangsongti-fonts.list
%files -n bitmap-fangsongti-opentype-fonts -f %{oreon_filedir}/bitmap-fangsongti-opentype-fonts.list
%files -n bitmap-console-fonts -f %{oreon_filedir}/bitmap-console-fonts.list
%files -n bitmap-console-opentype-fonts -f %{oreon_filedir}/bitmap-console-opentype-fonts.list
%files -n bitmap-fixed-fonts -f %{oreon_filedir}/bitmap-fixed-fonts.list
%files -n bitmap-fixed-opentype-fonts -f %{oreon_filedir}/bitmap-fixed-opentype-fonts.list
%files -n bitmap-ecolier-court-fonts-all -f %{oreon_filedir}/bitmap-ecolier-court-fonts-all.list

%changelog

%autochangelog
