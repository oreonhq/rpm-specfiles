%global source0_hash afd892f89d2ecee8d3f3b2314f1bd5bf2d02201872c6e3431e5c31096eca4c8b
%bcond_without check
%global upstream_name psqlodbc
Name: postgresql-odbc
Summary:        PostgreSQL ODBC driver
Version: 16.00.0000
Release:        1%{?dist}
License: LGPL-2.0-or-later
URL: https://odbc.postgresql.org/
Source0:        https://repo.huaweicloud.com/postgresql/odbc/versions/src/psqlodbc-16.00.0000.tar.gz#/postgresql-odbc-16.00.0000.tar.gz
Patch0: postgresql-odbc-09.06.0200-revert-money-fix.patch
Patch1: postgresql-odbc-09.05.0400-revert-money-testsuite-fix.patch
Patch2: postgresql-odbc-endianity-test-fix.patch
%if %{with check}
%endif
Provides: %upstream_name = %version-%release
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libpq)
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  unixODBC-devel
# /oreon:deps
%description
This package includes the driver needed for applications to access a
PostgreSQL system via ODBC (Open Database Connectivity).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{upstream_name}-%{version}

cat <<EOF >README.rpmdist
The upstream psqlodbc testsuite is distributed in '%{name}-tests'
(sub)package.
EOF

%build

export CFLAGS="$CFLAGS -std=gnu17"
%configure --with-unixodbc --disable-dependency-tracking
%make_build CFLAGS="%{optflags} -fcommon -std=gnu17"
%install
%make_install
%global testsuitedir %{_libdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT/%{testsuitedir}
cp -R test $RPM_BUILD_ROOT/%{testsuitedir}
sed -i 's~^drvr=.*~drvr=%{_libdir}/psqlodbc~' $RPM_BUILD_ROOT/%{testsuitedir}/test/odbcini-gen.sh
pushd ${RPM_BUILD_ROOT}%{_libdir}
	ln -s psqlodbcw.so psqlodbc.so
	rm psqlodbcw.la psqlodbca.la
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%postgresql_tests_run
mv test/expected/wchar-char_1.out test/expected/wchar-char.out
rm -rf test/expected/wchar-char_2.out
rm -rf test/expected/wchar-char_3.out
cd test && make installcheck %{_smp_mflags} CFLAGS="%{optflags} -fcommon -std=gnu17" || {
	echo "=== trying to find all regression.diffs files in build directory ==="
	find -name regression.diffs | while read line; do
		cat "$line"
	done
	false
}
%endif
%package tests
Summary: Testsuite files for psqlodbc
Requires: postgresql-test
Requires: %{name} = %{version}-%{release}
Requires: gcc make unixODBC-devel
%description tests
The postgresql-odbc-tests package contains files needed for various tests for
the PostgreSQL unixODBC driver.

%files -f %{oreon_filedir}/main.list
%files -n postgresql-odbc-tests -f %{oreon_filedir}/postgresql-odbc-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 16.00.0000-7
- Import
