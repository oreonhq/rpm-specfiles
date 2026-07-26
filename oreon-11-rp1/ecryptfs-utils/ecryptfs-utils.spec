%global source0_hash 112cb3e37e81a1ecd8e39516725dec0ce55c5f3df6284e0f4cc0f118750a987f

# FIXME rhbz#533920, automake does not support python3
%bcond_with python3

%bcond_without unittests

%global confflags %{shrink: \
 --enable-pywrap --enable-tspi --enable-nss \
 --enable-pkcs11-helper --enable-tests \
 --with-pamdir=%{_libdir}/security \
}

%global pydesc \
The package contains a module that permits\
applications written in the Python programming language to use\
the interface supplied by the %{name} library.

Name: ecryptfs-utils
Version: 111
Release: 42%{?dist}
Summary: The eCryptfs mount helper and support libraries
License: GPL-2.0-or-later
URL: https://launchpad.net/ecryptfs

Source0: http://launchpad.net/ecryptfs/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
Source1: ecryptfs-mount-private.png
Source2: ecryptfs-utils.sysusers

### upstream patches
# rhbz#1384023, openssl 1.1.x
Patch1: https://code.launchpad.net/~jelle-vdwaa/ecryptfs/ecryptfs/+merge/319746/+preview-diff/792383/+files/preview.diff#/%{name}-openssl11.patch

### downstream patches
# rhbz#500829, do not use ubuntu/debian only service
Patch92: %{name}-75-nocryptdisks.patch

# rhbz#553629, fix usage of salt together with file_passwd
Patch93: %{name}-83-fixsalt.patch

# fedora/rhel specific, rhbz#486139, remove nss dependency from umount.ecryptfs
Patch94: %{name}-83-splitnss.patch

# rhbz#664474, fix unsigned < 0 test
Patch95: %{name}-84-fixsigness.patch

# fix man pages
Patch98: %{name}-86-manpage.patch

# autoload ecryptfs module in ecryptfs-setup-private when needed, rhbz#707608
Patch99: %{name}-87-autoload.patch

# fedora/rhel specific, check for pam ecryptfs module before home migration
Patch911: %{name}-87-authconfig.patch

# using return after fork() in pam module has some nasty side effects, rhbz#722445
Patch914: %{name}-87-fixpamfork.patch

# we need gid==ecryptfs in pam module before mount.ecryptfs_private execution
Patch915: %{name}-87-fixexecgid.patch

# do not use zombie process, it causes lock ups at least for ssh login
Patch916: %{name}-87-nozombies.patch

# if we do not use zombies, we have to store passphrase in pam_data and init keyring later
Patch917: %{name}-87-pamdata.patch

# patch17 needs propper const on some places
Patch918: %{name}-87-fixconst.patch

Patch919: %{name}-87-syslog.patch

# if e-m-p fails, check if user is member of ecryptfs group
Patch921: %{name}-96-groupcheck.patch
Patch922: %{name}-99-selinux.patch

# rhbz#868330
Patch923: %{name}-100-sudokeyring.patch

# for e-u < 112
Patch924: %{name}-111-cve_2016_5224.patch

# do not crash if no password is available #1339714
Patch925: %{name}-111-nopasswd.patch

# Authconfig should no longer be used since F28
Patch926: %{name}-111-authselect.patch

# do not use ENGINE api, openssl 3 deprecated it
Patch927: ecryptfs-utils-111-noengine.patch

### patches for general cleanup, should be kept and executed after all others
# allow building with -Werror
Patch999: %{name}-75-werror.patch

BuildRequires: python-rpm-macros
BuildRequires: swig >= 1.3.31
BuildRequires: libgcrypt-devel keyutils-libs-devel openssl-devel pam-devel
BuildRequires: trousers-devel nss-devel desktop-file-utils intltool
BuildRequires: pkcs11-helper-devel
BuildRequires: automake autoconf libtool glib2-devel gettext-devel perl-podlators libattr-devel

Requires: keyutils, cryptsetup, util-linux, gettext-runtime
Requires: kmod(ecryptfs.ko)
Suggests: ecryptfs-utils-loginmount

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

%description
eCryptfs is a stacked cryptographic filesystem that ships in Linux
kernel versions 2.6.19 and above. This package provides the mount
helper and supporting libraries to perform key management and mount
functions.

Install %{name} if you would like to mount eCryptfs.

%package loginmount
Summary: The eCryptfs configuration to automount Private directory
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
BuildArch: noarch

%description loginmount
Configuration required to automatically mount eCryptfs ~/Private directory for users

%package devel
Summary: The eCryptfs userspace development package
Requires: %{name} = %{version}-%{release}
Requires: keyutils-libs-devel %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Userspace development files for eCryptfs.

