%global source0_hash 1f4c76af24e907593487c904ef5eba1993beb38ed385af82adb25a858f2d658d

%global srcname lmdb

Name:           python-%{srcname}
Version:        1.4.1
Release:        %autorelease
Summary:        Python binding for the LMDB 'Lightning' Database (CPython & CFFI included)

# Automatically converted from old format: OpenLDAP - review is highly recommended.
License:        LicenseRef-Callaway-OpenLDAP
URL:            https://github.com/dw/py-lmdb
Source0:        %{pypi_source lmdb}

Patch:          https://github.com/jnwatson/py-lmdb/pull/368.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  lmdb-devel
BuildRequires:  python3-pytest

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n lmdb-%{version}

%generate_buildrequires
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI
%pyproject_buildrequires

%build
# do not use bundled LMDB library
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI
%pyproject_wheel

%install
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI
%pyproject_install

%pyproject_save_files lmdb

%check
export LMDB_FORCE_SYSTEM=1
unset LMDB_FORCE_CFFI
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc ChangeLog

%changelog
%autochangelog
