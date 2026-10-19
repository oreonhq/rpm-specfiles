%global source0_hash 2ed4ecb28320a433db18a5bf029986aa8afcfd740745e78847e330d5d94922a9
%bcond bootstrap 0
%bcond doctests %{without bootstrap}
%bcond matplotlib 1
Name:           python-shapely
Version:        2.1.2
Release:        1%{?dist}
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane
License:        BSD-3-Clause AND Unlicense AND MIT
URL:            https://github.com/shapely/shapely
Source0:        https://files.pythonhosted.org/packages/source/s/shapely/shapely-%{version}.tar.gz
ExcludeArch:    %{ix86}
%if %{with matplotlib}
%endif
%if %{with doctests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy) < 3
BuildRequires:  python3dist(numpy) >= 1.25
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-shapely = %{version}-%{release}
# /oreon:deps
%package -n       python3-shapely+test
Summary:        Metapackage for python3-shapely test extras
Requires:       python3-shapely = %{version}-%{release}
Provides:       python3dist(shapely[test]) = %{version}-%{release}

%description -n python3-shapely+test
Metapackage for python3-shapely test extras.

%package -n       python3-shapely+docs
Summary:        Metapackage for python3-shapely docs extras
Requires:       python3-shapely = %{version}-%{release}
Requires:       python3dist(numpydoc) == 1.1.*
Provides:       python3dist(shapely[docs]) = %{version}-%{release}

%description -n python3-shapely+docs
Metapackage for python3-shapely docs extras.

%description

%package -n python3-shapely
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane
Provides:       bundled(klib-kvec) = 0.1.0
# oreon:reqs
Requires:       python3dist(numpy) >= 1.21
# /oreon:reqs
%description -n python3-shapely

%prep

%autosetup -p1
# Currently, the PyPI sdist does not ship with pre-generated Cython C sources.
# We preventively check for them anyway, as they must be removed if they do
# appear. Note that C sources in src/ are not generated.
find shapely -type f -name '*.c' -print -delete

# Patch out coverage analysis from the “test” extra.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem \
    project.optional-dependencies.test pytest-cov

%if %{without doctests}
tomcli set pyproject.toml lists delitem \
    project.optional-dependencies.test scipy-doctest
%endif

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-shapely usr/lib/python3*/site-packages/shapely* usr/lib64/python3*/site-packages/shapely* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/shapely* usr/lib64/python3*/site-packages/shapely* usr/bin/*

%check

mkdir empty
cd empty
ln -s ../shapely/tests/
%pyproject_check_import -e 'shapely.tests*' %{?!with_matplotlib:-e shapely.plotting}
%pytest -rs -v
%if %{with doctests}
dtk="${dtk-}${dtk+ and }not shapely.constructive.maximum_inscribed_circle"
%pytest --doctest-modules --doctest-only-doctests=true \
    '%{buildroot}%{python3_sitearch}/shapely' \
    --ignore='%{buildroot}%{python3_sitearch}/shapely/tests' \
    -k="${dtk-}" -v
%endif
%files
%files -n python3-shapely -f %{oreon_filedir}/python3-shapely.list

%changelog

%autochangelog
