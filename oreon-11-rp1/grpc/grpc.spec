# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 486d5e32b3627926476a9a472f9792e4d7fe4e89c962473f1296183f76c6b032
%global source100_hash 20f9b1f3e2119798aaffb04b17c8640b41224e5bb95e912517ac0db1bd26e4a9
%global source101_hash 820071ccb7ea42a9b0a5e12e2a7d44d8d677eec0c56b31b917ad8fc585c790f9
%global source102_hash 98b8833bfe2b9069c487b4c38c2ad266eb809e6d4e25852da0f1241d635c6ce5
%global source103_hash 30b24d38652728578478fd952fdac0a1c5d6a8aad28a34fba5a16b0303ff8cbb
%global source104_hash df8ba69eac1497fc8b69786d158a88dd88ad795b544c8e57a5ef7a58aef1346b
%global source105_hash e64124f22437736281b42d1726ea233144187d018d199391298d0db966661acd
%global source106_hash 5655fb5fc907b508b7b3f48c66a345172dc37b3338f437b2a2843d40d6291149
%global source107_hash 79928eae0f1d1c8a77ac48796801cc72af5fbb568d0d9764f00d9aee38c04371
%global source108_hash c889f20624141128b6332d5ce7acb9fceff3c7ad2ff87e40057435b58b89ed43
%global source2_hash cd8b49614408b43bd45d90e3e98d69e24eea632ff42ac3bfb8bca68bc31e377f
%global source3_hash 0513f0f40af63bd05dc789cacc334ab6cec27cc89db596557cb2dfe8919463e4
%global source4_hash b7e13f0b4259e80c3070b583c2f39e53153085a6918718b1c710caf7037572b0
%global source5_hash dc305e20c9fa80822322271b50aa2ffa917bf4fd3973bcec52bfc28dc32c5927
%global source6_hash e4718352754df1393b8792b631338aa8562f390e8160783e365454bc11d96328
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global cpp_std 17

%global envoy_api_commit 4de3c74cf21a9958c1cf26d8993c55c6e0d28b49
%global envoy_api_url https://github.com/envoyproxy/data-plane-api
%global envoy_api_dir data-plane-api-%{envoy_api_commit}

%global googleapis_commit fe8ba054ad4f7eca946c2d14a63c3f07c0b586a0
%global googleapis_url https://github.com/googleapis/googleapis
%global googleapis_dir googleapis-%{googleapis_commit}

%global opencensus_proto_version 0.3.0
%global opencensus_proto_url https://github.com/census-instrumentation/opencensus-proto
%global opencensus_proto_dir opencensus-proto-%{opencensus_proto_version}

%global xds_commit 3a472e524827f72d1ad621c4983dd5af54c46776
%global xds_url https://github.com/cncf/xds
%global xds_dir xds-%{xds_commit}

%global protoc_gen_validate_version 1.2.1
%global protoc_gen_validate_url https://github.com/envoyproxy/protoc-gen-validate
%global protoc_gen_validate_dir protoc-gen-validate-%{protoc_gen_validate_version}

%bcond core_tests          1

%bcond python_aio_tests    0

%ifnarch s390x
%bcond python_gevent_tests 0
%else
%bcond python_gevent_tests 0
%endif

%bcond valgrind            0
%bcond gdb                 0

Name:           grpc
Version:        1.75.1
Release:        %{autorelease}
Summary:        High performance, open source universal RPC framework

%global srcversion %{version}
%global pyversion %{version}

%global c_so_version 50
%global cpp_so_version 1.75

License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://www.grpc.io
%global forgeurl https://github.com/grpc/grpc
Source0:        %{forgeurl}/archive/v%{srcversion}/grpc-%{srcversion}.tar.gz
Source2:        %{envoy_api_url}/archive/%{envoy_api_commit}/%{envoy_api_dir}.tar.gz
Source3:        %{googleapis_url}/archive/%{googleapis_commit}/%{googleapis_dir}.tar.gz
Source4:        %{opencensus_proto_url}/archive/v%{opencensus_proto_version}/%{opencensus_proto_dir}.tar.gz
Source5:        %{xds_url}/archive/%{xds_commit}/%{xds_dir}.tar.gz
Source6:        %{protoc_gen_validate_url}/archive/v%{protoc_gen_validate_version}/%{protoc_gen_validate_dir}.tar.gz

