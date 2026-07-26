%global source0_hash 72e3117667eedf66951bb2d93f4296a56b94b078a8a95905a052611fb3f1b973

%global srcname aniso8601
%global sum Another ISO 8601 parser for Python

Name:           python-%{srcname}
Version:        9.0.1
Release:        19%{?dist}
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://bitbucket.org/nielsenb/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel python3-dateutil python3-setuptools

%description
Python library for parsing date strings
in ISO 8601 format into datetime format.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
Python 3 library for parsing date strings
in ISO 8601 format into datetime format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m unittest discover aniso8601/tests/

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
%autochangelog
