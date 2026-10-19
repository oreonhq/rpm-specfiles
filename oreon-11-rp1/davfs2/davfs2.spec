%global source1_hash e87a7507246cc09592e4a2b27980218f2c2891fc29f52625e39d8a3a8d804b6d
%global source0_hash a5368161eb5055651d7e5e8180c1606da95e78c941b6bb8a9286df7923cfcba9
Name:           davfs2
Version:        1.7.3
Release:        1%{?dist}
Summary:        A filesystem driver for WebDAV
License:        GPL-3.0-or-later
URL:            https://savannah.nongnu.org/projects/davfs2
Source0:        https://download.savannah.gnu.org/releases/davfs2/%{name}-%{version}.tar.gz
Source1:        https://download.savannah.gnu.org/releases/davfs2/%{name}-%{version}.tar.gz.sig
Source2:        davfs2-memberlist-gpgkeys.asc
Conflicts:      filesystem < 3
%define cachedir /var/cache/davfs2
%define piddir /var/run/mount.davfs
%define username davfs2
%define groupname %{username}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  neon-devel
# /oreon:deps
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
install -d $RPM_BUILD_ROOT%{cachedir} $RPM_BUILD_ROOT%{piddir}
rm -rf $RPM_BUILD_ROOT/usr/share/doc/davfs2
chmod 0755 $RPM_BUILD_ROOT/%{_sbindir}/mount.davfs
find $RPM_BUILD_ROOT/%{_mandir}/{de,es} -name "*.[58].gz" | while read m; do 
  gzip -dc $m | iconv -f "ISO8859-15" -t "UTF-8" - -o - | gzip -c9 > $m.utf8
  mv -f $m.utf8 $m
done
install -m0644 -D davfs2.sysusers.conf %{buildroot}%{_sysusersdir}/davfs2.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
