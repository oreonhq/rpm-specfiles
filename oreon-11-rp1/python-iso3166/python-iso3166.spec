%global source0_hash 89e6b3d2afff9faf320faa826a2b081853200fdd5acd5362d770fe252d0c258b

%global srcname iso3166
%global _description ISO 3166-1 defines two-letter, three-letter, and three-digit country\
codes. python-iso3166 is a self-contained module that converts between these\
codes and the corresponding country name.

Name:           python-%{srcname}
Version:        2.1.1
Release:        14%{?dist}
Summary:        Self-contained ISO 3166-1 country definitions

License:        MIT
URL:            https://github.com/deactivated/%{name}/
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildArch:      noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# Tox tests include mypy run but doesn't work ("Can't find package 'iso3166'")
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES README.rst
%license LICENSE.txt

%changelog
%autochangelog
