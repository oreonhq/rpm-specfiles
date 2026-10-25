%global source0_hash 372225fd40815b8423547f5d890c5debc72e88b91088fbfb13158c20495ccb59
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: xorgproto
Version: 2024.1
Release: 1%{?dist}
Summary: X.Org protocol headers
License: MIT
URL: https://www.x.org/
Source0: https://www.x.org/releases/individual/proto/xorgproto-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: make
BuildRequires: meson
BuildRequires: ninja-build
%endif

%description
X.Org protocol headers.

%prep
%oreon_sha256
%autosetup -n xorgproto-%{version} -p1

%build
%oreon_meson
%oreon_meson_build

%install
%oreon_meson_install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING-x11proto
