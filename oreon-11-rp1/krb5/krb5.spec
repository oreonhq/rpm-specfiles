%global source0_hash 3243ffbc8ea4d4ac22ddc7dd2a1dc54c57874c40648b60ff97009763554eaf13

Name: krb5
Version: 1.22.2
Release: 13%{?dist}
Summary: Kerberos network authentication
License: MIT
URL: https://web.mit.edu/kerberos/
Source0: https://web.mit.edu/kerberos/dist/krb5/1.22/krb5-%{version}.tar.gz
Patch0: https://github.com/krb5/krb5/commit/ceee5d558a2be93a9b2df717be1ea42c5d83ee51.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: bison
BuildRequires: flex
BuildRequires: openssl-devel
BuildRequires: keyutils-libs-devel
BuildRequires: libverto-devel
BuildRequires: readline-devel
BuildRequires: groff
BuildRequires: oreon-rpm-macros

%description
The Kerberos libraries and the client programs that use them.

%package devel
Summary: Development files for Kerberos
Requires: krb5%{?_isa} = %{version}-%{release}
Requires: openssl-devel
Requires: keyutils-libs-devel
Requires: libverto-devel

%description devel
Headers and the pkgconfig files for building against Kerberos.

%prep
%autosetup -n krb5-%{version} -p1
%oreon_sha256
sed -i 's/ error=discarded-qualifiers / /' src/configure
! grep -q 'error=discarded-qualifiers' src/configure

%build
cd src
%oreon_configure \
  --with-crypto-impl=openssl \
  --with-system-verto \
  --without-ldap
%oreon_make

%install
cd src
%oreon_make_install
find %{buildroot} -name '*.la' -delete
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license NOTICE

%files devel -f %{_builddir}/%{name}-devel.files
