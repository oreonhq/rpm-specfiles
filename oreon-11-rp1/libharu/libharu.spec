%global source0_hash ec8f327520d1d354ce58b5d2af75b64f380cddc522437c169463b39760921348
Name:           libharu
Version:        2.4.6
%global sover %(v=%{version}; echo ${v%.*})
Release:        1%{?dist}
Summary:        C library for generating PDF files
License:        zlib-acknowledgement
URL:            http://libharu.org
Source0:        https://github.com/libharu/libharu/archive/refs/tags/v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
libHaru is a library for generating PDF files. 
It is free, open source, written in ANSI C and cross platform.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake -DLIBHPDF_STATIC=NO
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libharu-devel -f %{oreon_filedir}/libharu-devel.list

%changelog

%autochangelog
