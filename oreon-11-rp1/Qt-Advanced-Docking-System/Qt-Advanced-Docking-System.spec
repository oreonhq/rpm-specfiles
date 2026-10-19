%global source0_hash 9ce947acbb1984946f9145c976e42e6984f99b98fb414dd7354a290af6d4ff04
Name:           Qt-Advanced-Docking-System
Summary:        Advanced Docking System for Qt
Version:        5.1.1
Release:        1%{?dist}
License:        LGPL-2.1-or-later AND BSL-1.0 AND Apache-2.0
URL:            https://github.com/githubuser0xFFFF/%{name}
Source0:        https://github.com/githubuser0xFFFF/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DADS_VERSION=%{version}
%cmake_build
%install
%cmake_install
rm -rfv %{buildroot}%{_prefix}/license/ads
rm -rfv %{buildroot}%{_datadir}/ads/license
%oreon_autofiles Qt-Advanced-Docking-System-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n Qt-Advanced-Docking-System-devel -f %{oreon_filedir}/Qt-Advanced-Docking-System-devel.list

%changelog

%autochangelog
