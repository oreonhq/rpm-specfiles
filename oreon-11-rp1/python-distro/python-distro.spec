%global source0_hash 2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python-distro
Version: 1.9.0
Release: 1%{?dist}
Summary: OS distribution information for Python
License: Apache-2.0
URL: https://github.com/python-distro/distro
Source0: https://files.pythonhosted.org/packages/source/d/distro/distro-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
%endif

Provides: python3-distro = %{version}-%{release}
Requires: python3

%description
distro looks up the OS distribution.

%prep
%oreon_sha256
%autosetup -n distro-%{version} -p1

%build
%oreon_py_build

%install
%oreon_py_install
%oreon_py_save_files distro

%files -f %{oreon_py_files}
%license LICENSE
