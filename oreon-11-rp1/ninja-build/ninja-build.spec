%global source0_hash 974d6b2f4eeefa25625d34da3cb36bdcebe7fbce40f4c16ac0835fd1c0cbae17
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: ninja-build
Version: 1.13.2
Release: 3%{?dist}
Summary: Small build system
License: Apache-2.0
URL: https://ninja-build.org/
Source0: https://github.com/ninja-build/ninja/archive/refs/tags/v%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python3
%endif

%description
ninja is a small build system.

%prep
%oreon_sha256
%autosetup -n ninja-%{version} -p1

%build
python3 configure.py --bootstrap

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 ninja %{buildroot}%{_bindir}/ninja
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
