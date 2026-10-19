%global source0_hash 8889755212271cc0ec7311d1e51a550cc0821f0b99b93d3e97a13bb5e221c7dd
%global module_name pgactivity
Name:           pg_activity
Version:        3.6.2
Release:        1%{?dist}
Summary:        Command line tool for PostgreSQL server activity monitoring
License:        PostgreSQL
URL:            https://github.com/dalibo/pg_activity/
Source0:        https://github.com/dalibo/pg_activity/archive/v%{version}.tar.gz
BuildArch:      noarch
Requires:       python3dist(psycopg)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-pg_activity = %{version}-%{release}
# /oreon:deps
%package -n       python3-pg_activity+dev
Summary:        Metapackage for python3-pg_activity dev extras
Requires:       python3-pg_activity = %{version}-%{release}
Requires:       python3dist(black) >= 24.10.0
Provides:       python3dist(pg_activity[dev]) = %{version}-%{release}

%description -n python3-pg_activity+dev
Metapackage for python3-pg_activity dev extras.

%package -n       python3-pg_activity+typing
Summary:        Metapackage for python3-pg_activity typing extras
Requires:       python3-pg_activity = %{version}-%{release}
Requires:       python3dist(types-psutil) >= 5.9.5.15
Provides:       python3dist(pg_activity[typing]) = %{version}-%{release}

%description -n python3-pg_activity+typing
Metapackage for python3-pg_activity typing extras.

%package -n       python3-pg_activity+psycopg
Summary:        Metapackage for python3-pg_activity psycopg extras
Requires:       python3-pg_activity = %{version}-%{release}
Requires:       python3dist(psycopg[binary]) >= 3.1
Provides:       python3dist(pg_activity[psycopg]) = %{version}-%{release}

%description -n python3-pg_activity+psycopg
Metapackage for python3-pg_activity psycopg extras.

%package -n       python3-pg_activity+psycopg2
Summary:        Metapackage for python3-pg_activity psycopg2 extras
Requires:       python3-pg_activity = %{version}-%{release}
Requires:       python3dist(psycopg2-binary) >= 2.8
Provides:       python3dist(pg_activity[psycopg2]) = %{version}-%{release}

%description -n python3-pg_activity+psycopg2
Metapackage for python3-pg_activity psycopg2 extras.

%package -n       python3-pg_activity+testing
Summary:        Metapackage for python3-pg_activity testing extras
Requires:       python3-pg_activity = %{version}-%{release}
Requires:       python3dist(pytest-postgresql) >= 4.0
Provides:       python3dist(pg_activity[testing]) = %{version}-%{release}

%description -n python3-pg_activity+testing
Metapackage for python3-pg_activity testing extras.

%description
Top like application for PostgreSQL server activity monitoring

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -Dpm 0644 docs/man/pg_activity.1 %{buildroot}%{_mandir}/man1/pg_activity.1
%oreon_autofiles main

%check

PY_IGNORE_IMPORTMISMATCH=1 %pytest
%license LICENSE.txt
%doc AUTHORS.md README.md
%{_bindir}/pg_activity
%{_mandir}/man1/%{name}*
%files

%changelog

%autochangelog
