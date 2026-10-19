%global source0_hash b0349f4829d3d1699a77e199850f870f48d376e2baaf2c69d27b28571c498cfe
%global sover   2
%global common_description %{expand:
Tox is a peer to peer (serverless) instant messenger aimed at making
security and privacy easy to obtain for regular users. It uses NaCl
for its encryption and authentication.}
Name:           toxcore
Version:        0.2.23
Release:        1%{?dist}
Summary:        Peer to peer instant messenger
License:        GPL-3.0-or-later AND MIT
URL:            https://github.com/TokTok/c-toxcore
Source0:        https://github.com/TokTok/c-%{name}/releases/download/v%{version}/c-%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
# /oreon:deps
%description %{common_description}

%package        devel
Summary:        Development files for Toxcore
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{common_description}

This package contains Toxcore development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir c-%{name}-%{version}
%oreon_prep
%build

export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%cmake -DSTRICT_ABI=ON
%cmake_build
%install
%cmake_install
rm -v %{buildroot}/%{_libdir}/*.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n toxcore-devel -f %{oreon_filedir}/toxcore-devel.list

%changelog

%autochangelog
