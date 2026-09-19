%global source0_hash 57c1e4637039a9fd93218a78f7f6e893c7d69960c7e180c1b8c9d3ed949495ce
%global source1_hash ebd0a660969b934ec653a78a1c843df3f327d7ea866493c0dde58e18d92c4e40
%global source3_hash 453a4943a7a9a0037c6105d22548c943998f6902224294ad4d616c9eca638c34

# There's no concept of debuginfo for SGX enclaves
%global debug_package %{nil}

%global linux_sgx_version 2.25
%global dcap_version 1.22

# Provisioning Certification Enclave. Required. ECDSA quote signing
%global with_enclave_pce 1

# ID Enclave. Required. Hardware identification
%global with_enclave_ide 1

# Quoting Enclave. Required for non-TDX usage. ECDSA quote generation
%if 0%{?rhel}
%global with_enclave_qe3 0
%else
%global with_enclave_qe3 1
%endif

# Quoting Enclave. Required for TDX usage. ECDSA quote generation
%global with_enclave_tdqe 1

# Quote Verification Enclave. Optional. ECDSA quote verification
#
# Disabled as it is known to link to an openssl build that has
# crypto algorithms that haven't been approved by legal. Thus it
# is currently unknown if we can ship such code.
%global with_enclave_qve 0


Name:           linux-sgx-enclaves-prebuilt
Version:        %{linux_sgx_version}
Release:        %autorelease
Summary:        Intel SGX prebuilt architectural enclaves

