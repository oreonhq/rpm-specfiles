%global source0_hash 7dd66878c5b7b41ac790775d82b8fccdfdb1deb80d6c95306e90ad3e8c3538ed

%global pypi_name click-repl

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        %autorelease
Summary:        REPL plugin for Click

License:        MIT
URL:            https://github.com/untitaker/click-repl
Source0:        %{url}/archive/%{version}.tar.gz
BuildArch:      noarch

# Fix compatibility with click 8.2+
# Sent upstream
Patch:          https://github.com/click-contrib/click-repl/pull/132.patch

BuildRequires:  python3-devel
BuildRequires:  python3-click
BuildRequires:  python3-pytest
BuildRequires:  python3-prompt-toolkit
BuildRequires:  python3-six

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
# Remove --cov from pytest
sed -i '/addopts = \[/,/]/ s/"--cov=[^"]*",\?//g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l click_repl

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