Source100:      grpc_cli.1
Source101:      grpc_cli-ls.1
Source102:      grpc_cli-call.1
Source103:      grpc_cli-type.1
Source104:      grpc_cli-parse.1
Source105:      grpc_cli-totext.1
Source106:      grpc_cli-tojson.1
Source107:      grpc_cli-tobinary.1
Source108:      grpc_cli-help.1

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
%if %{with core_tests}
BuildRequires:  chrpath
%endif

BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  protobuf-compiler
BuildRequires:  pkgconfig(protobuf-lite)
BuildRequires:  cmake(utf8_range)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  cmake(c-ares)
BuildRequires:  abseil-cpp-devel
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libsystemd)

%if %{with core_tests}
BuildRequires:  cmake(benchmark)
BuildRequires:  cmake(gtest)
BuildRequires:  pkgconfig(gmock)
%if %{with valgrind}
BuildRequires:  valgrind
%endif
%if %{with gdb}
BuildRequires:  gdb
%endif
%endif

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)

BuildRequires: python3dist(cython) > 0.23

BuildRequires:  (python3dist(protobuf) >= 6.31.1 with python3dist(protobuf) < 7.0.0)

BuildRequires:  python3dist(googleapis-common-protos) >= 1.5.5

BuildRequires:  python3dist(oauth2client) >= 1.4.7

BuildRequires:  python3dist(google-auth) >= 1.17.2

BuildRequires:  python3dist(requests) >= 2.14.2

BuildRequires:  python3dist(twisted)
BuildRequires:  python3dist(service-identity)
BuildRequires:  python3dist(pyyaml)

%if %{with python_gevent_tests}
BuildRequires:  python3dist(gevent)
%endif

BuildRequires:  curl

%global _lto_cflags %{nil}

BuildRequires:  ca-certificates
BuildRequires:  symlinks
BuildRequires:  hardlink

Patch0:         grpc-1.74.1-Use-the-system-OpenSSL-profile.patch
Patch1:         grpc-1.40.0-python-grpcio_tests-make-network-tests-skippable.patch
Patch2:         grpc-1.60.0-python-grpcio_tests-skip-compression-tests.patch
Patch3:         grpc-1.60.0-ChannelzServicerTest-python3.11-regressions.patch
Patch4:         grpc-1.60.0-Skip-hanging-DynamicStubTest.patch

Patch5:         grpc-1.75.1-system-gtest.patch

Patch6:         grpc-1.75.1-use-system-upb.patch

Patch7:         grpc-1.74.1-use-shared-xxhash.patch

Patch8:         grpc-1.74.1-openssl-no-engine.patch

Patch9:         0001-Remove-usage-of-coverage.patch

Patch10:        grpc-1.74.1-httpcli_test-fix-path.patch

Patch11:        0001-Skip-installing-otel-plugin-pkgconfig-if-not-enabled.patch

Patch12:        grpc-1.75.1-spiffe_bundle_map_end2end_test-fix.patch

Patch13:        grpc-1.75.1-missing-includes.patch

Patch14:        0001-Update-OpenSSL-API-usage-for-compatibility.patch

Requires:       grpc-data = %{version}-%{release}

%global common_description %{expand:
gRPC is a modern, open source, high-performance remote procedure call (RPC)
framework that can run anywhere. gRPC enables client and server applications to
communicate transparently, and simplifies the building of connected systems.}

%description %{common_description}

This package provides the shared C core library.

%package data
Summary:        Data for gRPC bindings
License:        Apache-2.0
BuildArch:      noarch

Requires:       ca-certificates

%description data %{common_description}

This package provides common data for gRPC bindings: currently, this contains
only a symbolic link to the system shared TLS certificates.

%package doc
Summary:        Documentation and examples for gRPC
License:        Apache-2.0
BuildArch:      noarch

Obsoletes:      python-grpcio-doc < 1.26.0-13
Provides:       python-grpcio-doc = %{version}-%{release}
Provides:       python-grpcio-admin-doc = %{version}-%{release}
Provides:       python-grpcio-csds-doc = %{version}-%{release}
Provides:       python-grpcio-channelz-doc = %{version}-%{release}
Provides:       python-grpcio-health-checking-doc = %{version}-%{release}
Provides:       python-grpcio-reflection-doc = %{version}-%{release}
Provides:       python-grpcio-status-doc = %{version}-%{release}
Provides:       python-grpcio-testing-doc = %{version}-%{release}

