%global source0_hash c6c0d2259945122819f171a32ecea2c349ead889ee28176caaf492143424be42
%bcond_without  tests
Name:           python-pytest-asyncio
Version:        1.4.0
Release:        1%{?dist}
BuildArch:      noarch
Summary:        Pytest support for asyncio
License:        Apache-2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_asyncio/pytest_asyncio-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-pytest-asyncio = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-asyncio+docs
Summary:        Metapackage for python3-pytest-asyncio docs extras
Requires:       python3-pytest-asyncio = %{version}-%{release}
Requires:       python3dist(sphinx) >= 5.3
Requires:       python3dist(sphinx-rtd-theme) >= 1
Requires:       python3dist(sphinx-tabs) >= 3.5
Provides:       python3dist(pytest-asyncio[docs]) = %{version}-%{release}

%description -n python3-pytest-asyncio+docs
Metapackage for python3-pytest-asyncio docs extras.

%package -n       python3-pytest-asyncio+testing
Summary:        Metapackage for python3-pytest-asyncio testing extras
Requires:       python3-pytest-asyncio = %{version}-%{release}
Requires:       python3dist(coverage) >= 6.2
Requires:       python3dist(hypothesis) >= 5.7.1
Provides:       python3dist(pytest-asyncio[testing]) = %{version}-%{release}

%description -n python3-pytest-asyncio+testing
Metapackage for python3-pytest-asyncio testing extras.

%description

%package -n python3-pytest-asyncio
Summary:        Pytest support for asyncio
# oreon:reqs
Requires:       python3dist(backports-asyncio-runner) < 2
Requires:       python3dist(backports-asyncio-runner) >= 1.1
Requires:       python3dist(pytest) < 10
Requires:       python3dist(pytest) >= 8.4
Requires:       python3dist(typing-extensions) >= 4.12
# /oreon:reqs
%description -n python3-pytest-asyncio

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n pytest_asyncio-%{version}

# disable code quality checks in "testing" extras
sed -i '/"coverage>=6.2",/d' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-asyncio usr/lib/python3*/site-packages/pytest_asyncio* usr/lib64/python3*/site-packages/pytest_asyncio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_asyncio* usr/lib64/python3*/site-packages/pytest_asyncio* usr/bin/*

%check

%if %{with tests}
export PYTEST_ADDOPTS="-k '\
not test_asyncio_mark_respects_parametrized_loop_policies and \
not test_asyncio_mark_respects_the_loop_policy and \
not test_asyncio_run_after_async_fixture_does_not_leak_loop and \
not test_can_use_explicit_event_loop_fixture and \
not test_closing_event_loop_in_sync_fixture_teardown_raises_warning and \
not test_event_loop_fixture_finalizer_raises_warning_when_fixture_leaves_loop_unclosed and \
not test_event_loop_fixture_finalizer_raises_warning_when_test_leaves_loop_unclosed and \
not test_event_loop_fixture_asyncgen_error and \
not test_event_loop_already_closed and \
not test_event_loop_fixture_handles_unclosed_async_gen and \
not test_standalone_test_does_not_trigger_warning_about_no_current_event_loop_being_set and \
not test_warns_when_scope_argument_is_present'"
%pytest
%else
%pyproject_check_import
%endif
%files
%files -n python3-pytest-asyncio -f %{oreon_filedir}/python3-pytest-asyncio.list

%changelog

%autochangelog
