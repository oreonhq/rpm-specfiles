%global source0_hash 4184d481d42aaad26877dc9b10045461f791b19e135c209a19dd6e909c133781
%global srcname	PyGreSQL
%global uversion 6.2.3
%{!?runselftest:%global runselftest 1}
Name:		%{srcname}
Version:	6.2.3
Release:        1%{?dist}
Summary:        Python client library for PostgreSQL
URL:		http://www.pygresql.org/
License:	PostgreSQL
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:		tox.patch
%if 0%{?runselftest:1}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 75
BuildRequires:  python3dist(wheel) >= 0.45
Requires:       python3-PyGreSQL = %{version}-%{release}
# /oreon:deps
%description
Python client library for PostgreSQL

%package -n python3-pygresql
Summary:	%summary
%{?python_provide:%python_provide python3-pygresql}
Provides: python3-PyGreSQL = %{uversion}-%{release}
Provides: python3-PyGreSQL%{?_isa} = %{uversion}-%{release}
Obsoletes: python3-PyGreSQL < %{uversion}-%{release}
%description -n python3-pygresql

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{uversion} -p1

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygresql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %runselftest == 0
exit 0
%endif
%postgresql_tests_run
cat > LOCAL_PyGreSQL.py <<EOF
dbname = '${PGTESTS_DATABASES##*:}'
dbhost = ''
dbport = $PGPORT
EOF
%tox
%files
%files -n python3-pygresql -f %{oreon_filedir}/python3-pygresql.list

%changelog

%autochangelog
