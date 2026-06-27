%global source0_hash 60dffc950e61a2b4ec980087d79352293f138f7b41bf3d7f8e1907160986c886

%bcond plugins 0
%bcond_without check

Name:           python-markdown-it-py
Version:        3.0.0
Release:        1%{?dist}
Summary:        Python port of markdown-it
License:        MIT
URL:            https://github.com/executablebooks/markdown-it-py
Source0:        https://github.com/executablebooks/markdown-it-py/archive/v%{version}/markdown-it-py-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Markdown parser done right.}

%description %_description

%package -n     python3-markdown-it-py
Summary:        %{summary}

%description -n python3-markdown-it-py %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n markdown-it-py-%{version}
sed -i '1{\@^#!/usr/bin/env python@d}' markdown_it/cli/parse.py
sed -i '/"coverage",/d' pyproject.toml
sed -i '/"pytest-cov",/d' pyproject.toml
sed -i '/"pytest-regressions",/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files markdown_it

%if %{with check}
%check
%pyproject_check_import
%pytest tests/ --ignore=tests/test_port --ignore=tests/test_tree.py --ignore=tests/test_cmark_spec --ignore=tests/test_api/test_main.py --ignore=tests/test_linkify.py
%endif

%files -n python3-markdown-it-py -f %{pyproject_files}
%license LICENSE LICENSE.markdown-it
%doc README.md
%{_bindir}/markdown-it

%changelog
%autochangelog
