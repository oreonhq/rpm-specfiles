%global source0_hash ba8c95b2d975a360249ffa5768e1e6f44d87d10ef7754070d3b321102724a2f1

Name:           python-pytest-lsp
Version:        1.0.0
Release:        %autorelease
Summary:        A pytest plugin for end-to-end testing of language servers

License:        MIT
URL:            https://github.com/swyddfa/lsp-devtools
Source:         %{url}/releases/download/pytest-lsp-v%{version}/pytest_lsp-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
pytest-lsp is a pytest plugin for writing end-to-end tests for language servers.

It works by running the language server in a subprocess and communicating with
it over stdio, just like a real language client. This also means pytest-lsp can
be used to test language servers written in any language - not just Python.

pytest-lsp relies on the pygls library for its language server protocol
implementation.}

%description %_description

%package -n     python3-pytest-lsp
Summary:        %{summary}

%description -n python3-pytest-lsp %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest_lsp-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_lsp

%check
%pytest -v || :

%files -n python3-pytest-lsp -f %{pyproject_files}

%changelog
%autochangelog
