%global source5_hash b4b3765ef8ea17661f1100f1b431be087cfd3a6521491d6d961690dd5ab2dbaf
%global source0_hash 3ba8a4d549201640f2b82d53fb1bec1250f908052a7983f0061c983c634c2dac
Summary:        A threaded Internet news reader
Name: slrn
Version: 1.0.3a
Release:        21%{?dist}
License: GPL-2.0-or-later
SourceLicense:  %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-1.0-or-later AND HPND-sell-variant AND FSFULLR AND FSFUL AND FSFAP
URL: https://slrn.sourceforge.net/
Source0:        https://jedsoft.org/releases/%{name}/%{name}-%{version}.tar.bz2
Source1: slrn-pull-expire
Source2: slrnpull.log
Source4: README.rpm-slrnpull
Source5: https://jedsoft.org/releases/%{name}/%{name}-%{version}.tar.bz2.asc
Source6: %{name}-gpgkeys.gpg
Patch1: slrn-1.0.2-Do-not-strip-binaries.patch
Patch2: slrn-0.9.9pre108-sendmail.patch
Patch3: fix-FSF-address.patch
Patch4: slrn-configure-c99.patch
Requires:      slang-slsh
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  inews
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  slang-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{cron.daily,logrotate.d}
install -d $RPM_BUILD_ROOT%{_var}/spool/slrnpull/out.going
install -p doc/slrnpull/slrnpull.conf $RPM_BUILD_ROOT%{_var}/spool/slrnpull
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/slrn-pull
install -p -m644 %{SOURCE4} doc/slrnpull/README.rpm
%find_lang %{name}
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/slrn
install -m0644 -D slrn.sysusers.conf %{buildroot}%{_sysusersdir}/slrn.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n slrn-pull -f %{oreon_filedir}/slrn-pull.list

%changelog

%autochangelog
