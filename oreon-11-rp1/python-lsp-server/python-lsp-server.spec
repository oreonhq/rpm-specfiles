%global source0_hash 8cb79ae54117a229d3119acd060e12f0a4cf8ef4ca46d6d0b6d5f1355e39e13c

Name:           python-lsp-server
Version:        1.13.1
Release:        %autorelease
Summary:        Python implementation of language server protocol

%global forgeurl https://github.com/python-lsp/python-lsp-server
%global tag v%{version}
%forgemeta

# SPDX
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli

%global _description %{expand:
A python implementation of language server protocol. pylsp provides for
auto-completion, code linting (via pycodestyle and pyflakes) and other
features.

This package provides the python-language-server package maintained by
spyder-IDE maintainers.}

%description %_description

%package -n     python3-lsp-server
Summary:        %{summary}

Provides:       pylsp = %{version}-%{release}

%description -n python3-lsp-server %_description

%pyproject_extras_subpkg -n python3-lsp-server all

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
# Remove version pinning from linters.
# Do this inline instead of a patch for automatic updates using Packit.
tomcli set pyproject.toml arrays replace \
    project.dependencies '(.+)>=+[0-9.]+.*' '\1'
tomcli set pyproject.toml arrays replace \
    project.optional-dependencies.all '(.+)>=+[0-9.]+.*' '\1'

# Remove linters from test extra and pytest options
tomcli set pyproject.toml arrays delitem --type fnmatch \
    project.optional-dependencies.test '*cov*'
tomcli set pyproject.toml arrays delitem --type fnmatch \
    project.optional-dependencies.test '*lint*'
tomcli set pyproject.toml del tool.pytest.ini_options.addopts

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_buildrequires -x test,all

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pylsp

%check
k="${k:-}${k:+ and }not test_missing_message"
export RUNNING_IN_CI="True"
%pytest -r fEs "${k:+-k ${k:-}}"

%files -n python3-lsp-server -f %{pyproject_files}
%doc README.md
%{_bindir}/pylsp

%changelog
%autochangelog
