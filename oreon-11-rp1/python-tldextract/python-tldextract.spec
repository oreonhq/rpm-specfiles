%global source0_hash b3d2b70a1594a0ecfa6967d57251527d58e00bb5a91a74387baa0d87a0678609

%global pypi_name tldextract

Name:           python-%{pypi_name}
Version:        5.3.0
Release:        6%{?dist}
Summary:        Accurately separate the TLD from the registered domain and subdomains of a URL

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/tldextract
Source0:        %{pypi_source %{pypi_name}}
# upstream uses setuptools_scm which picks up "tldextract/.tld_set_snapshot"
# as package data but the source tarball does not contain ".git" so "pip wheel"
# ignores the file by default.
# This patch declares the file as "package_data" explicitly.
# The code assumes this file is always present and uses it as a fallback.
Patch1:         python-tldextract-include-.tld_set_snapshot.patch

BuildArch:      noarch

BuildRequires:  python3-devel
# required for testing, pyproject.toml only contains a "testing" extra which
# contains many developer tools we do not need if we just want to run the test
# suite (e.g. mypy, ruff).
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-responses
BuildRequires:  python3-syrupy

%description
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

This is the Python 3 version of the package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# test_log_snapshot_diff is an integration test and requires network access
# (additionally that test requires python3-pytest-mock which is not available
# in EPEL 7)
TEST_SELECTOR="not test_log_snapshot_diff"

%pytest -k "$TEST_SELECTOR"

%files -n python3-%{pypi_name} -f %{pyproject_files}
# "LICENSE" files is included in "pyproject_files"
%doc README.md
%{_bindir}/tldextract

%changelog
%autochangelog
