%global source0_hash 71f5412b6722538ca2f5964d2c1b39731afa0e906daa1c5723b523cb6199bf77

%bcond tests 1
%bcond all_tests 0

%global srcname tmuxp

Name:           python-%{srcname}
Version:        1.52.2
Release:        %autorelease
Summary:        Tmux session manager

# This is the proper SPDX license
License:        MIT
URL:            https://tmuxp.git-pull.com/
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Session manager for tmux, which allows users to save and load tmux sessions
through simple configuration files.}

%description %_description

%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-rerunfailures)
BUildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(typing-extensions)
%endif

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tmuxp

%check
%pyproject_check_import
PYTHONPATH=src %pytest -v \
%if %{without all_tests}
  --deselect tests/workspace/test_builder.py::test_window_shell
%else
%nil
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGES examples
%{_bindir}/tmuxp

%changelog
%autochangelog