%description doc %{common_description}

This package provides examples and documentation sources (but not rendered
documentation) for gRPC. For rendered HTML documentation, please see
https://grpc.io/docs/.

%package cpp
Summary:        C++ language bindings for gRPC

Requires:       grpc%{?_isa} = %{version}-%{release}
Requires:       grpc-cpp%{?_isa} = %{version}-%{release}

%description cpp %{common_description}

This package provides C++ language bindings for gRPC.

%package plugins
Summary:        Protocol buffers compiler plugins for gRPC

Requires:       grpc%{?_isa} = %{version}-%{release}
Requires:       grpc-cpp%{?_isa} = %{version}-%{release}
Requires:       protobuf-compiler

%description plugins %{common_description}

This package provides plugins to the protocol buffers compiler to generate gRPC
sources.

%package cli
Summary:        Command-line tool for gRPC

Requires:       grpc%{?_isa} = %{version}-%{release}
Requires:       grpc-cpp%{?_isa} = %{version}-%{release}

%description cli %{common_description}

The command line tool can do the following things:

  • Send unary rpc.
  • Attach metadata and display received metadata.
  • Handle common authentication to server.
  • Infer request/response types from server reflection result.
  • Find the request/response types from a given proto file.
  • Read proto request in text form.
  • Read request in wire form (for protobuf messages, this means serialized
    binary form).
  • Display proto response in text form.
  • Write response in wire form to a file.

%package devel
Summary:        Development files for gRPC library
Requires:       grpc%{?_isa} = %{version}-%{release}
Requires:       grpc-cpp%{?_isa} = %{version}-%{release}
Requires:       grpc-plugins%{?_isa} = %{version}-%{release}

Requires:       kernel-headers%{?_isa}
Requires:       pkgconfig(protobuf)
Requires:       pkgconfig(gmock)
Requires:       cmake(absl)
Requires:       pkgconfig(re2)
Requires:       cmake(c-ares)
Requires:       pkgconfig(zlib)
Requires:       pkgconfig(libsystemd)

%description devel %{common_description}

This package provides development headers and files for gRPC libraries (both C
and C++).

%package -n python3-grpcio
Summary:        Python language bindings for gRPC

Requires:       grpc-data = %{version}-%{release}

Obsoletes:      python3-grpcio-admin < 1.48.4-7
Obsoletes:      python3-grpcio-csds < 1.48.4-7

%py_provides python3-grpc

%description -n python3-grpcio %{common_description}

This package provides Python language bindings for gRPC (HTTP/2-based RPC
framework).

%global grpcio_egg %{python3_sitearch}/grpcio-%{pyversion}.dist-info
%{?python_extras_subpkg:%python_extras_subpkg -n python3-grpcio -i %{grpcio_egg} protobuf}

%package -n python3-grpcio-tools
Summary:       Package for gRPC Python tools

%py_provides python3-grpc-tools

%description -n python3-grpcio-tools %{common_description}

This package provides gRPC Python tools.

%package -n python3-grpcio-channelz
Summary:        Channel Level Live Debug Information Service for gRPC
License:        Apache-2.0

BuildArch:      noarch

%py_provides python3-grpc-channelz

%description -n python3-grpcio-channelz %{common_description}

Channelz is a live debug tool in gRPC Python.

%package -n python3-grpcio-health-checking
Summary:        Standard Health Checking Service for gRPC
License:        Apache-2.0

BuildArch:      noarch

%py_provides python3-grpc-health

%description -n python3-grpcio-health-checking %{common_description}

This is the reference package for gRPC Python health checking.

%package -n python3-grpcio-reflection
Summary:        Standard Protobuf Reflection Service for gRPC
License:        Apache-2.0

BuildArch:      noarch

%py_provides python3-grpc-reflection

%description -n python3-grpcio-reflection %{common_description}
This is the reference package for reflection in gRPC Python.

%package -n python3-grpcio-status
Summary:        Status proto mapping for gRPC
License:        Apache-2.0

BuildArch:      noarch

%py_provides python3-grpc-status

%description -n python3-grpcio-status %{common_description}

This is the reference package for gRPC Python status proto mapping.

