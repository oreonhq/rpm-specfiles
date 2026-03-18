%global nspr_version 4.38.2
%global nss_version 3.121.0
# NOTE: To avoid NVR clashes of nspr* packages:
# - reset %%{nspr_release} to 1, when updating %%{nspr_version}
# - increment %%{nspr_version}, when updating the NSS part only
%global baserelease 1
%global nss_release %baserelease
# use "%%global nspr_release %%[%%baserelease+n]" to handle offsets when
# release number between nss and nspr are different.
%global nspr_release %[%baserelease+5]
# only need to update this as we added new
# algorithms under nss policy control
%global crypto_policies_version 20240521
%global unsupported_tools_directory %{_libdir}/nss/unsupported-tools
%global saved_files_dir %{_libdir}/nss/saved
%global dracutlibdir %{_prefix}/lib/dracut
%global dracut_modules_dir %{dracutlibdir}/modules.d/05nss-softokn/
%global dracut_conf_dir %{dracutlibdir}/dracut.conf.d

%bcond_without tests
%bcond_with dbm

# Produce .chk files for the final stripped binaries
#
# NOTE: The LD_LIBRARY_PATH line guarantees shlibsign links
# against the freebl that we just built. This is necessary
# because the signing algorithm changed on 3.14 to DSA2 with SHA256
# whereas we previously signed with DSA and SHA1. We must Keep this line
# until all mock platforms have been updated.
# After %%{__os_install_post} we would add
# export LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%%{_libdir}
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    $RPM_BUILD_ROOT/%{unsupported_tools_directory}/shlibsign -i $RPM_BUILD_ROOT/%{_libdir}/libsoftokn3.so \
    $RPM_BUILD_ROOT/%{unsupported_tools_directory}/shlibsign -i $RPM_BUILD_ROOT/%{_libdir}/libfreeblpriv3.so \
    $RPM_BUILD_ROOT/%{unsupported_tools_directory}/shlibsign -i $RPM_BUILD_ROOT/%{_libdir}/libfreebl3.so \
    %{?with_dbm:$RPM_BUILD_ROOT/%{unsupported_tools_directory}/shlibsign -i $RPM_BUILD_ROOT/%{_libdir}/libnssdbm3.so} \
%{nil}

# The upstream omits the trailing ".0", while we need it for
# consistency with the pkg-config version:
# https://bugzilla.redhat.com/show_bug.cgi?id=1578106
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

Summary:          Network Security Services
Name:             nss
Version:          %{nss_version}
Release:          %{nss_release}%{?dist}
License:          MPL-2.0
URL:              http://www.mozilla.org/projects/security/pki/nss/
Requires:         nspr >= %{nspr_version}
Requires:         nss-util >= %{nss_version}
# TODO: revert to same version as nss once we are done with the merge
Requires:         nss-softokn%{_isa} >= %{nss_version}
Requires:         nss-system-init
Requires:         p11-kit-trust
Requires:         crypto-policies >= %{crypto_policies_version}
# for shlibsign
BuildRequires: make
BuildRequires:    nss-softokn
BuildRequires:    sqlite-devel
BuildRequires:    zlib-devel
BuildRequires:    pkgconfig
BuildRequires:    gawk
BuildRequires:    psmisc
BuildRequires:    perl-interpreter
BuildRequires:    gcc-c++

Source0:          https://ftp.mozilla.org/pub/security/nss/releases/%{nss_release_tag}/src/%{nss_nspr_archive}.tar.gz
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
Source30:         nss-3.118-ml-dsa-test-for-sign-verify-pkcs12_files.tar.xz

Source101:        nspr-config.xml

# This patch uses the GCC -iquote option documented at
# http://gcc.gnu.org/onlinedocs/gcc/Directory-Options.html#Directory-Options
# to give the in-tree headers a higher priority over the system headers,
# when they are included through the quote form (#include "file.h").
#
# This ensures a build even when system headers are older. Such is the
# case when starting an update with API changes or even private export
# changes.
#
# Once the buildroot has been bootstrapped the patch may be removed
# but it doesn't hurt to keep it.
Patch4:           iquote.patch
Patch12:          nss-signtool-format.patch
Patch13:          nss-dso-ldflags.patch
# fedora disabled dbm by default
Patch40:          nss-no-dbm-man-page.patch

