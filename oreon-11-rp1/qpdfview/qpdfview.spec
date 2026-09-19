%global source0_hash 44efc440a461cbdd757a9b396f1461ee7a2f4364e81df55bd0221f910219be99

%if 0%{?rhel} && 0%{?rhel} < 10
%global with_qt5 1
%endif
%if 0%{?fedora} || 0%{?rhel} >= 9
%global with_fitz 1
%endif

%global __provides_exclude_from ^%{_libdir}/qpdfview/.*\\.so$

Name:		qpdfview
Version:	0.5.0
Release:	25%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Summary:	Tabbed PDF Viewer
Url:		https://launchpad.net/qpdfview
Source0:	%{url}/trunk/%{version}/+download/%{name}-0.5.tar.gz
Patch1:		qpdfview-c99.patch
# std::optional requires std=c++17 or later. Fixes:
# /usr/include/poppler/qt5/poppler-form.h:888:6: error: ‘optional’ in namespace ‘std’ does not name a template type
Patch2:         qpdfview-stdc++17.patch

BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	desktop-file-utils
BuildRequires:	file-devel
BuildRequires:	cups-devel
BuildRequires:	hicolor-icon-theme
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(ddjvuapi)
%if 0%{?with_fitz}
BuildRequires:	mupdf-devel
%endif
%if 0%{?with_qt5}
BuildRequires:	qt5-qttools-devel
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
%else
BuildRequires:	qt6-qttools-devel
BuildRequires:	pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Widgets)
%endif

# This package was previously split
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-qt5 < %{version}-%{release}
Obsoletes:      %{name}-qt6 < %{version}-%{release}
Provides:       %{name}-qt%{?with_qt5:5}%{!?with_qt5:6} = %{version}-%{release}

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
# unknown languages (epel7/8, f34) - qpdfview_{ast,ber,nds,rue,zdh}.qm
%if (0%{?rhel} && 0%{?rhel} < 9)
    rm -f %{buildroot}/%{_datadir}/%{name}/%{name}_???.qm
%endif

%files -f %{name}.lang
%license COPYING
%doc CHANGES CONTRIBUTORS README TODO
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help*.html
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
