%global source0_hash 3fbe225069755f46dae2bdee61129904a15ad000c8a4050a8b38d6d3b371b4a7

%global srcname keep

# no tests currently defined
%bcond tests 0

%if (%{defined fedora} && 0%{?fedora} <= 42) || (%{defined rhel} && 0%{?rhel} <= 10)
# license not picked up automatically by old tooling
%bcond license_found 0
%else
%bcond license_found 1
%endif

Name:           python-%{srcname}
Version:        2.11
Release:        %autorelease
Summary:        A Meta CLI toolkit

License:        MIT
URL:            https://github.com/orkohunter/keep
# pypi archive does not contain license text
# Source0:        {pypi_source}
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Personal shell command keeper and snippets manager

## Features
- Save a new command with a brief description
- Search the saved commands using powerful patterns
- Save the commands as a secret GitHub gist
- Use `keep push` and `keep pull` to sync the commands between GitHub
  gist and other computers.

**ProTip : Save the commands you usually forget in ssh sessions and sync
it with your local machine.**}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
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
%if %{with license_found}
%pyproject_save_files -l %{srcname}
%else
%pyproject_save_files -L %{srcname}
%endif

%check
%pyproject_check_import

%if %{with tests}
%pytest -v
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%if %{without license_found}
%license LICENSE.md
%endif
%doc README.md tutorial.md
%{_bindir}/%{srcname}

%changelog
%autochangelog
