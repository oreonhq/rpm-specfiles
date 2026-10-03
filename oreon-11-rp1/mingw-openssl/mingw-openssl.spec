%global source0_hash b23ad7fd9f73e43ad1767e636040e88ba7c9e5775bfa5618436a0dd2c17c3716

%global mingw_build_ucrt64 1
%{?mingw_package_header}

# For the curious:
# 0.9.8jk + EAP-FAST soversion = 8
# 1.0.0 soversion = 10
# 1.1.0 soversion = 1.1 (same as upstream although presence of some symbols
#                        depends on build configuration options)
%global soversion 3

# Enable the tests.
# These only work some of the time, but fail randomly at other times
# (although I have had them complete a few times, so I don't think
# there is any actual problem with the binaries).
%global run_tests 0

Name:           mingw-openssl
Version:        3.2.4
Release:        4%{?dist}
Summary:        MinGW port of the OpenSSL toolkit

License:        OpenSSL
URL:            http://www.openssl.org/

Source:  https://www.openssl.org/source/openssl-%{version}.tar.gz
Source2:        Makefile.certificate
Source3:        genpatches
Source6:        make-dummy-cert
Source7:        renew-dummy-cert
Source12:        ec_curve.c
Source13:        ectest.c

# Patches exported from source git
# Aarch64 and ppc64le use lib64
Patch1:   0001-Aarch64-and-ppc64le-use-lib64.patch
# Use more general default values in openssl.cnf
Patch2:   0002-Use-more-general-default-values-in-openssl.cnf.patch
# Do not install html docs
Patch3:   0003-Do-not-install-html-docs.patch
# Override default paths for the CA directory tree
Patch4:   0004-Override-default-paths-for-the-CA-directory-tree.patch
# apps/ca: fix md option help text
Patch5:   0005-apps-ca-fix-md-option-help-text.patch
# Disable signature verification with totally unsafe hash algorithms
Patch6:   0006-Disable-signature-verification-with-totally-unsafe-h.patch
# Add support for PROFILE=SYSTEM system default cipherlist
Patch7:   0007-Add-support-for-PROFILE-SYSTEM-system-default-cipher.patch
# Add FIPS_mode() compatibility macro
Patch8:   0008-Add-FIPS_mode-compatibility-macro.patch
# Add check to see if fips flag is enabled in kernel
Patch9:   0009-Add-Kernel-FIPS-mode-flag-support.patch
# Instead of replacing ectest.c and ec_curve.c, add the changes as a patch so
# that new modifications made to these files by upstream are not lost.
Patch10:  0010-Add-changes-to-ectest-and-eccurve.patch
# remove unsupported EC curves
Patch11:  0011-Remove-EC-curves.patch
# Disable explicit EC curves
# https://bugzilla.redhat.com/show_bug.cgi?id=2066412
Patch12:  0012-Disable-explicit-ec.patch
# Skipped tests from former 0011-Remove-EC-curves.patch
Patch13:  0013-skipped-tests-EC-curves.patch
# Instructions to load legacy provider in openssl.cnf
Patch24:  0024-load-legacy-prov.patch
# We load FIPS provider and set FIPS properties implicitly
Patch32:  0032-Force-fips.patch
# Embed HMAC into the fips.so
# RWMJ: Remove this patch for mingw as it causes
# > link.h: No such file or directory
# Patch33:  0033-FIPS-embed-hmac.patch
# Comment out fipsinstall command-line utility
Patch34:  0034.fipsinstall_disable.patch
# Skip unavailable algorithms running `openssl speed`
Patch35:  0035-speed-skip-unavailable-dgst.patch
# Extra public/private key checks required by FIPS-140-3
Patch44:  0044-FIPS-140-3-keychecks.patch
# Minimize fips services
# Remove this patch on mingw as it causes:
# > error: 'REDHAT_FIPS_VERSION' undeclared
# Patch45:  0045-FIPS-services-minimize.patch
# Execute KATS before HMAC verification
# RWMJ: Broken by removal of 0033
# Patch47:  0047-FIPS-early-KATS.patch
# Selectively disallow SHA1 signatures rhbz#2070977
Patch49:  0049-Allow-disabling-of-SHA1-signatures.patch
# Originally from https://github.com/openssl/openssl/pull/18103
# As we rebased to 3.0.7 and used the version of the function
# not matching the upstream one, we have to use aliasing.
# When we eliminate this patch, the `-Wl,--allow-multiple-definition`
# should also be removed
Patch56: 0056-strcasecmp.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2053289
Patch58:  0058-FIPS-limit-rsa-encrypt.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2087147
Patch61:  0061-Deny-SHA-1-signature-verification-in-FIPS-provider.patch
# 0062-fips-Expose-a-FIPS-indicator.patch
Patch62:  0062-fips-Expose-a-FIPS-indicator.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2102535
Patch73:  0073-FIPS-Use-OAEP-in-KATs-support-fixed-OAEP-seed.patch
# 0074-FIPS-Use-digest_sign-digest_verify-in-self-test.patch
Patch74:  0074-FIPS-Use-digest_sign-digest_verify-in-self-test.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2102535
Patch75:  0075-FIPS-Use-FFDHE2048-in-self-test.patch
# Downstream only. Reseed DRBG using getrandom(GRND_RANDOM)
# https://bugzilla.redhat.com/show_bug.cgi?id=2102541
#Patch76:  0076-FIPS-140-3-DRBG.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2102542
Patch77:  0077-FIPS-140-3-zeroization.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2114772
Patch78:  0078-KDF-Add-FIPS-indicators.patch
# We believe that some changes present in CentOS are not necessary
# because ustream has a check for FIPS version
Patch80:  0080-rand-Forbid-truncated-hashes-SHA-3-in-FIPS-prov.patch
# 0081-signature-Remove-X9.31-padding-from-FIPS-prov.patch
Patch81:  0081-signature-Remove-X9.31-padding-from-FIPS-prov.patch
# 0083-hmac-Add-explicit-FIPS-indicator-for-key-length.patch
Patch83:  0083-hmac-Add-explicit-FIPS-indicator-for-key-length.patch
# 0084-pbkdf2-Set-minimum-password-length-of-8-bytes.patch
Patch84:  0084-pbkdf2-Set-minimum-password-length-of-8-bytes.patch
# 0085-FIPS-RSA-disable-shake.patch
Patch85:  0085-FIPS-RSA-disable-shake.patch
# 0088-signature-Add-indicator-for-PSS-salt-length.patch
Patch88:  0088-signature-Add-indicator-for-PSS-salt-length.patch
# 0091-FIPS-RSA-encapsulate.patch
Patch91:  0091-FIPS-RSA-encapsulate.patch
# 0093-DH-Disable-FIPS-186-4-type-parameters-in-FIPS-mode.patch
Patch93:  0093-DH-Disable-FIPS-186-4-type-parameters-in-FIPS-mode.patch
# 0110-GCM-Implement-explicit-FIPS-indicator-for-IV-gen.patch
Patch110: 0110-GCM-Implement-explicit-FIPS-indicator-for-IV-gen.patch
# 0112-pbdkf2-Set-indicator-if-pkcs5-param-disabled-checks.patch
Patch112: 0112-pbdkf2-Set-indicator-if-pkcs5-param-disabled-checks.patch
# 0113-asymciphers-kem-Add-explicit-FIPS-indicator.patch
Patch113: 0113-asymciphers-kem-Add-explicit-FIPS-indicator.patch
# We believe that some changes present in CentOS are not necessary
# because ustream has a check for FIPS version
Patch114: 0114-FIPS-enforce-EMS-support.patch
# Amend tests according to Fedora/RHEL code
Patch115: 0115-skip-quic-pairwise.patch
# Add version aliasing due to
# https://github.com/openssl/openssl/issues/23534
# Patch116: 0116-version-aliasing.patch
# https://github.com/openssl/openssl/issues/23050
Patch117: 0117-ignore-unknown-sigalgorithms-groups.patch
# 
# Patch120: 0120-Allow-disabling-of-SHA1-signatures.patch
# From CentOS 9
Patch121: 0121-FIPS-cms-defaults.patch
# [PATCH 50/50] Assign IANA numbers for hybrid PQ KEX Porting the fix
#  in https://github.com/openssl/openssl/pull/22803
Patch122: 0122-Assign-IANA-numbers-for-hybrid-PQ-KEX.patch
# https://github.com/openssl/openssl/issues/24577
Patch124: 0124-PBMAC1-PKCS12-FIPS-support.patch
# Downstream patch: enforce PBMAC1 in FIPS mode
Patch125: 0125-PBMAC1-PKCS12-FIPS-default.patch
# https://github.com/openssl/openssl/issues/25127
Patch126: 0126-pkeyutl-encap.patch
# https://github.com/openssl/openssl/issues/25056
Patch127: 0127-speedup-SSL_add_cert_subjects_to_stack.patch
Patch128: 0128-SAST-findings.patch

