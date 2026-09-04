%global source0_hash 5c74ffbe62c182ffb29cecf456562183ad3f3b8c39dc26f61f78f2fdcbd6d3d9

%bcond check 0
%global srcname OBD

Name:          python-%{srcname}
Version:       0.7.3
Release:       1%{?dist}
Summary:       OBD-II serial module for reading engine data
License:       GPL-2.0-or-later
URL:           https://github.com/brendan-w/%{name}
Source0:       https://github.com/brendan-w/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix python dependency generator error
# error: Illegal char '*' (0x2a) in: 0.7.*
# error: Illegal char '*' (0x2a) in: 3.*
Patch0:        %{name}-dep-ver.patch
BuildArch:     noarch

%global desc A python module for handling realtime sensor data from OBD-II vehicle ports.\
Works with ELM327 OBD-II adapters, and is fit for the Raspberry Pi.

%description
%{desc}

%package -n python3-%{srcname}
Summary:       %{summary}
BuildRequires: python3-devel
%if %{with check}
BuildRequires: python3-pytest
%endif

%description -n python3-%{srcname}
%{desc}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
%generate_buildrequires
%if %{with check}
%pyproject_buildrequires -x test
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files obd

%if %{with check}
%check
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
