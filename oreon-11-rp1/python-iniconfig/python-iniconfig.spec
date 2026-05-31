%global source0_hash b485a7f6c060b2e758b6e58fd1bf7349a6f99954110ca61ceb59af25cf4ff458

Name:               python-iniconfig
Version:            2.3.0
Release:            %autorelease
Summary:            Brain-dead simple parsing of ini files
# SPDX
License:            MIT
URL:                http://github.com/pytest-dev/iniconfig
BuildArch:          noarch
BuildRequires:      python3-devel

# pytest 6+ needs this and this uses pytest for tests
%bcond_without tests

%if %{with tests}
# We BR pytest manually to avoid a dependency on tox in ELN/RHEL
BuildRequires:      python3-pytest
%endif

Source:        http://github.com/pytest-dev/iniconfig/archive/v2.3.0/iniconfig-2.3.0.tar.gz

%global _description %{expand:
iniconfig is a small and simple INI-file parser module
having a unique set of features:

* tested against Python2.4 across to Python3.2, Jython, PyPy
* maintains order of sections and entries
* supports multi-line values with or without line-continuations
* supports "#" comments everywhere
* raises errors with proper line-numbers
* no bells and whistles like automatic substitutions
* iniconfig raises an Error if two sections have the same name.}
%description %_description


%package -n python3-iniconfig
Summary:            %{summary}
%description -n python3-iniconfig %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n iniconfig-%{version}


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l iniconfig


%check
%pyproject_check_import
%if %{with tests}
%pytest -v
%endif


%files -n python3-iniconfig -f %{pyproject_files}
%doc README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.0-1
- Prepare for Oreon 11 (RP1)