# MinGW patches
# Attempt to compute openssl modules dir dynamically from executable path if not set by OPENSSL_MODULES
Patch1000: openssl_compute_moddir.patch

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  make
BuildRequires:  lksctp-tools-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Html)
BuildRequires:  sed
BuildRequires:  /usr/bin/cmp
BuildRequires:  /usr/bin/rename
BuildRequires:  /usr/bin/pod2man

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-zlib

BuildRequires:  ucrt64-filesystem >= 95
BuildRequires:  ucrt64-dlfcn
BuildRequires:  ucrt64-binutils
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-zlib


%if %{run_tests}
# Required both to build, and to run the tests.
# XXX This needs to be fixed - cross-compilation should not
# require running executables.
BuildRequires:  wine

# Required to run the tests.
BuildRequires:  xorg-x11-server-Xvfb
%endif


%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.


# Win32
%package -n mingw32-openssl
Summary:        MinGW port of the OpenSSL toolkit
#Requires:       ca-certificates >= 2008-5
Requires:       pkgconfig

%description -n mingw32-openssl
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.

%package -n mingw32-openssl-static
Summary:        Static version of the MinGW port of the OpenSSL toolkit
Requires:       mingw32-openssl = %{version}-%{release}

%description -n mingw32-openssl-static
Static version of the MinGW port of the OpenSSL toolkit.

