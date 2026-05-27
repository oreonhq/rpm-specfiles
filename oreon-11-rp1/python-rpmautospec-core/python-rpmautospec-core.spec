%global source0_hash c0acf19ed013355d02c1e28220ad9d6f9088f7f61b4a29d16d5364298bc6e6f3

# Only use poetry-core on Fedora and new EPEL releases because
# it is missing elsewhere. Fall back to using setuptools instead.
%if ! 0%{?rhel} || 0%{?epel} >= 10
%bcond_without poetry_core
%else
%bcond_with poetry_core
%endif

%global srcname rpmautospec_core
%global canonicalname rpmautospec-core

Name: python-%{canonicalname}
Version: 0.1.5
Release: %autorelease
Summary: Minimum functionality for rpmautospec

License: MIT
URL: https://github.com/fedora-infra/%{canonicalname}
Source0:        https://files.pythonhosted.org/packages/source/r/rpmautospec_core/rpmautospec_core-0.1.5.tar.gz
BuildArch: noarch
BuildRequires: python3-devel >= 3.6.0
# The dependencies needed for testing don’t get auto-generated.
BuildRequires: python3dist(pytest)
BuildRequires: sed

%global _description %{expand:
This package contains minimum functionality to determine if an RPM spec file
uses rpmautospec features.}

%description %_description

%package -n python3-%{canonicalname}
Summary: %{summary}
%if %{without pyproject_build}
%py_provides python3-%{canonicalname}
%endif

%description -n python3-%{canonicalname} %_description

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{srcname}-%{version}
%if %{without poetry_core}
# by renaming the [build-system] section we fallback to setuptools (default per PEP 517)
# this only works because there is also a setup.py file in the sdist
test -f setup.py
sed -i 's/\[build-system\]/[ignore-this]/' pyproject.toml
%endif

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -i -e '/pytest-cov/d; /addopts.*--cov/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}
%if %{with poetry_core}
# Work around poetry not listing license files as such in package metadata.
sed -i -e 's|^\(.*/LICENSE\)|%%license \1|g' %{pyproject_files}
%endif

%check
%pytest

%files -n python3-%{canonicalname} -f %{pyproject_files}
%doc README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.5-1
- Prepare for Oreon 11 (RP1)
