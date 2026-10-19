%global source0_hash 91b2b4da3aae9a7088d84acaf2ea0abee3f4fd9c0d2eae69a9b9122a71476590
Name:           python-subprocess-tee
Version:        0.4.2
Release:        1%{?dist}
Summary:        subprocess-tee
License:        MIT
URL:            https://github.com/pycontribs/subprocess-tee
Source0:        https://files.pythonhosted.org/packages/source/s/subprocess_tee/subprocess_tee-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Remove-unnecessary-test-deps.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 7.0.0
Requires:       python3-subprocess-tee = %{version}-%{release}
# /oreon:deps
%package -n       python3-subprocess-tee+docs
Summary:        Metapackage for python3-subprocess-tee docs extras
Requires:       python3-subprocess-tee = %{version}-%{release}
Provides:       python3dist(subprocess-tee[docs]) = %{version}-%{release}

%description -n python3-subprocess-tee+docs
Metapackage for python3-subprocess-tee docs extras.

%package -n       python3-subprocess-tee+test
Summary:        Metapackage for python3-subprocess-tee test extras
Requires:       python3-subprocess-tee = %{version}-%{release}
Requires:       python3dist(enrich) >= 1.2.6
Requires:       python3dist(molecule) >= 3.4.0
Requires:       python3dist(pytest-cov) >= 2.12.1
Requires:       python3dist(pytest-plus) >= 0.2
Requires:       python3dist(pytest-xdist) >= 2.3.0
Requires:       python3dist(pytest) >= 6.2.5
Provides:       python3dist(subprocess-tee[test]) = %{version}-%{release}

%description -n python3-subprocess-tee+test
Metapackage for python3-subprocess-tee test extras.

%description

%package -n     python3-subprocess-tee
Summary:        subprocess-tee
%description -n python3-subprocess-tee

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir subprocess_tee-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-subprocess-tee usr/lib/python3*/site-packages/subprocess_tee* usr/lib64/python3*/site-packages/subprocess_tee* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/subprocess_tee* usr/lib64/python3*/site-packages/subprocess_tee* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-subprocess-tee -f %{oreon_filedir}/python3-subprocess-tee.list

%changelog

%autochangelog
