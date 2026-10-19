%global source0_hash d122bd039416254567f2dfe7f4c9b6ed4d202d8c6a3ed91332da0d514d0974c0
%global nspr_version 4.39.0
%global nss_version 3.130.0
%global baserelease 2
%global nss_release %baserelease
%global nspr_release %[%baserelease+7]
%global crypto_policies_version 20240521
%global unsupported_tools_directory %{_libdir}/nss/unsupported-tools
%global saved_files_dir %{_libdir}/nss/saved
%global dracutlibdir %{_prefix}/lib/dracut
%global dracut_modules_dir %{dracutlibdir}/modules.d/05nss-softokn/
%global dracut_conf_dir %{dracutlibdir}/dracut.conf.d
%bcond_without tests
%bcond_with dbm
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    $RPM_BUILD_ROOT/%{unsupported_tools_directory}/shlibsign -i $RPM_BUILD_ROOT/%{_libdir}/libsoftokn3.so \
    $RPM_BUILD_ROOT/%{unsupported_tools_directory}/shlibsign -i $RPM_BUILD_ROOT/%{_libdir}/libfreeblpriv3.so \
    $RPM_BUILD_ROOT/%{unsupported_tools_directory}/shlibsign -i $RPM_BUILD_ROOT/%{_libdir}/libfreebl3.so \
    %{?with_dbm:$RPM_BUILD_ROOT/%{unsupported_tools_directory}/shlibsign -i $RPM_BUILD_ROOT/%{_libdir}/libnssdbm3.so} \
%{nil}
%{lua:
rpm.define(string.format("nspr_archive_version %s",
           string.gsub(rpm.expand("%nspr_version"), "(.*)%.0$", "%1")))
}
%{lua:
rpm.define(string.format("nss_archive_version %s",
           string.gsub(rpm.expand("%nss_version"), "(.*)%.0$", "%1")))
}
%{lua:
rpm.define(string.format("nss_release_tag NSS_%s_RTM",
           string.gsub(rpm.expand("%nss_archive_version"), "%.", "_")))
}
%global nss_nspr_archive nss-%{nss_archive_version}-with-nspr-%{nspr_archive_version}
Summary:        Network Security Services
Name:             nss
Version:          %{nss_version}
Release:        1%{?dist}
License:          MPL-2.0
URL:              http://www.mozilla.org/projects/security/pki/nss/
Requires:         nspr >= %{nspr_version}
Requires:         nss-util >= %{nss_version}
Requires:         nss-softokn%{_isa} >= %{nss_version}
Requires:         nss-system-init
Requires:         p11-kit-trust
Requires:         crypto-policies >= %{crypto_policies_version}
Source0:        https://ftp.mozilla.org/pub/security/%{name}/releases/NSS_3_130_RTM/src/%{name}-3.130-with-nspr-4.39.tar.gz
Source1:          nss-util.pc.in
Source2:          nss-util-config.in
Source3:          nss-softokn.pc.in
Source4:          nss-softokn-config.in
Source6:          nss-softokn-dracut-module-setup.sh
Source7:          nss-softokn-dracut.conf
Source8:          nss.pc.in
Source9:          nss-config.in
%if %{with dbm}
Source10:         blank-cert8.db
Source11:         blank-key3.db
Source12:         blank-secmod.db
%endif
Source13:         blank-cert9.db
Source14:         blank-key4.db
Source15:         system-pkcs11.txt
Source16:         setup-nsssysinit.sh
Source20:         nss-config.xml
Source21:         setup-nsssysinit.xml
Source22:         pkcs11.txt.xml
Source24:         cert9.db.xml
Source26:         key4.db.xml
%if %{with dbm}
Source23:         cert8.db.xml
Source25:         key3.db.xml
Source27:         secmod.db.xml
%endif
Source101:        nspr-config.xml
Patch4:           iquote.patch
Patch13:          nss-dso-ldflags.patch
Patch40:          nss-no-dbm-man-page.patch
Patch50:          nss-3.110-dissable_test-ssl_policy_pkix_oscp.patch
Patch70:          nss-3.125-drbg-reseed-after-fork.patch
Patch71:          nss-3.127-disable-dtls13-clientcert-test.patch
Patch100:         nspr-config-pc.patch
Patch101:         nspr-gcc-atomics.patch
# oreon:deps
BuildRequires:  binutils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nss-softokn
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  psmisc
BuildRequires:  sqlite-devel
BuildRequires:  xmlto
BuildRequires:  zlib-devel
# /oreon:deps
%description
Network Security Services (NSS) is a set of libraries designed to
support cross-platform development of security-enabled client and
server applications. Applications built with NSS can support SSL v2
and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509
v3 certificates, and other security standards.

