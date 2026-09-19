%global source0_hash 3ba8a4d549201640f2b82d53fb1bec1250f908052a7983f0061c983c634c2dac

Summary: A threaded Internet news reader
Name: slrn
Version: 1.0.3a
Release: 21%{?dist}
# COPYRIGHT:    GPL-2.0-or-later
# src:          GPL-2.0-or-later
# src/vms.c:    "donated for use in slrn by Andrew Greer"
## Not in any binary package
# autoconf/config.guess:        GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# autoconf/config.rpath:        FSFULLR
# autoconf/config.sub:          GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# autoconf/include/ax_lib_socket_nsl.m4:    FSFAP
# autoconf/include/gettext.m4:  GPL-1.0-or-later
# autoconf/include/iconv.m4:    FSFULLR
# autoconf/include/lib-ld.m4:   FSFULLR
# autoconf/include/lib-link.m4: FSFULLR
# autoconf/include/lib-prefix.m4:   FSFULLR
# autoconf/include/mkdirp.m4:   FSFULLR
# autoconf/include/nls.m4:      FSFULLR
# autoconf/include/po.m4:       FSFULLR
# autoconf/include/progtest.m4: FSFULLR
# autoconf/install.sh:          HPND-sell-variant
# configure:    FSFUL AND FSFAP AND FSFULLR
# contrib/cleanscore:       GPL-2.0-or-later
# po/Makefile.in.in:        "copied and used freely without restrictions"
License: GPL-2.0-or-later
SourceLicense:  %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-1.0-or-later AND HPND-sell-variant AND FSFULLR AND FSFUL AND FSFAP
URL: https://slrn.sourceforge.net/
Source0: https://jedsoft.org/releases/%{name}/%{name}-%{version}.tar.bz2
Source1: slrn-pull-expire
Source2: slrnpull.log
Source4: README.rpm-slrnpull
Source5: https://jedsoft.org/releases/%{name}/%{name}-%{version}.tar.bz2.asc
# 2016-06-09:
# Merged GPG keys from https://rg3.github.io/youtube-dl/download.html in one file
# gpg --export  --export-options export-minimal "428D F5D6 3EF0 7494 BB45 5AC0 EBF0 1804 BCF0 5F6B" \
# "ED7F 5BF4 6B3B BED8 1C87 368E 2C39 3E0F 18A9 236D" \
# "7D33 D762 FD6C 3513 0481 347F DB4B 54CB A482 6A18" > youtube-dl-gpgkeys.gpg
Source6: %{name}-gpgkeys.gpg
# Do not strip binaries by make install
Patch1: slrn-1.0.2-Do-not-strip-binaries.patch
Patch2: slrn-0.9.9pre108-sendmail.patch
Patch3: fix-FSF-address.patch
Patch4: slrn-configure-c99.patch
# Patch4: slrn-dont-limit-signatures.patch
BuildRequires: make
BuildRequires: inews
BuildRequires: openssl-devel, gcc
BuildRequires: slang-devel >= 2.2.3
BuildRequires: systemd-rpm-macros
# Some s-lang scripts (smime.sl) use slsh interpreter
Requires:      slang-slsh
%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
Requires(pre): shadow-utils
%endif
# For source verification with gpgv
BuildRequires:  gnupg2

%description
SLRN is a threaded Internet news reader. SLRN is highly customizable
and allows users to design complex filters for sorting or killing news
articles. SLRN works well over slow network lines. A helper utility
for reading news offline is provided in the slrn-pull package.

%package pull
Summary: Offline news reading support for the SLRN news reader
Requires: slrn%{?_isa} = %{version}-%{release}
Requires: crontabs

%description pull
The slrn-pull package provides the slrnpull utility, which allows you
to set up a small news spool for offline news reading using the SLRN
news reader. You also need to have the slrn package installed to use
the slrnpull utility.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%define shortver %(echo %{version}|tr -d 'a')
gpgv2 --quiet --keyring %{SOURCE6} %{SOURCE5} %{SOURCE0}
%setup -q -n %{name}-%{shortver}
%patch -P1 -p1 -b .nostrip
%patch -P2 -p1 -b .sendmail
%patch -P3 -p1 -b .FSFaddress
%patch -P4 -p1
#%#patch4 -p1 -b .longsignatures

for i in changes.txt; do
  iconv -f iso8859-1 -t utf8 -o ${i}{_,} && touch -r ${i}{,_} && mv -f ${i}{_,}
done

chmod 644 doc/slrnpull/* contrib/*

# Create a sysusers.d config file
# Static UID and GID defined by /usr/share/doc/setup-*/uidgid
cat >slrn.sysusers.conf <<EOF
g news 13
u news 9 'news user' - -
EOF

%build
%configure \
    --with-ssl=%{_prefix} \
    --without-nss-compat \
    --with-slrnpull=%{_var}/spool/slrnpull \
    --without-x \
    --enable-charmap \
    --enable-emph-text \
    --enable-inews \
    --enable-nls \
    --enable-nntp \
    --disable-rpath \
    --enable-setgid-code \
    --enable-spoilers \
    --enable-warnings
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m644 doc/slrn.rc $RPM_BUILD_ROOT%{_sysconfdir}/slrn.rc

# slrnpull stuff
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{cron.daily,logrotate.d}
install -d $RPM_BUILD_ROOT%{_var}/spool/slrnpull/out.going
install -p doc/slrnpull/slrnpull.conf $RPM_BUILD_ROOT%{_var}/spool/slrnpull
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/slrn-pull
install -p -m644 %{SOURCE4} doc/slrnpull/README.rpm

%find_lang %{name}

# remove unpackaged files from the buildroot
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/slrn

install -m0644 -D slrn.sysusers.conf %{buildroot}%{_sysusersdir}/slrn.conf

%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
# Static UID and GID defined by /usr/share/doc/setup-*/uidgid
%pre
getent group news >/dev/null || groupadd -r -g 13 news
getent passwd news >/dev/null || \
  useradd -r -u 9 -g news -d / -s /sbin/nologin -c "news user" news
exit 0
%endif

%files -f %{name}.lang
%license COPYING COPYRIGHT
%doc changes.txt NEWS README
%doc doc/FAQ doc/FIRST_STEPS doc/README.* doc/THANKS doc/*.txt doc/slrn*.html
%doc doc/score.sl contrib
%config(noreplace) %{_sysconfdir}/slrn.rc
%{_bindir}/slrn
%{_datadir}/slrn
%{_mandir}/man1/slrn.1*
%{_sysusersdir}/slrn.conf

%files pull
%doc doc/slrnpull/*
%config(noreplace) %{_sysconfdir}/cron.daily/slrn-pull-expire
%config(noreplace) %{_sysconfdir}/logrotate.d/slrn-pull
%{_bindir}/slrnpull
%attr(775,news,news) %dir %{_var}/spool/slrnpull
%attr(3777,news,news) %dir %{_var}/spool/slrnpull/out.going
%attr(644,news,news) %config(noreplace) %{_var}/spool/slrnpull/slrnpull.conf
%{_mandir}/man1/slrnpull.1*

%changelog
%autochangelog
