%global source0_hash 1b7f5b7a8daacea68b5a93c1e5a946c9ba9f776b8708f11ca047e591a446f300
%undefine __cmake_in_source_build
Name:           ktikz
Version:        0.13.2
Release:        15%{?dist}
Summary:        KDE Editor for the TikZ language
License:        GPL-2.0-or-later AND GFDL-1.2-or-later
URL:            https://github.com/fhackenberger/%{name}
Source0:        https://github.com/fhackenberger/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.12-default_editor.patch
Patch1:         %{name}-0.13.2-cmake_4.0.patch
Requires:       khelpcenter
Requires:       poppler-utils
Requires:       tex-latex-bin
Requires:       tex(preview.sty)
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
Requires:       xdg-utils
Requires:       oflb-prociono-fonts
%{?kde_runtime_requires}
# oreon:deps
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
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  qt5-qttools-devel
# /oreon:deps
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
Requires:       poppler-utils
Requires:       qt5-assistant
Requires:       tex-latex-bin
Requires:       tex(preview.sty)
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
Requires:       xdg-utils
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

%cmake_kf5 \
    -DKTIKZ_TIKZ_DOCUMENTATION_DEFAULT=%{_datadir}/texlive/texmf-dist/doc/generic/pgf/pgfmanual.pdf
%cmake_build
%qmake_qt5 \
    KTIKZ_TIKZ_DOCUMENTATION_DEFAULT=%{_datadir}/texlive/texmf-dist/doc/generic/pgf/pgfmanual.pdf
%make_build
%install
%cmake_install
%make_install INSTALL_ROOT=$RPM_BUILD_ROOT
rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/
%find_lang %{name} --with-kde --with-html
%find_lang qtikz --with-qt
install -Dpm 0644 data/%{name}.appdata.xml $RPM_BUILD_ROOT%{_datadir}/metainfo/%{name}.appdata.xml
sed \
    "s|ktikz\.desktop|qtikz.desktop|g; s|KtikZ|QtikZ|g" \
    data/%{name}.appdata.xml >$RPM_BUILD_ROOT%{_datadir}/metainfo/qtikz.appdata.xml
rm $RPM_BUILD_ROOT%{_datadir}/qtikz/LICENSE.GPL2
install -Dpm 0644 app/icons/qtikz.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/qtikz.svg
for i in 22 128; do
    install -Dpm 0644 app/icons/qtikz-$i.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x$i/apps/qtikz.png
done
desktop-file-edit --set-icon=qtikz $RPM_BUILD_ROOT%{_datadir}/applications/qtikz.desktop
%oreon_autofiles qtikz usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate $RPM_BUILD_ROOT%{_kf5_datadir}/applications/%{name}.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qtikz.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/%{name}.appdata.xml
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/qtikz.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n qtikz -f %{oreon_filedir}/qtikz.list

%changelog

%autochangelog
