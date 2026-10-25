%global source0_hash 2c1bacd2110f4799f74de6ebb714b94cf6f80fb112316b1219480fd22562148c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: xcb-proto
Version: 1.17.0
Release: 1%{?dist}
Summary: XCB protocol descriptions
License: MIT
URL: https://xcb.freedesktop.org/
Source0: https://www.x.org/releases/individual/xcb/xcb-proto-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: make
BuildRequires: python3
BuildRequires: python3-devel
%endif

%description
XCB protocol descriptions.

%prep
%oreon_sha256
%autosetup -n xcb-proto-%{version} -p1

%build
%oreon_configure
%oreon_make

%install
%oreon_make_install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
