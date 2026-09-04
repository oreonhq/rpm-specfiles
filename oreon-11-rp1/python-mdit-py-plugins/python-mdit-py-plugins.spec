%global source0_hash cc58c0cd7264b3b1972773f14126666462047fbfffaa4ba59a287ee5e6858165

%bcond_without check

Name:           python-mdit-py-plugins
Version:        0.6.1
Release:        1%{?dist}
Summary:        Collection of plugins for markdown-it-py
License:        MIT
URL:            https://github.com/executablebooks/mdit-py-plugins
Source0:        https://github.com/executablebooks/mdit-py-plugins/archive/v%{version}/mdit-py-plugins-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Collection of core plugins for markdown-it-py.}

%description %_description

%package -n     python3-mdit-py-plugins
Summary:        %{summary}

%description -n python3-mdit-py-plugins %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n mdit-py-plugins-%{version}
sed -i '/"coverage",/d' pyproject.toml
sed -i '/"pytest-cov",/d' pyproject.toml
sed -i '/"pytest-regressions",/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mdit_py_plugins

%if %{with check}
%check
%pyproject_check_import
%pytest --ignore=tests/test_references.py -k "not test_plugin_parse and not test_custom_renderer and not test_attrs_allowed and not test_no_new_line_issue and not test_tokens"
%endif

%files -n python3-mdit-py-plugins -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
