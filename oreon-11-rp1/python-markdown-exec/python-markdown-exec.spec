%global source0_hash d1fa017995ef337ec59e7ce49fbf3e051145a62c3124ae687c17e987f1392cd0

%bcond tests 1

Name:           python-markdown-exec
Version:        1.10.0
Release:        %autorelease
Summary:        Utilities to execute code blocks in Markdown files.

License:        ISC
URL:            https://pawamoy.github.io/markdown-exec
Source:         %{pypi_source markdown_exec}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(markupsafe)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
This package provides utilities to execute code blocks in Markdown files.

For example, you write a Python code block that computes some HTML, and this
HTML is injected in place of the code block.}

%description %_description

%package -n     python3-markdown-exec
Summary:        %{summary}

%description -n python3-markdown-exec %_description

%pyproject_extras_subpkg -n python3-markdown-exec ansi

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n markdown_exec-%{version}

%generate_buildrequires
%pyproject_buildrequires -x ansi

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L markdown_exec

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-markdown-exec -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
%autochangelog