# https://issues.redhat.com/browse/FC-1613
Patch50:          nss-3.110-dissable_test-ssl_policy_pkix_oscp.patch

# ML-DSA support patches that haven't made it to the 3.118.1 release
Patch60:          nss-3.118-ml-dsa-leancrypto.patch
Patch61:          nss-3.118-ml-dsa-tls.patch
#Patch62:          nss-3.118-prefer-all-hybrid.patch

Patch65:          nss-3.118-ml-dsa-test-for-sign-verify-pkcs12.patch
Patch66:          nss-3.118-ml-dsa-tls-test.patch
Patch67:          nss-3.118-ml-dsa-unittests.patch

Patch70:          nss-3.118.1-fix-test-typo.patch

Patch100:         nspr-config-pc.patch
Patch101:         nspr-gcc-atomics.patch

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
# providing nss-system-init without version so that it can
# be replaced by a better one, e.g. supplied by the os vendor
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
# For PR_GetEnvSecure() from nspr >= 4.12
Requires:         nspr >= 4.12
# For NSS_SecureMemcmpZero() from nss-util >= 3.33
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
%setup -q -T -b 0 -n %{name}-%{nss_archive_version}
cp ./nspr/config/nspr-config.in ./nspr/config/nspr-config-pc.in

%patch -P 100 -p0 -b .flags
pushd nspr
%patch -P 101 -p1 -b .gcc-atomics
popd

pushd nss
%autopatch -p1 -M 99
popd

