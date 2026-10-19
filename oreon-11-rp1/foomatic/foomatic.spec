%global source0_hash b5c89027aa26967d2e6db62e2af7db0c4039d2480d4fbf2476a6ddcf609a5faf
Summary:        Tools for using the foomatic database of printers and printer drivers
Name:       foomatic
Version:    4.0.13
Release:        1%{?dist}
License:    GPL-2.0-or-later
Source0:        http://www.openprinting.org/download/foomatic/foomatic-db-engine-%{version}.tar.gz
Patch101:  foomatic-manpages.patch
Patch102:  0001-Recognize-fractional-numbers-in-PageSize.patch
Url:          https://github.com/OpenPrinting/foomatic-db-engine  
%if 0%{!?perl_bootstrap:1}
%endif
Requires:       dbus
Requires:       cups-filters >= 1.0.42
Requires:       perl-interpreter >= 3:5.8.1
Requires(post): coreutils
Requires:       foomatic-db
Requires:       cups
Requires:       ghostscript
Requires:       colord
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cups
BuildRequires:  cups-devel
BuildRequires:  dbus-devel
BuildRequires:  foomatic
BuildRequires:  foomatic-db
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  python3-cups
# /oreon:deps
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
ln -sf ../../../bin/foomatic-ppdfile %{buildroot}%{_cups_serverbin}/driver/foomatic
mkdir -p %{buildroot}%{_var}/cache/foomatic
echo cups > %{buildroot}%{_sysconfdir}/foomatic/defaultspooler
rm -rf  \
        %{buildroot}%{_libdir}/ppr \
        %{buildroot}%{_sysconfdir}/foomatic/filter.conf.sample \
        %{buildroot}%{_datadir}/foomatic/templates
find %{buildroot} -name .packlist | xargs rm -f
%oreon_autofiles main

%post

/bin/rm -f /var/cache/foomatic/*
exit 0
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.13-35
- Prepare for Oreon 11 (RP1)
