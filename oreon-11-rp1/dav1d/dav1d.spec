%global source0_hash 686616b7c69eb88d44459391ab25cac13b6647a3b288835c5784e71c1514a5c5
Name:           dav1d
Version:        1.5.4
Release:        1%{?dist}
Summary:        AV1 cross-platform Decoder
License:        BSD-2-Clause AND ISC
URL:            https://code.videolan.org/videolan/dav1d
Source0:        https://download.videolan.org/pub/videolan/dav1d/%{version}/dav1d-%{version}.tar.xz
Requires:       libdav1d%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  nasm
BuildRequires:  pkgconfig(libxxhash)
# /oreon:deps
%description
dav1d is a new AV1 cross-platform Decoder, open-source, and focused on speed
and correctness.

%package     -n libdav1d
Summary:        Library files for dav1d
%description -n libdav1d
Library files for dav1d, the AV1 cross-platform Decoder.

%package     -n libdav1d-devel
Summary:        Development files for dav1d
Requires:       libdav1d%{?_isa} = %{version}-%{release}
%description -n libdav1d-devel
Development files for dav1d, the AV1 cross-platform Decoder.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir dav1d-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles libdav1d usr/*/lib*.so.*
%oreon_autofiles libdav1d-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libdav1d -f %{oreon_filedir}/libdav1d.list
%files -n libdav1d-devel -f %{oreon_filedir}/libdav1d-devel.list

%changelog

%autochangelog