tar -xf %{SOURCE30}
cp -r nss-3.118-ml-dsa-test-for-sign-verify-pkcs12_files/* nss/tests/tools/

# https://bugzilla.redhat.com/show_bug.cgi?id=1247353
find nss/lib/libpkix -perm /u+x -type f -exec chmod -x {} \;


%build
# Build, check, and install NSPR for building NSS in the later phase
#
# TODO: This phase can be done by the NSS build process if we switch
# to using "make nss_build_all".  For now, however, we need some
# adjustment in the NSS build process.
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

# The assembly files are only for legacy atomics, to which we prefer GCC atomics
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

# Build NSS
#
# This package fails its testsuite with LTO.  Disable LTO for now
#%global _lto_cflags %{nil}

#export FREEBL_NO_DEPEND=1

# Must export FREEBL_LOWHASH=1 for nsslowhash.h so that it gets
# copied to dist and the rpm install phase can find it
# This due of the upstream changes to fix
# https://bugzilla.mozilla.org/show_bug.cgi?id=717906
# export FREEBL_LOWHASH=1

# uncomment if the iquote patch is activated
export IN_TREE_FREEBL_HEADERS_FIRST=1

export NSS_FORCE_FIPS=1
export NSS_DISABLE_DEPRECATED_SEED=1

# Enable compiler optimizations and disable debugging code
export BUILD_OPT=1

# Uncomment to disable optimizations
#RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed -e 's/-O2/-O0/g'`
#export RPM_OPT_FLAGS

# Generate symbolic info for debuggers
export XCFLAGS=$RPM_OPT_FLAGS

# Work around false-positive warnings with gcc 10:
# https://bugzilla.redhat.com/show_bug.cgi?id=1803029
%ifarch s390x
export XCFLAGS="$XCFLAGS -Wno-error=maybe-uninitialized"
%endif

# Similarly, but for gcc-11
export XCFLAGS="$XCFLAGS -Wno-array-parameter"

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

# Set the policy file location
# if set NSS will always check for the policy file and load if it exists
export POLICY_FILE="nss.config"
# location of the policy file
export POLICY_PATH="/etc/crypto-policies/back-ends"


%{make_build} -C ./nss all
%{make_build} -C ./nss latest

# build the man pages clean
pushd ./nss
%{__make} clean_docs build_docs
popd

# and copy them to the dist directory for %%install to find them
mkdir -p ./dist/docs/nroff
cp ./nss/doc/nroff/* ./dist/docs/nroff

# Set up our package files
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

# configuration files and setup script
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
# Run test suite.
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
# Begin -- copied from the build section

export FREEBL_NO_DEPEND=1

export BUILD_OPT=1
export NSS_DISABLE_PPC_GHASH=1
export NSS_DISABLE_DEPRECATED_SEED=1

%ifnarch noarch
%if 0%{__isa_bits} == 64
export USE_64=1
%endif
%endif

# End -- copied from the build section

# copy the nspr libraries into the NSS object directory so we use the
# newly compiled nspr binaries in our test rather than the build root
# versions
export LOBJDIR=`make -s -C ./nss/tests/common objdir_name`
for i in ./dist/lib/*.so
do
   cp $i ./dist/${LOBJDIR}/lib
done

# This is necessary because the test suite tests algorithms that are
# disabled by the system policy.
export NSS_IGNORE_SYSTEM_POLICY=1

# enable the following line to force a test failure
# find ./nss -name \*.chk | xargs rm -f

# Run test suite.
# In order to support multiple concurrent executions of the test suite
# (caused by concurrent RPM builds) on a single host,
# we'll use a random port. Also, we want to clean up any stuck
# selfserv processes. If process name "selfserv" is used everywhere,
# we can't simply do a "killall selfserv", because it could disturb
# concurrent builds. Therefore we'll do a search and replace and use
# a different process name.
# Using xargs doesn't mix well with spaces in filenames, in order to
# avoid weird quoting we'll require that no spaces are being used.

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
# man perlrun, man perlrequick
# replace word-occurrences of selfserv with selfserv_$MYRAND
find ./nss/tests -type f |\
  grep -v "\.db$" |grep -v "\.crl$" | grep -v "\.crt$" |\
  grep -vw CVS  |xargs grep -lw selfserv |\
  xargs -l perl -pi -e "s/\bselfserv\b/$RANDSERV/g" ||:

killall $RANDSERV || :

rm -rf ./tests_results
pushd nss/tests
# all.sh is the test suite script

#  don't need to run all the tests when testing packaging
#  nss_cycles: standard pkix upgradedb sharedb
#  the full list from all.sh is:
#  "cipher lowhash libpkix cert dbtests tools fips sdr crmf smime ssl ocsp merge pkits chains ec gtests ssl_gtests"
%define nss_tests "libpkix cert dbtests tools fips sdr crmf smime ssl ocsp merge pkits chains ec gtests ssl_gtests"
#  nss_ssl_tests: crl bypass_normal normal_bypass normal_fips fips_normal iopr policy
#  nss_ssl_run: cov auth stapling stress
#
# Uncomment these lines if you need to temporarily
# disable some test suites for faster test builds
# % define nss_ssl_tests "normal_fips"
# % define nss_ssl_run "cov"

HOST=localhost DOMSUF=localdomain PORT=$MYRAND NSS_CYCLES=%{?nss_cycles} NSS_TESTS=%{?nss_tests} NSS_SSL_TESTS=%{?nss_ssl_tests} NSS_SSL_RUN=%{?nss_ssl_run} ./all.sh
popd

killall $RANDSERV || :
%endif

%install

pushd nspr_build
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig

# Get rid of the things we don't want installed (per upstream)
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

# Begin -- copied from the build section
# this is needed to make sure LOBJDIR is correct

export FREEBL_NO_DEPEND=1

export BUILD_OPT=1
export NSS_DISABLE_PPC_GHASH=1

%ifnarch noarch
%if 0%{__isa_bits} == 64
export USE_64=1
%endif
%endif

# End -- copied from the build section

# get the objdir value from the test make file
export LOBJDIR=`make -s -C ./nss/tests/common objdir_name`

# There is no make install target so we'll do it ourselves.

mkdir -p $RPM_BUILD_ROOT/%{_includedir}/nss3
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/nss3/templates
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%{unsupported_tools_directory}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT/%{saved_files_dir}
mkdir -p $RPM_BUILD_ROOT/%{dracut_modules_dir}
mkdir -p $RPM_BUILD_ROOT/%{dracut_conf_dir}
%if %{defined rhel}
# not needed for rhel and its derivatives only fedora
%else
# because of the pp.1 conflict with perl-PAR-Packer
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/nss-tools
%endif

install -m 755 %{SOURCE6} $RPM_BUILD_ROOT/%{dracut_modules_dir}/module-setup.sh
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT/%{dracut_conf_dir}/50-nss-softokn.conf

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man5

# Copy the binary libraries we want
for file in libnssutil3.so libsoftokn3.so %{?with_dbm:libnssdbm3.so} libfreebl3.so libfreeblpriv3.so libnss3.so libnsssysinit.so libsmime3.so libssl3.so
do
  install -p -m 755 dist/${LOBJDIR}/lib/$file $RPM_BUILD_ROOT/%{_libdir}
done

# Install the empty NSS db files
# Legacy db
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb
%if %{with dbm}
install -p -m 644 %{SOURCE10} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/cert8.db
install -p -m 644 %{SOURCE11} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/key3.db
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/secmod.db
%endif
# Shared db
install -p -m 644 %{SOURCE13} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/cert9.db
install -p -m 644 %{SOURCE14} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/key4.db
install -p -m 644 %{SOURCE15} $RPM_BUILD_ROOT/%{_sysconfdir}/pki/nssdb/pkcs11.txt

# Copy the development libraries we want
for file in libcrmf.a libnssb.a libnssckfw.a
do
  install -p -m 644 dist/${LOBJDIR}/lib/$file $RPM_BUILD_ROOT/%{_libdir}
done

# Copy the binaries we want
for file in certutil cmsutil crlutil modutil nss-policy-check pk12util signver ssltap
do
  install -p -m 755 dist/${LOBJDIR}/bin/$file $RPM_BUILD_ROOT/%{_bindir}
done

# Copy the binaries we ship as unsupported
for file in bltest dbtool ecperf fbectest fipstest shlibsign atob btoa derdump listsuites ocspclnt pp selfserv signtool strsclnt symkeyutil tstclnt vfyserv vfychain
do
  install -p -m 755 dist/${LOBJDIR}/bin/$file $RPM_BUILD_ROOT/%{unsupported_tools_directory}
done

# Copy the include files we want
for file in dist/public/nss/*.h
do
  install -p -m 644 $file $RPM_BUILD_ROOT/%{_includedir}/nss3
done

# Copy some freebl include files we also want
for file in blapi.h alghmac.h cmac.h
do
  install -p -m 644 dist/private/nss/$file $RPM_BUILD_ROOT/%{_includedir}/nss3
done

# Copy the static freebl library
for file in libfreebl.a
do
install -p -m 644 dist/${LOBJDIR}/lib/$file $RPM_BUILD_ROOT/%{_libdir}
done

# Copy the template files we want
for file in dist/private/nss/templates.c dist/private/nss/nssck.api
do
  install -p -m 644 $file $RPM_BUILD_ROOT/%{_includedir}/nss3/templates
done

# Copy the package configuration files
install -p -m 644 ./dist/pkgconfig/nss-util.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/nss-util.pc
install -p -m 755 ./dist/pkgconfig/nss-util-config $RPM_BUILD_ROOT/%{_bindir}/nss-util-config
install -p -m 644 ./dist/pkgconfig/nss-softokn.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/nss-softokn.pc
install -p -m 755 ./dist/pkgconfig/nss-softokn-config $RPM_BUILD_ROOT/%{_bindir}/nss-softokn-config
install -p -m 644 ./dist/pkgconfig/nss.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/nss.pc
install -p -m 755 ./dist/pkgconfig/nss-config $RPM_BUILD_ROOT/%{_bindir}/nss-config
# Copy the pkcs #11 configuration script
install -p -m 755 ./dist/pkgconfig/setup-nsssysinit.sh $RPM_BUILD_ROOT/%{_bindir}/setup-nsssysinit.sh
# install a symbolic link to it, without the ".sh" suffix,
# that matches the man page documentation
ln -r -s -f $RPM_BUILD_ROOT/%{_bindir}/setup-nsssysinit.sh $RPM_BUILD_ROOT/%{_bindir}/setup-nsssysinit

# Copy the man pages for scripts
for f in %{configFiles}; do
   install -c -m 644 ${f}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${f}.1
done
# Copy the man pages for the nss tools
for f in certutil cmsutil crlutil derdump modutil pk12util signtool signver ssltap vfychain vfyserv; do
  install -c -m 644 ./dist/docs/nroff/${f}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${f}.1
done
%if %{defined rhel}
install -c -m 644 ./dist/docs/nroff/pp.1 $RPM_BUILD_ROOT%{_mandir}/man1/pp.1
%else
install -c -m 644 ./dist/docs/nroff/pp.1 $RPM_BUILD_ROOT%{_datadir}/doc/nss-tools/pp.1
%endif

# Copy the man pages for the nss databases
for f in %{dbfiles}; do
   install -c -m 644 ${f}.5 $RPM_BUILD_ROOT%{_mandir}/man5/${f}.5
done

%triggerpostun -n nss-sysinit -- nss-sysinit < 3.12.8-3
# Reverse unwanted disabling of sysinit by faulty preun sysinit scriplet
# from previous versions of nss.spec
/usr/bin/setup-nsssysinit.sh on

%post
%if %{with dbm}
%else
# Upon upgrade, ensure that the existing database locations are migrated to SQL
# database.
if test $1 -eq 2; then
    for dbdir in %{_sysconfdir}/pki/nssdb; do
        if test ! -e ${dbdir}/pkcs11.txt; then
            /usr/bin/certutil --merge -d ${dbdir} --source-dir ${dbdir}
        fi
    done
fi
%endif


%files
%{!?_licensedir:%global license %%doc}
%license nss/COPYING
%{_libdir}/libnss3.so
%{_libdir}/libssl3.so
%{_libdir}/libsmime3.so
%dir %{_sysconfdir}/pki/nssdb
%if %{with dbm}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/pki/nssdb/cert8.db
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/pki/nssdb/key3.db
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/pki/nssdb/secmod.db
%endif
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/pki/nssdb/cert9.db
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/pki/nssdb/key4.db
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/pki/nssdb/pkcs11.txt
%if %{with dbm}
%doc %{_mandir}/man5/cert8.db.5*
%doc %{_mandir}/man5/key3.db.5*
%doc %{_mandir}/man5/secmod.db.5*
%endif
%doc %{_mandir}/man5/cert9.db.5*
%doc %{_mandir}/man5/key4.db.5*
%doc %{_mandir}/man5/pkcs11.txt.5*

%files sysinit
%{_libdir}/libnsssysinit.so
%{_bindir}/setup-nsssysinit.sh
# symbolic link to setup-nsssysinit.sh
%{_bindir}/setup-nsssysinit
%doc %{_mandir}/man1/setup-nsssysinit.1*

%files tools
%{_bindir}/certutil
%{_bindir}/cmsutil
%{_bindir}/crlutil
%{_bindir}/modutil
%{_bindir}/nss-policy-check
%{_bindir}/pk12util
%{_bindir}/signver
%{_bindir}/ssltap
%{unsupported_tools_directory}/atob
%{unsupported_tools_directory}/btoa
%{unsupported_tools_directory}/derdump
%{unsupported_tools_directory}/listsuites
%{unsupported_tools_directory}/ocspclnt
%{unsupported_tools_directory}/pp
%{unsupported_tools_directory}/selfserv
%{unsupported_tools_directory}/signtool
%{unsupported_tools_directory}/strsclnt
%{unsupported_tools_directory}/symkeyutil
%{unsupported_tools_directory}/tstclnt
%{unsupported_tools_directory}/vfyserv
%{unsupported_tools_directory}/vfychain
# instead of %%{_mandir}/man*/* let's list them explicitly
# supported tools
%doc %{_mandir}/man1/certutil.1*
%doc %{_mandir}/man1/cmsutil.1*
%doc %{_mandir}/man1/crlutil.1*
%doc %{_mandir}/man1/modutil.1*
%doc %{_mandir}/man1/pk12util.1*
%doc %{_mandir}/man1/signver.1*
# unsupported tools
%doc %{_mandir}/man1/derdump.1*
%doc %{_mandir}/man1/signtool.1*
%if %{defined rhel}
%doc %{_mandir}/man1/pp.1*
%else
%dir %{_datadir}/doc/nss-tools
%doc %{_datadir}/doc/nss-tools/pp.1
%endif
%doc %{_mandir}/man1/ssltap.1*
%doc %{_mandir}/man1/vfychain.1*
%doc %{_mandir}/man1/vfyserv.1*

