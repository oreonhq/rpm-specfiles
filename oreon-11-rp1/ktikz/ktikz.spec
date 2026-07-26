%global source0_hash 1b7f5b7a8daacea68b5a93c1e5a946c9ba9f776b8708f11ca047e591a446f300

%undefine __cmake_in_source_build

Name:           ktikz
Version:        0.13.2
Release:        15%{?dist}
Summary:        KDE Editor for the TikZ language

# ktikz/qtikz are GPLv2+, documentation is GFDL
License:        GPL-2.0-or-later AND GFDL-1.2-or-later
URL:            https://github.com/fhackenberger/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Use xdg-open instead of kwrite as defaut editor in qtikz
Patch0:         %{name}-0.12-default_editor.patch
# Fix build with CMake 4.0
Patch1:         %{name}-0.13.2-cmake_4.0.patch

BuildRequires:  cmake
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  qt5-qttools-devel
# Required to display help
Requires:       khelpcenter
# pdftops required by ktikz
Requires:       poppler-utils
# Minimum TeX dependencies
Requires:       tex-latex-bin
Requires:       tex(preview.sty)
# Includes PGF documentation, required to display PGF documentation from the
# help menu
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
Requires:       xdg-utils
# Required for the KTikZ SVG icon
Requires:       oflb-prociono-fonts
%{?kde_runtime_requires}

%description
KTikZ is a small application to assist in the creation of diagrams and drawings
using the TikZ macros from the LaTeX package "pgf". It consists of a text editor
pane in which the TikZ code for the drawing is edited and a preview pane showing
the drawing as rendered by LaTeX. The preview pane can be updated in
real-time. Common drawing tools, options and styles are available from the menus
to assist the coding process.

This package contains the KDE version of the program.

%package -n qtikz
Summary:        Editor for the TikZ language
# pdftops required by qtikz
Requires:       poppler-utils
# Required to display help
Requires:       qt5-assistant
# Minimum TeX dependencies
Requires:       tex-latex-bin
Requires:       tex(preview.sty)
# Includes PGF documentation, required to display PGF documentation from the
# help menu
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
Requires:       xdg-utils
# Required for the QTikZ SVG icon
Requires:       oflb-prociono-fonts

%description -n qtikz
QTikZ is a small application to assist in the creation of diagrams and drawings
using the TikZ macros from the LaTeX package "pgf". It consists of a text editor
pane in which the TikZ code for the drawing is edited and a preview pane showing
the drawing as rendered by LaTeX. The preview pane can be updated in
real-time. Common drawing tools, options and styles are available from the menus
to assist the coding process.

This package contains the Qt version of the program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%build
# Build ktikz
%cmake_kf5 \
    -DKTIKZ_TIKZ_DOCUMENTATION_DEFAULT=%{_datadir}/texlive/texmf-dist/doc/generic/pgf/pgfmanual.pdf
%cmake_build

# Build qtikz
%qmake_qt5 \
    KTIKZ_TIKZ_DOCUMENTATION_DEFAULT=%{_datadir}/texlive/texmf-dist/doc/generic/pgf/pgfmanual.pdf
%make_build

%install
# Install ktikz
%cmake_install
# Install qtikz
%make_install INSTALL_ROOT=$RPM_BUILD_ROOT

# Delete qtikz locale files wrongly installed in ktikz directories
rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/

%find_lang %{name} --with-kde --with-html
%find_lang qtikz --with-qt

# Install AppData files
install -Dpm 0644 data/%{name}.appdata.xml $RPM_BUILD_ROOT%{_datadir}/metainfo/%{name}.appdata.xml
# Since no AppData file is provided for qtikz, create one from the ktikz one
sed \
    "s|ktikz\.desktop|qtikz.desktop|g; s|KtikZ|QtikZ|g" \
    data/%{name}.appdata.xml >$RPM_BUILD_ROOT%{_datadir}/metainfo/qtikz.appdata.xml

# Remove useless license file in qtikz directories
rm $RPM_BUILD_ROOT%{_datadir}/qtikz/LICENSE.GPL2

# Install QTikZ icon in /usr/share/icons/ and update desktop file for
# integration with appstream-data
install -Dpm 0644 app/icons/qtikz.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/qtikz.svg
for i in 22 128; do
    install -Dpm 0644 app/icons/qtikz-$i.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x$i/apps/qtikz.png
done
desktop-file-edit --set-icon=qtikz $RPM_BUILD_ROOT%{_datadir}/applications/qtikz.desktop

%check
desktop-file-validate $RPM_BUILD_ROOT%{_kf5_datadir}/applications/%{name}.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qtikz.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/%{name}.appdata.xml
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/qtikz.appdata.xml

%files -f %{name}.lang
%doc Changelog README.md TODO
%license LICENSE.FDL1.2 LICENSE.GPL2
%{_kf5_bindir}/%{name}
%{_kf5_qtplugindir}/*.so
%{_kf5_datadir}/applications/%{name}.desktop
%{_kf5_datadir}/config.kcfg/%{name}.kcfg
%{_kf5_datadir}/%{name}part/
%{_kf5_datadir}/kxmlgui5/%{name}/
%{_kf5_datadir}/kservices5/%{name}part.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*

%files -n qtikz -f qtikz.lang
%doc Changelog README.md TODO
%license LICENSE.FDL1.2 LICENSE.GPL2
%{_bindir}/qtikz
%{_datadir}/applications/qtikz.desktop
%{_datadir}/icons/hicolor/*/apps/qtikz.*
%{_datadir}/mime/packages/qtikz.xml
%dir %{_datadir}/qtikz/
%{_datadir}/qtikz/*.png
%{_datadir}/qtikz/documentation/
%dir %{_datadir}/qtikz/locale/
%{_datadir}/qtikz/templates/
%{_datadir}/metainfo/qtikz.appdata.xml
%{_mandir}/man1/qtikz.1.*

%changelog
%autochangelog
