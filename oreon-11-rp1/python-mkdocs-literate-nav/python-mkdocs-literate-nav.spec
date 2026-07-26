%global source0_hash 760e1708aa4be86af81a2b56e82c739d5a8388a0eab1517ecfd8e5aa40810a75

%bcond tests 1

Name:           python-mkdocs-literate-nav
Version:        0.6.2
Release:        %autorelease
Summary:        MkDocs plugin to specify the navigation in Markdown instead of YAML

License:        MIT
URL:            https://oprypin.github.io/mkdocs-literate-nav
Source:         %{pypi_source mkdocs_literate_nav}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-golden)
%endif

%global _description %{expand:
This package provides a plugin for MkDocs to specify the navigation in Markdown
instead of YAML.}

%description %_description

%package -n     python3-mkdocs-literate-nav
Summary:        %{summary}

%description -n python3-mkdocs-literate-nav %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mkdocs_literate_nav-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_literate_nav

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-literate-nav -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