%files devel
%{_libdir}/libcrmf.a
%{_libdir}/pkgconfig/nss.pc
%{_bindir}/nss-config
%doc %{_mandir}/man1/nss-config.1*

%dir %{_includedir}/nss3
%{_includedir}/nss3/cert.h
%{_includedir}/nss3/certdb.h
%{_includedir}/nss3/certt.h
%{_includedir}/nss3/cmmf.h
%{_includedir}/nss3/cmmft.h
%{_includedir}/nss3/cms.h
%{_includedir}/nss3/cmsreclist.h
%{_includedir}/nss3/cmst.h
%{_includedir}/nss3/crmf.h
%{_includedir}/nss3/crmft.h
%{_includedir}/nss3/cryptohi.h
%{_includedir}/nss3/cryptoht.h
%{_includedir}/nss3/sechash.h
%{_includedir}/nss3/jar-ds.h
%{_includedir}/nss3/jar.h
%{_includedir}/nss3/jarfile.h
%{_includedir}/nss3/key.h
%{_includedir}/nss3/keyhi.h
%{_includedir}/nss3/keyt.h
%{_includedir}/nss3/keythi.h
%{_includedir}/nss3/nss.h
%{_includedir}/nss3/nssckbi.h
%{_includedir}/nss3/ocsp.h
%{_includedir}/nss3/ocspt.h
%{_includedir}/nss3/p12.h
%{_includedir}/nss3/p12plcy.h
%{_includedir}/nss3/p12t.h
%{_includedir}/nss3/pk11func.h
%{_includedir}/nss3/pk11hpke.h
%{_includedir}/nss3/pk11pqg.h
%{_includedir}/nss3/pk11priv.h
%{_includedir}/nss3/pk11pub.h
%{_includedir}/nss3/pk11sdr.h
%{_includedir}/nss3/pkcs12.h
%{_includedir}/nss3/pkcs12t.h
%{_includedir}/nss3/pkcs7t.h
%{_includedir}/nss3/preenc.h
%{_includedir}/nss3/secmime.h
%{_includedir}/nss3/secmod.h
%{_includedir}/nss3/secmodt.h
%{_includedir}/nss3/secpkcs5.h
%{_includedir}/nss3/secpkcs7.h
%{_includedir}/nss3/smime.h
%{_includedir}/nss3/ssl.h
%{_includedir}/nss3/sslerr.h
%{_includedir}/nss3/sslexp.h
%{_includedir}/nss3/sslproto.h
%{_includedir}/nss3/sslt.h

