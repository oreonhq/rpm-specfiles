%global source0_hash 7c95ab264f1b4ba612c696801bef5b33cb0c974203cd391f46e163dddd358335

%bcond_without  tests
%bcond_without  docs

Summary:        Tool and Python library for interacting with Large Language Models
Name:           python-llm
Version:        0.28
Release:        3%{?dist}
License:        Apache-2.0
URL:            https://github.com/simonw/llm
Source:         https://github.com/simonw/llm/archive/%{version}/llm-%{version}.tar.gz
Patch:          python-llm-0.28-relax-click.patch
Patch:          python-llm-0.27.1-disable-tests.patch
Patch:          python-llm-0.27.1-sqlite-3.51.patch

# Fix compatibility with click 8.2+
# Backported from upstream PR
Patch:          https://github.com/simonw/llm/pull/1333.patch

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(llm-echo)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-httpx
BuildRequires:  python3-pytest-vcr
%endif
%if %{with docs}
BuildRequires:  make
BuildRequires:  python3-furo
BuildRequires:  python3-myst-parser
BuildRequires:  python3-sphinx-copybutton
BuildRequires:  python3-sphinx-markdown-builder
%endif
%global _description \
%{expand:
A CLI tool and Python library for interacting with Large Language Models,
both via remote APIs and with models that can be installed and run on
your own machine.
}
%description %_description

%package     -n python3-llm
Summary:        %{summary}
%description -n python3-llm %_description

%if %{with docs}
%package     -n python3-llm-docs
Summary:        Documentation of python3-llm
%description -n python3-llm-docs %_description
Package contains documentation of python-llm
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n llm-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{with docs}
(pushd docs && make man html)
%endif

%install
%pyproject_install
%pyproject_save_files llm
%if %{with docs}
install -D -m0644 docs/_build/man/llm.1 %{buildroot}%{_mandir}/man1/llm.1
%endif

%check
%pyproject_check_import
%if %{with tests}
export ISOLATED_CI_ENV=1
%pytest
%endif

%files -n python3-llm -f %{pyproject_files}
%doc README.*
%{_bindir}/llm
%if %{with docs}
%{_mandir}/man1/llm.1*
%endif

%if %{with docs}
%files -n python3-llm-docs
%doc docs/_build/html/
%endif

%changelog
%autochangelog
