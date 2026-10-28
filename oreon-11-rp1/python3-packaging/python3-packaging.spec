%global source0_hash d443872c98d677bf60f6a1f2f8c1cb748e8fe762d2bf9d3148b5599295b0fc4f
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python3-packaging
Version: 25.0
Release: 9%{?dist}
Summary: Core utilities for Python packages
License: Apache-2.0 OR BSD-2-Clause
URL: https://github.com/pypa/packaging
Source0: https://files.pythonhosted.org/packages/source/p/packaging/packaging-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3
%endif
Requires: python3

%description
Core utilities for Python packages.

%prep
%oreon_sha256
%autosetup -n packaging-%{version} -p1

%build

%install
sitelib=$(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib"))')
mkdir -p %{buildroot}$sitelib
cp -a src/packaging %{buildroot}$sitelib/
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license LICENSE LICENSE.APACHE LICENSE.BSD
