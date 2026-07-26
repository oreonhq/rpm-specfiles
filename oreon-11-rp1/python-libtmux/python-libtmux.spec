%global source0_hash 5a13bc98d85fdb7105eea880d8f7017c8c4cca6563485972dd4550c57b66ee6f

# most tests currently fail
%bcond tests 0

%global srcname libtmux
%global tmux_minver 1.8

Name:           python-%{srcname}
Version:        0.42.0
Release:        %autorelease
Summary:        Scripting library for tmux

License:        MIT
URL:            https://github.com/tmux-python/libtmux
Source:         %{pypi_source}
# Patch to remove gp-libs test dependency; still unpackaged
Patch:          %{srcname}-no-gp-libs.diff

BuildArch:      noarch

%global _description %{expand:
libtmux is the tool behind tmuxp, a tmux workspace manager in
python.  It builds upon tmux's target and formats to create an object
mapping to traverse, inspect and interact with live tmux sessions.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  tmux >= %{tmux_minver}
%endif
Requires:       tmux >= %{tmux_minver}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
%if %{without tests}
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l libtmux

%check
# Do not check import of test modules
%pyproject_check_import -e 'libtmux.pytest_plugin' -e 'libtmux.test'
%if %{with tests}
PYTHONPATH=src %pytest tests
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGES

%changelog
%autochangelog
