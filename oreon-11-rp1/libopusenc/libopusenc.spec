%global source0_hash f616d3aff9b2034547894ccb8ab56c36cf1a4acb0d922c5d7119f97bbe58642c
Name:     libopusenc
Version:  0.3
Release:        1%{?dist}
Summary:        A library that provides an easy way to encode Ogg Opus files
License:  LicenseRef-Callaway-BSD
URL:      https://opus-codec.org/
Source0:        https://archive.mozilla.org/pub/opus/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  opus-devel
# /oreon:deps
%description
A library that provides an easy way to encode Ogg Opus files.

%package  devel
Summary:  Development package for libopusenc
Requires: opus-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with libopusenc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
rm -rf %{buildroot}%{_datadir}/doc/libopusenc/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check %{?_smp_mflags} V=1
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libopusenc-devel -f %{oreon_filedir}/libopusenc-devel.list

%changelog

%autochangelog