%if %{with python3}
%package -n python%{python3_pkgversion}-%{name}
Summary: Python bindings for the eCryptfs utils
Requires: %{name} = %{version}-%{release}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: make
Provides: %{name}-python = %{version}-%{release}
Obsoletes:  %{name}-python < %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description -n python%{python3_pkgversion}-%{name} %pydesc
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P1 -p0 -b .openssl11

%patch -P92 -p1 -b .nocryptdisks
%patch -P93 -p1 -b .fixsalt
%patch -P94 -p1 -b .splitnss
%patch -P95 -p1 -b .fixsigness
%patch -P98 -p1 -b .manfix
%patch -P99 -p1 -b .autoload
%patch -P911 -p1 -b .authconfig
%patch -P914 -p1 -b .fixpamfork
%patch -P915 -p1 -b .fixexecgid
%patch -P916 -p1 -b .nozombies
%patch -P917 -p1 -b .pamdata
%patch -P918 -p1 -b .fixconst
%patch -P919 -p1 -b .syslog
%patch -P921 -p1 -b .groupcheck
%patch -P922 -p1 -b .selinux
%patch -P923 -p1 -b .sudokeyring
%patch -P924 -p1 -b .cve_2016_5224
%patch -P925 -p1 -b .nopasswd
%patch -P926 -p1 -b .authselect
%patch -P 927 -p1 -b .noengine

%patch -P999 -p1 -b .werror

sed -i -r 's:^_syslog\(LOG:ecryptfs_\0:' src/pam_ecryptfs/pam_ecryptfs.c

# snprintf directive output may be truncated
sed -i -r 's:(snprintf.*"\%)(s/\%)(s"):\1.42\2.23\3:' \
 tests/kernel/inotify/test.c

# fix usr-move
sed -i -r 's:(rootsbindir=).*:\1"%{_sbindir}":' configure.ac
autoreconf -fiv

%build
# openssl 1.1 marks some functions as deprecated
export ERRFLAGS="-Werror -Wtype-limits -Wno-unused -Wno-error=deprecated-declarations"

%if %{with python3}
export PYTHON_VERSION=3
export PYTHON=%{__python3}
export PYTHON_NOVERSIONCHECK=1
export PY3FLAGS='%(pkg-config --cflags --libs python3)'
export CFLAGS="$RPM_OPT_FLAGS $PY3FLAGS $ERRFLAGS"
%configure %{confflags}
%else
%configure %{confflags} --disable-pywrap
%endif
%make_build

%install
%make_install

find $RPM_BUILD_ROOT/ -name '*.la' -print -delete
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

#install files Makefile forgot to install
install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/ecryptfs-mount-private.png
printf "Encoding=UTF-8\n" >>$RPM_BUILD_ROOT/%{_datadir}/%{name}/ecryptfs-mount-private.desktop
printf "Encoding=UTF-8\n" >>$RPM_BUILD_ROOT/%{_datadir}/%{name}/ecryptfs-setup-private.desktop
printf "Icon=%{_datadir}/%{name}/ecryptfs-mount-private.png\n" >>$RPM_BUILD_ROOT/%{_datadir}/%{name}/ecryptfs-mount-private.desktop
printf "Icon=%{_datadir}/%{name}/ecryptfs-mount-private.png\n" >>$RPM_BUILD_ROOT/%{_datadir}/%{name}/ecryptfs-setup-private.desktop
sed -i 's|^_||' $RPM_BUILD_ROOT/%{_datadir}/%{name}/ecryptfs-mount-private.desktop
sed -i 's|^_||' $RPM_BUILD_ROOT/%{_datadir}/%{name}/ecryptfs-setup-private.desktop
chmod +x $RPM_BUILD_ROOT%{_datadir}/%{name}/ecryptfs-mount-private.desktop
chmod +x $RPM_BUILD_ROOT%{_datadir}/%{name}/ecryptfs-setup-private.desktop
for file in $(find py2/src/desktop -name ¸*.desktop) ; do
 touch -r $file $RPM_BUILD_ROOT%{_datadir}/%{name}/$(basename $file)
done
rm -f $RPM_BUILD_ROOT/%{_datadir}/%{name}/ecryptfs-record-passphrase

#we need ecryptfs kernel module
mkdir -p $RPM_BUILD_ROOT/usr/lib/modules-load.d/
echo -e "# ecryptfs module is needed before ecryptfs mount, so mount helper can \n# check for file name encryption support\necryptfs" \
 >$RPM_BUILD_ROOT/usr/lib/modules-load.d/ecryptfs.conf

install -p -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf

