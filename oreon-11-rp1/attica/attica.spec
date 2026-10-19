%global source0_hash 3b9c53770862c0b21b7af7ea15951c35831126022bb8d052760d9cf8bd7ee4f8
Name:           attica
Version:        0.4.2
Release:        1%{?dist}
Summary:        Implementation of the Open Collaboration Services API
License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/kde/attica
Source0:        https://download.kde.org/stable/attica/attica-%{version}.tar.bz2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(QtNetwork)
# /oreon:deps
%description
Attica is a Qt library that implements the Open Collaboration Services
API version 1.4.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
%if "%{?_lib}" == "lib64"
  %{?_cmake_lib_suffix64} \
%endif
  -DQT4_BUILD:BOOL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles attica-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libattica)" = "%{version}"
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n attica-devel -f %{oreon_filedir}/attica-devel.list

%changelog

* Mon May 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.2-36
- Import from Fedora 44 dist-git, debrand