%package -n python3-grpcio-testing
Summary:        Testing utilities for gRPC Python
License:        Apache-2.0

BuildArch:      noarch

%py_provides python3-grpc-testing

%description -n python3-grpcio-testing %{common_description}

This package provides testing utilities for gRPC Python.

%prep
%oreon_sha256
echo '%{source100_hash}  %{SOURCE100}' | sha256sum -c -
echo '%{source101_hash}  %{SOURCE101}' | sha256sum -c -
echo '%{source102_hash}  %{SOURCE102}' | sha256sum -c -
echo '%{source103_hash}  %{SOURCE103}' | sha256sum -c -
echo '%{source104_hash}  %{SOURCE104}' | sha256sum -c -
echo '%{source105_hash}  %{SOURCE105}' | sha256sum -c -
echo '%{source106_hash}  %{SOURCE106}' | sha256sum -c -
echo '%{source107_hash}  %{SOURCE107}' | sha256sum -c -
echo '%{source108_hash}  %{SOURCE108}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
echo '%{source5_hash}  %{SOURCE5}' | sha256sum -c -
echo '%{source6_hash}  %{SOURCE6}' | sha256sum -c -
%autosetup -p1 -n grpc-%{srcversion}

echo '===== Patching grpcio_tools for system protobuf/abseil-cpp =====' 2>&1
cat >> 'tools/distrib/python/grpcio_tools/protoc_lib_deps.py' <<'EOF'

del PROTOBUF_SUBMODULE_VERSION
PROTO_INCLUDE="%{_includedir}"

_unbundle_libs = {"abseil-cpp", "protobuf", "upb", "utf8_range"}
_unbundle_prefixes = {f"third_party/{lib}" for lib in _unbundle_libs}

def _ok_prefix(path):
    return not any(map(path.startswith, _unbundle_prefixes))

CC_FILES = list(filter(_ok_prefix, CC_FILES))
CC_INCLUDES = list(filter(_ok_prefix, CC_INCLUDES))
EOF

%setup -q -T -D -b 2 -n grpc-%{srcversion}
%setup -q -T -D -b 3 -n grpc-%{srcversion}
%setup -q -T -D -b 4 -n grpc-%{srcversion}
%setup -q -T -D -b 5 -n grpc-%{srcversion}
%setup -q -T -D -b 6 -n grpc-%{srcversion}
{
  awk '$1 ~ /^(#|$)/ { next }; 1' <<'EOF'
../%{envoy_api_dir}/ third_party/envoy-api/
../%{googleapis_dir}/ third_party/googleapis/
../%{opencensus_proto_dir}/ third_party/opencensus-proto/
../%{xds_dir}/ third_party/xds/
../%{protoc_gen_validate_dir}/ third_party/protoc-gen-validate/
EOF
} | while read -r fromdir todir
do
  find "${fromdir}" -type f ! -name '*.proto' -print -delete
  rm -rvf "${todir}"
  mv "${fromdir}" "${todir}"
done

echo '===== Removing bundled xxhash =====' 2>&1
rm -rvf third_party/xxhash

echo '===== Fixing permissions =====' 2>&1
find . -type f -perm /0111 \
    -exec gawk '!/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r chmod -v a-x

echo '===== Removing selected unused sources =====' 2>&1
rm -rfv \
    src/boringssl/boringssl_prefix_symbols.h \
    third_party/cares/ares_build.h \
    third_party/upb third_party/utf8_range
echo '' > etc/roots.pem

rm -rvf examples/android src/android

rm -vf examples/node/package-lock.json

find . -type f -name .gitignore -print -delete

echo '===== Fixing shebangs =====' 2>&1
find . -type f -perm /0111 -exec gawk \
    '/^#!\/usr\/bin\/env[[:blank:]]/ { print FILENAME }; { nextfile }' \
    '{}' '+' |
  xargs -r sed -r -i '1{s|^(#!/usr/bin/)env[[:blank:]]+([^[:blank:]]+)|\1\2|}'

echo '===== Fixing hard-coded C++ standard =====' 2>&1
sed -r -i 's/(std=c\+\+)17/\1%{cpp_std}/g' \
    setup.py Rakefile \
    examples/cpp/*/Makefile \
    examples/cpp/*/CMakeLists.txt \
    tools/run_tests/artifacts/artifact_targets.py \
    tools/distrib/python/grpcio_tools/setup.py

