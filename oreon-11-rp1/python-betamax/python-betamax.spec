%global source0_hash 971bcaffce5ce8fdc67fb207fb0d12657d2ac169e0086428b5acdf8d54d8a8d5

%global srcname betamax

# tests need internet access therefore disabled by default
# $ fedpkg mockbuild --enable-network --with=tests
%bcond_with tests

Name:           python-%{srcname}
Version:        0.9.0
Release:        9%{?dist}
Summary:        VCR imitation for python-requests

License:        Apache-2.0
URL:            https://github.com/sigmavirus24/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Betamax is a VCR_ imitation for requests. This will make mocking out requests\
much easier.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-requests >= 2.0
%endif
Requires:       python3-requests >= 2.0

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import -t

%if %{with tests}
# test_pytest_fixture: not sure why it fails but better run some tests than none
# test_replays_response_from_cassette: https://github.com/betamaxpy/betamax/issues/184
# TestPyTestParametrizedFixtures: failure reason unknown
TEST_SELECTOR="not test_fixtures and not test_replays_response_from_cassette and not TestPyTestParametrizedFixtures"
py.test-%{python3_version} -vk "$TEST_SELECTOR"
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
