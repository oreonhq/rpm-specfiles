%global source0_hash 82377eae21716165f2b0b6b632b4c7eddfc0ccf841f378bf6e5401867eb09faa

%global pypi_name orderly-set
%global pypi_version 5.5.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        4%{?dist}
Summary:        A package containing multiple implementations of Ordered Set
License:        MIT
URL:            https://github.com/seperman/orderly-set
Source0:        https://github.com/seperman/orderly-set/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Orderly Set is a package containing multiple implementations of
Ordered Set.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Orderly Set is a package containing multiple implementations
of Ordered Set.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n orderly-set-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l orderly_set

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
