%global source0_hash acb91c845c3f101a75ae01e7bdbfba5f992c390cc52583e4c165be2b4ff65241

# tests are enabled by default
%bcond_without  tests

%global         srcname     msrest
%global         forgeurl    https://github.com/Azure/msrest-for-python
Version:        0.7.1
# MSFT isn't making tags any longer in this repo for some reason.
%global         commit      2d8fd04f68a124d0f3df7b81584accc3270b1afc
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        The runtime library "msrest" for AutoRest generated Python clients
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(trio)
%endif

%global _description %{expand:
The runtime library "msrest" for AutoRest generated Python clients}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} async

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%generate_buildrequires
%pyproject_buildrequires -x async

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%if %{with tests}
# Some tests require network connectivity, so they are skipped here.
%pytest \
    --ignore=tests/asynctests/test_pipeline.py \
    --ignore=tests/asynctests/test_universal_http.py \
    --ignore=tests/test_auth.py \
    --ignore=tests/test_runtime.py
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
