%global source0_hash a72c484b97ec42b80834353b029cc8ee1b79f0ffca1179b2210bb3baf26c01ae

%global srcname gpxpy

Name:           python-%{srcname}
Version:        1.6.2
Release:        %autorelease
Summary:        GPX file parser and GPS track manipulation library

License:        Apache-2.0
URL:            https://github.com/tkrajina/gpxpy
Source0:        %pypi_source %{srcname}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{python3} test.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/gpxinfo

%changelog
%autochangelog
