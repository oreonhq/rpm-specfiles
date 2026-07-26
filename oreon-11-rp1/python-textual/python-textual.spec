%global source0_hash none

Name:           python-textual
Version:        4.0.0
Release:        4%{?dist}
Summary:        TUI (Text User Interface) framework for Python
License:        MIT
URL:            https://github.com/Textualize/textual
Source0:        %{url}/archive/v%{version}/textual-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  pytest
BuildRequires:  python3-jinja2
BuildRequires:  python3-syrupy
BuildRequires:  python3-time-machine
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-aiohttp
BuildRequires:  python3-pytest-aiohttp

%global _description %{expand:
Textual is a TUI (Text User Interface) framework for Python inspired
by modern web development. Currently a Work in Progress.}

%description
%{_description}

%package -n python3-textual
Summary:        %{summary}

%description -n python3-textual
%{_description}

%package -n python3-textual-doc
Summary:        Docs and examples for python3-textual

%description -n python3-textual-doc
%{_description}

%prep
%autosetup -n textual-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x dev

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files textual

%check
# skip these tests until https://github.com/Textualize/pytest-textual-snapshot
# is packaged
rm -rf tests/snapshot_tests
rm -rf tests/test_slug.py
%pytest -k "not test_textual_env_var and not test_softbreak_split_links_rendered_correctly and not test_setting_unknown_language and not test_register_language and not test_update_highlight_query"

%files -n python3-textual -f %{pyproject_files}
%license LICENSE

%files -n python3-textual-doc
%license LICENSE
%doc README.md docs/ examples/

%changelog
%autochangelog
