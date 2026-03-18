Summary: Utilities for managing accounts and shadow password files
Name: shadow-utils
Version: 4.19.3
Release: 1%{?dist}
Epoch: 2
License: BSD-3-Clause AND GPL-2.0-or-later
URL: https://github.com/shadow-maint/shadow
Source0: https://github.com/shadow-maint/shadow/releases/download/4.19.3/shadow-4.19.3.tar.xz
Source1: https://github.com/shadow-maint/shadow/releases/download/4.19.3/shadow-4.19.3.tar.xz.asc
Source2: shadow-utils.useradd
Source3: shadow-utils.login.defs
Source4: shadow-bsd.txt
Source5: https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Source6: shadow-utils.HOME_MODE.xml
Source7: passwd.pamd

### Globals ###
%global includesubiddir %{_includedir}/shadow
# Fail linking if there are undefined symbols.
%global _ld_strict_symbol_defs 1

### Patches ###
# Misc manual page changes - non-upstreamable
Patch0: shadow-4.15.0-manfix.patch
# Probably non-upstreamable
Patch1: shadow-4.19.0-account-tools-setuid.patch
# https://github.com/shadow-maint/shadow/commit/3e8c105f0703264e947d8c034b90419794955d49
Patch2: shadow-4-19-useradd-support-btrfs.patch
# https://github.com/shadow-maint/shadow/commit/6be13b2f84a2c1a0d0f4129b5258b4b443e7f86c
Patch3: shadow-4.19.3-chkhash.patch

### Dependencies ###
Requires: audit-libs >= 1.6.5
Requires: libselinux >= 1.25.2-1
Requires: pam-libs
Requires: setup

### Build Dependencies ###
BuildRequires: audit-libs-devel >= 1.6.5
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: docbook-dtds
BuildRequires: docbook-style-xsl
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: git
BuildRequires: itstool
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: libcmocka-devel
BuildRequires: libeconf-devel
BuildRequires: libselinux-devel >= 1.25.2-1
BuildRequires: libsemanage-devel
BuildRequires: libtool
BuildRequires: libxcrypt-devel
BuildRequires: libxslt
BuildRequires: make
BuildRequires: pam
BuildRequires: pam-devel

### Provides ###
Provides: shadow = %{epoch}:%{version}-%{release}
Provides: passwd = 0.80-18
Obsoletes: passwd <= 0.80-19

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/adduser
Provides: /usr/sbin/useradd
Provides: /usr/sbin/userdel
Provides: /usr/sbin/usermod
Provides: /usr/sbin/groupadd
Provides: /usr/sbin/groupdel
Provides: /usr/sbin/groupmod
%endif

%description
The shadow-utils package includes the necessary programs for
converting UNIX password files to the shadow password format, plus
programs for managing user and group accounts. The pwconv command
converts passwords to the shadow password format. The pwunconv command
unconverts shadow passwords and generates a passwd file (a standard
UNIX password file). The pwck command checks the integrity of password
and shadow files. The useradd, userdel, and usermod commands are used
for managing user accounts. The groupadd, groupdel, and groupmod
commands are used for managing group accounts.


### Subpackages ###
%package subid
Summary: A library to manage subordinate uid and gid ranges

%description subid
Utility library that provides a way to manage subid ranges.


%package subid-devel
Summary: Development package for shadow-utils-subid
Requires: shadow-utils-subid = %{epoch}:%{version}-%{release}

%description subid-devel
Development files for shadow-utils-subid.

%prep
%autosetup -p 1 -S git -n shadow-4.19.3

iconv -f ISO88591 -t utf-8  doc/HOWTO > doc/HOWTO.utf8
cp -f doc/HOWTO.utf8 doc/HOWTO

cp -a %{SOURCE4} %{SOURCE5} .
cp -a %{SOURCE6} man/login.defs.d/HOME_MODE.xml

%build
autoreconf
%configure \
        --disable-account-tools-setuid \
        --enable-logind=no \
        --enable-man \
        --enable-shadowgrp \
        --enable-shared \
        --with-audit \
        --with-bcrypt \
        --with-group-name-max-length=32 \
        --with-libpam \
        --with-selinux \
        --with-sha-crypt \
        --with-yescrypt \
        --without-libbsd \
        --without-libcrack \
        --without-nscd \
        --without-sssd
%make_build

%check
make check

%install
%make_install gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale MKINSTALLDIRS=`pwd`/mkinstalldirs
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/default
install -p -c -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/login.defs
install -p -c -m 0600 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/default/useradd
install -d -m 755 $RPM_BUILD_ROOT%{_pam_confdir}
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_pam_confdir}/passwd


ln -s useradd $RPM_BUILD_ROOT%{_sbindir}/adduser
ln -s useradd.8 $RPM_BUILD_ROOT%{_mandir}/man8/adduser.8
for subdir in $RPM_BUILD_ROOT%{_mandir}/{??,??_??,??_??.*}/man* ; do
        test -d $subdir && test -e $subdir/useradd.8 && echo ".so man8/useradd.8" > $subdir/adduser.8
done

