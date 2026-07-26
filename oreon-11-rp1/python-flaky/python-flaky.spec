%global source0_hash 47204a81ec905f3d5acfbd61daeabcada8f9d4031616d9bcb0618461729699f5

Name:           python-flaky
Version:        3.8.1
Release:        %autorelease
Summary:        Plugin for pytest that automatically reruns flaky tests
License:        Apache-2.0
URL:            https://github.com/box/flaky
Source:         %{pypi_source flaky}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
Flaky is a plugin for pytest that automatically reruns flaky
tests. Ideally, tests reliably pass or fail, but sometimes test fixtures must
rely on components that aren't 100% reliable. With flaky, instead of removing
those tests or marking them to @skip, they can be automatically retried.

%package -n     python3-flaky
Summary:        %{summary}

%description -n python3-flaky
Flaky is a plugin for pytest that automatically reruns flaky
tests. Ideally, tests reliably pass or fail, but sometimes test fixtures must
rely on components that aren't 100% reliable. With flaky, instead of removing
those tests or marking them to @skip, they can be automatically retried.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n flaky-%{version}

# Use mock from standard library:
sed -i -e 's/import mock/from unittest import mock/' \
       -e 's/from mock/from unittest.mock/' \
       test/test_*/test_*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l flaky

%check
# adapted from upstream's tox.ini
%pytest -v -k 'example and not options' --doctest-modules test/test_pytest/
%pytest -v -k 'example and not options' test/test_pytest/
%pytest -v -p no:flaky test/test_pytest/test_flaky_pytest_plugin.py
%pytest -v --force-flaky --max-runs 2 test/test_pytest/test_pytest_options_example.py

%files -n python3-flaky -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
