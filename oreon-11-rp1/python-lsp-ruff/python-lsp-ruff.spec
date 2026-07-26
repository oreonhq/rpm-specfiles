%global source0_hash 21bb1e014ff466ad7b478ff64920ecfb812df45b06bc802b54102d63cc2ba6bb

Name:           python-lsp-ruff
Version:        2.3.0
Release:        %{autorelease}
Summary:        Ruff linting plugin for Python LSP Server

%global forgeurl https://github.com/python-lsp/python-lsp-ruff
%global tag v%{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A plugin for python-lsp-server that adds linting, code action and
formatting capabilities that are provided by ruff, an extremely fast
Python linter and formatter written in Rust.}

%description %_description

%package -n python3-lsp-ruff
Summary:        %{summary}

%description -n python3-lsp-ruff %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pylsp_ruff

%check
%pytest -r fEs

%files -n python3-lsp-ruff -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
