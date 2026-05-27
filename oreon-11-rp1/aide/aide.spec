%global source0_hash 23762b05f46111edeb3c8a05016c8731c01bdb8c1f91be48c156c31ab85e74c4

Summary:        Intrusion detection environment
Name:           aide
Version:        0.19.2
Release:        %autorelease
URL:            https://github.com/aide/aide
License:        GPL-2.0-or-later

Source0:        https://github.com/aide/aide/releases/download/v0.19.2/aide-0.19.2.tar.gz
Source1:        https://github.com/aide/aide/releases/download/v0.19.2/aide-0.19.2.tar.gz.asc
# gpg2 --recv-keys 2BBBD30FAAB29B3253BCFBA6F6947DAB68E7B931
# gpg2 --export --export-options export-minimal 2BBBD30FAAB29B3253BCFBA6F6947DAB68E7B931 >gpgkey-aide.gpg
Source2:        gpgkey-aide.gpg
Source3:        aide.conf
Source4:        README.quickstart
Source5:        aide.logrotate

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  bison flex
BuildRequires:  pcre2-devel
BuildRequires:  libgpg-error-devel nettle-devel
BuildRequires:  zlib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libacl-devel
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  libattr-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  audit-libs-devel
BuildRequires:  autoconf automake libtool
# For verifying signatures
BuildRequires:  gnupg2
# For being able to run 'make check'
BuildRequires:  check-devel


Requires:       logrotate

%description
AIDE (Advanced Intrusion Detection Environment) is a file integrity
checker and intrusion detection program.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp -a %{SOURCE4} .

%build
#autoreconf -ivf
%configure  \
  --disable-static \
  --with-config_file=%{_sysconfdir}/aide.conf \
  --without-gcrypt \
  --with-nettle \
  --with-zlib \
  --with-curl \
  --with-posix-acl \
  --with-selinux \
  --with-xattr \
  --with-e2fsattrs \
  --with-audit
%make_build

%check
make check

%install
%make_install bindir=%{_sbindir}
install -Dpm0644 -t %{buildroot}%{_sysconfdir} %{SOURCE3}
install -Dpm0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/aide
mkdir -p %{buildroot}%{_localstatedir}/log/aide
mkdir -p -m0700 %{buildroot}%{_localstatedir}/lib/aide

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc README.quickstart
%{_sbindir}/aide
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/aide.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/aide
%dir %attr(0700,root,root) %{_localstatedir}/lib/aide
%dir %attr(0700,root,root) %{_localstatedir}/log/aide

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19.2-1
- Prepare for Oreon 11 (RP1)
