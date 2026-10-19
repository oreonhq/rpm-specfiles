%global source1_hash 4c7ff278ae2de1ac858857a9c308629574f6f9c00fc404619afd7f18a850d156
%global source0_hash 8afebb6f7eb6bb8542929458841f5c7e6f240e30c86358c1fbcefbea076c87d9
%global cache /var/cache/man
Summary:        Tools for searching and reading man pages
Name: man-db
Version: 2.13.1
Release:        1%{?dist}
License: GPL-2.0-or-later AND GPL-3.0-or-later
URL: http://www.nongnu.org/man-db/
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz.asc
Source2: 0xac0a4ff12611b6fccf01c111393587d97d86500b
Source3: man-db.crondaily
Source4: man-db.sysconfig
Source5: man-db-cache-update.service
Source6: man-db-restart-cache-update.service
Obsoletes: man < 2.0
Provides: man = %{version}
Provides: man-pages-reader = %{version}
Provides: bundled(gnulib)
Requires: coreutils, grep, groff-base, gzip, less
Recommends: glibc-gconv-extra
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  groff
BuildRequires:  less
BuildRequires:  libpipeline-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-version
BuildRequires:  po4a
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
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
for f in man apropos whatis; do
    mv %{buildroot}%{_bindir}/$f %{buildroot}%{_bindir}/$f.%{name}
    touch %{buildroot}%{_bindir}/$f
    mv %{buildroot}%{_mandir}/man1/$f.1 %{buildroot}%{_mandir}/man1/$f.%{name}.1
    touch %{buildroot}%{_mandir}/man1/$f.1
done
mv $RPM_BUILD_ROOT%{_datadir}/doc/man-db/* ./
rm $RPM_BUILD_ROOT%{_datadir}/man/man1/zsoelim.1
rm $RPM_BUILD_ROOT%{_libdir}/man-db/*.la
install -d -m 0755  $RPM_BUILD_ROOT%{cache}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -D -p -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/man-db.cron
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/man-db
install -D -p -m 0644 init/systemd/man-db.conf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/.
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/man-db-cache-update.service
install -D -p -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/man-db-restart-cache-update.service
%find_lang %{name}
%find_lang %{name}-gnulib
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

for f in man apropos whatis; do
    [ -L %{_bindir}/$f ] || %{__rm} -f %{_bindir}/$f >/dev/null 2>&1 || :
    [ -L %{_mandir}/man1/$f.1.gz ] || %{__rm} -f %{_mandir}/man1/$f.1.gz >/dev/null 2>&1 || :
done
if [ -e /usr/lib/systemd/system/mandb.timer ]; then
    if test -d /run/systemd; then
        systemctl stop man-db.timer >/dev/null 2>&1 || :
        systemctl -q disable man-db.timer >/dev/null 2>&1 || :
    fi
fi
%post

%{_sbindir}/update-alternatives --install %{_bindir}/man man %{_bindir}/man.%{name} 300 \
    --slave %{_bindir}/apropos apropos %{_bindir}/apropos.%{name} \
    --slave %{_bindir}/whatis whatis %{_bindir}/whatis.%{name} \
    --slave %{_mandir}/man1/man.1.gz man.1.gz %{_mandir}/man1/man.%{name}.1.gz \
    --slave %{_mandir}/man1/apropos.1.gz apropos.1.gz %{_mandir}/man1/apropos.%{name}.1.gz \
    --slave %{_mandir}/man1/whatis.1.gz whatis.1.gz %{_mandir}/man1/whatis.%{name}.1.gz \
    >/dev/null 2>&1 || :
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
if [ -x /usr/bin/systemd-run -a -x /usr/bin/systemctl ]; then
    /usr/bin/systemd-run /usr/bin/systemctl start man-db-cache-update >/dev/null 2>&1 || :
fi
%transfiletriggerpostun -- %{_mandir}
if [ -x /usr/bin/systemd-run -a -x /usr/bin/systemctl ]; then
    /usr/bin/systemd-run /usr/bin/systemctl start man-db-cache-update >/dev/null 2>&1 || :
fi
%files -f %{oreon_filedir}/main.list
%files -n man-db-cron -f %{oreon_filedir}/man-db-cron.list

%changelog

* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.13.1-4
- Ship Colin Watson GPG key next to the spec for gpgverify

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.13.1-3
- Prepare for Oreon 11 (RP1)
