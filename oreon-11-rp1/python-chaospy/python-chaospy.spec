%global source0_hash a7ab9bd376c5e956a5f263d5b481a0a596e49954531698cc169f0711851d5ae3
Name:           python-chaospy
Version:        4.3.21
Release:        1%{?dist}
Summary:        Numerical tool for performing uncertainty quantification
License:        ...
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/c/chaospy/chaospy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
Requires:       python3-chaospy = %{version}-%{release}
# /oreon:deps
%package -n       python3-chaospy+dev
Summary:        Metapackage for python3-chaospy dev extras
Requires:       python3-chaospy = %{version}-%{release}
Requires:       python3dist(openturns) == 1.23
Requires:       python3dist(black) == 22.10.0
Requires:       python3dist(pylint) == 2.15.5
Requires:       python3dist(pydocstyle) == 3.0.0
Requires:       python3dist(pydata-sphinx-theme) == 0.11.0
Requires:       python3dist(coverage) >= 5.0
Provides:       python3dist(chaospy[dev]) = %{version}-%{release}

%description -n python3-chaospy+dev
Metapackage for python3-chaospy dev extras.

%description

%package -n     python3-chaospy
Summary:        Numerical tool for performing uncertainty quantification
# oreon:reqs
Requires:       python3dist(numpoly) >= 1.2.12
Requires:       python3dist(numpy) >= 1.20
Requires:       python3dist(setuptools) >= 40.9.0
# /oreon:reqs
%description -n python3-chaospy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir chaospy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-chaospy usr/lib/python3*/site-packages/chaospy* usr/lib64/python3*/site-packages/chaospy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/chaospy* usr/lib64/python3*/site-packages/chaospy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-chaospy -f %{oreon_filedir}/python3-chaospy.list

%changelog

%autochangelog
