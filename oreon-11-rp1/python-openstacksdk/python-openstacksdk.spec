%global source0_hash f533050d7441b6d41c53488434d2f2df79f1f963a4b431695b4c7f49380ea85c
Name:           python-openstacksdk
Version:        4.20.0
Release:        1%{?dist}
Summary:        An SDK for building applications to work with OpenStack
License:        Apache-2.0
URL:            https://docs.openstack.org/openstacksdk
Source0:        https://files.pythonhosted.org/packages/source/o/openstacksdk/openstacksdk-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-openstacksdk = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-openstacksdk
Summary:        An SDK for building applications to work with OpenStack
# oreon:reqs
Requires:       python3dist(cryptography) >= 2.7
Requires:       python3dist(decorator) >= 4.4.1
Requires:       python3dist(dogpile.cache) >= 0.6.5
Requires:       python3dist(iso8601) >= 0.1.11
Requires:       python3dist(jmespath) >= 0.9.0
Requires:       python3dist(jsonpatch) >= 1.16
Requires:       python3dist(keystoneauth1) >= 5.16.0
Requires:       python3dist(os-service-types) >= 1.8.1
Requires:       python3dist(pbr) >= 2.0.0
Requires:       python3dist(platformdirs) >= 3
Requires:       python3dist(psutil) >= 3.2.2
Requires:       python3dist(pyyaml) >= 3.13
# /oreon:reqs
%description -n python3-openstacksdk

%prep
%global oreon_srcdir openstacksdk-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-openstacksdk usr/lib/python3*/site-packages/openstacksdk* usr/lib64/python3*/site-packages/openstacksdk* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openstacksdk* usr/lib64/python3*/site-packages/openstacksdk* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-openstacksdk -f %{oreon_filedir}/python3-openstacksdk.list

%changelog

%autochangelog
