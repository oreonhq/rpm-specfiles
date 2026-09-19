%global source0_hash 7ed2c90486967058a73a547781121983839522d67041ae52c4979616f1b2b746

%bcond tests 1

Name:           python-markdown-callouts
Version:        0.4.0
Release:        %autorelease
Summary:        Markdown extension to provide a classier syntax for admonitions

License:        MIT
URL:            https://oprypin.github.io/markdown-callouts
Source:         %{pypi_source markdown_callouts}

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-golden)
%endif

%global _description %{expand:
This package provides an extension for Python-Markdown that adds a classier
syntax for admonitions.}

%description %_description

%package -n     python3-markdown-callouts
Summary:        %{summary}

%description -n python3-markdown-callouts %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n markdown_callouts-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l markdown_callouts

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-markdown-callouts -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
