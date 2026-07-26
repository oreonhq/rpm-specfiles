%global source0_hash 64ae16dbda66c3db775ef596828d8d7adda09c6f34dd85099c119e4ff8cfe5b6

%global srcname pytest_doctestplus
%global pkgname pytest-doctestplus

Name:           python-%{pkgname}
Version:        1.7.1
Release:        %autorelease
Summary:        Pytest plugin with advanced doctest features

License:        BSD-3-Clause
URL:            https://github.com/scientific-python/pytest-doctestplus
Source0:        %{pypi_source %srcname}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The doctestplus plugin provides advanced features for testing example Python
code that is included in Python docstrings and in standalone documentation
files.

Good documentation for developers contains example code. This is true of both
standalone documentation and of documentation that is integrated with the
code itself. Python provides a mechanism for testing code snippets that are
provided in Python docstrings. The unit test framework pytest provides a
mechanism for running doctests against both docstrings in source code and in
standalone documentation files.

This plugin augments the functionality provided by Python and pytest by
providing the following features:
* approximate floating point comparison for doctests that produce floating 
  point results 
* skipping particular classes, methods, and functions when running doctests
* handling doctests that use remote data in conjunction with the
  pytest-remotedata plugin
* optional inclusion of *.rst files for doctests}

%description %_description

%package -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Remove egg files from source
rm -r %{srcname}.egg-info

%generate_buildrequires
%pyproject_buildrequires -x test 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst

%changelog
%autochangelog
