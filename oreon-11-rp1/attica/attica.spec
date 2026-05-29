%global source0_hash 3b9c53770862c0b21b7af7ea15951c35831126022bb8d052760d9cf8bd7ee4f8

Name:           attica
Version:        0.4.2
Release:        36%{?dist}
Summary:        Implementation of the Open Collaboration Services API

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/kde/attica
Source0:        https://download.kde.org/stable/attica/attica-0.4.2.tar.bz2

BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(QtNetwork) >= 4.7

%description
Attica is a Qt library that implements the Open Collaboration Services
API version 1.4.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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


%check
# verify pkg-config sanitry/version
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libattica)" = "%{version}"


%ldconfig_scriptlets

%files
%doc AUTHORS README
%doc ChangeLog
%license COPYING
%{_libdir}/libattica.so.0.4*

%files devel
%{_includedir}/attica/
%{_libdir}/libattica.so
%{_libdir}/pkgconfig/libattica.pc


%changelog
* Mon May 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.2-36
- Import from Fedora 44 dist-git, debrand
