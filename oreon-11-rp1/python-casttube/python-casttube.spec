%global source0_hash 351819818a10a107641675cab71c4154afb490762410b3138c18ef410cbf5c33

# No outside connectivity in koji
%global with_tests 0
%global pypi_name casttube

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        21%{?dist}
Summary:        A python library to interact with the Youtube Chromecast api

License:        MIT
URL:            https://github.com/ur1katz/casttube
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
%if 0%{?with_tests}
BuildRequires:  python3-requests
%endif

%description
Casttube is a python library to interact with the Youtube Chromecast api.

%package -n python3-casttube
Summary:        A python library to interact with the Youtube Chromecast api
%{?python_provide:%python_provide python3-casttube}

Requires: python3-requests

%description -n python3-casttube
Casttube is a python library to interact with the Youtube Chromecast api.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -f %{buildroot}%{_prefix}/LICENSE
%pyproject_save_files %{pypi_name}

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-casttube -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
