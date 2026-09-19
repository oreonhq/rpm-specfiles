%global source0_hash 1a3207b30cffce418423c254b839f6914ed510c675fed5793f83bb1992e95183

%global commit 161e14621640775e98bd7d7f46520b09c84d8f09
%global date 20210927
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: wxmacmolplt
Version: 7.7.3
Release: 6%{?dist}
Summary: A graphics program for plotting 3-D molecular structures and normal modes
License: GPL-2.0-or-later
URL: http://brettbode.github.io/wxmacmolplt/
Source0: https://github.com/brettbode/wxmacmolplt/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: glew-devel
BuildRequires: wxGTK-devel
BuildRequires: automake
Requires: hicolor-icon-theme

%description
MacMolPlt is:
* A modern graphics program for plotting 3-D molecular structures and
  normal modes (vibrations). Modern means:
  o Mouse driven interface for real-time rotation and translation.
  o copy and paste functionality for interfacing to other programs such
    as word processors or other graphics programs (like ChemDraw).
  o simple printing to color or black and white printers (publication
    quality).
  o multiple files open at once.
* It reads a variety of file formats including any GAMESS input, log or
  IRC file directly to create animations of IRC's, DRC's, and
  optimizations. You may also import a $VEC group from any file (such as
  a GAMESS .DAT file). In addition xMol XYZ files, MolDen format files
  and Chemical Markup Language (CML) files are supported. Also some PDB
  file support and MDL MolFile support is included.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
chmod -x MacMolPlt_Manual.html
rm -rv src/glew.{cpp,h}

%build
autoreconf -vif
%configure \
  --docdir=%{_pkgdocdir} \
  --with-glew \
  --with-wx-config=%{_bindir}/wx-config-3.2 \

%make_build

%install
%make_install
install -Dpm644 resources/wxmacmolplt.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/wxmacmolplt.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications resources/wxmacmolplt.desktop
rm %{buildroot}%{_pkgdocdir}/LICENSE

%files
%license LICENSE
%{_bindir}/wxmacmolplt
%{_mandir}/man1/wxmacmolplt.1*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/128x128/apps/wxmacmolplt.png
%{_datadir}/wxmacmolplt

%changelog
%autochangelog
