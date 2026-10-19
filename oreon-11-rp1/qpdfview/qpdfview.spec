%global source0_hash 44efc440a461cbdd757a9b396f1461ee7a2f4364e81df55bd0221f910219be99
%global __provides_exclude_from ^%{_libdir}/qpdfview/.*\\.so$
Name:		qpdfview
Version:	0.5.0
Release:        1%{?dist}
License:	GPL-2.0-or-later
Summary:        Tabbed PDF Viewer
Url:		https://launchpad.net/qpdfview
Source0:        https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-0.5.tar.gz
Patch1:		qpdfview-c99.patch
Patch2:         qpdfview-stdc++17.patch
%if 0%{?with_fitz}
%endif
%if 0%{?with_qt5}
%else
%endif
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-qt5 < %{version}-%{release}
Obsoletes:      %{name}-qt6 < %{version}-%{release}
Provides:       %{name}-qt%{?with_qt5:5}%{!?with_qt5:6} = %{version}-%{release}
# oreon:deps
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt5-qttools-devel
# /oreon:deps
%description
qpdfview is a tabbed PDF viewer.
It uses the Poppler library for rendering and CUPS for printing.
It provides a clear and simple graphical user interface using the Qt framework.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-0.5
%patch -P 1 -p1
%patch -P 2 -p1

%build

%if 0%{?with_qt5}
lrelease-qt5 qpdfview.pro
%{qmake_qt5} \
%else
lrelease-qt6 qpdfview.pro
%{qmake_qt6} \
%endif
    TARGET_INSTALL_PATH="%{_bindir}" \
    PLUGIN_INSTALL_PATH="%{_libdir}/%{name}" \
    DATA_INSTALL_PATH="%{_datadir}/%{name}" \
    MANUAL_INSTALL_PATH="%{_mandir}/man1" \
    ICON_INSTALL_PATH="%{_datadir}/icons/hicolor/scalable/apps" \
    LAUNCHER_INSTALL_PATH="%{_datadir}/applications" \
    APPDATA_INSTALL_PATH="%{_metainfodir}" \
%if 0%{?with_fitz}
    CONFIG+=with_fitz \
    FITZ_PLUGIN_LIBS="-lmupdf" \
%endif
    qpdfview.pro
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt --without-mo
install -Dm 0644 icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
