%global source0_hash 9371b2f6372da574d4c6dc96fe9b1463037bcf6afcb6671c1555afde7b17e2de
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: pkgconf
Version: 3.0.10
Release: 1%{?dist}
Summary: compiler and linker flags for development libraries
License: ISC
URL: https://gitea.treehouse.systems/ariadne/pkgconf
Source0: https://distfiles.ariadne.space/pkgconf/pkgconf-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
pkgconf is a program which helps to configure compiler and linker flags for development libraries. It is a superset of the functionality provided by pkg-config from freedesktop.org, but does not provide bug-compatibility with the original pkg-config.

libpkgconf is a library which provides access to most of pkgconf's functionality, to allow other tooling such as compilers and IDEs to discover and use libraries configured by pkgconf.

%package devel
Summary: compiler and linker flags for development libraries
Requires: pkgconf%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libpkgconf)

%description devel
libpkgconf is a library which provides access to most of pkgconf's functionality, to allow other tooling such as compilers and IDEs to discover and use libraries configured by pkgconf.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
ln -sf pkgconf %{buildroot}%{_bindir}/pkg-config

%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
