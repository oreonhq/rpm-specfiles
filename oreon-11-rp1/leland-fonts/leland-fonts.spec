%global source0_hash d16d0c8949af268840f6e670b988444085f11049fc62609bc0e4322ef5e24134
%global giturl  https://github.com/MuseScoreFonts/Leland
Version:        0.80
Release:        1%{?dist}
URL:            https://musescore.org/
VCS:            git:%{giturl}.git
%global fontorg         org.musescore
%global fontlicense     OFL-1.1-RFN
%global fontlicenses    LICENSE.txt OFL-FAQ.txt
%global fontdocs        FONTLOG.txt README.md
%global _desc %{expand:The Leland music fonts (Leland & Leland Text) were initially developed for the
MuseScore (https://www.musescore.org) music composition software.
Leland is compliant with Standard Music Font Layout (SMuFL), which provides a
standard way of mapping the thousands of musical symbols required by
conventional music notation into the Private Use Area in Unicode's Basic
Multilingual Plane for a single (format-independent) font.
The font is named after Leland Smith, creator of the SCORE music notation
software.}
%global fontfamily0     Leland
%global fontsummary0    SMuFL-compliant OpenType music font
%global fontpkgheader1  %{expand:
Obsoletes:      mscore-leland-fonts < 4.0
Provides:       mscore-leland-fonts = 1:%{version}-%{release}
}
%global fonts0          Leland.otf
%global fontconfs0      %{SOURCE1}
%global fontdescription0 %{expand:%_desc
This package contains the music font.}
%global fontfamily1     Leland Text
%global fontsummary1    Text font to complement Leland
%global fonts1          LelandText.otf
%global fontconfs1      %{SOURCE2}
%global fontdescription1 %{expand:%_desc
This package contains the text font.}
Source0:        %{giturl}/archive/v%{version}/%{fontfamily0}-%{version}.tar.gz
Source1:        65-%{fontpkgname0}.conf
Source2:        65-%{fontpkgname1}.conf
%fontpkg -a
%fontmetapkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Leland-%{version}
%oreon_prep
%build

%fontbuild -a
%install
%fontinstall -a
mkdir -p %{buildroot}%{_datadir}/SMuFL/Fonts/Leland
install -p -m 0644 leland_metadata.json \
  %{buildroot}%{_datadir}/SMuFL/Fonts/Leland/metadata.json
ln -s metadata.json %{buildroot}%{_datadir}/SMuFL/Fonts/Leland/Leland.json
for name in leland leland-text; do
  sed -e 's,<!\[CDATA\[\([^]]*\)\]\]>,\1,g' \
      -e 's,\(MuseScore\) (\(https://www.musescore.org\)),<a href="\2">\1</a>,' \
      -e 's,&,&amp;,' \
      -i %{buildroot}%{_metainfodir}/%{fontorg}.${name}-fonts.metainfo.xml
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck -a
%fontfiles -z 0
%dir %{_datadir}/SMuFL/
%dir %{_datadir}/SMuFL/Fonts/
%{_datadir}/SMuFL/Fonts/Leland/
%fontfiles -z 1
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
