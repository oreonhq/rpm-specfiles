%global source0_hash 0b2c880b5d13660a7ea651001fb4acb527696c01f15c9ee650f377aa543fd523

%global common_description %{expand:
Create beautiful and testable command-line interfaces.

Cleo is mostly a higher level wrapper for CliKit, so a lot of the
components and utilities comes from it. Refer to its documentation for
more information.}

#global prerel ...
%global base_version 2.1.0

Name:           python-cleo
Summary:        Create beautiful and testable command-line interfaces
Version:        %{base_version}%{?prerel:~%{prerel}}
Release:        %autorelease -b 5
License:        MIT

URL:            https://github.com/sdispater/cleo
Source0:        %{pypi_source cleo}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock

%description %{common_description}

%package -n     python3-cleo
Summary:        %{summary}

%description -n python3-cleo %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cleo-%{base_version}%{?prerel} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cleo

%check
%pytest

%files -n python3-cleo -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
