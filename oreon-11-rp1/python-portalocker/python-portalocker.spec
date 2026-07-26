%global source0_hash 9f7375348b3a0dd9a03342d8f1506b5914a9eeb5f034f0eb5bcdaa799ac4d795

# tests are enabled by default
%bcond_without  tests

# python-redis is missing from EPEL 9, but many of the tests will still run without
# it being present at test time. See BZ 2063713.
%if 0%{?el9} || 0%{?centos} >= 9
%global test_with_redis 0
%else
%global test_with_redis 1
%endif

%global         srcname     portalocker
%global         forgeurl    https://github.com/WoLpH/portalocker
Version:        3.1.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Library to provide an easy API to file locking

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pytest)
%if 0%{?test_with_redis}
BuildRequires:  python3dist(redis)
%endif
%endif

%global _description %{expand:
%{summary}}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

# NOTE(mhayden): Upstream has a custom pytest.ini that requires 100% test
# coverage, but upstream does not have 100% test coverage yet.
mv pytest.ini pytest.ini_disabled

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files portalocker

%check
%if %{test_with_redis}
%pyproject_check_import
%else
%pyproject_check_import -e portalocker.redis
%endif

%if %{with tests}
%pytest %{?test_with_redis:--ignore=portalocker_tests/test_redis.py} portalocker_tests
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