%package tools
Summary:          Tools for the Network Security Services
Requires:         %{name}%{?_isa} = %{nss_version}-%{release}
%description tools
Network Security Services (NSS) is a set of libraries designed to
support cross-platform development of security-enabled client and
server applications. Applications built with NSS can support SSL v2
and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509
v3 certificates, and other security standards.

Install the nss-tools package if you need command-line tools to
manipulate the NSS certificate and key database.

%package sysinit
Summary:          System NSS Initialization
Provides:         nss-system-init
Requires:         nss%{?_isa} = %{nss_version}-%{release}
Requires(post):   coreutils, sed
%description sysinit
Default Operating System module that manages applications loading
NSS globally on the system. This module loads the system defined
PKCS #11 modules for NSS and chains with other NSS modules to load
any system or user configured modules.

%package devel
Summary:          Development libraries for Network Security Services
Provides:         nss-static = %{nss_version}-%{release}
Requires:         nss%{?_isa} = %{nss_version}-%{release}
Requires:         nss-util-devel
Requires:         nss-softokn-devel
Requires:         nspr-devel >= %{nspr_version}
Requires:         pkgconfig
BuildRequires:    xmlto
%description devel
Header and Library files for doing development with Network Security Services.

%package pkcs11-devel
Summary:          Development libraries for PKCS #11 (Cryptoki) using NSS
Provides:         nss-pkcs11-devel-static = %{nss_version}-%{release}
Requires:         nss-devel = %{nss_version}-%{release}
Requires:         nss-softokn-freebl-devel = %{nss_version}-%{release}
%description pkcs11-devel
Library files for developing PKCS #11 modules using basic NSS
low level services.

%package util
Summary:          Network Security Services Utilities Library
Requires:         nspr >= %{nspr_version}
%description util
Utilities for Network Security Services and the Softoken module

%package util-devel
Summary:          Development libraries for Network Security Services Utilities
Requires:         nss-util%{?_isa} = %{nss_version}-%{release}
Requires:         nspr-devel >= %{nspr_version}
Requires:         pkgconfig
%description util-devel
Header and library files for doing development with Network Security Services.

%package softokn
Summary:          Network Security Services Softoken Module
Requires:         nspr >= %{nspr_version}
Requires:         nss-util >= %{nss_version}-%{release}
Requires:         nss-softokn-freebl%{_isa} >= %{nss_version}-%{release}
%description softokn
Network Security Services Softoken Cryptographic Module

%package softokn-freebl
Summary:          Freebl library for the Network Security Services
Requires:         nspr >= 4.12
Requires:         nss-util >= 3.33
Conflicts:        nss < 3.12.2.99.3-5
Conflicts:        filesystem < 3
%description softokn-freebl
NSS Softoken Cryptographic Module Freebl Library

Install the nss-softokn-freebl package if you need the freebl library.

%package softokn-freebl-devel
Summary:          Header and Library files for doing development with the Freebl library for NSS
Provides:         nss-softokn-freebl-static = %{nss_version}-%{release}
Requires:         nss-softokn-freebl%{?_isa} = %{nss_version}-%{release}
%description softokn-freebl-devel
NSS Softoken Cryptographic Module Freebl Library Development Tools
This package supports special needs of some PKCS #11 module developers and
is otherwise considered private to NSS. As such, the programming interfaces
may change and the usual NSS binary compatibility commitments do not apply.
Developers should rely only on the officially supported NSS public API.

