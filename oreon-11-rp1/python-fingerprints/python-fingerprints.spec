%global source0_hash bde51cf15e2ff28799158c36cbff0fb43f93a50588252f79092d3e02e1bd8ac3

%global pypi_name fingerprints

Name:           python-%{pypi_name}
Version:        1.3.1
Release:        %autorelease
Summary:        Compare the names of companies and people by applying strong normalization

License:        MIT
URL:            https://github.com/alephdata/fingerprints
Source:         %url/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyicu)

%global common_description %{expand:
This library helps with the generation of fingerprints for entity data. A
fingerprint in this context is understood as a simplified entity identifier,
derived from it's name or address and used for cross-referencing of entity
across different datasets.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
Recommends:     python3dist(pyicu)

%description -n python3-%{pypi_name} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