%find_lang %{name}

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/%{name}/*.desktop

if ldd $RPM_BUILD_ROOT%{_sbindir}/umount.ecryptfs | grep -q '%{_prefix}/'
then
  exit 1
fi

%if %{with unittests}
for folder in $(find . -name py\* -type d) ; do
 export LD_LIBRARY_PATH=${folder}/src/libecryptfs/.libs
 make check -C $folder
done
%endif

%pre
%if 0%{?fedora} < 42
%sysusers_create_compat %{SOURCE2}
%endif

%post loginmount
/sbin/ldconfig
if [ $1 -eq 1 ] ; then 
 # Initial installation 
 authselect enable-feature with-ecryptfs >/dev/null 2>&1
fi

%postun loginmount
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
 # Package removal, not upgrade
 authselect disable-feature with-ecryptfs >/dev/null 2>&1
fi

%files -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS THANKS
%doc doc/ecryptfs-faq.html
%doc doc/ecryptfs-pkcs11-helper-doc.txt
%{_sbindir}/mount.ecryptfs
%{_sbindir}/umount.ecryptfs
%attr(4750,root,ecryptfs) %{_sbindir}/mount.ecryptfs_private
%{_sbindir}/umount.ecryptfs_private
%{_bindir}/ecryptfs-add-passphrase
%{_bindir}/ecryptfs-find
%{_bindir}/ecryptfs-generate-tpm-key
%{_bindir}/ecryptfs-insert-wrapped-passphrase-into-keyring
%{_bindir}/ecryptfs-manager
%{_bindir}/ecryptfs-migrate-home
%{_bindir}/ecryptfs-mount-private
%{_bindir}/ecryptfs-recover-private
%{_bindir}/ecryptfs-rewrap-passphrase
%{_bindir}/ecryptfs-rewrite-file
%{_bindir}/ecryptfs-setup-private
%{_bindir}/ecryptfs-setup-swap
%{_bindir}/ecryptfs-stat
%{_bindir}/ecryptfs-umount-private
%{_bindir}/ecryptfs-unwrap-passphrase
%{_bindir}/ecryptfs-verify
%{_bindir}/ecryptfs-wrap-passphrase
%{_bindir}/ecryptfsd
%{_libdir}/ecryptfs
%{_libdir}/libecryptfs.so.*
%{_libdir}/security/pam_ecryptfs.so
%{_prefix}/lib/modules-load.d/ecryptfs.conf
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ecryptfs-mount-private.txt
%{_datadir}/%{name}/ecryptfs-mount-private.desktop
%{_datadir}/%{name}/ecryptfs-mount-private.png
%{_datadir}/%{name}/ecryptfs-setup-private.desktop
%{_mandir}/man1/ecryptfs-add-passphrase.1.gz
%{_mandir}/man1/ecryptfs-find.1*
%{_mandir}/man1/ecryptfs-generate-tpm-key.1.gz
%{_mandir}/man1/ecryptfs-insert-wrapped-passphrase-into-keyring.1.gz
%{_mandir}/man1/ecryptfs-mount-private.1.gz
%{_mandir}/man1/ecryptfs-recover-private.1.gz
%{_mandir}/man1/ecryptfs-rewrap-passphrase.1.gz
%{_mandir}/man1/ecryptfs-rewrite-file.1.gz
%{_mandir}/man1/ecryptfs-setup-private.1.gz
%{_mandir}/man1/ecryptfs-setup-swap.1.gz
%{_mandir}/man1/ecryptfs-stat.1.gz
%{_mandir}/man1/ecryptfs-umount-private.1.gz
%{_mandir}/man1/ecryptfs-unwrap-passphrase.1.gz
%{_mandir}/man1/ecryptfs-verify.1*
%{_mandir}/man1/ecryptfs-wrap-passphrase.1.gz
%{_mandir}/man1/mount.ecryptfs_private.1.gz
%{_mandir}/man1/umount.ecryptfs_private.1.gz
%{_mandir}/man7/ecryptfs.7.gz
%{_mandir}/man8/ecryptfs-manager.8.gz
%{_mandir}/man8/ecryptfs-migrate-home.8*
%{_mandir}/man8/ecryptfsd.8.gz
%{_mandir}/man8/mount.ecryptfs.8.gz
%{_mandir}/man8/pam_ecryptfs.8.gz
%{_mandir}/man8/umount.ecryptfs.8.gz
%{_sysusersdir}/%{name}.conf

%files loginmount

%files devel
%{_libdir}/libecryptfs.so
%{_libdir}/pkgconfig/libecryptfs.pc
%{_includedir}/ecryptfs.h

%if %{with python3}
%files -n python%{python3_pkgversion}-%{name}
%{python3_sitearch}/%{name}/
%{python3_sitelib}/%{name}/
%endif

%changelog
%autochangelog