echo '===== Adding any neccessary Python test skips =====' 2>&1
from='^([[:blank:]]+)(def testTestsJsonUpToDate\()'
skip='@unittest.skip("JSON representations differ; cause not ascertained")'
sed -r -i "s/${from}/\\1${skip}\\n\\1\\2/" \
    src/python/grpcio_tests/tests/_sanity/_sanity_test.py
rm src/python/grpcio_tests/tests_py3_only/unit/_leak_test.py
%ifarch aarch64 s390x x86_64
rm src/python/grpcio_tests/tests_py3_only/unit/_simple_stubs_test.py
%endif

%build

%global rmprefix %(echo $(($(wc -c <<<'%{_prefix}')+1)))

echo '===== Building C (core) and C++ components =====' 2>&1
%cmake \
    -DgRPC_INSTALL:BOOL=ON \
    -DCMAKE_CXX_STANDARD:STRING=%{cpp_std} \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DgRPC_INSTALL_BINDIR:PATH=%(cut -b %{rmprefix}- <<<'%{_bindir}') \
    -DgRPC_INSTALL_LIBDIR:PATH=%(cut -b %{rmprefix}- <<<'%{_libdir}') \
    -DgRPC_INSTALL_INCLUDEDIR:PATH=%(cut -b %{rmprefix}- <<<'%{_includedir}') \
    -DgRPC_INSTALL_CMAKEDIR:PATH=%(cut -b %{rmprefix}- <<<'%{_libdir}/cmake/grpc') \
    -DgRPC_INSTALL_SHAREDIR:PATH=%(cut -b %{rmprefix}- <<<'%{_datadir}/grpc') \
    -DgRPC_BUILD_TESTS:BOOL=%{?with_core_tests:ON}%{?!with_core_tests:OFF} \
    -DgRPC_BUILD_CODEGEN:BOOL=ON \
    -DgRPC_BUILD_CSHARP_EXT:BOOL=ON \
    -DgRPC_BACKWARDS_COMPATIBILITY_MODE:BOOL=OFF \
    -DgRPC_ZLIB_PROVIDER:STRING='package' \
    -DgRPC_CARES_PROVIDER:STRING='package' \
    -DgRPC_RE2_PROVIDER:STRING='package' \
    -DgRPC_SSL_PROVIDER:STRING='package' \
    -DgRPC_PROTOBUF_PROVIDER:STRING='package' \
    -DgRPC_BENCHMARK_PROVIDER:STRING='package' \
    -DgRPC_ABSL_PROVIDER:STRING='package' \
    -DgRPC_GTEST_PROVIDER:STRING='package' \
    -DgRPC_USE_PROTO_LITE:BOOL=OFF \
    -DgRPC_USE_SYSTEMD:BOOL=ON \
    -DgRPC_BUILD_GRPC_CPP_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_CSHARP_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_NODE_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_OBJECTIVE_C_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_PHP_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_PYTHON_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_RUBY_PLUGIN:BOOL=ON \
    -DgRPC_DOWNLOAD_ARCHIVES:BOOL=OFF \
    -GNinja
%cmake_build

echo '===== Building Python grpcio package =====' 2>&1
PYROOT="${PWD}/%{_vpath_builddir}/pyroot"
if [ -n "${PYTHONPATH-}" ]; then PYTHONPATH="${PYTHONPATH}:"; fi
PYTHONPATH="${PYTHONPATH-}${PYROOT}%{python3_sitelib}"
PYTHONPATH="${PYTHONPATH}:${PYROOT}%{python3_sitearch}"
export PYTHONPATH

export GRPC_PYTHON_BUILD_WITH_CYTHON='True'
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL='True'
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB='True'
export GRPC_PYTHON_BUILD_SYSTEM_CARES='True'
export GRPC_PYTHON_BUILD_SYSTEM_RE2='True'
export GRPC_PYTHON_BUILD_SYSTEM_ABSL='True'
export GRPC_PYTHON_BUILD_SYSTEM_UPB='True'
export GRPC_PYTHON_BUILD_SYSTEM_UTF8_RANGE='True'
export GRPC_PYTHON_BUILD_SYSTEM_XXHASH='True'
export GRPC_PYTHON_DISABLE_LIBC_COMPATIBILITY='True'
export GRPC_PYTHON_ENABLE_DOCUMENTATION_BUILD='False'
export GRPC_PYTHON_CFLAGS="$(
  pkg-config --cflags protobuf
) -std=c++%{cpp_std} -fvisibility=hidden -fno-wrapv -fno-exceptions"
export GRPC_PYTHON_LDFLAGS="$(pkg-config --libs protobuf)"
%pyproject_wheel
%{__python3} %{py_setup} %{?py_setup_args} install \
    -O1 --skip-build --root "${PYROOT}" --prefix %{_prefix}

