%global source2_hash 44323ffc2f7fdf7a4d7d7cff940d5961a2436abc86e5cfa309644bae0a203b2f
%global source1_hash 790566ac910c8f05ce38f4100619b6a90f8508af4ef86407c1952fb45c7abfca
%global source0_hash a0d47876548bec806774bbf8dbf20bb19ba139464383156b32eb8e59915b90a9
%global abi 8
Name:           libdvdread
Version:        7.1.1
Release:        1%{?dist}
Summary:        A library for reading DVD video discs based on Ogle code
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND LicenseRef-Fedora-Public-Domain
URL:            https://www.videolan.org/developers/libdvdnav.html
Source0:        https://download.videolan.org/pub/videolan/libdvdread/%{version}/libdvdread-%{version}.tar.xz
Source1:        https://download.videolan.org/pub/videolan/libdvdread/%{version}/libdvdread-%{version}.tar.xz.asc
Source2:        https://download.videolan.org/pub/keys/7180713BE58D1ADC.asc
Provides:       bundled(md5-gcc)
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
# /oreon:deps
%description
libdvdread provides a simple foundation for reading DVD video disks.
It provides the functionality that is required to access many DVDs.

%package        devel
Summary:        Development files for libdvdread
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
libdvdread provides a simple foundation for reading DVD video disks.
It provides the functionality that is required to access many DVDs.

This package contains development files for libdvdread.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

%build

%meson \
  -Ddefault_library=shared \
  -Denable_docs=true \
  -Dlibdvdcss=disabled
%meson_build
%install
%meson_install
mv %{buildroot}%{_pkgdocdir}/ docdir/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdvdread-devel -f %{oreon_filedir}/libdvdread-devel.list

%changelog

%autochangelog
