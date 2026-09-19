%global source0_hash 45188a7a88a36ca3ec5a3aa04e5fa227f42d17415a6e168fb523375c1aabe291

%global srcname astroML

Name:           python-%{srcname}
Version:        1.0.2.post1
Release:        %autorelease
Summary:        Python tools for machine learning and data mining in Astronomy

License:        BSD-2-Clause
URL:            http://www.astroml.org/
Source0:        %{pypi_source}
Patch:          https://github.com/astroML/astroML/pull/277.patch
# Compatibility with astropy 6
# https://github.com/astroML/astroML/issues/273
Patch:          https://github.com/astroML/astroML/pull/280.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description\
AstroML is a Python module for machine learning and data mining built on\
numpy, scipy, scikit-learn, and matplotlib, and distributed under the\
3-clause BSD license. It contains a growing library of statistical and\
machine learning routines for analyzing astronomical data in python,\
loaders for several open astronomical datasets, and a large suite of\
examples of analyzing and visualizing astronomical datasets.\

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%package doc
Summary:        Docs and examples for the %{srcname} package

%description doc
Documentation and examples for %{srcname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import
%pytest -q %{srcname}/tests

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst

%files doc
%license LICENSE.rst
%doc CHANGES.rst README.rst examples

%changelog
%autochangelog