# Win64
%package -n mingw64-openssl
Summary:        MinGW port of the OpenSSL toolkit
#Requires:       ca-certificates >= 2008-5
Requires:       pkgconfig

%description -n mingw64-openssl
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.

%package -n mingw64-openssl-static
Summary:        Static version of the MinGW port of the OpenSSL toolkit
Requires:       mingw64-openssl = %{version}-%{release}

%description -n mingw64-openssl-static
Static version of the MinGW port of the OpenSSL toolkit.

# UCRT64
%package -n ucrt64-openssl
Summary:        MinGW port of the OpenSSL toolkit
#Requires:       ca-certificates >= 2008-5
Requires:       pkgconfig

%description -n ucrt64-openssl
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.

%package -n ucrt64-openssl-static
Summary:        Static version of the MinGW port of the OpenSSL toolkit
Requires:       ucrt64-openssl = %{version}-%{release}

%description -n ucrt64-openssl-static
Static version of the MinGW port of the OpenSSL toolkit.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n openssl-%{version}

cp %{SOURCE12} crypto/ec/
cp %{SOURCE13} test/


# Create two copies of the source folder as OpenSSL doesn't support out of source builds
mkdir ../build_win32
mv * ../build_win32
mv ../build_win32 .
mkdir build_win64
cp -Rp build_win32/* build_win64
mkdir build_ucrt64
cp -Rp build_win32/* build_ucrt64


%build
###############################################################################
# Win32
###############################################################################
pushd build_win32

PERL=%{__perl} \
CFLAGS="%{mingw32_cflags}" \
LDFLAGS="%{mingw32_ldflags}" \
./Configure \
  --prefix=%{mingw32_prefix} \
  --libdir=%{mingw32_libdir} \
  --openssldir=%{mingw32_sysconfdir}/pki/tls \
  zlib enable-camellia enable-seed enable-rfc3779 \
  enable-cms enable-md2 enable-rc5 enable-ktls enable-fips \
  no-mdc2 no-ec2m no-sm2 no-sm4 \
  --cross-compile-prefix=%{mingw32_target}- \
  shared mingw \
  -Dsecure_getenv=getenv

make -s %{?_smp_mflags} all

# Clean up the .pc files
for i in libcrypto.pc libssl.pc openssl.pc ; do
  sed -i '/^Libs.private:/{s/-L[^ ]* //;s/-Wl[^ ]* //}' $i
done

popd

###############################################################################
# Win64
###############################################################################
pushd build_win64

PERL=%{__perl} \
CFLAGS="%{mingw64_cflags}" \
LDFLAGS="%{mingw64_ldflags}" \
./Configure \
  --prefix=%{mingw64_prefix} \
  --libdir=%{mingw64_libdir} \
  --openssldir=%{mingw64_sysconfdir}/pki/tls \
  zlib enable-camellia enable-seed enable-rfc3779 \
  enable-cms enable-md2 enable-rc5 enable-ktls enable-fips \
  no-mdc2 no-ec2m no-sm2 no-sm4 \
  --cross-compile-prefix=%{mingw64_target}- \
  shared mingw64 \
  -Dsecure_getenv=getenv

# Do not run this in a production package the FIPS symbols must be patched-in
#util/mkdef.pl crypto update

make -s %{?_smp_mflags} all

# Clean up the .pc files
for i in libcrypto.pc libssl.pc openssl.pc ; do
  sed -i '/^Libs.private:/{s/-L[^ ]* //;s/-Wl[^ ]* //}' $i
done

popd

###############################################################################
# UCRT64
###############################################################################
pushd build_ucrt64

PERL=%{__perl} \
CFLAGS="%{ucrt64_cflags}" \
LDFLAGS="%{ucrt64_ldflags}" \
./Configure \
  --prefix=%{ucrt64_prefix} \
  --libdir=%{ucrt64_libdir} \
  --openssldir=%{ucrt64_sysconfdir}/pki/tls \
  zlib enable-camellia enable-seed enable-rfc3779 \
  enable-cms enable-md2 enable-rc5 enable-ktls enable-fips \
  no-mdc2 no-ec2m no-sm2 no-sm4 \
  --cross-compile-prefix=%{ucrt64_target}- \
  shared mingw64 \
  -Dsecure_getenv=getenv

# Do not run this in a production package the FIPS symbols must be patched-in
#util/mkdef.pl crypto update

make -s %{?_smp_mflags} all

# Clean up the .pc files
for i in libcrypto.pc libssl.pc openssl.pc ; do
  sed -i '/^Libs.private:/{s/-L[^ ]* //;s/-Wl[^ ]* //}' $i
done

popd


%if %{run_tests}
%check
#----------------------------------------------------------------------
# Run some tests.

# We must revert patch4 before tests otherwise they will fail
patch -p1 -R < %{PATCH4}

# This is a bit of a hack, but the test scripts look for 'openssl'
# by name.
pushd build_win32/apps
ln -s openssl.exe openssl
popd

# This is useful for diagnosing Wine problems.
WINEDEBUG=+loaddll
export WINEDEBUG

# Make sure we can find the installed DLLs.
WINEDLLPATH=%{mingw32_bindir}
export WINEDLLPATH

# The tests run Wine and require an X server (but don't really use
# it).  Therefore we create a virtual framebuffer for the duration of
# the tests.
# XXX There is no good way to choose a random, unused display.
# XXX Setting depth to 24 bits avoids bug 458219.
unset DISPLAY
display=:21
Xvfb $display -screen 0 1024x768x24 -ac -noreset & xpid=$!
trap "kill -TERM $xpid ||:" EXIT
sleep 3
DISPLAY=$display
export DISPLAY

make test

#----------------------------------------------------------------------
%endif

# Add generation of HMAC checksum of the final stripped library
##define __spec_install_post \
#    #{?__debug_package:#{__debug_install_post}} \
#    #{__arch_install_post} \
#    #{__os_install_post} \
#    fips/fips_standalone_sha1 %%{buildroot}/#{_lib}/libcrypto.so.#{version} >%%{buildroot}/#{_lib}/.libcrypto.so.#{version}.hmac \
#    ln -sf .libcrypto.so.#{version}.hmac %%{buildroot}/#{_lib}/.libcrypto.so.#{soversion}.hmac \
##{nil}


%install
mkdir -p %{buildroot}%{mingw32_libdir}/openssl
mkdir -p %{buildroot}%{mingw32_bindir}
mkdir -p %{buildroot}%{mingw32_includedir}
mkdir -p %{buildroot}%{mingw32_mandir}

mkdir -p %{buildroot}%{mingw64_libdir}/openssl
mkdir -p %{buildroot}%{mingw64_bindir}
mkdir -p %{buildroot}%{mingw64_includedir}
mkdir -p %{buildroot}%{mingw64_mandir}

mkdir -p %{buildroot}%{ucrt64_libdir}/openssl
mkdir -p %{buildroot}%{ucrt64_bindir}
mkdir -p %{buildroot}%{ucrt64_includedir}
mkdir -p %{buildroot}%{ucrt64_mandir}

%mingw_make_install DESTDIR=%{buildroot} install

# Install the file applink.c (#499934)
install -m644 build_win32/ms/applink.c %{buildroot}%{mingw32_includedir}/openssl/applink.c
install -m644 build_win64/ms/applink.c %{buildroot}%{mingw64_includedir}/openssl/applink.c
install -m644 build_ucrt64/ms/applink.c %{buildroot}%{ucrt64_includedir}/openssl/applink.c

# Remove the man pages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{ucrt64_mandir}

# Install a makefile for generating keys and self-signed certs, and a script
# for generating them on the fly.
mkdir -p %{buildroot}%{mingw32_sysconfdir}/pki/tls/certs
install -m644 %{SOURCE2} %{buildroot}%{mingw32_sysconfdir}/pki/tls/certs/Makefile
install -m755 %{SOURCE6} %{buildroot}%{mingw32_bindir}/make-dummy-cert
install -m755 %{SOURCE7} %{buildroot}%{mingw32_bindir}/renew-dummy-cert

mkdir -p %{buildroot}%{mingw64_sysconfdir}/pki/tls/certs
install -m644 %{SOURCE2} %{buildroot}%{mingw64_sysconfdir}/pki/tls/certs/Makefile
install -m755 %{SOURCE6} %{buildroot}%{mingw64_bindir}/make-dummy-cert
install -m755 %{SOURCE7} %{buildroot}%{mingw64_bindir}/renew-dummy-cert

mkdir -p %{buildroot}%{ucrt64_sysconfdir}/pki/tls/certs
install -m644 %{SOURCE2} %{buildroot}%{ucrt64_sysconfdir}/pki/tls/certs/Makefile
install -m755 %{SOURCE6} %{buildroot}%{ucrt64_bindir}/make-dummy-cert
install -m755 %{SOURCE7} %{buildroot}%{ucrt64_bindir}/renew-dummy-cert

mkdir -m700 %{buildroot}%{mingw32_sysconfdir}/pki/CA
mkdir -m700 %{buildroot}%{mingw32_sysconfdir}/pki/CA/private

mkdir -m700 %{buildroot}%{mingw64_sysconfdir}/pki/CA
mkdir -m700 %{buildroot}%{mingw64_sysconfdir}/pki/CA/private

mkdir -m700 %{buildroot}%{ucrt64_sysconfdir}/pki/CA
mkdir -m700 %{buildroot}%{ucrt64_sysconfdir}/pki/CA/private


# Win32
%files -n mingw32-openssl
%doc build_win32/LICENSE.txt
%{mingw32_bindir}/c_rehash
%{mingw32_bindir}/libcrypto-%{soversion}.dll
%{mingw32_bindir}/libssl-%{soversion}.dll
%{mingw32_bindir}/make-dummy-cert
%{mingw32_bindir}/openssl.exe
%{mingw32_bindir}/renew-dummy-cert
%{mingw32_libdir}/engines-%{soversion}
%{mingw32_libdir}/ossl-modules/
%{mingw32_libdir}/pkgconfig/*.pc
%{mingw32_libdir}/libcrypto.dll.a
%{mingw32_libdir}/libssl.dll.a
%{mingw32_includedir}/openssl/
%config(noreplace) %{mingw32_sysconfdir}/pki

%files -n mingw32-openssl-static
%{mingw32_libdir}/libcrypto.a
%{mingw32_libdir}/libssl.a

# Win64
%files -n mingw64-openssl
%doc build_win64/LICENSE.txt
%{mingw64_bindir}/c_rehash
%{mingw64_bindir}/libcrypto-%{soversion}-x64.dll
%{mingw64_bindir}/libssl-%{soversion}-x64.dll
%{mingw64_bindir}/make-dummy-cert
%{mingw64_bindir}/openssl.exe
%{mingw64_bindir}/renew-dummy-cert
%{mingw64_libdir}/engines-%{soversion}
%{mingw64_libdir}/ossl-modules/
%{mingw64_libdir}/pkgconfig/*.pc
%{mingw64_libdir}/libcrypto.dll.a
%{mingw64_libdir}/libssl.dll.a
%{mingw64_includedir}/openssl/
%config(noreplace) %{mingw64_sysconfdir}/pki

%files -n mingw64-openssl-static
%{mingw64_libdir}/libcrypto.a
%{mingw64_libdir}/libssl.a

# UCRT64
%files -n ucrt64-openssl
%doc build_win64/LICENSE.txt
%{ucrt64_bindir}/c_rehash
%{ucrt64_bindir}/libcrypto-%{soversion}-x64.dll
%{ucrt64_bindir}/libssl-%{soversion}-x64.dll
%{ucrt64_bindir}/make-dummy-cert
%{ucrt64_bindir}/openssl.exe
%{ucrt64_bindir}/renew-dummy-cert
%{ucrt64_libdir}/engines-%{soversion}
%{ucrt64_libdir}/ossl-modules/
%{ucrt64_libdir}/pkgconfig/*.pc
%{ucrt64_libdir}/libcrypto.dll.a
%{ucrt64_libdir}/libssl.dll.a
%{ucrt64_includedir}/openssl/
%config(noreplace) %{ucrt64_sysconfdir}/pki

%files -n ucrt64-openssl-static
%{ucrt64_libdir}/libcrypto.a
%{ucrt64_libdir}/libssl.a


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2.4-4
- Import