%files pkcs11-devel
%{_includedir}/nss3/nssbase.h
%{_includedir}/nss3/nssbaset.h
%{_includedir}/nss3/nssckepv.h
%{_includedir}/nss3/nssckft.h
%{_includedir}/nss3/nssckfw.h
%{_includedir}/nss3/nssckfwc.h
%{_includedir}/nss3/nssckfwt.h
%{_includedir}/nss3/nssckg.h
%{_includedir}/nss3/nssckmdt.h
%{_includedir}/nss3/nssckt.h
%{_includedir}/nss3/templates/nssck.api
%{_libdir}/libnssb.a
%{_libdir}/libnssckfw.a

%files util
%{!?_licensedir:%global license %%doc}
%license nss/COPYING
%{_libdir}/libnssutil3.so

%files util-devel
# package configuration files
%{_libdir}/pkgconfig/nss-util.pc
%{_bindir}/nss-util-config

# co-owned with nss
%dir %{_includedir}/nss3
# these are marked as public export in nss/lib/util/manifest.mk
%{_includedir}/nss3/base64.h
%{_includedir}/nss3/ciferfam.h
%{_includedir}/nss3/eccutil.h
%{_includedir}/nss3/hasht.h
%{_includedir}/nss3/kyber.h
%{_includedir}/nss3/nssb64.h
%{_includedir}/nss3/nssb64t.h
%{_includedir}/nss3/nsslocks.h
%{_includedir}/nss3/nsshash.h
%{_includedir}/nss3/nssilock.h
%{_includedir}/nss3/nssilckt.h
%{_includedir}/nss3/nssrwlk.h
%{_includedir}/nss3/nssrwlkt.h
%{_includedir}/nss3/nssutil.h
%{_includedir}/nss3/pkcs1sig.h
%{_includedir}/nss3/pkcs11.h
%{_includedir}/nss3/pkcs11f.h
%{_includedir}/nss3/pkcs11n.h
%{_includedir}/nss3/pkcs11p.h
%{_includedir}/nss3/pkcs11t.h
%{_includedir}/nss3/pkcs11u.h
%{_includedir}/nss3/pkcs11uri.h
%{_includedir}/nss3/portreg.h
%{_includedir}/nss3/secasn1.h
%{_includedir}/nss3/secasn1t.h
%{_includedir}/nss3/seccomon.h
%{_includedir}/nss3/secder.h
%{_includedir}/nss3/secdert.h
%{_includedir}/nss3/secdig.h
%{_includedir}/nss3/secdigt.h
%{_includedir}/nss3/secerr.h
%{_includedir}/nss3/secitem.h
%{_includedir}/nss3/secoid.h
%{_includedir}/nss3/secoidt.h
%{_includedir}/nss3/secport.h
%{_includedir}/nss3/utilmodt.h
%{_includedir}/nss3/utilpars.h
%{_includedir}/nss3/utilparst.h
%{_includedir}/nss3/utilrename.h
%{_includedir}/nss3/templates/templates.c

