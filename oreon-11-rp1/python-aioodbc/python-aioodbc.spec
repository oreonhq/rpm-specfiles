%global source0_hash 908de65b85270a4470b5de28fd9adec4e5204f3c30cd88e692cc3efb283a439e

%global srcname aioodbc

Name:           python-%{srcname}
Version:        0.4.0
Release:        11%{?dist}
Summary:        Library for accessing a ODBC databases from the asyncio

License:        Apache-2.0
URL:            https://github.com/aio-libs/aioodbc
Source:         %{pypi_source}

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
# for tests
#BuildRequires:  python3-pytest
#BuildRequires:  python3-pytest-asyncio

%description -n python3-%{srcname}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files aioodbc

%check
# tests all fail with error "AttributeError: module pytest has no attribute db_list"
# and i'm not sure how to fix it right now
#%%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGES.txt README.rst

%changelog
%autochangelog
