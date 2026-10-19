%global stable_kf6 stable
%global source0_hash fb03b04fa7d9b9097ff3570a45ca03aafd5da5f33ead17e5ceecb7b3ecc5cb87
Name:    kpkpass
Version: 26.04.3
Release:        1%{?dist}
Summary:        Library to deal with Apple Wallet pass files
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}
Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if "%(pkg-config --modversion shared-mime-info 2> /dev/null || echo 2.1)" < "2.2"
%global mime 1
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  qt6-doctools
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Archive)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kpkpass-devel -f %{oreon_filedir}/kpkpass-devel.list

%changelog

%autochangelog