%files softokn
%if %{with dbm}
%{_libdir}/libnssdbm3.so
%{_libdir}/libnssdbm3.chk
%endif
%{_libdir}/libsoftokn3.so
%{_libdir}/libsoftokn3.chk
# shared with nss-tools
%dir %{_libdir}/nss
%dir %{saved_files_dir}
%dir %{unsupported_tools_directory}
%{unsupported_tools_directory}/bltest
%{unsupported_tools_directory}/dbtool
%{unsupported_tools_directory}/ecperf
%{unsupported_tools_directory}/fbectest
%{unsupported_tools_directory}/fipstest
%{unsupported_tools_directory}/shlibsign

%files softokn-freebl
%{!?_licensedir:%global license %%doc}
%license nss/COPYING
%{_libdir}/libfreebl3.so
%{_libdir}/libfreebl3.chk
%{_libdir}/libfreeblpriv3.so
%{_libdir}/libfreeblpriv3.chk
#shared
%dir %{dracut_modules_dir}
%{dracut_modules_dir}/module-setup.sh
%{dracut_conf_dir}/50-nss-softokn.conf

%files softokn-freebl-devel
%{_libdir}/libfreebl.a
%{_includedir}/nss3/blapi.h
%{_includedir}/nss3/blapit.h
%{_includedir}/nss3/alghmac.h
%{_includedir}/nss3/cmac.h
%{_includedir}/nss3/lowkeyi.h
%{_includedir}/nss3/lowkeyti.h

%files softokn-devel
%{_libdir}/pkgconfig/nss-softokn.pc
%{_bindir}/nss-softokn-config

# co-owned with nss
%dir %{_includedir}/nss3
#
# The following headers are those exported public in
# nss/lib/freebl/manifest.mn and
# nss/lib/softoken/manifest.mn
#
# The following list is short because many headers, such as
# the pkcs #11 ones, have been provided by nss-util-devel
# which installed them before us.
#
%{_includedir}/nss3/ecl-exp.h
%{_includedir}/nss3/nsslowhash.h
%{_includedir}/nss3/shsign.h
%{_includedir}/nss3/ml_dsat.h

%files -n nspr
%{!?_licensedir:%global license %%doc}
%license nspr/LICENSE
%{_libdir}/libnspr4.so
%{_libdir}/libplc4.so
%{_libdir}/libplds4.so

%files -n nspr-devel
%{_includedir}/nspr4
%{_libdir}/pkgconfig/nspr.pc
%{_bindir}/nspr-config
%doc %{_mandir}/man1/nspr-config.*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{nss_version}-1
- Prepare for Oreon 11 (RP1)
