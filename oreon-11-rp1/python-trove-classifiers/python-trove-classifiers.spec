%global source0_hash 0a9ebc8d4e2f3e8a22848c5258033035bec17a3012ac3fea16dbaa764489eb71
Name:           python-trove-classifiers
Version:        2026.9.21.13
Release:        1%{?dist}
Summary:        Canonical source for classifiers on PyPI _pypi.org_.
License:        ...
URL:            https://github.com/pypa/trove-classifiers
Source0:        https://files.pythonhosted.org/packages/source/t/trove_classifiers/trove_classifiers-%{version}.tar.gz
BuildArch:      noarch
Patch:          Move-to-PEP-621-declarative-metadata.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-trove-classifiers = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-trove-classifiers
Summary:        Canonical source for classifiers on PyPI _pypi.org_.
%description -n python3-trove-classifiers

%prep

%autosetup -p1 -n trove_classifiers-%{version}
sed -i 's/@@VERSION@@/%{version}/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-trove-classifiers usr/lib/python3*/site-packages/trove_classifiers* usr/lib64/python3*/site-packages/trove_classifiers* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/trove_classifiers* usr/lib64/python3*/site-packages/trove_classifiers* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-trove-classifiers -f %{oreon_filedir}/python3-trove-classifiers.list

%changelog

%autochangelog