%package softokn-devel
Summary:          Development libraries for Network Security Services
Requires:         nss-softokn%{?_isa} = %{nss_version}-%{release}
Requires:         nss-softokn-freebl-devel%{?_isa} = %{nss_version}-%{release}
Requires:         nspr-devel >= %{nspr_version}
Requires:         nss-util-devel >= %{nss_version}-%{release}
Requires:         pkgconfig
%description softokn-devel
Header and library files for doing development with Network Security Services.

%package -n nspr
Summary:        Netscape Portable Runtime
Version:        %{nspr_version}
Release:        %{nspr_release}%{?dist}
License:        MPL-2.0
URL:            http://www.mozilla.org/projects/nspr/
Conflicts:      filesystem < 3
BuildRequires:  gcc
BuildRequires:  binutils >= 2.45.50-9
%description -n nspr
NSPR provides platform independence for non-GUI operating system
facilities. These facilities include threads, thread synchronization,
normal file and network I/O, interval timing and calendar time, basic
memory management (malloc and free) and shared library linking.

%package -n nspr-devel
Summary:        Development libraries for the Netscape Portable Runtime
Version:        %{nspr_version}
Release:        %{nspr_release}%{?dist}
Requires:       nspr%{?_isa} = %{nspr_version}-%{nspr_release}%{?dist}
Requires:       pkgconfig
BuildRequires:  xmlto
Conflicts:      filesystem < 3
%description -n nspr-devel
Header files for doing development with the Netscape Portable Runtime.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -T -b 0 -n %{name}-%{nss_archive_version}
cp ./nspr/config/nspr-config.in ./nspr/config/nspr-config-pc.in

%patch -P 100 -p0 -b .flags
pushd nspr
%patch -P 101 -p1 -b .gcc-atomics
popd

pushd nss
%autopatch -p1 -M 99
popd

# https://bugzilla.redhat.com/show_bug.cgi?id=1247353
find nss/lib/libpkix -perm /u+x -type f -exec chmod -x {} \;

%build

mkdir -p nspr_build
pushd nspr_build
../nspr/configure \
                 --prefix=%{_prefix} \
                 --libdir=%{_libdir} \
                 --includedir=%{_includedir}/nspr4 \
                 --with-dist-prefix=$PWD/../dist \
%ifnarch noarch
%if 0%{__isa_bits} == 64
                 --enable-64bit \
%endif
%endif
%ifarch armv7l armv7hl armv7nhl
                 --enable-thumb2 \
%endif
                 --enable-optimize="$RPM_OPT_FLAGS" \
                 --disable-debug
%ifarch i686 x86_64
sed -i '/^PR_MD_ASFILES/d' config/autoconf.mk
%endif
%{make_build}
date +"%e %B %Y" | tr -d '\n' > date.xml
echo -n %{nspr_version} > version.xml
for m in %{SOURCE101}; do
  cp ${m} .
done
for m in nspr-config.xml; do
  xmlto man ${m}
