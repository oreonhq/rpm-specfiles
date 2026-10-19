%global source0_hash c08e7b51ba4c98eed77ac3f3c6e336ed6163647d9e27ea1d928f79b542178cbe
Name:           python-pytest-mpl
Version:        0.19.0
Release:        1%{?dist}
Summary:        pytest plugin to help with testing figures output from Matplotlib
License:        BSD-2-Clause
URL:            https://github.com/matplotlib/pytest-mpl
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_mpl/pytest_mpl-%{version}.tar.gz
BuildArch:      noarch
Patch0001:      0001-Increase-tolerance-for-new-FreeType.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
BuildRequires:  python3dist(setuptools-scm[simple]) >= 8
Requires:       python3-pytest-mpl = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-mpl+test
Summary:        Metapackage for python3-pytest-mpl test extras
Requires:       python3-pytest-mpl = %{version}-%{release}
Requires:       python3dist(pytest-cov) >= 6.0.0
Provides:       python3dist(pytest-mpl[test]) = %{version}-%{release}

%description -n python3-pytest-mpl+test
Metapackage for python3-pytest-mpl test extras.

%package -n       python3-pytest-mpl+docs
Summary:        Metapackage for python3-pytest-mpl docs extras
Requires:       python3-pytest-mpl = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.0.0
Requires:       python3dist(mpl-sphinx-theme) >= 3.9.0
Requires:       python3dist(sphinx-design) >= 0.6.0
Requires:       python3dist(matplotlib) == 3.10.*
Provides:       python3dist(pytest-mpl[docs]) = %{version}-%{release}

%description -n python3-pytest-mpl+docs
Metapackage for python3-pytest-mpl docs extras.

%description

%package -n     python3-pytest-mpl
Summary:        pytest plugin to help with testing figures output from Matplotlib
# oreon:reqs
Requires:       python3dist(jinja2) >= 2.10.2
Requires:       python3dist(matplotlib) >= 3.5.3
Requires:       python3dist(packaging) >= 22.0.0
Requires:       python3dist(pillow) >= 8.1.1
Requires:       python3dist(pytest) >= 6.2.5
# /oreon:reqs
%description -n python3-pytest-mpl

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_mpl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-mpl usr/lib/python3*/site-packages/pytest_mpl* usr/lib64/python3*/site-packages/pytest_mpl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_mpl* usr/lib64/python3*/site-packages/pytest_mpl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-mpl -f %{oreon_filedir}/python3-pytest-mpl.list

%changelog

%autochangelog
