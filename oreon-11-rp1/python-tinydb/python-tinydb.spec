%global source0_hash 805c7dcff0b23415dda4e6e2a5db5aee7f7bf7c2cace5c211e3c921d9291de25

Name:           python-tinydb
Version:        4.8.0
Release:        %autorelease
Summary:        TinyDB is a tiny, document oriented database

License:        MIT
URL:            https://github.com/msiemens/tinydb
Source:         https://github.com/msiemens/tinydb/archive/refs/tags/v%{version}.tar.gz#/tinydb-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
TinyDB is a lightweight document oriented database optimized for your happiness}

%description %_description

%package -n     python3-tinydb
Summary:        %{summary}

%description -n python3-tinydb %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tinydb-%{version}
# don't run coverage in %%check:
rm pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tinydb

%check
%pyproject_check_import -e '*mypy*'
%pytest

%files -n python3-tinydb -f %{pyproject_files}

%changelog
%autochangelog
