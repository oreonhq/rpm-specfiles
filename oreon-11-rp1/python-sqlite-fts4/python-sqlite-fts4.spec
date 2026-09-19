%global source0_hash 6d2d227665e609cdb00e78323a4cd8c778143e07e8dc98453b8edd0a2e3c8ad8

Summary:        Custom SQLite functions to rank documents indexed using the FTS4 extension
Name:           python-sqlite-fts4
Version:        1.0.3
Release:        %autorelease
License:        Apache-2.0
URL:            https://pypi.python.org/project/sqlite-fts4/
Source:         https://github.com/simonw/sqlite-fts4/archive/%{version}/sqlite-fts4-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%global _description \
Custom SQLite functions written in Python for ranking documents \
indexed using the FTS4 extension

%description %{_description}

%package     -n python3-sqlite-fts4
Summary:        %{summary}
%description -n python3-sqlite-fts4 %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sqlite-fts4-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sqlite_fts4

%check
%pyproject_check_import
%pytest

%files -n python3-sqlite-fts4 -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
