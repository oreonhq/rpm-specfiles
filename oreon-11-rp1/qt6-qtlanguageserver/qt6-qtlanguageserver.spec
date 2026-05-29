%global source0_hash 94f90484be8e49d3eb3bfcf0ba6cb2d8a170fc831c78de138332feebdf193964

%global qt_module qtlanguageserver

%global debug_package %{nil}

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

Summary: Qt6 - LanguageServer component
Name:    qt6-%{qt_module}
Version: 6.10.3
Release: 2%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

## upstreamable patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
The Qt Language Server component provides an implementation of the Language
Server protocol.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6

%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx

%files devel
%{_qt6_headerdir}/QtJsonRpc/
%{_qt6_headerdir}/QtLanguageServer/
%{_qt6_libdir}/libQt6JsonRpc.a
%{_qt6_libdir}/libQt6JsonRpc.prl
%{_qt6_libdir}/libQt6LanguageServer.a
%{_qt6_libdir}/libQt6LanguageServer.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtLanguageServer*
%{_qt6_libdir}/cmake/Qt6JsonRpcPrivate/
%{_qt6_libdir}/cmake/Qt6LanguageServerPrivate/
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_jsonrpc*.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_languageserver*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/JsonRpcPrivate.json
%{_qt6_libdir}/qt6/modules/LanguageServerPrivate.json
#{_qt6_libdir}/pkgconfig/*.pc


%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-2
- Sync module to Qt 6.10.3 (match qt6-qtbase / qt6-rpm-macros)

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-2
- bump release (retry failed build)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-1
- Prepare for Oreon 11 (RP1)
