%global source0_hash 9f96d8eb974944aa788c10e6ef610bf74b12b6dbd5257acacec78962b7753f40

Name:	 qt5-qtstyleplugins
Summary: Classic Qt widget styles
Version: 5.0.0
Release: 59%{?dist}
# Automatically converted from old format: LGPLv2 or GPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2 OR GPL-2.0-only
URL:	 https://github.com/qtproject/qtstyleplugins
Source0: http://download.qt.io/community_releases/additional_qt_src_pkgs/qtstyleplugins-src-%{version}.tar.gz

## upstream (in lookaside cache)
BuildRequires: make
BuildRequires: git-core
Patch1: 0001-Cleanlooks-style-Fix-floating-point-exception.patch
Patch2: 0002-Sync-QStyleHelper-code-with-the-latest-code-in-qtbas.patch
Patch3: 0003-Import-gtk2-style-from-qtbase.patch
Patch4: 0004-QGtkStyle-fix-spinbox-arrows.patch
Patch5: 0005-Ensure-the-right-color-is-used-for-drawing-the-label.patch
Patch6: 0006-GTK-style-Disable-Ubuntu-scrollbars.patch
Patch7: 0007-Relocate-bb10style-from-qtbase.patch
Patch8: 0008-gtk2-style-get-rid-of-GConf-usage.patch
Patch9: 0009-Import-gtk2-platform-theme-from-qtbase-5.6.patch
Patch10: 0010-Allow-building-of-gtk2-style-when-GConf-is-missing.patch
Patch11: 0011-skip-building-gtk2-platform-theme-if-gtk-2.0-is-miss.patch
Patch12: 0012-Remove-use-of-deprecated-QStyleOption-V-N.patch
Patch13: 0013-Add-Q_DECL_OVERRIDE.patch
Patch14: 0014-Build-the-BB10-style-with-Qt-5.7-or-later-only.patch
Patch15: 0015-Add-missing-PLUGIN_CLASS_NAMEs.patch
Patch16: 0016-Remove-obsolete-and-unused-QBB10StylePlugin-keys.patch
Patch17: 0017-Remove-unused-sync.profile.patch
Patch18: 0018-Fix-build-with-Qt-5.8.0.patch
Patch19: 0019-QCleanlooksStyle-Use-QCommonStyle-instead-of-QProxyS.patch
Patch20: 0020-QPlastiqueStyle-Use-QCommonStyle-instead-of-QProxySt.patch
Patch21: 0021-Plastique-Fix-QSpinBox-height-in-layout.patch
Patch22: 0022-Motif-CDE-Fix-QSpinBox-height-in-layout.patch
Patch23: 0023-Fix-plastique-cleanlooks-and-motif-animation-timer.patch
Patch24: 0024-Fix-build-qt-5.15.patch

## upstreamable patches

BuildRequires: gtk2-devel
BuildRequires: qt5-qtbase-devel >= 5.7
BuildRequires: qt5-qtbase-static
BuildRequires: qt5-qtbase-private-devel

# Do not check gtk2-related files for for requires.
# If the required libraries are not there, the platform/style to integrate
# with isn't either. Then Qt will just silently ignore the plugin.
%global __requires_exclude_from ^(%{_qt5_plugindir}/platformthemes/libqgtk2.so|%{_qt5_plugindir}/styles/libqgtk2style.so)$

%description
%{summary}, including cleanlooks, motif, plastique, qgtk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n qtstyleplugins-src-%{version} -Sgit

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} ..
%make_build
popd

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%files
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_QCleanlooksStylePlugin.cmake
%{_qt5_plugindir}/styles/libqcleanlooksstyle.so
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_QMotifStylePlugin.cmake
%{_qt5_plugindir}/styles/libqmotifstyle.so
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_QPlastiqueStylePlugin.cmake
%{_qt5_plugindir}/styles/libqplastiquestyle.so
# qgtk2 platform/style
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_QGtk2StylePlugin.cmake
%{_qt5_plugindir}/styles/libqgtk2style.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QGtk2ThemePlugin.cmake
%{_qt5_plugindir}/platformthemes/libqgtk2.so
# bb10
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_QBB10StylePlugin.cmake
%{_qt5_plugindir}/styles/libbb10styleplugin.so

%changelog
%autochangelog
