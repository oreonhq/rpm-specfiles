%global source0_hash 921feb241c29c2fb9a45daaede0cb8d4f955e4831a1f08a7f66a9192865fe77d

Name:           python-toml-cli
Version:        0.7.0
Release:        %autorelease
Summary:        Read and write keys/values to/from toml files

License:        MIT
URL:            https://github.com/mrijken/toml-cli
# PyPI tarball doesn't include tests
Source:         %{url}/archive/v%{version}/toml-cli-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Command line interface for toml files.}

%description %_description

%package -n     python3-toml-cli
Summary:        %{summary}

%description -n python3-toml-cli %_description

%package -n     toml-cli
Summary:        %{summary}
Requires:       python3-toml-cli
# Provides a binary at the same path
Conflicts:      libtoml

%description -n toml-cli %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n toml-cli-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L toml_cli

%check
%pytest -v

%files -n python3-toml-cli -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%files -n toml-cli
%{_bindir}/toml

%changelog
%autochangelog
