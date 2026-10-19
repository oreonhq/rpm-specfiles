%global source5_hash edaef632cbb643e4e7a221717a6c441a4c1a7c918e6e4d56debc3d8739b233f6
%global source1_hash 7e339baf514d8b141e739f1c11c88d3816b1bfdf32f69bfd069db8b4edd2d61b
%global source0_hash 623be9429f64fa2165bfc5957c6a642ec309c5cf23c0d53855c99f7591922297
Summary:        Utilities for managing accounts and shadow password files
Name: shadow-utils
Version: 4.20.3
Release:        1%{?dist}
Epoch: 2
License: BSD-3-Clause AND GPL-2.0-or-later
URL: https://github.com/shadow-maint/shadow
Source0:        https://github.com/shadow-maint/shadow/releases/download/%{version}/shadow-%{version}.tar.xz
Source1: https://github.com/shadow-maint/shadow/releases/download/%{version}/shadow-%{version}.tar.xz.asc
Source2: shadow-utils.useradd
Source3: shadow-utils.login.defs
Source4: shadow-bsd.txt
Source5: https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Source6: shadow-utils.HOME_MODE.xml
Source7: passwd.pamd
%global includesubiddir %{_includedir}/shadow
%global _ld_strict_symbol_defs 1
Patch0: shadow-4.15.0-manfix.patch
Requires: audit-libs >= 1.6.5
Requires: libselinux >= 1.25.2-1
Requires: pam-libs
Requires: setup
Provides: shadow = %{epoch}:%{version}-%{release}
Provides: passwd = 0.80-18
Obsoletes: passwd <= 0.80-19
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/adduser
Provides: /usr/sbin/useradd
Provides: /usr/sbin/userdel
Provides: /usr/sbin/usermod
Provides: /usr/sbin/groupadd
Provides: /usr/sbin/groupdel
Provides: /usr/sbin/groupmod
%endif
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  itstool
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libcmocka-devel
BuildRequires:  libeconf-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsemanage-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pam
BuildRequires:  pam-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p 1 -S git -n shadow-%{version}

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
mv -v $RPM_BUILD_ROOT/usr/sbin/* $RPM_BUILD_ROOT%{_bindir}/
%endif
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
    echo "%%lang($lang) $dir/man*/*" >> shadow.lang
done
echo $(ls)
mkdir -p $RPM_BUILD_ROOT/%{includesubiddir}
install -m 644 libsubid/subid.h $RPM_BUILD_ROOT/%{includesubiddir}/
rm -f $RPM_BUILD_ROOT/%{_libdir}/libsubid.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/libsubid.a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n shadow-utils-subid -f %{oreon_filedir}/shadow-utils-subid.list
%files -n shadow-utils-subid-devel -f %{oreon_filedir}/shadow-utils-subid-devel.list

%changelog

%autochangelog
