%global source0_hash 9194f6513955d0fd7300f67158175064460197abab1a92fa127a67a4b0b71530

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

%bcond_without qt5
%bcond_without qt6

Name:    qwt
Summary: Qt Widgets for Technical Applications
Version: 6.2.0
Release: 11%{?dist}

License: LGPL-2.1-or-later WITH Qwt-exception-1.0
URL:     http://qwt.sourceforge.net
Source:  http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

## upstream patches

## upstreamable patches
# Use QT_INSTALL_ paths instead of custom prefix
Patch51: qwt-qt_install_paths.patch
# Add qt suffix to libraries to make them parallel-installable
Patch52: qwt-libsuffix.patch
# Kill rpath
Patch53: qwt-no_rpath.patch
# Fix incorrect requires in pkgconfig files
Patch54: qwt-pkgconfig.patch

BuildRequires: make

%description
The Qwt library contains GUI Components and utility classes which are primarily
useful for programs with a technical background.
Besides a 2D plot widget it provides scales, sliders, dials, compasses,
thermometers, wheels and knobs to control or display values, arrays
or ranges of type double.

%package doc
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.

%if %{with qt5}
%package qt5
Summary: Qt5 Widgets for Technical Applications
BuildRequires: pkgconfig(Qt5Concurrent) pkgconfig(Qt5PrintSupport) pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5OpenGL) pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Designer)
Provides: qwt6-qt5 = %{version}-%{release}
Provides: qwt6-qt5%{_isa} = %{version}-%{release}
%description qt5
%{summary}.

%package qt5-devel
Summary:  Development files for %{name}-qt5
Provides: qwt6-qt5-devel = %{version}-%{release}
Provides: qwt6-qt5-devel%{_isa} = %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.
%endif

%if %{with qt6}
%package qt6
Summary: Qt6 Widgets for Technical Applications
BuildRequires: pkgconfig(Qt6Concurrent) pkgconfig(Qt6PrintSupport) pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6OpenGL) pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Designer)
Provides: qwt6-qt6 = %{version}-%{release}
Provides: qwt6-qt6%{_isa} = %{version}-%{release}
%description qt6
%{summary}.

%package qt6-devel
Summary:  Development files for %{name}-qt6
Provides: qwt6-qt6-devel = %{version}-%{release}
Provides: qwt6-qt6-devel%{_isa} = %{version}-%{release}
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%if %{with qt5}
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%{qmake_qt5} QWT_CONFIG+=QwtPkgConfig ..

%make_build
popd
%endif

%if %{with qt6}
mkdir %{_target_platform}-qt6
pushd %{_target_platform}-qt6
%{qmake_qt6} QWT_CONFIG+=QwtPkgConfig ..

%make_build
popd
%endif

%install
%if %{with qt5}
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}-qt5
%endif
%if %{with qt6}
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}-qt6
%endif

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mkdir -p %{buildroot}%{_mandir}

# Move docs to proper dirs
%if %{with qt5}
# Last build "wins"
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/html %{buildroot}%{_mandir}/*
mv %{buildroot}%{_qt5_docdir}/html/html %{buildroot}%{_defaultdocdir}/%{name}/html
mv %{buildroot}%{_qt5_docdir}/html/man/man3 %{buildroot}%{_mandir}/

%if %{with qt6}
# Last build "wins"
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/html %{buildroot}%{_mandir}/*
mv %{buildroot}%{_qt6_docdir}/html/html %{buildroot}%{_defaultdocdir}/%{name}/html
mv %{buildroot}%{_qt6_docdir}/html/man/man3 %{buildroot}%{_mandir}/
%endif
%endif

%files doc
%doc %{_defaultdocdir}/%{name}/
%{_mandir}/man3/*

%if %{with qt5}
%files qt5
%license COPYING
%doc README
%{_qt5_libdir}/libqwt-qt5.so.6*

%files qt5-devel
%{_qt5_headerdir}/qwt/
%{_qt5_libdir}/libqwt-qt5.so
%{_qt5_libdir}/pkgconfig/Qt5Qwt6.pc
%{_qt5_archdatadir}/mkspecs/features/qwt*
%{_qt5_plugindir}/designer/libqwt_designer_plugin.so
%endif

%if %{with qt6}
%files qt6
%license COPYING
%doc README
%{_qt6_libdir}/libqwt-qt6.so.6*

%files qt6-devel
%{_qt6_headerdir}/qwt/
%{_qt6_libdir}/libqwt-qt6.so
%{_qt6_libdir}/pkgconfig/Qt6Qwt6.pc
%{_qt6_archdatadir}/mkspecs/features/qwt*
%{_qt6_plugindir}/designer/libqwt_designer_plugin.so
%endif

%changelog
%autochangelog
