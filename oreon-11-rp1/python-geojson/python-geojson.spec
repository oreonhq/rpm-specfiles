%global source0_hash aea34d7a6798df63eb76e17c64815b45527723b90dd42667d924c87dfe13070a

%global pypi_name geojson

Name:       python-%{pypi_name}
Version:    3.3.0
Release:    1%{?dist}
Summary:    Encoder/decoder for simple GIS features

License:    LicenseRef-Callaway-BSD
URL:        https://github.com/jazzband/geojson
Source0:    https://github.com/jazzband/geojson/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch0:     remove-check.patch

BuildArch:  noarch

BuildRequires: python3-devel
BuildRequires: python3-pytest

%global _description %{expand:
Geojson provides geometry, feature, and collection classes, and supports\
pickle-style dump and load of objects that provide the lab's Python geo\
interface.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p0

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%{pytest} -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.rst README.rst 
%license LICENSE.rst

%changelog
%autochangelog
