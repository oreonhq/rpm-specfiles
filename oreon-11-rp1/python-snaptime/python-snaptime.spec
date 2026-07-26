%global source0_hash f9afce88ac303a147253a9407e8c06847adc30303abf7d6c421eefbe6ae16bac

%bcond_without tests

%global pretty_name snaptime
%global commit          cc8b7d4489ee8104b717ed461dd21aee806ae322
%global snapshotdate    20210420
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global _description %{expand:
The snaptime package is about transforming timestamps simply.}

Name:           python-%{pretty_name}
Version:        0.2.4
Release:        24%{?dist}
Summary:        Transforming timestamps simply

License:        MIT
URL:            https://github.com/zartstrom/snaptime
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
%endif

%description -n python3-%{pretty_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pretty_name}-%{commit}

%build
%py3_build

%install
%py3_install

%check
#skipping three tests
%if %{with tests}
k="${k-}${k+ and }not test_bad_weekday"
k="${k-}${k+ and }not test_parse_error"
k="${k-}${k+ and }not test_unit_error"
%pytest -k "${k-}"
%endif

%files -n python3-%{pretty_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%pycached %{python3_sitelib}/%{pretty_name}/main.py
%pycached %{python3_sitelib}/%{pretty_name}/__init__.py

%changelog
%autochangelog
