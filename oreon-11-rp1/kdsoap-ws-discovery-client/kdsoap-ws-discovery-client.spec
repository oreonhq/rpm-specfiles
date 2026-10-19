%global source0_hash 2cd247c013e75f410659bac372aff93d22d71c5a54c059e137b9444af8b3427a
Name:           kdsoap-ws-discovery-client
Version:        0.4.0
Release:        1%{?dist}
Summary:        Library for finding WS-Discovery devices in the network using Qt6 and KDSoap
License:        GPL-3.0-or-later AND LicenseRef-OASIS AND LicenseRef-WS-Addressing AND LicenseRef-Discovery AND W3C
URL:            https://invent.kde.org/libraries/kdsoap-ws-discovery-client/
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KDSoap-qt6)
BuildRequires:  cmake(Qt6)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development libraries and header files for Qt6 %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KDSoap-qt6)
%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest || :
%files -f %{oreon_filedir}/main.list
%files -n kdsoap-ws-discovery-client-devel -f %{oreon_filedir}/kdsoap-ws-discovery-client-devel.list
%files -n kdsoap-ws-discovery-client-doc -f %{oreon_filedir}/kdsoap-ws-discovery-client-doc.list

%changelog

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.0-2
- Rebuild

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.0-1
- Import EL10 kdsoap-ws-discovery-client for kio-extras
