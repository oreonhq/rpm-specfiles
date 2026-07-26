%global source0_hash 928c37731c8d24daa04ec421b0a1c60d5e52e6aa4dc02d3febc17efd66a26861

%global srcname async-timeout
%global common_desc This is a deprecated package.\
The functionality has been merged into asyncio.Timeout\
in the Python standard library.\
https://fedoraproject.org/wiki/Changes/DeprecatePythonAsyncTimeout

%if %{defined fedora}
%bcond_without tests
%endif

Name:           python-%{srcname}
Version:        5.0.1
Release:        8%{?dist}
Summary:        Deprecated, use asyncio.Timeout from the standard library instead

License:        Apache-2.0
URL:            https://github.com/aio-libs/async-timeout
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        %{summary}

Provides:       deprecated()

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
%endif

%description -n python3-%{srcname}
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# remove pytest coverage flags
sed -e '/^addopts/d' -i setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files async_timeout

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGES.rst

%changelog
%autochangelog
