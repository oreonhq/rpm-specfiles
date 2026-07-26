%global source0_hash 8d502b3ca4b9c45e56012bd35c03d23235f0823c976d4ce940cbb40e33087ded

%global pypi_version %(echo '%{version}' | tr -d '~')

Summary:        A simple database migration system for SQLite
Name:           python-sqlite-migrate
Version:        0.1~b0
Release:        2%{?dist}
License:        Apache-2.0
URL:            https://pypi.python.org/project/sqlite-migrate/
Source:         %{pypi_source sqlite-migrate}
# https://github.com/simonw/sqlite-migrate/pull/14/commits
Patch:          python-sqlite-migrate-0.1b0-toml.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%global _description \
A simple database migration system for SQLite, based on sqlite-utils

%description %{_description}

%package     -n python3-sqlite-migrate
Summary:        %{summary}
%description -n python3-sqlite-migrate %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sqlite-migrate-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sqlite_migrate

%check
%pyproject_check_import
%pytest

%files -n python3-sqlite-migrate -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
