%global source0_hash 4f0fd4ca7ecfe511fbc0e012d3c63fce57009f360199e9e9cc2329ed55ec911e
Name:           python-oslo-config
Version:        10.7.0
Release:        1%{?dist}
Summary:        Oslo Configuration API
License:        Apache-2.0
URL:            https://docs.openstack.org/oslo.config
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_config/oslo_config-%{version}.tar.gz
BuildArch:      noarch
Patch0001:  0001-Fix-test_sub_command_multiple-on-Python-3.12.5.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-oslo-config = %{version}-%{release}
# /oreon:deps
%package -n       python3-oslo-config+rst-generator
Summary:        Metapackage for python3-oslo-config rst-generator extras
Requires:       python3-oslo-config = %{version}-%{release}
Requires:       python3dist(rst2txt) >= 1.1.0
Requires:       python3dist(sphinx) >= 1.8.0
Provides:       python3dist(oslo-config[rst-generator]) = %{version}-%{release}

%description -n python3-oslo-config+rst-generator
Metapackage for python3-oslo-config rst-generator extras.

%description

%package -n     python3-oslo-config
Summary:        Oslo Configuration API
%description -n python3-oslo-config

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir oslo_config-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oslo-config usr/lib/python3*/site-packages/oslo_config* usr/lib64/python3*/site-packages/oslo_config* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oslo_config* usr/lib64/python3*/site-packages/oslo_config* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oslo-config -f %{oreon_filedir}/python3-oslo-config.list

%changelog

%autochangelog
