%global source0_hash fff5fe59a87295b278abd31bec92c15d9bc4a06885ab12bcea52c71119392e79

%global pypi_name tomlkit

%global common_description %{expand:
TOML Kit is a 1.0.0-compliant TOML library.

It includes a parser that preserves all comments, indentations, whitespace and
internal element ordering, and makes them accessible and editable via an
intuitive API.

You can also create new TOML documents from scratch using the provided helpers.

Part of the implementation has been adapted, improved and fixed from Molten.}

Name:           python-%{pypi_name}
Summary:        Style preserving TOML library
Version:        0.13.2
Release:        %autorelease
License:        MIT

URL:            https://github.com/sdispater/tomlkit
Source:         %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel

# test dependencies
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
