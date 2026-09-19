%global source0_hash 3b4f8cc51f2f361badfba0637a590c9fb702f1ededb0ebc9cdcef471dd81129b

%global srcname stravalib

Name:           python-%{srcname}
Version:        1.7
Release:        %autorelease
Summary:        Python package to access and download data from Strava

License:        Apache-2.0
URL:            https://pypi.org/project/stravalib/
Source:         %{pypi_source %{srcname}}
# From https://github.com/stravalib/stravalib/tree/pydantic-v2
Patch:          %{srcname}-pydantic-v2.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The stravalib Python package provides easy-to-use tools for accessing and
downloading Strava data from the Strava V3 web service.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x build,tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
