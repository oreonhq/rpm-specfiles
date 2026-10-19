%global source0_hash 85a9dec2f48976b0d800aa7692346fc2967b6195c0e524195f02a110535010e0
%global libcurl_version 7.52.0
%undefine __cmake_in_source_build
%bcond_without zchunk
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%bcond_with use_gpgme
%bcond_with use_selinux
%else
%bcond_without use_gpgme
%bcond_without use_selinux
%endif
%bcond_with run_gnupg_user_socket
%bcond_with sanitizers
%if %{with use_gpgme} && %{with use_selinux}
%global need_selinux 1
%else
%global need_selinux 0
%endif
%global dnf_conflict 2.8.8
Name:           librepo
Version:        1.21.1
Release:        1%{?dist}
Summary:        Repodata downloading library
License:        LGPL-2.1-or-later
URL:            https://github.com/rpm-software-management/librepo
Source0:        https://github.com/rpm-software-management/librepo/archive/refs/tags/1.21.1.tar.gz#/librepo-1.20.0.tar.gz
%if %{with use_gpgme}
%else
%endif
%if %{with zchunk}
%endif
Requires:       libcurl%{?_isa} >= %{libcurl_version}
%if %{with sanitizers}
%endif
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libattr-devel
BuildRequires:  libcurl-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(zck)
BuildRequires:  python3-devel
BuildRequires:  python3-gpg
BuildRequires:  python3-pyxattr
BuildRequires:  python3-requests
BuildRequires:  python3-sphinx
# /oreon:deps
%description
A library providing C and Python (libcURL like) API to downloading repository
metadata.

%package devel
Summary:        Repodata downloading library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with zchunk}
Requires:       zchunk-devel%{?_isa}
%endif
%description devel
Development files for librepo.

%package -n python3-%{name}
Summary:        Python 3 bindings for the librepo library
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires:  python3-gpg
BuildRequires:  python3-pyxattr
BuildRequires:  python3-requests
BuildRequires:  python3-sphinx
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      platform-python-%{name} < %{version}-%{release}
Conflicts:      python3-dnf < %{dnf_conflict}
%description -n python3-%{name}
Python 3 bindings for the librepo library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -DWITH_ZCHUNK=%{?with_zchunk:ON}%{!?with_zchunk:OFF} \
    -DUSE_GPGME=%{?with_use_gpgme:ON}%{!?with_use_gpgme:OFF} \
    -DUSE_RUN_GNUPG_USER_SOCKET=%{?with_run_gnupg_user_socket:ON}%{!?with_run_gnupg_user_socket:OFF} \
    -DWITH_SANITIZERS=%{?with_sanitizers:ON}%{!?with_sanitizers:OFF} \
    -DENABLE_SELINUX=OFF
%cmake_build
%check

%ctest
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n librepo-devel -f %{oreon_filedir}/librepo-devel.list
%files -n python3-librepo -f %{oreon_filedir}/python3-librepo.list

%changelog

%autochangelog
