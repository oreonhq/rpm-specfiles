%global source0_hash 8d1756fd704f147549f606cd987050fb94b0b1ff621ea6aa4d6bf0b74450468a

Name: libverto
Version: 0.3.2
Release: 1%{?dist}
Summary: Event loop abstraction
License: MIT
URL: https://github.com/latchset/libverto
Source0: https://github.com/latchset/libverto/releases/download/%{version}/libverto-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: libevent-devel
BuildRequires: oreon-rpm-macros

%description
A library that lets callers use one event loop API and run it on libevent.

%package devel
Summary: Development files for libverto
Requires: libverto%{?_isa} = %{version}-%{release}

%description devel
Headers and the pkgconfig file for libverto.

%prep
%autosetup -n libverto-%{version} -p1
%oreon_sha256

%build
%oreon_configure --disable-static --with-libevent --without-glib --without-libev
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
