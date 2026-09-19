%global source0_hash 0d5f2cd12bdab9401b4c836854ebbf241675051875557783c332a6a40dac0711

%global patchlevel 302

Summary:       The quintessential all-purpose communications program
Name:          ckermit
Version:       9.0.%{patchlevel}
Release:       41%{?dist}
# Most of the package is under a three-clause BSD license, but the file
# ckaut2.h appears to be covered by three licenses:
#   The blanket license in COPYING.TXT and ckcmai.c, which is BSD three-clause
#   BSD four-clause (w/ advertising)
#   MIT Old Style (no advertising without permission)
License:       BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND BSD-4-Clause-UC AND NTP AND X11
Source0:       ftp://ftp.kermitproject.org/kermit/archives/cku%{patchlevel}.tar.gz
Source1:       ckermit.ini
Source2:       cku-%{name}.local.ini
Source3:       cku-%{name}.modem.generic.ini
Source4:       cku-%{name}.locale.ini
Source5:       cku-%{name}.phone
Source6:       README.fedora
# See: https://bugs.gentoo.org/669332
Patch0:        ckermit-9.0.302-fix_build_with_glibc_2_28_and_earlier.patch
Patch1:        ckermit-9.0.302-printw.patch
# C99 fixes - unneeded for ckermit 10
Patch2:        ckermit-9.0.302-fedora-c99.patch
URL:           http://www.kermitproject.org/ck90.html
BuildRequires: gcc
BuildRequires: pam-devel
BuildRequires: pkgconfig
BuildRequires: openssl-devel >= 0.9.7
BuildRequires: gmp-devel >= 3.1.1
BuildRequires: ncurses-devel
BuildRequires: lockdev-devel >= 1.0.1-8
BuildRequires: make
BuildRequires: libxcrypt-devel

Requires:      lockdev >= 1.0.1-8
# NB There used to be a spurious "Obsoletes: gkermit" line here, but ckermit
# does NOT obsolete gkermit. They are independent programs with different
# purposes.

%description
C-Kermit is a combined serial and network communication software
package offering a consistent, medium-independent, cross-platform
approach to connection establishment, terminal sessions, file transfer
and management, character-set translation, and automation of
communication tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cp %{SOURCE6} .
%patch -P 0 -p 1 -b .glibc2_28
%patch -P 1 -p 1 -b .printw
%patch -P 2 -p 1 -b .c99

%build
%make_build linux \
        KFLAGS="-O0 $RPM_OPT_FLAGS -Wall -ansi -D_DEFAULT_SOURCE -DOPENSSL_097 -Dsdata=s_data -DHAVE_OPENPTY -D'krb5_init_ets(__ctx)=' -DMAINTYPE=int" \
        LNKFLAGS="%{?optflags} %{?__global_ldflags}" \
        K4LIB= \
        K4INC= \
        K5LIB=-lutil \
        K5INC=-I%{_includedir}/et \
        SSLLIB= \
        SSLINC= \
;

# convert doc file from ISO-8859-1 to UTF-8 encoding
for f in ckc%{patchlevel}.txt ; do
    iconv -fiso88591 -tutf8 $f >$f.new
    touch -r $f $f.new
    mv $f.new $f
done

%install
install -D -m 0755 wermit %{buildroot}%{_bindir}/kermit
install -D -m 0644 ckuker.nr %{buildroot}%{_mandir}/man1/kermit.1
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/kermit/ckermit.ini
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/kermit/ckermit.local.ini
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/kermit/ckermit.modem.ini
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/kermit/ckermit.locale.ini
install -D -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/kermit/ckermit.phone

%files
%license COPYING.TXT
%doc ckc%{patchlevel}.txt
%doc README.fedora
%{_bindir}/kermit
%dir %{_sysconfdir}/kermit
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/kermit/*
%{_mandir}/man1/kermit.1*

%changelog
%autochangelog
