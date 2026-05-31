%global source0_hash 8afebb6f7eb6bb8542929458841f5c7e6f240e30c86358c1fbcefbea076c87d9

%global cache /var/cache/man

Summary: Tools for searching and reading man pages
Name: man-db
Version: 2.13.1
Release: 4%{?dist}
# GPLv2+ .. man-db
# GPLv3+ .. gnulib
License: GPL-2.0-or-later AND GPL-3.0-or-later
URL: http://www.nongnu.org/man-db/

Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz.asc
# Colin Watson signing key (also https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xac0a4ff12611b6fccf01c111393587d97d86500b)
Source2: 0xac0a4ff12611b6fccf01c111393587d97d86500b

Source3: man-db.crondaily
Source4: man-db.sysconfig
Source5: man-db-cache-update.service
Source6: man-db-restart-cache-update.service

Obsoletes: man < 2.0
Provides: man = %{version}
Provides: man-pages-reader = %{version}
# FPC exception for gnulib - copylib - https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib)

Requires: coreutils, grep, groff-base, gzip, less
BuildRequires: make
BuildRequires: gcc
BuildRequires: systemd
BuildRequires: gdbm-devel, gettext, groff, less, libpipeline-devel, zlib-devel
BuildRequires: po4a, perl-interpreter, perl-version
BuildRequires: gnupg2
Recommends: glibc-gconv-extra

Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

%description
The man-db package includes five tools for browsing man-pages:
man, whatis, apropos, manpath and lexgrog. man formats and displays
manual pages. whatis searches the manual page names. apropos searches the
manual page names and descriptions. manpath determines search path
for manual pages. lexgrog directly reads header information in
manual pages.

%package cron
Summary: Periodic update of man-db cache

Requires: %{name} = %{version}-%{release}
Requires: crontabs

BuildArch: noarch

%description cron
This package provides periodic update of man-db cache.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure \
    --with-sections="1 1p 8 2 3 3p 3pm 4 5 6 7 9 0p n l p o 1x 2x 3x 4x 5x 6x 7x 8x" \
    --disable-setuid --disable-cache-owner \
    --with-systemdsystemunitdir=no \
    --with-browser=elinks --with-lzip=lzip \
    --with-snapdir=/var/lib/snapd/snap \
    --with-override-dir=overrides
%make_build CC="%{__cc} %{optflags}"

%check
make check

%install
%make_install prefix=%{_prefix}

# rename files for alternative usage
for f in man apropos whatis; do
    mv %{buildroot}%{_bindir}/$f %{buildroot}%{_bindir}/$f.%{name}
    touch %{buildroot}%{_bindir}/$f
    mv %{buildroot}%{_mandir}/man1/$f.1 %{buildroot}%{_mandir}/man1/$f.%{name}.1
    touch %{buildroot}%{_mandir}/man1/$f.1
done

