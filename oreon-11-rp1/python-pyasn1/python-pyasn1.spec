# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6b11616a6bcf3a40e635f082bb232fa57b5e0dd7f517bd7ddd69ec3794508a47
%global source1_hash 677091de870a80aae844b1ca6134f54652fa2c8c5a52aa396440ac3106e941e6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global module pyasn1
%global modules_version 0.4.2

Name:           python-pyasn1
Version:        0.6.5
Release:        1%{?dist}
Summary:        ASN.1 tools for Python
License:        BSD-2-Clause
Source0:        https://github.com/pyasn1/pyasn1/archive/v%{version}.tar.gz
Source1:        https://github.com/pyasn1/pyasn1-modules/archive/v%{modules_version}.tar.gz
URL:            https://github.com/pyasn1/pyasn1
BuildArch:      noarch

%description
This is an implementation of ASN.1 types and codecs in the Python programming
language.

%package -n python3-pyasn1
Summary:    ASN.1 tools for Python 3
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-pyasn1
This is an implementation of ASN.1 types and codecs in the Python 3 programming
language.

%package -n python3-pyasn1-modules
Summary:    Modules for pyasn1
Requires:   python3-pyasn1 >= 0.4.7, python3-pyasn1 < 0.7.0

%description -n python3-pyasn1-modules
ASN.1 types modules for python3-pyasn1.

%package doc
Summary:        Documentation for pyasn1
BuildRequires:  make
BuildRequires:  python3-sphinx

%description doc
%{summary}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%setup -n %{module}-%{version} -q -b1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

pushd ../pyasn1_modules-%{modules_version}
%pyproject_wheel
popd

pushd docs
PYTHONPATH=%{buildroot}%{python3_sitelib} make SPHINXBUILD=sphinx-build-3 html
popd

%install
%pyproject_install

pushd ../pyasn1_modules-%{modules_version}
%pyproject_install
popd

%check
%pytest

%files -n python3-pyasn1
%doc README.md
%license LICENSE.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}.dist-info/

%files -n python3-pyasn1-modules
%{python3_sitelib}/%{module}_modules/
%{python3_sitelib}/%{module}_modules-%{modules_version}.dist-info/

%files doc
%license LICENSE.rst
%doc docs/build/html/*

%changelog
%autochangelog
