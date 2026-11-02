%global source0_hash aad731aa22118ff327b9b4ddfc4b6f18ef9476586205da88a532e90940b523d2

Name: openldap
Version: 2.7.2
Release: 1%{?dist}
Summary: OpenLDAP libraries and server
License: OLDAP-2.8
URL: https://www.openldap.org/
Source0: https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-%{version}.tgz

BuildRequires: gcc
BuildRequires: make
BuildRequires: groff
BuildRequires: openssl-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: libevent-devel
BuildRequires: libsodium-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: cracklib-devel
BuildRequires: unixODBC-devel
BuildRequires: libxcrypt-devel
BuildRequires: oreon-rpm-macros

%description
The OpenLDAP client libraries, including libldap and liblber, and the slapd server with the mdb backend.

%package devel
Summary: Development files for OpenLDAP
Requires: openldap%{?_isa} = %{version}-%{release}
Requires: cyrus-sasl-devel
Requires: openssl-devel

%description devel
Headers for building against libldap and liblber.

%prep
%autosetup -n openldap-%{version} -p1
%oreon_sha256

%build
%oreon_configure \
  --disable-static \
  --enable-versioning \
  --enable-crypt \
  --enable-argon2 \
  --enable-mdb \
  --enable-modules \
  --with-tls=openssl \
  --with-cyrus-sasl
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
