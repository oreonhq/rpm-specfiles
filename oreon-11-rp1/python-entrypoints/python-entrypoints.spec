%global source0_hash d2197a94aa73e70a7f60600e654ac9918ca2a0ee5480eb875296c42220a02272

%global srcname entrypoints
%global sum Discover and load entry points from installed packages

Name:		python-%{srcname}

# WARNING: Check if an update does not break flake8!
Version:	0.4
Release:	%autorelease
Summary:	%{sum}
# SPDX
License:	MIT

URL:		https://entrypoints.readthedocs.io/
Source0:	https://github.com/takluyver/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Compatibility with Sphinx 8
Patch:		https://github.com/takluyver/entrypoints/pull/50.patch

BuildArch:	noarch
BuildRequires: make
BuildRequires:	python3-devel
BuildRequires:	python3-sphinx

%description
Entry points are a way for Python packages to advertise objects with some
common interface. The most common examples are console_scripts entry points,
which define shell commands by identifying a Python function to run.

The entrypoints module contains functions to find and load entry points.

%package -n python3-%{srcname}
Summary:	%{sum}

%description -n python3-%{srcname}
Entry points are a way for Python packages to advertise objects with some
common interface. The most common examples are console_scripts entry points,
which define shell commands by identifying a Python function to run.

The entrypoints module contains functions to find and load entry points.

%package -n python-%{srcname}-doc
Summary:	Documentation for python-entrypoints

%description -n python-%{srcname}-doc
Documentation files for python-entrypoints

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

pushd doc
make html PYTHON="%{__python3}" SPHINXBUILD=sphinx-build-%{python3_version}
rm _build/html/.buildinfo
popd

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc doc/_build/html
%license LICENSE

%files -n python-%{srcname}-doc
%doc doc/_build/html
%license LICENSE

%changelog
%autochangelog
