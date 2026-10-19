%global source0_hash a7db850025b95ded1eae8a46181a1a6c56c92c96f0e2b005d9ff8dc0210cab44
Name:           python-idna
Version:        3.20
Release:        1%{?dist}
Summary:        Internationalized Domain Names in Applications _IDNA_
License:        BSD-3-Clause
URL:            https://github.com/kjd/idna
Source0:        https://files.pythonhosted.org/packages/source/i/idna/idna-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-idna = %{version}-%{release}
# /oreon:deps
%package -n       python3-idna+all
Summary:        Metapackage for python3-idna all extras
Requires:       python3-idna = %{version}-%{release}
Requires:       python3dist(ruff) >= 0.16.0
Requires:       python3dist(mypy) >= 1.11.2
Requires:       python3dist(ty) >= 0.0.37
Requires:       python3dist(pytest) >= 8.3.2
Requires:       python3dist(hypothesis) >= 6.141.1
Requires:       python3dist(coverage) >= 7.10.0
Provides:       python3dist(idna[all]) = %{version}-%{release}

%description -n python3-idna+all
Metapackage for python3-idna all extras.

%description

%package -n     python3-idna
Summary:        Internationalized Domain Names in Applications _IDNA_
%description -n python3-idna

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir idna-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-idna usr/lib/python3*/site-packages/idna* usr/lib64/python3*/site-packages/idna* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/idna* usr/lib64/python3*/site-packages/idna* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-idna -f %{oreon_filedir}/python3-idna.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.11-1
- Prepare for Oreon 11 (RP1)
