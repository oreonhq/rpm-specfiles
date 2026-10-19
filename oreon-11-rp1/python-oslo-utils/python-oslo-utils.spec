%global source0_hash ba839dea2c1eb415e3ee151c4cc688f52e283f59bc1f77cc86772190a8b34259
Name:           python-oslo-utils
Version:        10.2.0
Release:        1%{?dist}
Summary:        Oslo Utility library
License:        Apache-2.0
URL:            https://docs.openstack.org/oslo.utils
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_utils/oslo_utils-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-oslo-utils = %{version}-%{release}
# /oreon:deps
%package -n       python3-oslo-utils+image-inspection
Summary:        Metapackage for python3-oslo-utils image-inspection extras
Requires:       python3-oslo-utils = %{version}-%{release}
Requires:       python3dist(cryptography) >= 43.0.3
Provides:       python3dist(oslo-utils[image-inspection]) = %{version}-%{release}

%description -n python3-oslo-utils+image-inspection
Metapackage for python3-oslo-utils image-inspection extras.

%description

%package -n     python3-oslo-utils
Summary:        Oslo Utility library
%description -n python3-oslo-utils

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir oslo_utils-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oslo-utils usr/lib/python3*/site-packages/oslo_utils* usr/lib64/python3*/site-packages/oslo_utils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oslo_utils* usr/lib64/python3*/site-packages/oslo_utils* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oslo-utils -f %{oreon_filedir}/python3-oslo-utils.list

%changelog

%autochangelog