# move the documentation to the relevant place
mv $RPM_BUILD_ROOT%{_datadir}/doc/man-db/* ./

# remove zsoelim man page - part of groff package
rm $RPM_BUILD_ROOT%{_datadir}/man/man1/zsoelim.1

# remove libtool archives
rm $RPM_BUILD_ROOT%{_libdir}/man-db/*.la

# install cache directory
install -d -m 0755  $RPM_BUILD_ROOT%{cache}

# install cron script for man-db creation/update
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -D -p -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/man-db.cron

# config for cron script
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/man-db

# config for tmpfiles.d
install -D -p -m 0644 init/systemd/man-db.conf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/.

# man-db-cache-update.service and man-db-restart-cache-update.service
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/man-db-cache-update.service
install -D -p -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/man-db-restart-cache-update.service

%find_lang %{name}
%find_lang %{name}-gnulib

%pre
# remove alternativized files if they are not symlinks
for f in man apropos whatis; do
    [ -L %{_bindir}/$f ] || %{__rm} -f %{_bindir}/$f >/dev/null 2>&1 || :
    [ -L %{_mandir}/man1/$f.1.gz ] || %{__rm} -f %{_mandir}/man1/$f.1.gz >/dev/null 2>&1 || :
done

# stop and disable timer from previous builds
if [ -e /usr/lib/systemd/system/mandb.timer ]; then
    if test -d /run/systemd; then
        systemctl stop man-db.timer >/dev/null 2>&1 || :
        systemctl -q disable man-db.timer >/dev/null 2>&1 || :
    fi
fi

%post
# set up the alternatives files
%{_sbindir}/update-alternatives --install %{_bindir}/man man %{_bindir}/man.%{name} 300 \
    --slave %{_bindir}/apropos apropos %{_bindir}/apropos.%{name} \
    --slave %{_bindir}/whatis whatis %{_bindir}/whatis.%{name} \
    --slave %{_mandir}/man1/man.1.gz man.1.gz %{_mandir}/man1/man.%{name}.1.gz \
    --slave %{_mandir}/man1/apropos.1.gz apropos.1.gz %{_mandir}/man1/apropos.%{name}.1.gz \
    --slave %{_mandir}/man1/whatis.1.gz whatis.1.gz %{_mandir}/man1/whatis.%{name}.1.gz \
    >/dev/null 2>&1 || :

# clear the old cache
%{__rm} -rf %{cache}/* >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove man %{_bindir}/man.%{name} >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ]; then
    if [ "$(readlink %{_sysconfdir}/alternatives/man)" == "%{_bindir}/man.%{name}" ]; then
        %{_sbindir}/update-alternatives --set man %{_bindir}/man.%{name} >/dev/null 2>&1 || :
    fi
fi

%transfiletriggerin -- %{_mandir}
# update cache
if [ -x /usr/bin/systemd-run -a -x /usr/bin/systemctl ]; then
    /usr/bin/systemd-run /usr/bin/systemctl start man-db-cache-update >/dev/null 2>&1 || :
fi

%transfiletriggerpostun -- %{_mandir}
# update cache
if [ -x /usr/bin/systemd-run -a -x /usr/bin/systemctl ]; then
    /usr/bin/systemd-run /usr/bin/systemctl start man-db-cache-update >/dev/null 2>&1 || :
fi

%files -f %{name}.lang -f %{name}-gnulib.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md man-db-manual.txt man-db-manual.ps ChangeLog NEWS.md
%config(noreplace) %{_sysconfdir}/man_db.conf
%config(noreplace) %{_sysconfdir}/sysconfig/man-db
%config(noreplace) %{_tmpfilesdir}/man-db.conf
%{_unitdir}/man-db-cache-update.service
%{_unitdir}/man-db-restart-cache-update.service
%{_sbindir}/accessdb
%ghost %{_bindir}/man
%ghost %{_bindir}/apropos
%ghost %{_bindir}/whatis
%{_bindir}/man.%{name}
%{_bindir}/apropos.%{name}
%{_bindir}/whatis.%{name}
%{_bindir}/man-recode
%{_bindir}/manpath
%{_bindir}/lexgrog
%{_bindir}/catman
%{_bindir}/mandb
%dir %{_libdir}/man-db
%{_libdir}/man-db/*.so
%dir %{_libexecdir}/man-db
%{_libexecdir}/man-db/globbing
%{_libexecdir}/man-db/manconv
%{_libexecdir}/man-db/zsoelim
%verify(not mtime) %dir %{cache}
# documentation and translation
%ghost %{_mandir}/man1/man.1*
%ghost %{_mandir}/man1/apropos.1*
%ghost %{_mandir}/man1/whatis.1*
%{_mandir}/man1/man.%{name}.1*
%{_mandir}/man1/apropos.%{name}.1*
%{_mandir}/man1/whatis.%{name}.1*
%{_mandir}/man1/man-recode.1*
%{_mandir}/man1/lexgrog.1*
%{_mandir}/man1/manconv.1*
%{_mandir}/man1/manpath.1*
%{_mandir}/man5/manpath.5*
%{_mandir}/man8/accessdb.8*
%{_mandir}/man8/catman.8*
%{_mandir}/man8/mandb.8*
%lang(da)       %{_datadir}/man/da/man*/*
%lang(de)       %{_datadir}/man/de/man*/*
%lang(es)       %{_datadir}/man/es/man*/*
%lang(fr)       %{_datadir}/man/fr/man*/*
%lang(id)       %{_datadir}/man/id/man*/*
%lang(it)       %{_datadir}/man/it/man*/*
%lang(ja)       %{_datadir}/man/ja/man*/*
%lang(ko)	%{_datadir}/man/ko/man*/*
%lang(nl)       %{_datadir}/man/nl/man*/*
%lang(pl)       %{_datadir}/man/pl/man*/*
%lang(pt)       %{_datadir}/man/pt/man*/*
%lang(pt_BR)    %{_datadir}/man/pt_BR/man*/*
%lang(ro)       %{_datadir}/man/ro/man*/*
%lang(ru)       %{_datadir}/man/ru/man*/*
%lang(sr)       %{_datadir}/man/sr/man*/*
%lang(sv)       %{_datadir}/man/sv/man*/*
%lang(tr)       %{_datadir}/man/tr/man*/*
%lang(zh_CN)    %{_datadir}/man/zh_CN/man*/*
%lang(uk)	%{_datadir}/man/uk/man*/*

%files cron
%config(noreplace) %{_sysconfdir}/cron.daily/man-db.cron

%changelog
* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.13.1-4
- Ship Colin Watson GPG key next to the spec for gpgverify

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.13.1-3
- Prepare for Oreon 11 (RP1)
