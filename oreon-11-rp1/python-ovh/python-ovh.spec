%global source0_hash d311f08ec17b62cc61216b3dacf03ee89f95a1da9036a595dac29fc9d798b827
Name:           python-ovh
Version:        1.2.0
Release:        1%{?dist}
Summary:        _Official module to perform HTTP requests to the OVHcloud APIs_
License:        ...
URL:            https://github.com/ovh/python-ovh.git
Source0:        https://files.pythonhosted.org/packages/source/o/ovh/ovh-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ovh = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ovh
Summary:        _Official module to perform HTTP requests to the OVHcloud APIs_
%description -n python3-ovh

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ovh-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ovh usr/lib/python3*/site-packages/ovh* usr/lib64/python3*/site-packages/ovh* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ovh* usr/lib64/python3*/site-packages/ovh* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ovh -f %{oreon_filedir}/python3-ovh.list

%changelog

%autochangelog
