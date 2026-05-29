%global source0_hash 3248a1373bff552c500834adbea4b6caee04224516ae581fb25a4c6a6dee89ea

%global with_libdb_migration 1
%global libdb_migration_build_dir libdb_migration_build
%{!?with_system_gsl: %global with_system_gsl (%{undefined rhel} || 0%{?rhel} < 10)}

Summary: Fast anti-spam filtering by Bayesian statistical analysis
Name: bogofilter
Version: 1.2.5
Release: 22%{?dist}
License: GPL-2.0-only
URL: http://bogofilter.sourceforge.net/
Source0:        http://downloads.sourceforge.net/bogofilter/bogofilter-1.2.5.tar.xz
BuildRequires: gcc
BuildRequires: flex
BuildRequires: pkgconfig(sqlite3)
BuildRequires: /usr/bin/iconv
BuildRequires: /usr/bin/xmlto
BuildRequires: perl-generators
BuildRequires: make

%if %{with_system_gsl}
BuildRequires: gsl-devel
%else
Provides: bundled(gsl) = 1.4
%endif

%if %{with_libdb_migration}
BuildRequires: libdb-devel-static
%endif

%description
Bogofilter is a Bayesian spam filter.  In its normal mode of
operation, it takes an email message or other text on standard input,
does a statistical check against lists of "good" and "bad" words, and
returns a status code indicating whether or not the message is spam.
Bogofilter is designed with fast algorithms, coded directly in C, and
tuned for speed, so it can be used for production by sites that process
a lot of mail.

%if %{with_libdb_migration}
The current version switched from Berkeley DB to SQLite format. To migrate
to the new format run: bogomigrate-berkeley wordlist.db
%endif

%package bogoupgrade
Summary: Upgrades bogofilter database to current version
Requires: %{name} = %{version}-%{release}

%description bogoupgrade
bogoupgrade is a command to upgrade bogofilter’s databases from an old
format to the current format. Since the format of the database changes
once in a while, the utility is designed to make the upgrade easy.

bogoupgrade is in an extra package to remove the perl dependency on the
main bogofilter package.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
iconv -f iso-8859-1 -t utf-8 \
 doc/bogofilter-faq-fr.html > doc/bogofilter-faq-fr.html.utf8
mv -f doc/bogofilter-faq-fr.html.utf8 \
 doc/bogofilter-faq-fr.html

%if %{with_libdb_migration}
# make a copy of the sources for the build with the libdb backend
mkdir ../%{libdb_migration_build_dir}
cp -a * ../%{libdb_migration_build_dir}/
mv ../%{libdb_migration_build_dir} .
%endif

%build
%configure --disable-rpath \
	--with-database=sqlite3 \
%if !%{with_system_gsl}
	--with-included-gsl=yes \
%endif
	%{nil}

%make_build

%if %{with_libdb_migration}
pushd %{libdb_migration_build_dir}
STATIC_DB=
BF_ZAP_LIBDB=
if [ -e /usr/lib64/libdb-5.3.a ]; then
   STATIC_DB='/usr/lib64/libdb-5.3.a -lpthread'
   BF_ZAP_LIBDB=zap
elif [ -e /usr/lib/libdb-5.3.a ]; then
   STATIC_DB='/usr/lib/libdb-5.3.a -lpthread'
   BF_ZAP_LIBDB=zap
fi
%configure --disable-rpath --with-database=db BF_ZAP_LIBDB=${BF_ZAP_LIBDB} STATIC_DB="${STATIC_DB}" LIBS="${LIBS} ${STATIC_DB}"
%make_build
popd
%endif

%install
%make_install

mv -f %{buildroot}%{_sysconfdir}/bogofilter.cf.example \
 %{buildroot}%{_sysconfdir}/bogofilter.cf

install -d -m0755 rpm-doc/xml/ rpm-doc/html/
install -m644 doc/*.xml rpm-doc/xml/
install -m644 doc/*.html rpm-doc/html/

chmod -x contrib/*
rm -v contrib/bogogrep.o
rm -rfv contrib/.deps

%if %{with_libdb_migration}
pushd %{libdb_migration_build_dir}
cp -f src/bogoutil %{buildroot}/%{_bindir}/bogoutil-berkeley

cat >> %{buildroot}%{_bindir}/bogomigrate-berkeley << FOE
#!/bin/bash

if [ "\${1}" = "" ] || [ "\${1}" = "--help" ]; then
	echo "Migrate Bogofilter Berkeley database into the current format."
	echo "Expects one argument, the file name to migrate."
	echo "Usage: bogomigrate-berkeley wordlist.db"
	exit 1;
fi

if [ -e "\${1}" ]; then
	bogoutil-berkeley -d "\${1}" > "\${1}.txt.migrate" && \\
	bogoutil -I "\${1}.txt.migrate" -l "\${1}.migrated" && \\
	rm "\${1}.txt.migrate" && \\
	mv "\${1}" "\${1}.berkeley.bak" && \\
	mv "\${1}.migrated" "\${1}" && \\
	echo "Successfully migrated '\${1}' with \`bogoutil -d "\${1}" | wc -l\` entries." && \\
	echo "Backup of the original file is stored as '\${1}.berkeley.bak'."
else
	echo "File '\${1}' does not exist" 1>&2
fi
FOE

chmod a+x %{buildroot}%{_bindir}/bogomigrate-berkeley

popd
%endif

%check
# Tests seem to use V or VERBOSE for something else, so cannot use %%make_build which defines it
make %{?_smp_mflags} check

%files bogoupgrade
%{_bindir}/bogoupgrade
%{_mandir}/man1/bogoupgrade*

%files
%doc AUTHORS COPYING NEWS README* RELEASE.NOTES* TODO bogofilter.cf.example
%doc doc/bogofilter-SA* doc/bogofilter-tuning.HOWTO* doc/integrating* doc/programmer/
%doc rpm-doc/html/ rpm-doc/xml/ contrib
%{_mandir}/man1/bogo*.1*
%{_mandir}/man1/bf_*.1*
%config(noreplace) %{_sysconfdir}/bogofilter.cf
%{_bindir}/bogo*
%{_bindir}/bf_*
%exclude %{_bindir}/bogoupgrade
%exclude %{_mandir}/man1/bogoupgrade*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.5-22
- Prepare for Oreon 11 (RP1)