echo '===== Building Python grpcio_tools package =====' 2>&1
pushd "tools/distrib/python/grpcio_tools/" >/dev/null
mkdir -p grpc_root/src
for srcdir in compiler
do
  cp -rp "../../../../src/${srcdir}" "grpc_root/src/"
done
cp -rp '../../../../include' 'grpc_root/'
export GRPC_PYTHON_CFLAGS="-fno-wrapv -frtti $(pkg-config --cflags protobuf)"
export GRPC_PYTHON_LDFLAGS="$(pkg-config --libs protobuf) -lprotoc"
%pyproject_wheel
find . -type f -name protoc.py -execdir sed -r -i '1{/^#!/d}' '{}' '+'
%{__python3} %{py_setup} %{?py_setup_args} install \
    -O1 --skip-build --root "${PYROOT}" --prefix %{_prefix}
popd >/dev/null

echo '===== Building Python xds_protos package =====' 2>&1
pushd "tools/distrib/python/xds_protos" >/dev/null
%pyproject_wheel
%{__python3} %{py_setup} %{?py_setup_args} install \
      -O1 --skip-build --root "${PYROOT}" --prefix %{_prefix}
popd >/dev/null

echo '===== Building pure-Python packages =====' 1>&2
for suffix in channelz health_checking reflection status testing tests
do
  echo "----> grpcio_${suffix} <----" 1>&2
  pushd "src/python/grpcio_${suffix}/" >/dev/null
  if ! echo "${suffix}" | grep -E "^(admin|csds)$" >/dev/null
  then
    %{__python3} %{py_setup} %{?py_setup_args} preprocess
  fi
  if ! echo "${suffix}" | grep -E "^(admin|csds|testing)$" >/dev/null
  then
    %{__python3} %{py_setup} %{?py_setup_args} build_package_protos
  fi
  %pyproject_wheel
  %{__python3} %{py_setup} %{?py_setup_args} install \
      -O1 --skip-build --root "${PYROOT}" --prefix %{_prefix}
  popd >/dev/null
done

%install
%cmake_install

%if %{with core_tests}
install -t '%{buildroot}%{_bindir}' -p -D '%{_vpath_builddir}/grpc_cli'
chrpath --delete '%{buildroot}%{_bindir}/grpc_cli'

install -t '%{buildroot}%{_libdir}' -p \
    '%{_vpath_builddir}/libgrpc++_test_config.so.%{cpp_so_version}'
chrpath --delete \
    '%{buildroot}%{_libdir}/libgrpc++_test_config.so.%{cpp_so_version}'

install -d '%{buildroot}/%{_mandir}/man1'
install -t '%{buildroot}/%{_mandir}/man1' -p -m 0644 \
    %{SOURCE100} %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} \
    %{SOURCE106} %{SOURCE107} %{SOURCE108}
%endif

find %{buildroot} -type f -name '*.a' -print -delete
find %{buildroot}%{_includedir}/grpc* -type f -name '*.h' -perm /0111 \
    -execdir chmod -v a-x '{}' '+'

pushd '%{buildroot}'
PYROOT="${PWD}"
popd
if [ -n "${PYTHONPATH-}" ]; then PYTHONPATH="${PYTHONPATH}:"; fi
PYTHONPATH="${PYTHONPATH-}${PYROOT}%{python3_sitelib}"
PYTHONPATH="${PYTHONPATH}:${PYROOT}%{python3_sitearch}"
export PYTHONPATH

rm -rvf %{_pyproject_wheeldir}/grpcio_tests-*.whl
rm -rvf %{_pyproject_wheeldir}/xds_protos-*.whl

%pyproject_install

%global sysbundle /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
install -D -t "%{buildroot}$(dirname '%{sysbundle}')" -m 0644 '%{sysbundle}'

