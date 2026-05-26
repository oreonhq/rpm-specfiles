# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 a2a18f5ad36d133c74bf9106b6445806fa253b09141a46392550394b647b221e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libdvdread-devel >= 6.0.0
BuildRequires:  meson

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
%oreon_verify_sources
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


%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_libdir}/libdvdnav.so.%{abi}*

%files devel
%doc docdir/*
%{_libdir}/libdvdnav.so
%{_includedir}/dvdnav
%{_libdir}/pkgconfig/dvdnav.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0.0-1
- Prepare for Oreon 11 (RP1)
