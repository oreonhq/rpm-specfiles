%global source0_hash 1169d376c297e7de388d18b4481760d478b0e99a777cad3a9c86e556f4b697cb

%global pypi_name tenacity
%global _description %{expand:
Tenacity is a general-purpose retrying library to simplify the task of adding
retry behavior to just about anything.}

Name:           python-%{pypi_name}
Version:        9.1.2
Release:        5%{?dist}
Summary:        Retry code until it succeeds
License:        Apache-2.0
URL:            https://github.com/jd/%{pypi_name}
Source:         %{pypi_source}
# Python 3.14 fixes
# https://bugzilla.redhat.com/show_bug.cgi?id=2327977
# Pushed upstream: https://github.com/jd/tenacity/pull/528
# Rebased on tenacity-9.1.2.tar.gz
Patch0:         528.patch
BuildArch:      noarch

%description %{_description}

%package -n python3-%{pypi_name}
Summary:          %{summary}
BuildRequires:    python3-devel
# for tests
BuildRequires:    python3-pytest
BuildRequires:    python3-tornado >= 4.5

%description -n python3-%{pypi_name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p 1
# Avoid type checking dependency
sed -e '/typeguard/d' -i setup.cfg
# [toml] is an empty feature since setuptools switched to builtin tomllib
sed -e 's/setuptools_scm\[toml\]/setuptools_scm/' -i pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -k "not test_retry_type_annotations"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
