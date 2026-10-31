%global source0_hash 623be9429f64fa2165bfc5957c6a642ec309c5cf23c0d53855c99f7591922297
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: shadow-utils
Version: 4.20.3
Release: 1%{?dist}
Summary: Account and shadow password tools
License: BSD-3-Clause AND GPL-2.0-or-later
URL: https://github.com/shadow-maint/shadow
Source0: https://github.com/shadow-maint/shadow/releases/download/%{version}/shadow-%{version}.tar.xz
Source1: shadow-%{version}.tar.xz.asc
Source2: shadow-key.gpg
Source3: shadow-utils.useradd
Source4: shadow-utils.login.defs
Source5: shadow-bsd.txt
Source6: gpl-2.0.txt
Source7: passwd.pamd

Provides: shadow = %{version}-%{release}
Provides: passwd = %{version}-%{release}
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/useradd
Provides: /usr/sbin/userdel
Provides: /usr/sbin/usermod
Provides: /usr/sbin/groupadd
Provides: /usr/sbin/groupdel
Provides: /usr/sbin/groupmod
%endif
Requires: pam%{?_isa} = 1.7.1-1%{?dist}
Requires: audit%{?_isa} = 4.2.1-1%{?dist}
Requires: libselinux%{?_isa} = 3.11-1%{?dist}
Requires: setup

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gettext
BuildRequires: pkgconf
BuildRequires: pam-devel = 1.7.1-1%{?dist}
BuildRequires: audit-devel = 4.2.1-1%{?dist}
BuildRequires: libselinux-devel = 3.11-1%{?dist}
BuildRequires: libsemanage-devel
BuildRequires: libxcrypt-devel = 4.5.2-1%{?dist}
BuildRequires: libacl-devel = 2.3.2-1%{?dist}
BuildRequires: attr-devel = 2.5.2-1%{?dist}
BuildRequires: libeconf-devel
BuildRequires: systemd-devel
BuildRequires: kernel-headers
BuildRequires: libcap = 2.78-1%{?dist}
%endif

%description
shadow-utils manages user accounts, groups, and shadow passwords.

%package subid
Summary: Library for subordinate uid and gid ranges

%description subid
libsubid and getsubids manage subordinate id ranges.

%package subid-devel
Summary: Development files for libsubid
Requires: shadow-utils-subid%{?_isa} = %{version}-%{release}

%description subid-devel
Headers and the libsubid link library.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n shadow-%{version} -p1
cp -a %{SOURCE5} %{SOURCE6} .

%build
%oreon_configure \
  --disable-static \
  --enable-shadowgrp \
  --enable-subordinate-ids \
  --with-audit \
  --with-libpam \
  --with-selinux \
  --with-acl \
  --with-btrfs \
  --with-bcrypt \
  --with-yescrypt \
  --with-fcaps \
  --with-group-name-max-length=32 \
  --without-su \
  --without-libbsd
%oreon_make

%install
%oreon_make_install
install -d -m 755 %{buildroot}%{_sysconfdir}/default
install -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/login.defs
install -p -m 0600 %{SOURCE3} %{buildroot}%{_sysconfdir}/default/useradd
install -d -m 755 %{buildroot}%{_pam_confdir}
install -m 644 %{SOURCE7} %{buildroot}%{_pam_confdir}/passwd
ln -sf useradd %{buildroot}%{_sbindir}/adduser
ln -sf useradd.8 %{buildroot}%{_mandir}/man8/adduser.8

%if "%{_sbindir}" == "%{_bindir}"
if [ -d %{buildroot}/usr/sbin ]; then
  find %{buildroot}/usr/sbin -mindepth 1 -maxdepth 1 -exec mv -t %{buildroot}%{_bindir}/ {} +
fi
%endif

for t in chfn chsh login nologin; do
  rm -f %{buildroot}%{_bindir}/$t %{buildroot}%{_sbindir}/$t
  find %{buildroot}%{_mandir} -type f -name "$t.*" -delete
  find %{buildroot}%{_mandir} -type l -name "$t.*" -delete
  rm -f %{buildroot}%{_pam_confdir}/$t
done
rm -f %{buildroot}%{_pam_confdir}/su %{buildroot}%{_pam_confdir}/groupmems
find %{buildroot} -name '*.la' -delete
find %{buildroot}%{_mandir} -depth -type d -empty -delete

main=%{_builddir}/shadow-utils.files
sub=%{_builddir}/shadow-utils-subid.files
dev=%{_builddir}/shadow-utils-subid-devel.files
: > "$main"
: > "$sub"
: > "$dev"
find %{buildroot} \( -type f -o -type l \) | sort | while read -r path; do
  rel=${path#%{buildroot}}
  case "$rel" in
    %{_sysconfdir}/login.defs|%{_sysconfdir}/default/useradd|%{_pam_confdir}/passwd)
      continue
      ;;
  esac
  case "$rel" in
    %{_mandir}/*)
      dir=$(dirname "$rel")
      base=$(basename "$rel")
      base=${base%.gz}
      line="$dir/${base}*"
      ;;
    *)
      line="$rel"
      ;;
  esac
  case "$rel" in
    %{_includedir}/shadow/*|%{_libdir}/libsubid.so)
      echo "$line" >> "$dev"
      ;;
    %{_libdir}/libsubid.so.*|%{_bindir}/getsubids|%{_bindir}/newuidmap|%{_bindir}/newgidmap|%{_mandir}/*/getsubids.1*|%{_mandir}/*/newuidmap.1*|%{_mandir}/*/newgidmap.1*)
      echo "$line" >> "$sub"
      ;;
    *)
      echo "$line" >> "$main"
      ;;
  esac
done
sort -u -o "$main" "$main"
sort -u -o "$sub" "$sub"
sort -u -o "$dev" "$dev"
sed -i \
  -e 's|^%{_bindir}/chage$|%attr(4755,root,root) %{_bindir}/chage|' \
  -e 's|^%{_bindir}/gpasswd$|%attr(4755,root,root) %{_bindir}/gpasswd|' \
  -e 's|^%{_bindir}/newgrp$|%attr(4755,root,root) %{_bindir}/newgrp|' \
  -e 's|^%{_bindir}/passwd$|%attr(4755,root,root) %{_bindir}/passwd|' \
  "$main"
sed -i \
  -e 's|^%{_bindir}/newuidmap$|%attr(0755,root,root) %caps(cap_setuid=ep) %{_bindir}/newuidmap|' \
  -e 's|^%{_bindir}/newgidmap$|%attr(0755,root,root) %caps(cap_setgid=ep) %{_bindir}/newgidmap|' \
  "$sub"

%files -f %{_builddir}/shadow-utils.files
%license COPYING shadow-bsd.txt gpl-2.0.txt
%dir %{_sysconfdir}/default
%config(noreplace) %{_sysconfdir}/login.defs
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/default/useradd
%config(noreplace) %{_pam_confdir}/passwd

%files subid -f %{_builddir}/shadow-utils-subid.files
%license COPYING

%files subid-devel -f %{_builddir}/shadow-utils-subid-devel.files
