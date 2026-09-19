%global source0_hash 4d94adb8d3cde1fa94a28aeb0dfcc7be73145bcdfcdf3d5e225434db31dc8a5c

Name:		sqliteodbc
Version:	0.99991
Release:	8%{?dist}
Summary:	SQLite ODBC Driver

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.ch-werner.de/sqliteodbc
Source:		http://www.ch-werner.de/sqliteodbc/%{name}-%{version}.tar.gz
Patch0:		sqliteodbc-0.99991-Fix-too-many-args-to-gpps-compilation-error.patch
Patch1:		sqliteodbc-0.99991-Fix-incompatible-pointer-compilation-error.patch

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	libxml2-devel
BuildRequires:	sqlite-devel
BuildRequires:	sqlite2-devel
BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel
BuildRequires:	/usr/bin/iconv

Requires:	%{_bindir}/odbcinst

%description
ODBC driver for SQLite interfacing SQLite 2.x and/or 3.x using the
unixODBC or iODBC driver managers. For more information refer to:
- http://www.sqlite.org    -  SQLite engine
- http://www.unixodbc.org  -  unixODBC Driver Manager
- http://www.iodbc.org     -  iODBC Driver Manager

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# correct EOL
for i in README; do
	sed 's#\r##g' $i > $i.tmp && \
	touch -r $i $i.tmp && \
	mv $i.tmp $i
done

# Convert encoding to UTF-8
for i in ChangeLog; do
	iconv -f ISO-8859-1 -t UTF-8 -o $i.tmp $i && \
	touch -r $i $i.tmp && \
	mv $i.tmp $i
done

%build
%configure --with-odbc=$(pkg-config --variable=prefix odbc)
make %{_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libsqliteodbc*.{a,la}
rm -f %{buildroot}%{_libdir}/libsqlite3odbc*.{a,la}
rm -f %{buildroot}%{_libdir}/libsqlite3_mod_*.{a,la}
# install example file
cat > odbc.ini.sample <<- 'EOD'
	# ~/.odbc.ini example file
	[mysqlitedb]
	Description=My SQLite3 test database
	Driver=SQLite3
	Database=/home/user_name/Documents/databases/testdb.sqlite
	# optional lock timeout in milliseconds
	# Timeout=2000
	# StepAPI = No|Yes
	# ShortNames = No|Yes
	# FKSupport = No|Yes
	# SyncPragma = NORMAL|OFF|FULL
	# JournalMode = WAL|MEMORY|TRUNCATE|OFF|PERSIST|DELETE
	# BigInt = No|Yes
EOD

%post
if [ -x %{_bindir}/odbcinst ] ; then
	INST=$(mktemp)

	if [ -r %{_libdir}/libsqliteodbc.so ] ; then
		cat > $INST <<- 'EOD'
			[SQLITE]
			Description=SQLite ODBC 2.X
			Driver=%{_libdir}/libsqliteodbc.so
			Setup=%{_libdir}/libsqliteodbc.so
			Threading=2
			FileUsage=1
		EOD

		%{_bindir}/odbcinst -q -d -n SQLITE | grep '^\[SQLITE\]' >/dev/null || {
			%{_bindir}/odbcinst -i -d -n SQLITE -f $INST || true
		}

		cat > $INST <<- 'EOD'
			[SQLite Datasource]
			Driver=SQLITE
		EOD

		%{_bindir}/odbcinst -q -s -n "SQLite Datasource" | \
		grep '^\[SQLite Datasource\]' >/dev/null || {
			%{_bindir}/odbcinst -i -l -s -n "SQLite Datasource" -f $INST || true
		}
	fi

	if [ -r %{_libdir}/libsqlite3odbc.so ] ; then
		cat > $INST <<- 'EOD'
			[SQLITE3]
			Description=SQLite ODBC 3.X
			Driver=%{_libdir}/libsqlite3odbc.so
			Setup=%{_libdir}/libsqlite3odbc.so
			Threading=2
			FileUsage=1
		EOD

		%{_bindir}/odbcinst -q -d -n SQLITE3 | grep '^\[SQLITE3\]' >/dev/null || {
			%{_bindir}/odbcinst -i -d -n SQLITE3 -f $INST || true
		}

		cat > $INST <<- 'EOD'
			[SQLite3 Datasource]
			Driver=SQLITE3
		EOD

		%{_bindir}/odbcinst -q -s -n "SQLite3 Datasource" | \
		grep '^\[SQLite3 Datasource\]' >/dev/null || {
			%{_bindir}/odbcinst -i -l -s -n "SQLite3 Datasource" -f $INST || true
		}
	fi

	rm -f $INST || true
fi

%preun
if [ "$1" = "0" ] ; then
	test -x %{_bindir}/odbcinst && {
		%{_bindir}/odbcinst -u -d -n SQLITE || true
		%{_bindir}/odbcinst -u -l -s -n "SQLite Datasource" || true
		%{_bindir}/odbcinst -u -d -n SQLITE3 || true
		%{_bindir}/odbcinst -u -l -s -n "SQLite3 Datasource" || true
	}

	true
fi

%files
%license license.terms
%doc README ChangeLog odbc.ini.sample
%{_libdir}/*.so*

%changelog
%autochangelog
