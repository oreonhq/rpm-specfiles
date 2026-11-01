%global source0_hash ebb65ef6ca439333c2bb41a0c1990587288da07f6c7fd07cb3a18cc18d30ce19

Name: libsodium
Version: 1.0.20
Release: 1%{?dist}
Summary: A modern cryptographic library
License: ISC
URL: https://libsodium.org/
Source0: https://download.libsodium.org/libsodium/releases/libsodium-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: oreon-rpm-macros

%description
The crypto library OpenLDAP uses for Argon2 password hashing.

%package devel
Summary: Development files for libsodium
Requires: libsodium%{?_isa} = %{version}-%{release}

%description devel
Headers and the pkgconfig file for libsodium.

%prep
%autosetup -n libsodium-%{version} -p1
%oreon_sha256

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
