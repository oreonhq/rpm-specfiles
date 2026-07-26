%global source0_hash 542cb151461263216a4e37c3fd9afc425feeaf38aaa3025cd2a981fadb422235

%bcond_without unittests
%global modname munch

Name:               python-munch
Version:            4.0.0
Release:            7%{?dist}
Summary:            A dot-accessible dictionary (a la JavaScript objects)

License:            MIT
URL:                https://pypi.io/project/munch
Source0:            %pypi_source %{modname}

# Compatibility with Python 3.13 which has added more class attributes
# https://github.com/Infinidat/munch/pull/104
Patch:              Adjust-tests-for-Python-3.13.patch

BuildArch:          noarch

BuildRequires:      python3-devel

%if %{with unittests}
# the testing extra combines coverage, pylint, etc.
# tox uses the testing extra and runs coverage command
# we'll use pytest directly instead to avoid all those dependencies
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:      python3-pytest
%endif

%global _description %{expand:
munch is a fork of David Schoonover's **Bunch** package, providing similar
functionality. 99% of the work was done by him, and the fork was made
mainly for lack of responsiveness for fixes and maintenance on the original
code.

Munch is a dictionary that supports attribute-style access, a la
JavaScript.}

%description %_description

%package -n python3-munch
Summary:            %{summary}
# This could go away in a subsequent release as per https://github.com/Infinidat/munch/pull/64
Requires:           %{py3_dist setuptools}

%description -n python3-munch %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires %{?with_unittests:-x yaml}

# Remove shebang to make rpmlint happy.
sed -i '/\/usr\/bin\/python/d' munch/__init__.py

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files munch

%check
%pyproject_check_import
%if %{with unittests}
%pytest
%endif

%files -n python3-munch -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
