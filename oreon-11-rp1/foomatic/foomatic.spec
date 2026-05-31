%global source0_hash b5c89027aa26967d2e6db62e2af7db0c4039d2480d4fbf2476a6ddcf609a5faf

Summary: Tools for using the foomatic database of printers and printer drivers
Name:       foomatic
Version:    4.0.13
Release:    35%{?dist}
License:    GPL-2.0-or-later

# The database engine.
Source0:        http://www.openprinting.org/download/foomatic/foomatic-db-engine-%{version}.tar.gz

## PATCHES FOR FOOMATIC-DB-ENGINE (PATCHES 101 TO 200)
Patch101:  foomatic-manpages.patch
# backported from upstream https://github.com/OpenPrinting/foomatic-db-engine/commit/75de02d
Patch102:  0001-Recognize-fractional-numbers-in-PageSize.patch

## PATCHES FOR FOOMATIC-DB-HPIJS (PATCHES 201 TO 300)

Url:          https://github.com/OpenPrinting/foomatic-db-engine  

# gcc is no longer in buildroot by default
BuildRequires:  gcc
# for autosetup
BuildRequires:  git-core
# uses make
BuildRequires:  make
BuildRequires:  perl-interpreter >= 3:5.8.1
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  libxml2-devel
BuildRequires:  autoconf, automake
BuildRequires:  cups-devel
BuildRequires:  dbus-devel
# Make sure we get postscriptdriver tags.  Safe to comment out when
# bootstrapping a new architecture.
BuildRequires:  python3-cups, cups
%if 0%{!?perl_bootstrap:1}
BuildRequires:  foomatic, foomatic-db
%endif

Requires:       dbus
Requires:       cups-filters >= 1.0.42
Requires:       perl-interpreter >= 3:5.8.1
Requires(post): coreutils
Requires:       foomatic-db
Requires:       cups
Requires:       ghostscript
Requires:       colord

%description
Foomatic is a comprehensive, spooler-independent database of printers,
printer drivers, and driver descriptions. This package contains
utilities to generate driver description files and printer queues for
CUPS, LPD, LPRng, and PDQ using the database (packaged separately).
There is also the possibility to read the PJL options out of PJL-capable
laser printers and take them into account at the driver description
file generation.

There are spooler-independent command line interfaces to manipulate
queues (foomatic-configure) and to print files/manipulate jobs
(foomatic printjob).

The site http://www.linuxprinting.org/ is based on this database.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n foomatic-db-engine-%{version} -S git

chmod a+x mkinstalldirs

%build
export LIB_CUPS=%{_cups_serverbin}
export CUPS_BACKENDS=%{_cups_serverbin}/backend
export CUPS_FILTERS=%{_cups_serverbin}/filter
export CUPS_PPDS=%{_datadir}/cups/model

aclocal
autoconf
%configure --disable-xmltest
make PREFIX=%{_prefix} CFLAGS="$RPM_OPT_FLAGS"

%install
make    DESTDIR=%buildroot PREFIX=%{_prefix} \
        INSTALLSITELIB=%{perl_vendorlib} \
        INSTALLSITEARCH=%{perl_vendorarch} \
        install

# Use relative, not absolute, symlink for CUPS driver.
ln -sf ../../../bin/foomatic-ppdfile %{buildroot}%{_cups_serverbin}/driver/foomatic

mkdir -p %{buildroot}%{_var}/cache/foomatic

echo cups > %{buildroot}%{_sysconfdir}/foomatic/defaultspooler

# Remove things we don't ship.
rm -rf  \
        %{buildroot}%{_libdir}/ppr \
        %{buildroot}%{_sysconfdir}/foomatic/filter.conf.sample \
        %{buildroot}%{_datadir}/foomatic/templates
#%%{buildroot}%%{_libdir}/perl5/site_perl
find %{buildroot} -name .packlist | xargs rm -f

%post
/bin/rm -f /var/cache/foomatic/*
exit 0


%files
%doc COPYING
%dir %{_sysconfdir}/foomatic
%config(noreplace) %{_sysconfdir}/foomatic/defaultspooler
%{_bindir}/foomatic-combo-xml
%{_bindir}/foomatic-compiledb
%{_bindir}/foomatic-configure
%{_bindir}/foomatic-datafile
%{_bindir}/foomatic-perl-data
%{_bindir}/foomatic-ppd-options
%{_bindir}/foomatic-ppd-to-xml
%{_bindir}/foomatic-ppdfile
%{_bindir}/foomatic-printjob
%{_bindir}/foomatic-searchprinter
%{_sbindir}/*
%{perl_vendorlib}/Foomatic
%{_cups_serverbin}/driver/*
%{_mandir}/man1/foomatic-cleanupdrivers.1*
%{_mandir}/man1/foomatic-combo-xml.1*
%{_mandir}/man1/foomatic-compiledb.1*
%{_mandir}/man1/foomatic-configure.1*
%{_mandir}/man1/foomatic-datafile.1*
%{_mandir}/man1/foomatic-extract-text.1*
%{_mandir}/man1/foomatic-fix-xml.1*
%{_mandir}/man1/foomatic-nonumericalids.1*
%{_mandir}/man1/foomatic-perl-data.1*
%{_mandir}/man1/foomatic-ppd-options.1*
%{_mandir}/man1/foomatic-ppd-to-xml.1*
%{_mandir}/man1/foomatic-ppdfile.1*
%{_mandir}/man1/foomatic-printermap-to-gutenprint-xml.1*
%{_mandir}/man1/foomatic-printjob.1*
%{_mandir}/man1/foomatic-replaceoldprinterids.1*
%{_mandir}/man1/foomatic-searchprinter.1*
%{_mandir}/man8/*
%{_var}/cache/foomatic

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.13-35
- Prepare for Oreon 11 (RP1)