find '%{buildroot}' -type f -name 'roots.pem' |
  while read -r fn
  do
    ln -s -f "%{buildroot}%{sysbundle}" "${fn}"
    symlinks -c -o "${fn}"
  done

rm -rvf "%{buildroot}$(dirname '%{sysbundle}')"

install -D -t '%{buildroot}%{_pkgdocdir}' -m 0644 -p \
    AUTHORS \
    CONCEPTS.md \
    MAINTAINERS.md \
    README.md \
    SECURITY.md \
    TROUBLESHOOTING.md
cp -rvp doc examples '%{buildroot}%{_pkgdocdir}'
hardlink -v '%{buildroot}%{_pkgdocdir}/examples/'

%check
%ifarch %{ix86} s390x

cat <<'EOF'
Tests are skipped on these secondary arches:

- i686: not a leaf package so we still build it, but skip tests to avoid
  tracking 32-bit-specific issues (see the F37 ARMv7-retirement and
  i686-leaf-removal changes).
  https://fedoraproject.org/wiki/Changes/RetireARMv7
  https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval

- s390x (big-endian): grpc has open upstream big-endian bugs that fail %check,
  e.g. address_sorting (grpc/grpc#35350), ALTS (grpc/grpc#43067), and
  buffer_list (atomic reads back 1<<32). The 1.75.x suite hits enough of these
  that per-test exclusion is unmaintainable, so skip %check on s390x. Big-endian
  support is tracked upstream (grpc#35350) and with the Fedora s390x WG.
EOF

%else

export FEDORA_NO_NETWORK_TESTS=1

%if %{with core_tests}
PORT_SERVER_PORT="$(awk '
  /_PORT_SERVER_PORT[[:blank:]]*=[[:blank:]]*[[:digit:]]+$/ { print $NF }
' tools/run_tests/python_utils/start_port_server.py)"

%ctest

{ sed -r -e '/^(#|$)/d' -e 's|^(.*)$|%{_vpath_builddir}/\1_test|' <<'EOF'

resolve_address_using_ares_resolver
resolve_address_using_ares_resolver_posix
resolve_address_using_native_resolver
resolve_address_using_native_resolver_posix
ssl_transport_security

flaky_network

%ifarch ppc64le
channel_init
%endif

%if 0%{?fedora} <= 42
examine_stack
stack_tracer
%endif

filter_test

grpc_tool

thread_pool

xds_security_end2end

party_mpsc

spiffe_bundle_map_end2end
spiffe_ssl_transport_security
xds_security_spiffe_end2end

EOF
} | xargs -r chmod -v a-x

trap '' PIPE

find %{_vpath_builddir} -type f -perm /0111 -name '*_test' | sort |
  while read -r testexe
  do
    echo "==== $(date -u --iso-8601=ns): $(basename "${testexe}") ===="
    %{__python3} tools/run_tests/start_port_server.py

%if %{without gdb}
    timeout -k 61m -v 60m \
%if %{with valgrind}
        valgrind --trace-children=yes --leak-check=full --track-origins=yes \
%endif
        "${testexe}"
%else
    tee "${testexe}-script.gdb" <<EOF
set pagination off
set logging file ${testexe}-gdb.log
set logging on
file ${testexe}
run
bt -full
set logging off
quit
EOF
    gdb -q -x "${testexe}-script.gdb" --batch </dev/null || :
%endif
  done

curl "http://localhost:${PORT_SERVER_PORT}/quitquitquit" || :
%endif

pushd src/python/grpcio_tests
for suite in \
    %{?with_python_aio_tests:test_aio} \
    %{?with_python_gevent_tests:test_gevent} \
    test_py3_only
do
  echo "==== $(date -u --iso-8601=ns): Python ${suite} ===="
  %{py3_test_envvars} timeout -k 31m -v 30m \
      %{python3} %{py_setup} %{?py_setup_args} "${suite}"
done
popd

%endif

%if %{without system_gtest}
foundgtest=0
if find %{buildroot} -type f -perm /0111 \
      -execdir objdump --syms --dynamic-syms --demangle '{}' '+' 2>/dev/null |
    grep -E '[^:]testing::'
then
  echo 'Found traces of gtest/gmock' 1>&2
  exit 1
fi
%endif

%files
%license LICENSE NOTICE.txt
%{_libdir}/libaddress_sorting.so.%{c_so_version}{,.*}
%{_libdir}/libgpr.so.%{c_so_version}{,.*}
%{_libdir}/libgrpc.so.%{c_so_version}{,.*}
%{_libdir}/libgrpc_unsecure.so.%{c_so_version}{,.*}

%files data
%license LICENSE NOTICE.txt
%dir %{_datadir}/grpc/
%{_datadir}/grpc/roots.pem

%files doc
%license LICENSE NOTICE.txt

%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/CONCEPTS.md
%doc %{_pkgdocdir}/MAINTAINERS.md
%doc %{_pkgdocdir}/README.md
%doc %{_pkgdocdir}/SECURITY.md
%doc %{_pkgdocdir}/TROUBLESHOOTING.md

%doc %{_pkgdocdir}/doc/
%doc %{_pkgdocdir}/examples/

%files cpp
%{_libdir}/libgrpc++.so.%{cpp_so_version}{,.*}
%{_libdir}/libgrpc++_alts.so.%{cpp_so_version}{,.*}
%{_libdir}/libgrpc++_error_details.so.%{cpp_so_version}{,.*}
%{_libdir}/libgrpc++_reflection.so.%{cpp_so_version}{,.*}
%{_libdir}/libgrpc++_unsecure.so.%{cpp_so_version}{,.*}
%{_libdir}/libgrpc_authorization_provider.so.%{cpp_so_version}{,.*}
%{_libdir}/libgrpc_plugin_support.so.%{cpp_so_version}{,.*}

%{_libdir}/libgrpcpp_channelz.so.%{cpp_so_version}{,.*}

%if %{with core_tests}
%files cli
%{_bindir}/grpc_cli
%{_libdir}/libgrpc++_test_config.so.%{cpp_so_version}
%{_mandir}/man1/grpc_cli.1*
%{_mandir}/man1/grpc_cli-*.1*
%endif

%files plugins
%{_bindir}/grpc_*_plugin

%files devel
%{_libdir}/libaddress_sorting.so
%{_libdir}/libgpr.so
%{_libdir}/libgrpc.so
%{_libdir}/libgrpc_authorization_provider.so
%{_libdir}/libgrpc_unsecure.so

%{_includedir}/grpc/
%{_libdir}/pkgconfig/gpr.pc
%{_libdir}/pkgconfig/grpc.pc
%{_libdir}/pkgconfig/grpc_unsecure.pc
%{_libdir}/cmake/grpc/

%{_libdir}/libgrpc++.so
%{_libdir}/libgrpc++_alts.so
%{_libdir}/libgrpc++_error_details.so
%{_libdir}/libgrpc++_reflection.so
%{_libdir}/libgrpc++_unsecure.so
%{_libdir}/libgrpc_plugin_support.so
%{_includedir}/grpc++/
%{_libdir}/pkgconfig/grpc++.pc
%{_libdir}/pkgconfig/grpc++_unsecure.pc

%{_libdir}/libgrpcpp_channelz.so
%{_includedir}/grpcpp/

%files -n python3-grpcio
%{python3_sitearch}/grpc/
%{python3_sitearch}/grpcio-%{pyversion}.dist-info/
%license LICENSE NOTICE.txt

%files -n python3-grpcio-tools
%{_bindir}/python-grpc-tools-protoc
%{python3_sitearch}/grpc_tools/
%{python3_sitearch}/grpcio_tools-%{pyversion}.dist-info/
%license LICENSE NOTICE.txt

%files -n python3-grpcio-channelz
%{python3_sitelib}/grpc_channelz/
%{python3_sitelib}/grpcio_channelz-%{pyversion}.dist-info/

%files -n python3-grpcio-health-checking
%{python3_sitelib}/grpc_health/
%{python3_sitelib}/grpcio_health_checking-%{pyversion}.dist-info/

%files -n python3-grpcio-reflection
%{python3_sitelib}/grpc_reflection/
%{python3_sitelib}/grpcio_reflection-%{pyversion}.dist-info/

%files -n python3-grpcio-status
%{python3_sitelib}/grpc_status/
%{python3_sitelib}/grpcio_status-%{pyversion}.dist-info/

%files -n python3-grpcio-testing
%{python3_sitelib}/grpc_testing/
%{python3_sitelib}/grpcio_testing-%{pyversion}.dist-info/

%changelog
%autochangelog
