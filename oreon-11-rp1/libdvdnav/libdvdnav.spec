%global source2_hash 44323ffc2f7fdf7a4d7d7cff940d5961a2436abc86e5cfa309644bae0a203b2f
%global source1_hash a66cecca8de03524605482788c3d7734e089534b5b657e1ba6eb309a336c1588
%global source0_hash a2a18f5ad36d133c74bf9106b6445806fa253b09141a46392550394b647b221e
%global abi 4
Name:           libdvdnav
Version:        7.0.0
Release:        1%{?dist}
Summary:        A library for reading DVD video discs based on Ogle code
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://dvdnav.mplayerhq.hu/
Source0:        https://download.videolan.org/pub/videolan/libdvdnav/%{version}/libdvdnav-%{version}.tar.xz
Source1:        https://download.videolan.org/pub/videolan/libdvdnav/%{version}/libdvdnav-%{version}.tar.xz.asc
Source2:        https://download.videolan.org/pub/keys/7180713BE58D1ADC.asc
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libdvdread-devel
BuildRequires:  meson
# /oreon:deps
%description
libdvdnav provides a simple library for reading DVD video discs.
The code is based on Ogle and used in, among others, the Xine dvdnav plug-in.

%package        devel
Summary:        Development files for libdvdnav
Requires:       %{name} = %{version}-%{release}
Requires:       libdvdread-devel >= 6.0.0
Requires:       pkgconfig
%description    devel
libdvdnav-devel contains the files necessary to build packages that use the
libdvdnav library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

%build

%meson \
  -Ddefault_library=shared \
  -Denable_docs=true \
  -Denable_examples=true
%meson_build
%install
%meson_install
rm %{buildroot}%{_pkgdocdir}/{COPYING,TODO,AUTHORS,ChangeLog,README.md}
mv %{buildroot}%{_pkgdocdir}/ docdir/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdvdnav-devel -f %{oreon_filedir}/libdvdnav-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0.0-1
- Prepare for Oreon 11 (RP1)
