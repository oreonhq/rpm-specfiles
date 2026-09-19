%global source0_hash a5368161eb5055651d7e5e8180c1606da95e78c941b6bb8a9286df7923cfcba9

Name:           davfs2
Version:        1.7.3
Release:        1%{?dist}
Summary:        A filesystem driver for WebDAV
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://savannah.nongnu.org/projects/davfs2
Source0:        https://download.savannah.gnu.org/releases/davfs2/%{name}-%{version}.tar.gz
Source1:        https://download.savannah.gnu.org/releases/davfs2/%{name}-%{version}.tar.gz.sig
# key retrieved via
#  wget -O davfs2-memberlist-gpgkeys.asc 'https://savannah.nongnu.org/project/memberlist-gpgkeys.php?group=davfs2&download=1'
# Using the URL above directly as "Source2" does not work as spectool/mock do
# no not like the query string.
Source2:        davfs2-memberlist-gpgkeys.asc

Conflicts:      filesystem < 3
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  neon-devel
BuildRequires:  make

%define cachedir /var/cache/davfs2
%define piddir /var/run/mount.davfs
%define username davfs2
%define groupname %{username}

%description
davfs2 is a Linux file system driver that allows you to mount a WebDAV server
as a disk drive.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

# Create a sysusers.d config file
cat >davfs2.sysusers.conf <<EOF
g davfs2 -
u davfs2 - 'User account for %{name}' %{cachedir} -
EOF

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure ssbindir=%{_sbindir}
%make_build

%install
%make_install
%find_lang %{name}
# Create directories used by mount.davfs
install -d $RPM_BUILD_ROOT%{cachedir} $RPM_BUILD_ROOT%{piddir}
# Don't need this - we'll do our own doc install, thanks
rm -rf $RPM_BUILD_ROOT/usr/share/doc/davfs2
# Remove suid bit, to work around a problem with brp-strip on suid binaries
chmod 0755 $RPM_BUILD_ROOT/%{_sbindir}/mount.davfs
# UTF8ify translated man pages
find $RPM_BUILD_ROOT/%{_mandir}/{de,es} -name "*.[58].gz" | while read m; do 
  gzip -dc $m | iconv -f "ISO8859-15" -t "UTF-8" - -o - | gzip -c9 > $m.utf8
  mv -f $m.utf8 $m
done

install -m0644 -D davfs2.sysusers.conf %{buildroot}%{_sysusersdir}/davfs2.conf

%files -f %{name}.lang
# Docs
%license AUTHORS COPYING
%doc BUGS ChangeLog FAQ INSTALL NEWS README.md README.translators THANKS TODO
%{_mandir}/man5/*.gz
%{_mandir}/man8/*.gz
# localized man pages
%{_mandir}/*/man5/*.gz
%{_mandir}/*/man8/*.gz

# Configfiles etc.
%config(noreplace) %{_sysconfdir}/davfs2/davfs2.conf
%config(noreplace) %{_sysconfdir}/davfs2/secrets
%dir %{_sysconfdir}/davfs2/certs/private/
%dir %{_sysconfdir}/davfs2/certs/
%dir %{_sysconfdir}/davfs2/
%dir %{_datarootdir}/davfs2/
%{_datarootdir}/davfs2/*

# Binaries
%{_sbindir}/umount.davfs
# re-apply suid bit to mount.davfs
%attr (4755,root,root) %{_sbindir}/mount.davfs

# Extra dirs needed by mount.davfs
%ghost %dir %attr(00775,root,%{groupname}) %{cachedir}
%ghost %dir %attr(01775,root,%{groupname}) %{piddir}
%{_sysusersdir}/davfs2.conf

%changelog
%autochangelog
