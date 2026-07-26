%global source0_hash 09200bcf837ad35070e6da973aa0cb682e69ed6e16f254a30584550c6d2d8ebb

Name:           python-mkdocs-monorepo-plugin
Version:        1.1.2
Release:        %autorelease
Summary:        Plugin for adding monorepository support in Mkdocs

License:        Apache-2.0
URL:            https://github.com/backstage/mkdocs-monorepo-plugin
Source:         %{pypi_source mkdocs-monorepo-plugin}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This packages provides a Mkdocs plugin to build multiple sets of documentation
in a single Mkdocs.}

%description %_description

%package -n     python3-mkdocs-monorepo-plugin
Summary:        %{summary}

%description -n python3-mkdocs-monorepo-plugin %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mkdocs-monorepo-plugin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mkdocs_monorepo_plugin

%check
%pytest -v -k "not test_plugin_on_config_with_nav"

%files -n python3-mkdocs-monorepo-plugin -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
