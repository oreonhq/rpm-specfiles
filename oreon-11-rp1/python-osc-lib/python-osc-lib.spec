%global source0_hash 5b896de12ed69fb1111d2971467d403b838d414fc27df2024fc50e8652a53f2b
Name:           python-osc-lib
Version:        4.7.0
Release:        1%{?dist}
Summary:        OpenStackClient Library
License:        Apache-2.0
URL:            https://docs.openstack.org/osc-lib/
Source0:        https://files.pythonhosted.org/packages/source/o/osc_lib/osc_lib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-osc-lib = %{version}-%{release}
# /oreon:deps
%package -n       python3-osc-lib+test
Summary:        Metapackage for python3-osc-lib test extras
Requires:       python3-osc-lib = %{version}-%{release}
Requires:       python3dist(fixtures) >= 3.0.0
Requires:       python3dist(testtools) >= 2.2.0
Provides:       python3dist(osc-lib[test]) = %{version}-%{release}

%description -n python3-osc-lib+test
Metapackage for python3-osc-lib test extras.

%description

%package -n     python3-osc-lib
Summary:        OpenStackClient Library
%description -n python3-osc-lib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir osc_lib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-osc-lib usr/lib/python3*/site-packages/osc_lib* usr/lib64/python3*/site-packages/osc_lib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/osc_lib* usr/lib64/python3*/site-packages/osc_lib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-osc-lib -f %{oreon_filedir}/python3-osc-lib.list

%changelog

%autochangelog
