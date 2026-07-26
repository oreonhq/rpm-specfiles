%global source0_hash a4bc13d623356b373c2c27c53dbd9c68cae5d526270bfa71f6c6fa69669c6b27

%global srcname cligj

Name:           python-%{srcname}
Version:        0.7.2
Release:        21%{?dist}
Summary:        Click params for GeoJSON CLI

License:        BSD-3-Clause
URL:            https://github.com/mapbox/cligj
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
Common arguments and options for GeoJSON processing commands, using Click.

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Common arguments and options for GeoJSON processing commands, using Click.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# README is executable
chmod -x README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