# The project pulls together source from a wide variety of places,
# so while the license of the combined work is declared to be
# BSD-3-Clause, there is actually a huge set of licenses to track
#
# While this package contains pre-built signed enclaves, upstream
# has a reproducible build process to create unsigned enclaves.
# This license list is determined from analyzing that build
# which is equivalent to the pre-bult binaries, without a sig.
License: %{shrink:
  %dnl sdk/tlibcxx, external/ippcp_internal, external/epid-sdk
  Apache-2.0 AND

  %dnl sdk/cpprt, sdk/tlibc
  BSD-2-Clause AND

  %dnl external/dcap_source, sdk/*
  BSD-3-Clause AND

  %dnl sdk/tlibc
  BSD-4-Clause AND

  %dnl sdk/tlibc
  BSD-4-Clause-UC AND

  %dnl psd/urts/linux/isgx_user.h
  GPL-2.0-only AND

  %dnl sdk/tlibc, sdk/pthread
  ISC AND

  %dnl external/cbor/libcbor, sdk/*
  MIT AND

  %dnl sdk/tlibc/stdlib/malloc.c
  MIT-0 AND

  %dnl sdk/compiler-rt
  NCSA AND

  %dnl sdk/protected_code_loader
  OpenSSL AND

  %dnl sdk/tlibc/gdtoa
  SMLNJ AND

  %dnl sdk/tlibc/math
  SunPro AND

  %dnl sdk/tlibc
  LicenseRef-Fedora-Public-Domain
}

URL:            https://github.com/intel/confidential-computing.sgx

# The sources are needed so we can determine the ELF so version
# symlinks that the loader code will expect to find

Source0:        https://github.com/intel/confidential-computing.sgx/archive/refs/tags/sgx_%{linux_sgx_version}_reproducible.tar.gz#/linux-sgx-%{linux_sgx_version}-reproducible.tar.gz

Source1:        https://github.com/intel/confidential-computing.tee.dcap/archive/refs/tags/dcap_%{dcap_version}_reproducible.tar.gz#/linux-sgx-dcap-%{dcap_version}-reproducible.tar.gz

Source2:        repack.sh

Source3:        https://download.01.org/intel-sgx/sgx-dcap/%{dcap_version}/linux/prebuilt_dcap_%{dcap_version}.tar.gz

BuildRequires: sgx-rpm-macros

ExclusiveArch: x86_64

%description
The Intel SGX prebuilt architectural enclaves bootstrap the
SGX hardware for use by applications.

%package -n sgx-enclave-prebuilt-common
Summary: Intel SGX prebuilt architectural enclaves common

%description -n sgx-enclave-prebuilt-common
Common files for the Intel SGX prebuilt architectural enclaves

%global do_package() \
%if %2 \
%package -n sgx-enclave-prebuilt-%1-signed \
Summary: SGX %1 enclave (signed) \
\
Provides: sgx-enclave(%1:signed) = %3 \
Provides: sgx-enclave(%1:signed:prebuilt) = %3 \
Requires: sgx-enclave-prebuilt-common = %{version}-%{release} \
\
%description -n sgx-enclave-prebuilt-%1-signed \
This package contains the signed SGX %1 enclave, \
prebuilt by Intel. \
%endif

%do_package pce %{with_enclave_pce} %{linux_sgx_version}
%do_package ide %{with_enclave_ide} %{dcap_version}
%do_package qe3 %{with_enclave_qe3} %{dcap_version}
%do_package tdqe %{with_enclave_tdqe} %{dcap_version}
%do_package qve %{with_enclave_qve} %{dcap_version}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }

_repacked="$(pwd)/prebuilt_dcap_%{dcap_version}-repacked.tar.gz"
_strip="libcrypto.a policy.wasm"
%if ! %{with_enclave_pce}
_strip="$_strip libsgx_pce.signed.so"
%endif
%if ! %{with_enclave_ide}
_strip="$_strip libsgx_id_enclave.signed.so"
%endif
%if ! %{with_enclave_qe3}
_strip="$_strip libsgx_qe3.signed.so"
%endif
%if ! %{with_enclave_tdqe}
_strip="$_strip libsgx_tdqe.signed.so"
%endif
%if ! %{with_enclave_qve}
_strip="$_strip libsgx_qve.signed.so"
%endif
rm -rf _repack && mkdir _repack
(
  cd _repack
  tar zxf %{SOURCE3}
  for _f in $_strip; do
    find . -name "$_f" -delete -print
  done
  find . \( -name '*.h' -o -name '*.H' \) -delete -print
  tar zcf "$_repacked" *
)
rm -rf _repack

%autosetup -n confidential-computing.sgx-sgx_%{linux_sgx_version}_reproducible

(
  cd external/dcap_source
  tar zxf %{SOURCE1} --strip 1
)

(
  cd external/dcap_source/QuoteGeneration
  tar zxf "$_repacked"
)

%build
# No real 'build' logic
#
# The architectural enclaves are considered to be 'firmware'
# for SGX, and thus the firmware exception permits shipping
# them pre-built. This is required since Intel signatures
# are a pre-requisite for using the architectural enclaves
#
# Approved by FESCo in https://pagure.io/fesco/issue/3304

# Pull together all license files relevant to the code
# that is known to be built into the enclaves
mkdir licenses
for f in License.txt \
         external/epid-sdk/LICENSE.txt \
         external/epid-sdk/ext/argtable3/LICENSE \
         sdk/compiler-rt/LICENSE.TXT \
         sdk/cpprt/linux/libunwind/LICENSE \
         sdk/gperftools/gperftools-2.7/COPYING \
         sdk/tlibcxx/LICENSE.TXT \
         external/dcap_source/License.txt \
         external/dcap_source/QuoteGeneration/ThirdPartyLicenses.txt
do
  d=$(dirname $f)
  mkdir -p licenses/$d
  cp $f licenses/$f
done

%install

############################################################
# Install phase
#
# There's nothing useful like 'make install' to install
# everything in the right place :-(

%__install -d %{buildroot}%{sgx_libdir}

# This logic for figuring out symlink versions matches what
# upstream uses with their installation scripts:
#
#  https://github.com/intel/linux-sgx/blob/main/linux/installer/common/psw-dcap/Makefile

# @arg1: boolean condition for whether to ship this enclave
# @arg2: base name of the enclave
# @arg3: directory containing locally built enclave
# @arg4: directory containing pre-bult enclave
# @arg5: symbol name that defines the enclave SO version
%global do_install() \
%if %1 \
version="$(grep %5 $version_file | awk '{print $3}' | sed -e 's/"//g')" \
libname="libsgx_%2.signed.so" \
libnameso="$libname.$(echo $version | awk -F . '{print $1}')" \
libnamever="$libname.$version" \
%__install -m 0755 %4/$libname %{buildroot}%{sgx_libdir}/$libnamever \
ln -s $libnamever %{buildroot}%{sgx_libdir}/$libnameso \
ln -s $libnameso %{buildroot}%{sgx_libdir}/$libname \
%endif

version_file=common/inc/internal/se_version.h
%do_install %{with_enclave_pce} pce psw/ae/pce external/dcap_source/QuoteGeneration/psw/ae/data/prebuilt PCE_VERSION

version_file=external/dcap_source/QuoteGeneration/common/inc/internal/se_version.h
%do_install %{with_enclave_ide} id_enclave external/dcap_source/QuoteGeneration/quote_wrapper/quote/id_enclave/linux external/dcap_source/QuoteGeneration/psw/ae/data/prebuilt IDE_VERSION
%do_install %{with_enclave_qe3} qe3 external/dcap_source/QuoteGeneration/quote_wrapper/quote/enclave/linux external/dcap_source/QuoteGeneration/psw/ae/data/prebuilt QE3_VERSION
%do_install %{with_enclave_tdqe} tdqe external/dcap_source/QuoteGeneration/quote_wrapper/tdx_quote/enclave/linux external/dcap_source/QuoteGeneration/psw/ae/data/prebuilt TDQE_VERSION
%do_install %{with_enclave_qve} qve external/dcap_source/QuoteVerification/QvE external/dcap_source/QuoteGeneration/psw/ae/data/prebuilt QVE_VERSION


%files -n sgx-enclave-prebuilt-common
%license licenses/
%dir %{sgx_prefix}
%dir %{sgx_libdir}

%global do_files() \
%if %3 \
%files -n sgx-enclave-prebuilt-%1-signed \
%{sgx_libdir}/libsgx_%2.signed.so* \
%endif

%do_files pce pce %{with_enclave_pce}
%do_files ide id_enclave %{with_enclave_ide}
%do_files qe3 qe3 %{with_enclave_qe3}
%do_files tdqe tdqe %{with_enclave_tdqe}
%do_files qve qve %{with_enclave_qve}


%changelog
* Fri Apr 3 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{linux_sgx_version}-1
- Autosetup -n for GitHub archive after intel/linux-sgx repo rename

* Thu Apr 2 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{linux_sgx_version}-1
- Add prebuilt_dcap repacked tarball, escape macros in URL comment

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{linux_sgx_version}-1
- Prepare for Oreon 11 (RP1)
