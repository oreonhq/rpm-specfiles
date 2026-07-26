%global source0_hash 58e3053e33b423f3594031cb758c3f4d1df931307f1e67928e30cf352df7709f

# Enable tests by default.
%bcond_without  tests

%global modname vcrpy

Name:               python-%{modname}
Version:            8.1.1
Release:            2%{?dist}
Summary:            Automatically mock your HTTP interactions to simplify and speed up testing

License:            MIT
URL:                https://pypi.io/project/%{modname}
Source0:            %pypi_source %{modname}

BuildArch:          noarch

BuildRequires:      python3-devel

%if %{with tests}
BuildRequires:      python3dist(pytest)

# For checking imports.
# https://vcrpy.readthedocs.io/en/latest/installation.html
BuildRequires:      python3dist(aiohttp)
BuildRequires:      python3dist(boto3)
BuildRequires:      python3dist(httplib2)
BuildRequires:      python3dist(httpx)
BuildRequires:      python3dist(requests)
BuildRequires:      python3dist(tornado)
%endif

%global _description %{expand:
Simplify and speed up testing HTTP by recording all HTTP interactions and
saving them to "cassette" files, which are yaml files containing the contents
of your requests and responses.  Then when you run your tests again, they all
just hit the text files instead of the internet.  This speeds up your tests and
lets you work offline.

If the server you are testing against ever changes its API, all you need to do
is delete your existing cassette files, and run your tests again.  All of the
mocked responses will be updated with the new API.}

%description %{_description}

%package -n python3-%{modname}
Summary:            %{summary}

%description -n python3-%{modname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1

# asyncio.iscoroutinefunction() is deprecated in Python 3.14 and will be removed
# in Python 3.16. Use inspect.iscoroutinefunction() instead
# Also sent upstream: https://github.com/kevin1024/vcrpy/pull/910
sed -i "s/from asyncio/from inspect/" vcr/cassette.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files vcr

%check
%pyproject_check_import

%if %{with tests}
# These tests make lots of outgoing connections, so we can't run them in
# the fedora buildsystem.
rm -rf tests/integration
# This test tries to contact google.com and fails in the fedora build system
rm -rf tests/unit/test_stubs.py
# Skip two tests that require DNS resolution
%pytest -k 'not test_get_vcr_with_matcher and not test_testcase_playback'
%endif

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
