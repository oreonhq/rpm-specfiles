%global source0_hash b90d87e15553a3a741be96a168a82075731c83bb4a5302e84ac9ea3ff3692a5f

%global pypi_name dparse2

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        %autorelease
Summary:        Parser for Python dependency files

License:        MIT
URL:            https://github.com/nexB/dparse2
Source:         %url/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# https://github.com/aboutcode-org/dparse2/pull/7
Patch:          0001-Depends-on-tomllib-instead-of-deprecated-toml.patch
# Update project references
# https://github.com/aboutcode-org/dparse2/commit/9b6bd1c223ca5a874c6dcf96cad8fe4c47b0bf2a
Patch:          0001-Update_link_references_of_ownership_from_nexB_to_aboutcode-org.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
A parser for Python dependency files.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

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
%doc CONTRIBUTING.rst README.rst

%changelog
%autochangelog
