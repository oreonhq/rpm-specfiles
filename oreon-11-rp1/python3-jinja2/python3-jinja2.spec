%global source0_hash 0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python3-jinja2
Version: 3.1.6
Release: 8%{?dist}
Summary: Template engine for Python
License: BSD-3-Clause
URL: https://github.com/pallets/jinja
Source0: https://files.pythonhosted.org/packages/source/j/jinja2/jinja2-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3
%endif
Requires: python3
Requires: python3-markupsafe

%description
Template engine for Python.

%prep
%oreon_sha256
%autosetup -n jinja2-%{version} -p1

%build

%install
sitelib=$(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib"))')
mkdir -p %{buildroot}$sitelib
cp -a src/jinja2 %{buildroot}$sitelib/
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license LICENSE.txt