%if "%{_sbindir}" == "%{_bindir}"
# The installation script doesn't actually use the configured paths :(
mv -v $RPM_BUILD_ROOT/usr/sbin/* $RPM_BUILD_ROOT%{_bindir}/
%endif

# Remove binaries we don't use.
rm $RPM_BUILD_ROOT%{_bindir}/chfn
rm $RPM_BUILD_ROOT%{_bindir}/chsh
rm $RPM_BUILD_ROOT%{_bindir}/expiry
rm $RPM_BUILD_ROOT%{_bindir}/login
rm $RPM_BUILD_ROOT%{_bindir}/su
rm $RPM_BUILD_ROOT%{_bindir}/faillog
rm $RPM_BUILD_ROOT%{_sbindir}/logoutd
rm $RPM_BUILD_ROOT%{_sbindir}/nologin
rm $RPM_BUILD_ROOT%{_mandir}/man1/chfn.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man1/chfn.*
rm $RPM_BUILD_ROOT%{_mandir}/man1/chsh.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man1/chsh.*
rm $RPM_BUILD_ROOT%{_mandir}/man1/expiry.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man1/expiry.*
rm $RPM_BUILD_ROOT%{_mandir}/man1/login.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man1/login.*
rm $RPM_BUILD_ROOT%{_mandir}/man1/su.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man1/su.*
rm $RPM_BUILD_ROOT%{_mandir}/man5/passwd.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man5/passwd.*
rm $RPM_BUILD_ROOT%{_mandir}/man8/logoutd.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man8/logoutd.*
rm $RPM_BUILD_ROOT%{_mandir}/man8/nologin.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man8/nologin.*
rm $RPM_BUILD_ROOT%{_mandir}/man3/getspnam.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man3/getspnam.*
rm $RPM_BUILD_ROOT%{_mandir}/man5/faillog.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man5/faillog.*
rm $RPM_BUILD_ROOT%{_mandir}/man8/faillog.*
rm $RPM_BUILD_ROOT%{_mandir}/*/man8/faillog.*

# Remove PAM service files we don't use.
rm $RPM_BUILD_ROOT%{_pam_confdir}/chfn
rm $RPM_BUILD_ROOT%{_pam_confdir}/chpasswd
rm $RPM_BUILD_ROOT%{_pam_confdir}/chsh
rm $RPM_BUILD_ROOT%{_pam_confdir}/groupmems
rm $RPM_BUILD_ROOT%{_pam_confdir}/login
rm $RPM_BUILD_ROOT%{_pam_confdir}/newusers
rm $RPM_BUILD_ROOT%{_pam_confdir}/su

find $RPM_BUILD_ROOT%{_mandir} -depth -type d -empty -delete
%find_lang shadow
for dir in $(ls -1d $RPM_BUILD_ROOT%{_mandir}/{??,??_??}) ; do
    dir=$(echo $dir | sed -e "s|^$RPM_BUILD_ROOT||")
    lang=$(basename $dir)
#   echo "%%lang($lang) $dir" >> shadow.lang
#   echo "%%lang($lang) $dir/man*" >> shadow.lang
    echo "%%lang($lang) $dir/man*/*" >> shadow.lang
done

# Move header files to its own folder
echo $(ls)
mkdir -p $RPM_BUILD_ROOT/%{includesubiddir}
install -m 644 libsubid/subid.h $RPM_BUILD_ROOT/%{includesubiddir}/

# Remove .la and .a files created by libsubid
rm -f $RPM_BUILD_ROOT/%{_libdir}/libsubid.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/libsubid.a

%files -f shadow.lang
%doc NEWS doc/HOWTO README
%license gpl-2.0.txt shadow-bsd.txt
%attr(0644,root,root)   %config(noreplace) %{_sysconfdir}/login.defs
%attr(0644,root,root)   %config(noreplace) %{_sysconfdir}/default/useradd
%config(noreplace) %{_pam_confdir}/passwd
%{_bindir}/sg
%attr(4755,root,root) %{_bindir}/chage
%attr(4755,root,root) %{_bindir}/gpasswd
%attr(4755,root,root) %{_bindir}/newgrp
%attr(0755,root,root) %caps(cap_setgid=ep) %{_bindir}/newgidmap
%attr(0755,root,root) %caps(cap_setuid=ep) %{_bindir}/newuidmap
%attr(4755,root,root) %{_bindir}/passwd
%{_sbindir}/adduser
%attr(0755,root,root)   %{_sbindir}/user*
%attr(0755,root,root)   %{_sbindir}/group*
%{_sbindir}/grpck
%{_sbindir}/pwck
%{_sbindir}/*conv
%{_sbindir}/chpasswd
%{_sbindir}/chgpasswd
%{_sbindir}/newusers
%{_sbindir}/vipw
%{_sbindir}/vigr
%{_mandir}/man1/chage.1*
%{_mandir}/man1/gpasswd.1*
%{_mandir}/man1/sg.1*
%{_mandir}/man1/newgrp.1*
%{_mandir}/man1/newgidmap.1*
%{_mandir}/man1/newuidmap.1*
%{_mandir}/man1/passwd.*
%{_mandir}/man3/shadow.3*
%{_mandir}/man5/shadow.5*
%{_mandir}/man5/login.defs.5*
%{_mandir}/man5/gshadow.5*
%{_mandir}/man5/subuid.5*
%{_mandir}/man5/subgid.5*
%{_mandir}/man8/adduser.8*
%{_mandir}/man8/group*.8*
%{_mandir}/man8/user*.8*
%{_mandir}/man8/pwck.8*
%{_mandir}/man8/grpck.8*
%{_mandir}/man8/chpasswd.8*
%{_mandir}/man8/chgpasswd.8*
%{_mandir}/man8/newusers.8*
%{_mandir}/man8/*conv.8*
%{_mandir}/man8/vipw.8*
%{_mandir}/man8/vigr.8*

%files subid
%{_libdir}/libsubid.so.*
%{_bindir}/getsubids
%{_mandir}/man1/getsubids.1*

%files subid-devel
%{includesubiddir}/subid.h
%{_libdir}/libsubid.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.19.3-1
- Prepare for Oreon 11 (RP1)