done
popd
export IN_TREE_FREEBL_HEADERS_FIRST=1
export NSS_FORCE_FIPS=1
export NSS_DISABLE_DEPRECATED_SEED=1
export BUILD_OPT=1
export XCFLAGS=$RPM_OPT_FLAGS
%ifarch s390x
export XCFLAGS="$XCFLAGS -Wno-error=maybe-uninitialized"
%endif
export XCFLAGS="$XCFLAGS -Wno-array-parameter -Wno-error=stringop-overflow"
export LDFLAGS=$RPM_LD_FLAGS
export DSO_LDFLAGS=$RPM_LD_FLAGS
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1
export NSPR_INCLUDE_DIR=$PWD/dist/include/nspr
export NSPR_LIB_DIR=$PWD/dist/lib
export NSS_USE_SYSTEM_SQLITE=1
export NSS_ALLOW_SSLKEYLOGFILE=1
export NSS_SEED_ONLY_DEV_URANDOM=1
%if %{with dbm}
%else
export NSS_DISABLE_DBM=1
%endif
%ifnarch noarch
%if 0%{__isa_bits} == 64
export USE_64=1
%endif
%endif
export POLICY_FILE="nss.config"
export POLICY_PATH="/etc/crypto-policies/back-ends"
%{make_build} -C ./nss all
%{make_build} -C ./nss latest
pushd ./nss
%{__make} clean_docs build_docs
popd
mkdir -p ./dist/docs/nroff
cp ./nss/doc/nroff/* ./dist/docs/nroff
mkdir -p ./dist/pkgconfig
cat %{SOURCE1} | sed -e "s,%%libdir%%,%{_libdir},g" \
                          -e "s,%%prefix%%,%{_prefix},g" \
                          -e "s,%%exec_prefix%%,%{_prefix},g" \
                          -e "s,%%includedir%%,%{_includedir}/nss3,g" \
                          -e "s,%%NSPR_VERSION%%,%{nspr_version},g" \
                          -e "s,%%NSSUTIL_VERSION%%,%{nss_version},g" > \
                          ./dist/pkgconfig/nss-util.pc
NSSUTIL_VMAJOR=`cat nss/lib/util/nssutil.h | grep "#define.*NSSUTIL_VMAJOR" | awk '{print $3}'`
NSSUTIL_VMINOR=`cat nss/lib/util/nssutil.h | grep "#define.*NSSUTIL_VMINOR" | awk '{print $3}'`
NSSUTIL_VPATCH=`cat nss/lib/util/nssutil.h | grep "#define.*NSSUTIL_VPATCH" | awk '{print $3}'`
cat %{SOURCE2} | sed -e "s,@libdir@,%{_libdir},g" \
                          -e "s,@prefix@,%{_prefix},g" \
                          -e "s,@exec_prefix@,%{_prefix},g" \
                          -e "s,@includedir@,%{_includedir}/nss3,g" \
                          -e "s,@MOD_MAJOR_VERSION@,$NSSUTIL_VMAJOR,g" \
                          -e "s,@MOD_MINOR_VERSION@,$NSSUTIL_VMINOR,g" \
                          -e "s,@MOD_PATCH_VERSION@,$NSSUTIL_VPATCH,g" \
                          > ./dist/pkgconfig/nss-util-config
chmod 755 ./dist/pkgconfig/nss-util-config
cat %{SOURCE3} | sed -e "s,%%libdir%%,%{_libdir},g" \
                          -e "s,%%prefix%%,%{_prefix},g" \
                          -e "s,%%exec_prefix%%,%{_prefix},g" \
                          -e "s,%%includedir%%,%{_includedir}/nss3,g" \
                          -e "s,%%NSPR_VERSION%%,%{nspr_version},g" \
                          -e "s,%%NSSUTIL_VERSION%%,%{nss_version},g" \
                          -e "s,%%SOFTOKEN_VERSION%%,%{nss_version},g" > \
                          ./dist/pkgconfig/nss-softokn.pc
SOFTOKEN_VMAJOR=`cat nss/lib/softoken/softkver.h | grep "#define.*SOFTOKEN_VMAJOR" | awk '{print $3}'`
SOFTOKEN_VMINOR=`cat nss/lib/softoken/softkver.h | grep "#define.*SOFTOKEN_VMINOR" | awk '{print $3}'`
SOFTOKEN_VPATCH=`cat nss/lib/softoken/softkver.h | grep "#define.*SOFTOKEN_VPATCH" | awk '{print $3}'`
cat %{SOURCE4} | sed -e "s,@libdir@,%{_libdir},g" \
                          -e "s,@prefix@,%{_prefix},g" \
                          -e "s,@exec_prefix@,%{_prefix},g" \
                          -e "s,@includedir@,%{_includedir}/nss3,g" \
                          -e "s,@MOD_MAJOR_VERSION@,$SOFTOKEN_VMAJOR,g" \
                          -e "s,@MOD_MINOR_VERSION@,$SOFTOKEN_VMINOR,g" \
                          -e "s,@MOD_PATCH_VERSION@,$SOFTOKEN_VPATCH,g" \
                          > ./dist/pkgconfig/nss-softokn-config
chmod 755 ./dist/pkgconfig/nss-softokn-config
cat %{SOURCE8} | sed -e "s,%%libdir%%,%{_libdir},g" \
                          -e "s,%%prefix%%,%{_prefix},g" \
                          -e "s,%%exec_prefix%%,%{_prefix},g" \
                          -e "s,%%includedir%%,%{_includedir}/nss3,g" \
                          -e "s,%%NSS_VERSION%%,%{nss_version},g" \
                          -e "s,%%NSPR_VERSION%%,%{nspr_version},g" \
                          -e "s,%%NSSUTIL_VERSION%%,%{nss_version},g" \
                          -e "s,%%SOFTOKEN_VERSION%%,%{nss_version},g" > \
                          ./dist/pkgconfig/nss.pc
NSS_VMAJOR=`cat nss/lib/nss/nss.h | grep "#define.*NSS_VMAJOR" | awk '{print $3}'`
NSS_VMINOR=`cat nss/lib/nss/nss.h | grep "#define.*NSS_VMINOR" | awk '{print $3}'`
NSS_VPATCH=`cat nss/lib/nss/nss.h | grep "#define.*NSS_VPATCH" | awk '{print $3}'`
cat %{SOURCE9} | sed -e "s,@libdir@,%{_libdir},g" \
                          -e "s,@prefix@,%{_prefix},g" \
                          -e "s,@exec_prefix@,%{_prefix},g" \
                          -e "s,@includedir@,%{_includedir}/nss3,g" \
                          -e "s,@MOD_MAJOR_VERSION@,$NSS_VMAJOR,g" \
                          -e "s,@MOD_MINOR_VERSION@,$NSS_VMINOR,g" \
                          -e "s,@MOD_PATCH_VERSION@,$NSS_VPATCH,g" \
                          > ./dist/pkgconfig/nss-config
chmod 755 ./dist/pkgconfig/nss-config
cat %{SOURCE16} > ./dist/pkgconfig/setup-nsssysinit.sh
chmod 755 ./dist/pkgconfig/setup-nsssysinit.sh
cp ./nss/lib/ckfw/nssck.api ./dist/private/nss/
date +"%e %B %Y" | tr -d '\n' > date.xml
echo -n %{nss_version} > version.xml
%if %{with dbm}
%global XMLSOURCES %{SOURCE23} %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27}
%global dbfiles cert8.db key3.db secmod.db cert9.db key4.db pkcs11.txt
%else
%global XMLSOURCES %{SOURCE22} %{SOURCE24} %{SOURCE26}
%global dbfiles cert9.db key4.db pkcs11.txt
%endif
for m in %{SOURCE20} %{SOURCE21} %{XMLSOURCES}; do
  cp ${m} .
done
%global configFiles nss-config setup-nsssysinit
for m in %{configFiles}  %{dbfiles}; do
  xmlto man ${m}.xml
done
%check

%if %{with tests}
pushd nspr_build
perl ../nspr/pr/tests/runtests.pl 2>&1 | tee output.log
TEST_FAILURES=`grep -c FAILED ./output.log` || :
if [ $TEST_FAILURES -ne 0 ]; then
  echo "error: test suite returned failure(s)"
  exit 1
fi
echo "test suite completed"
popd
%endif
%if %{with tests}
export FREEBL_NO_DEPEND=1
export BUILD_OPT=1
export NSS_DISABLE_PPC_GHASH=1
export NSS_DISABLE_DEPRECATED_SEED=1
%ifnarch noarch
%if 0%{__isa_bits} == 64
export USE_64=1
%endif
%endif
export LOBJDIR=`make -s -C ./nss/tests/common objdir_name`
for i in ./dist/lib/*.so
do
   cp $i ./dist/${LOBJDIR}/lib
done
export NSS_IGNORE_SYSTEM_POLICY=1
SPACEISBAD=`find ./nss/tests | grep -c ' '` ||:
if [ $SPACEISBAD -ne 0 ]; then
  echo "error: filenames containing space are not supported (xargs)"
  exit 1
fi
export MYRAND=`perl -e 'print 9000 + int rand 1000'`; echo $MYRAND
export RANDSERV=selfserv_${MYRAND}; echo $RANDSERV
export DISTBINDIR=./dist/${LOBJDIR}/bin
pushd "$DISTBINDIR"
ln -s selfserv $RANDSERV
popd
find ./nss/tests -type f |\
  grep -v "\.db$" |grep -v "\.crl$" | grep -v "\.crt$" |\
  grep -vw CVS  |xargs grep -lw selfserv |\
  xargs -l perl -pi -e "s/\bselfserv\b/$RANDSERV/g" ||:
killall $RANDSERV || :
rm -rf ./tests_results
pushd nss/tests
%define nss_tests "libpkix cert dbtests tools fips sdr smime ssl ocsp merge pkits chains ec gtests ssl_gtests"
HOST=localhost DOMSUF=localdomain PORT=$MYRAND NSS_CYCLES=%{?nss_cycles} NSS_TESTS=%{?nss_tests} NSS_SSL_TESTS=%{?nss_ssl_tests} NSS_SSL_RUN=%{?nss_ssl_run} ./all.sh
popd
killall $RANDSERV || :
%endif
%install
pushd nspr_build
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
rm -rf \
   $RPM_BUILD_ROOT/%{_bindir}/compile-et.pl \
   $RPM_BUILD_ROOT/%{_bindir}/prerr.properties \
   $RPM_BUILD_ROOT/%{_libdir}/libnspr4.a \
   $RPM_BUILD_ROOT/%{_libdir}/libplc4.a \
   $RPM_BUILD_ROOT/%{_libdir}/libplds4.a \
   $RPM_BUILD_ROOT/%{_datadir}/aclocal/nspr.m4 \
   $RPM_BUILD_ROOT/%{_includedir}/nspr4/md
for f in nspr-config; do
   install -c -m 644 ${f}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${f}.1
done
popd
export FREEBL_NO_DEPEND=1
export BUILD_OPT=1
export NSS_DISABLE_PPC_GHASH=1
%ifnarch noarch
%if 0%{__isa_bits} == 64
export USE_64=1
%endif
%endif
export LOBJDIR=`make -s -C ./nss/tests/common objdir_name`
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/nss3
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/nss3/templates
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%{unsupported_tools_directory}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT/%{saved_files_dir}
mkdir -p $RPM_BUILD_ROOT/%{dracut_modules_dir}
mkdir -p $RPM_BUILD_ROOT/%{dracut_conf_dir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/nss-tools
install -m 755 %{SOURCE6} $RPM_BUILD_ROOT/%{dracut_modules_dir}/module-setup.sh
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT/%{dracut_conf_dir}/50-nss-softokn.conf
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man5
for file in libnssutil3.so libsoftokn3.so %{?with_dbm:libnssdbm3.so} libfreebl3.so libfreeblpriv3.so libnss3.so libnsssysinit.so libsmime3.so libssl3.so
do
  install -p -m 755 dist/${LOBJDIR}/lib/$file $RPM_BUILD_ROOT/%{_libdir}
done
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb
%if %{with dbm}
install -p -m 644 %{SOURCE10} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/cert8.db
install -p -m 644 %{SOURCE11} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/key3.db
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/secmod.db
%endif
install -p -m 644 %{SOURCE13} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/cert9.db
install -p -m 644 %{SOURCE14} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/key4.db
install -p -m 644 %{SOURCE15} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/pkcs11.txt
for file in libnssb.a libnssckfw.a
do
  install -p -m 644 dist/${LOBJDIR}/lib/$file $RPM_BUILD_ROOT/%{_libdir}
done
for file in certutil cmsutil crlutil modutil nss-policy-check pk12util signver ssltap
do
  install -p -m 755 dist/${LOBJDIR}/bin/$file $RPM_BUILD_ROOT/%{_bindir}
done
for file in bltest dbtool ecperf fbectest fipstest shlibsign atob btoa derdump listsuites ocspclnt pp selfserv signtool strsclnt symkeyutil tstclnt vfyserv vfychain
do
  install -p -m 755 dist/${LOBJDIR}/bin/$file $RPM_BUILD_ROOT/%{unsupported_tools_directory}
done
for file in dist/public/nss/*.h
do
  install -p -m 644 $file $RPM_BUILD_ROOT/%{_includedir}/nss3
done
for file in blapi.h alghmac.h cmac.h
do
  install -p -m 644 dist/private/nss/$file $RPM_BUILD_ROOT/%{_includedir}/nss3
done
for file in libfreebl.a
do
install -p -m 644 dist/${LOBJDIR}/lib/$file $RPM_BUILD_ROOT/%{_libdir}
done
for file in dist/private/nss/templates.c dist/private/nss/nssck.api
do
  install -p -m 644 $file $RPM_BUILD_ROOT/%{_includedir}/nss3/templates
done
install -p -m 644 ./dist/pkgconfig/nss-util.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/nss-util.pc
install -p -m 755 ./dist/pkgconfig/nss-util-config $RPM_BUILD_ROOT/%{_bindir}/nss-util-config
install -p -m 644 ./dist/pkgconfig/nss-softokn.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/nss-softokn.pc
install -p -m 755 ./dist/pkgconfig/nss-softokn-config $RPM_BUILD_ROOT/%{_bindir}/nss-softokn-config
install -p -m 644 ./dist/pkgconfig/nss.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/nss.pc
install -p -m 755 ./dist/pkgconfig/nss-config $RPM_BUILD_ROOT/%{_bindir}/nss-config
install -p -m 755 ./dist/pkgconfig/setup-nsssysinit.sh $RPM_BUILD_ROOT/%{_bindir}/setup-nsssysinit.sh
ln -r -s -f $RPM_BUILD_ROOT/%{_bindir}/setup-nsssysinit.sh $RPM_BUILD_ROOT/%{_bindir}/setup-nsssysinit
for f in %{configFiles}; do
   install -c -m 644 ${f}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${f}.1
done
for f in certutil cmsutil crlutil derdump modutil pk12util signtool signver ssltap vfychain vfyserv; do
  install -c -m 644 ./dist/docs/nroff/${f}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${f}.1
done
install -c -m 644 ./dist/docs/nroff/pp.1 $RPM_BUILD_ROOT%{_datadir}/doc/nss-tools/pp.1
for f in %{dbfiles}; do
   install -c -m 644 ${f}.5 $RPM_BUILD_ROOT%{_mandir}/man5/${f}.5
done
%oreon_autofiles nspr usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nspr-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%triggerpostun -n nss-sysinit -- nss-sysinit < 3.12.8-3

/usr/bin/setup-nsssysinit.sh on
%post

%if %{with dbm}
%else
if test $1 -eq 2; then
    for dbdir in %{_sysconfdir}/pki/nssdb; do
        if test ! -e ${dbdir}/pkcs11.txt; then
            /usr/bin/certutil --merge -d ${dbdir} --source-dir ${dbdir}
        fi
    done
fi
%endif
%files -f %{oreon_filedir}/main.list
%files -n nss-tools -f %{oreon_filedir}/nss-tools.list
%files -n nss-sysinit -f %{oreon_filedir}/nss-sysinit.list
%files -n nss-devel -f %{oreon_filedir}/nss-devel.list
%files -n nss-pkcs11-devel -f %{oreon_filedir}/nss-pkcs11-devel.list
%files -n nss-util -f %{oreon_filedir}/nss-util.list
%files -n nss-util-devel -f %{oreon_filedir}/nss-util-devel.list
%files -n nss-softokn -f %{oreon_filedir}/nss-softokn.list
%files -n nss-softokn-freebl -f %{oreon_filedir}/nss-softokn-freebl.list
%files -n nss-softokn-freebl-devel -f %{oreon_filedir}/nss-softokn-freebl-devel.list
%files -n nss-softokn-devel -f %{oreon_filedir}/nss-softokn-devel.list
%files -n nspr -f %{oreon_filedir}/nspr.list
%files -n nspr-devel -f %{oreon_filedir}/nspr-devel.list

%changelog

%autochangelog
