%global source0_hash 162b3d129c7fad9b19abfdcb9c1458a651628e4b1dea628ac68790fb3061c60c

%global pypi_name mkdocs-get-deps
%global srcname mkdocs_get_deps

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        %autorelease
Summary:        MkDocs extension that lists all dependencies according to a mkdocs.yml file

License:        MIT
URL:            https://github.com/mkdocs/get-deps
Source:         %{pypi_source %{srcname}}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides an extra command for MkDocs that infers required PyPI
packages from plugins in mkdocs.yml.}

%description %_description

%package -n     python3-mkdocs-get-deps
Summary:        %{summary}

%description -n python3-mkdocs-get-deps %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{pypi_name}

%changelog
%autochangelog
