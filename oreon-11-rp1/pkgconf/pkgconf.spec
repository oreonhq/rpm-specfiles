%global source0_hash 9371b2f6372da574d4c6dc96fe9b1463037bcf6afcb6671c1555afde7b17e2de
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: pkgconf
Version: 3.0.10
Release: 2%{?dist}
Summary: compiler and linker flags for development libraries
License: ISC
URL: https://gitea.treehouse.systems/ariadne/pkgconf
Source0: https://distfiles.ariadne.space/pkgconf/pkgconf-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make

Provides: pkgconfig = 1:%{version}-%{release}
Provides: pkgconfig%{?_isa} = 1:%{version}-%{release}
Provides: pkg-config = %{version}-%{release}
Provides: pkg-config%{?_isa} = %{version}-%{release}
Provides: pkgconf-pkg-config = %{version}-%{release}
Provides: pkgconf-pkg-config%{?_isa} = %{version}-%{release}
Obsoletes: pkgconf-pkg-config < %{version}-%{release}
Provides: pkgconf-m4 = %{version}-%{release}
Obsoletes: pkgconf-m4 < %{version}-%{release}
Provides: libpkgconf = %{version}-%{release}
Provides: libpkgconf%{?_isa} = %{version}-%{release}
Obsoletes: libpkgconf < %{version}-%{release}

%description
pkgconf is a program which helps to configure compiler and linker flags for development libraries. It is a superset of the functionality provided by pkg-config from freedesktop.org, but does not provide bug-compatibility with the original pkg-config.

libpkgconf is a library which provides access to most of pkgconf's functionality, to allow other tooling such as compilers and IDEs to discover and use libraries configured by pkgconf.

%package devel
Summary: compiler and linker flags for development libraries
Requires: pkgconf%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libpkgconf)
Provides: libpkgconf-devel = %{version}-%{release}
Obsoletes: libpkgconf-devel < %{version}-%{release}

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
