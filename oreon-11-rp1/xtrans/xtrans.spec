%global source0_hash faafea166bf2451a173d9d593352940ec6404145c5d1da5c213423ce4d359e92
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: xtrans
Version: 1.6.0
Release: 3%{?dist}
Summary: X11 network transport code
License: MIT
URL: https://www.x.org/
Source0: https://www.x.org/releases/individual/lib/xtrans-%{version}.tar.xz
Provides: xorg-x11-xtrans-devel = %{version}-%{release}
Obsoletes: xorg-x11-xtrans-devel < 1.6.1

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconf
%endif

%description
X11 network transport code

%prep
%oreon_sha256
%autosetup -n xtrans-%{version} -p1

%build
%oreon_configure --disable-docs
%oreon_make

%install
%oreon_make_install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
