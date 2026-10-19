%global source0_hash a2b1266fd6cb89295dbb79e3442e5ff1c27db35a0b62b84c7846002676d12ae2
Name:           python-testresources
Version:        2.1.2
Release:        1%{?dist}
Summary:        Testresources, a pyunit extension for managing expensive test resources
License:        ...
URL:            https://github.com/testing-cabal/testresources
Source0:        https://files.pythonhosted.org/packages/source/t/testresources/testresources-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-testresources = %{version}-%{release}
# /oreon:deps
%package -n       python3-testresources+test
Summary:        Metapackage for python3-testresources test extras
Requires:       python3-testresources = %{version}-%{release}
Provides:       python3dist(testresources[test]) = %{version}-%{release}

%description -n python3-testresources+test
Metapackage for python3-testresources test extras.

%description

%package -n     python3-testresources
Summary:        Testresources, a pyunit extension for managing expensive test resources
%description -n python3-testresources

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir testresources-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-testresources usr/lib/python3*/site-packages/testresources* usr/lib64/python3*/site-packages/testresources* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/testresources* usr/lib64/python3*/site-packages/testresources* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-testresources -f %{oreon_filedir}/python3-testresources.list

%changelog

%autochangelog
