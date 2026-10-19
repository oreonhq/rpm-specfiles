%global source0_hash 17a4d25717f4871eb71cfdf191f7491f66a59c8ebc782ab53d52fcbfc478959f
%global cpp_std 17
%global gtest_url https://github.com/google/googletest
%global gtest_dir googletest-%{gtest_commit}
%global gtest_commit 0e402173c97aea7a00749e825b194bfede4f2e45
%bcond system_gtest        0
%global envoy_api_commit 9c42588c956220b48eb3099d186487c2f04d32ec
%global envoy_api_url https://github.com/envoyproxy/data-plane-api
%global envoy_api_dir data-plane-api-%{envoy_api_commit}
%global googleapis_commit 2f9af297c84c55c8b871ba4495e01ade42476c92
%global googleapis_url https://github.com/googleapis/googleapis
%global googleapis_dir googleapis-%{googleapis_commit}
%global opencensus_proto_version 0.3.0
%global opencensus_proto_url https://github.com/census-instrumentation/opencensus-proto
%global opencensus_proto_dir opencensus-proto-%{opencensus_proto_version}
%global xds_commit cb28da3451f158a947dfc45090fe92b07b243bc1
%global xds_url https://github.com/cncf/xds
%global xds_dir xds-%{xds_commit}
%bcond core_tests          1
%bcond python_aio_tests    0
%bcond google_auth_tests   0
%ifnarch s390x
%bcond python_gevent_tests 0
%else
%bcond python_gevent_tests 0
%endif
%bcond valgrind            0
%bcond gdb                 0
Name:           grpc
Version:        1.84.0
Release:        1%{?dist}
Summary:        RPC library and framework
%global srcversion %(echo '%{version}' | sed -r 's/~rc/-pre/')
%global pyversion %(echo '%{version}' | tr -d '~')
%global c_so_version 26
%global cpp_so_version 1.84
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://www.grpc.io
%global forgeurl https://github.com/grpc/grpc/
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{gtest_url}/archive/%{gtest_commit}/%{gtest_dir}.tar.gz
Source2:        %{envoy_api_url}/archive/%{envoy_api_commit}/%{envoy_api_dir}.tar.gz
Source3:        %{googleapis_url}/archive/%{googleapis_commit}/%{googleapis_dir}.tar.gz
Source4:        %{opencensus_proto_url}/archive/v%{opencensus_proto_version}/%{opencensus_proto_dir}.tar.gz
Source5:        %{xds_url}/archive/%{xds_commit}/%{xds_dir}.tar.gz
Source100:      grpc_cli.1
Source101:      grpc_cli-ls.1
Source102:      grpc_cli-call.1
Source103:      grpc_cli-type.1
Source104:      grpc_cli-parse.1
Source105:      grpc_cli-totext.1
Source106:      grpc_cli-tojson.1
Source107:      grpc_cli-tobinary.1
Source108:      grpc_cli-help.1
Patch1000:      grpc-spinlock-test-bound.patch
%if %{with core_tests}
%endif
%if %{with core_tests}
%if %{with system_gtest}
%endif
%if %{with valgrind}
%endif
%if %{with gdb}
%endif
%endif
%if %{with google_auth_tests}
%endif
%if %{with google_auth_tests}
%endif
%if %{with python_gevent_tests}
%endif
%global _lto_cflags %{nil}
Patch:          grpc-1.39.0-system-crypto-policies.patch
Patch:          grpc-1.36.4-python-grpcio_tests-fixture-super.patch
Patch:          grpc-1.40.0-python-grpcio_tests-make-network-tests-skippable.patch
Patch:          grpc-1.48.0-python-grpcio_tests-skip-compression-tests.patch
Patch:          grpc-1.45.0-python_wrapper-path.patch
Patch:          grpc-1.48.0-python-grpcio_tests-DynamicStubTest-hang.patch
Patch:          0001-Remove-usage-of-coverage.patch
Patch:		grpc-1.48.4-core-tsi-ssl_transport_security.cc.patch
Patch:          grpc-python-parallel-absolute-paths.patch
Patch:          grpc-1.48.4-fast-test-compilation.patch
Requires:       grpc-data = %{version}-%{release}
Provides:       bundled(upb)
Provides:       bundled(utf8_range)
# oreon:deps
BuildRequires:  abseil-cpp-devel
BuildRequires:  ca-certificates
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  cmake(benchmark)
BuildRequires:  cmake(c-ares)
BuildRequires:  cmake(gflags)
BuildRequires:  curl
BuildRequires:  gcc-c++
BuildRequires:  hardlink
BuildRequires:  libpfm-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pkg-resources
BuildRequires:  python3-protobuf
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(oauth2client)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  symlinks
BuildRequires:  xxhash-static
# /oreon:deps
%description
gRPC is a modern open source high performance RPC framework that can run in any
environment. It can efficiently connect services in and across data centers
with pluggable support for load balancing, tracing, health checking and
authentication. It is also applicable in last mile of distributed computing to
connect devices, mobile applications and browsers to backend services.

The main usage scenarios:

  • Efficiently connecting polyglot services in microservices style
    architecture
  • Connecting mobile devices, browser clients to backend services
  • Generating efficient client libraries

Core Features that make it awesome:

  • Idiomatic client libraries in 10 languages
  • Highly efficient on wire and with a simple service definition framework
  • Bi-directional streaming with http/2 based transport
  • Pluggable auth, tracing, load balancing and health checking

This package provides the shared C core library.

%package data
Summary:        Data for gRPC bindings
License:        Apache-2.0
BuildArch:      noarch
Requires:       ca-certificates
%description data
Common data for gRPC bindings: currently, this contains only a symbolic link to
the system shared TLS certificates.

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
%description doc
Documentation and examples for gRPC, including Markdown documentation sources
for the following:

  • C (core)
    ○ API
    ○ Internals
  • C++
    ○ API
    ○ Internals
  • Objective C
    ○ API
    ○ Internals
  • Python
    ○ grpcio
    ○ grpcio_admin
    ○ grpcio_csds
    ○ grpcio_channelz
    ○ grpcio_health_checking
    ○ grpcio_reflection
    ○ grpcio_status
    ○ grpcio_testing

For rendered HTML documentation, please see https://grpc.io/docs/.

%package cpp
Summary:        C++ language bindings for gRPC
Requires:       grpc%{?_isa} = %{version}-%{release}
Requires:       grpc-cpp%{?_isa} = %{version}-%{release}
Provides:       bundled(upb)
Provides:       bundled(utf8_range)
%description cpp
C++ language bindings for gRPC.

%package plugins
Summary:        Protocol buffers compiler plugins for gRPC
Requires:       grpc%{?_isa} = %{version}-%{release}
Requires:       grpc-cpp%{?_isa} = %{version}-%{release}
Requires:       protobuf-compiler < 4
Provides:       bundled(upb)
Provides:       bundled(utf8_range)
%description plugins
Plugins to the protocol buffers compiler to generate gRPC sources.

%package cli
Summary:        Command-line tool for gRPC
Requires:       grpc%{?_isa} = %{version}-%{release}
Requires:       grpc-cpp%{?_isa} = %{version}-%{release}
Provides:       bundled(upb)
Provides:       bundled(utf8_range)
%description cli
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
Requires:       abseil-cpp-devel%{?_isa}
Requires:       pkgconfig(re2)
Requires:       cmake(c-ares)
Requires:       pkgconfig(zlib)
%description devel
Development headers and files for gRPC libraries (both C and C++).

%package -n python3-grpcio
Summary:        Python language bindings for gRPC
Requires:       grpc-data = %{version}-%{release}
Provides:       bundled(upb)
Provides:       bundled(utf8_range)
Obsoletes:      python3-grpcio-admin < 1.84.0-7
Obsoletes:      python3-grpcio-csds < 1.84.0-7
%py_provides python3-grpc
%description -n python3-grpcio
Python language bindings for gRPC (HTTP/2-based RPC framework).

%global grpcio_egg %{python3_sitearch}/grpcio-%{pyversion}-py%{python3_version}.egg-info
%{?python_extras_subpkg:%python_extras_subpkg -n python3-grpcio -i %{grpcio_egg} protobuf}

%package -n python3-grpcio-tools
Summary:       Package for gRPC Python tools
Requires:      python3-pkg-resources
Provides:       bundled(upb)
Provides:       bundled(utf8_range)
%py_provides python3-grpc-tools
%description -n python3-grpcio-tools
Package for gRPC Python tools.

%package -n python3-grpcio-channelz
Summary:        Channel Level Live Debug Information Service for gRPC
License:        Apache-2.0
BuildArch:      noarch
%py_provides python3-grpc-channelz
%description -n python3-grpcio-channelz
gRPC Python Channelz package
============================

Channelz is a live debug tool in gRPC Python.

%package -n python3-grpcio-health-checking
Summary:        Standard Health Checking Service for gRPC
License:        Apache-2.0
BuildArch:      noarch
%py_provides python3-grpc-health
%description -n python3-grpcio-health-checking
gRPC Python Health Checking
===========================

Reference package for GRPC Python health checking.

%package -n python3-grpcio-reflection
Summary:        Standard Protobuf Reflection Service for gRPC
License:        Apache-2.0
BuildArch:      noarch
%py_provides python3-grpc-reflection
%description -n python3-grpcio-reflection
gRPC Python Reflection package
==============================

Reference package for reflection in GRPC Python.

%package -n python3-grpcio-status
Summary:        Status proto mapping for gRPC
License:        Apache-2.0
BuildArch:      noarch
%py_provides python3-grpc-status
%description -n python3-grpcio-status
gRPC Python Status Proto
===========================

Reference package for GRPC Python status proto mapping.

%package -n python3-grpcio-testing
Summary:        Testing utilities for gRPC Python
License:        Apache-2.0
BuildArch:      noarch
%py_provides python3-grpc-testing
%description -n python3-grpcio-testing
gRPC Python Testing Package
===========================

Testing utilities for gRPC Python.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n grpc-%{srcversion}

cp -p third_party/utf8_range/LICENSE LICENSE-utf8_range

echo '===== Patching grpcio_tools for system protobuf =====' 2>&1
# Build python3-grpcio_tools against system protobuf packages instead of
# expecting a git submodule. Must also add requisite linker flags using
# GRPC_PYTHON_LDFLAGS. This was formerly done by
# grpc-VERSION-python-grpcio_tools-use-system-protobuf.patch, but it had to be
# tediously but trivially rebased every patch release as the CC_FILES list
# changed, so we automated the patch.
sed -r -i \
    -e "s/^(# AUTO-GENERATED .*)/\\1\\n\
# Then, modified by hand to build with an external system protobuf\
# installation./" \
    -e 's/^(CC_FILES=\[).*(\])/\1\2/' \
    -e "s@^((CC|PROTO)_INCLUDE=')[^']+'@\1%{_includedir}'@" \
    -e '/^PROTOBUF_SUBMODULE_VERSION=/d' \
    'tools/distrib/python/grpcio_tools/protoc_lib_deps.py'

echo '===== Preparing gtest/gmock =====' 2>&1
%if %{without system_gtest}
# Copy in the needed gtest/gmock implementations.
%setup -q -T -D -b 1 -n grpc-%{srcversion}
rm -rvf 'third_party/googletest'
mv '../%{gtest_dir}' 'third_party/googletest'
%else
# Patch CMakeLists for external gtest/gmock.
#
#  1. Create dummy sources, adding a typedef so the translation unit is not
#     empty, rather than removing references to these sources from
#     CMakeLists.txt. This is so that we do not end up with executables with no
#     sources, only libraries, which is a CMake error.
#  2. Either remove references to the corresponding include directories, or
#     create the directories and leave them empty.
#  3. “Stuff” the external library into the target_link_libraries() for each
#     test by noting that GMock/GTest/GFlags are always used together.
for gwhat in test mock
do
  mkdir -p "third_party/googletest/google${gwhat}/src" \
      "third_party/googletest/google${gwhat}/include"
  echo "typedef int dummy_${gwhat}_type;" \
      > "third_party/googletest/google${gwhat}/src/g${gwhat}-all.cc"
done
sed -r -i 's/^([[:blank:]]*)(\$\{_gRPC_GFLAGS_LIBRARIES\})/'\
'\1\2\n\1gtest\n\1gmock/' CMakeLists.txt
%endif

%if %{defined flatpak}
# Fix hard-coded search paths of some libraries
sed -r -i '/((RE2|ABSL)_INCLUDE|libabsl_)/s|/usr|%{_prefix}|' setup.py
%endif

# Extract the source tarballs needed for their .proto files, which upstream
# expects to download at build time.
%setup -q -T -D -b 2 -n grpc-%{srcversion}
%setup -q -T -D -b 3 -n grpc-%{srcversion}
%setup -q -T -D -b 4 -n grpc-%{srcversion}
%setup -q -T -D -b 5 -n grpc-%{srcversion}
{
  awk '$1 ~ /^(#|$)/ { next }; 1' <<'EOF'
../%{envoy_api_dir}/ third_party/envoy-api/
../%{googleapis_dir}/ third_party/googleapis/
../%{opencensus_proto_dir}/ third_party/opencensus-proto/
../%{xds_dir}/ third_party/xds/
EOF
} | while read -r fromdir todir
do
  # Remove everything from the external source tree except the .proto files, to
  # prove that none of it is bundled.
  find "${fromdir}" -type f ! -name '*.proto' -print -delete
  # Remove the empty directory corresponding to the git submodule
  rm -rvf "${todir}"
  # Move the extracted source, to the location where the git submodule would be
  # in a git checkout that included it.
  mv "${fromdir}" "${todir}"
done

echo '===== Removing bundled xxhash =====' 2>&1
# Remove bundled xxhash
rm -rvf third_party/xxhash
# Since grpc sets XXH_INCLUDE_ALL wherever it uses xxhash, it is using xxhash
# as a header-only library. This means we can replace it with the system copy
# by doing nothing further; xxhash.h is in the system include path and will be
# found instead, and there are no linker flags to add. See also
# https://github.com/grpc/grpc/issues/25945.

echo '===== Fixing permissions =====' 2>&1
# https://github.com/grpc/grpc/pull/27069
find . -type f -perm /0111 \
    -exec gawk '!/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r chmod -v a-x

echo '===== Removing selected unused sources =====' 2>&1
# Remove unused sources that have licenses not in the License field, to ensure
# they are not accidentally used in the build. See the comment above the base
# package License field for more details.
rm -rfv \
    src/boringssl/boringssl_prefix_symbols.h \
    third_party/cares/ares_build.h \
    third_party/upb/third_party/lunit
# Since we are replacing roots.pem with a symlink to the shared system
# certificates, we do not include its license (MPLv2.0) in any License field.
# We remove its contents so that, if we make a packaging mistake, we will have
# a bug but not an incorrect License field.
echo '' > etc/roots.pem

# Remove Android sources and examples. We do not need these on Linux, and they
# have some issues that will be flagged when reviewing the package, such as:
#   - Another copy of the MPLv2.0-licensed certificate bundle from
#     etc/roots.pem, in src/android/test/interop/app/src/main/assets/roots.pem
#   - Pre-built jar files at
#     src/android/test/interop/gradle/wrapper/gradle-wrapper.jar and
#     examples/android/helloworld/gradle/wrapper/gradle-wrapper.jar
rm -rvf examples/android src/android

# Drop the NodeJS example’s package-lock.json file, which will hopefully keep
# us from having bugs filed due to CVE’s in its (unpackaged) recursive
# dependencies.
rm -vf examples/node/package-lock.json

# Remove unwanted .gitignore files, generally in examples. One could argue that
# a sample .gitignore file is part of the example, but, well, we’re not going
# to do that.
find . -type f -name .gitignore -print -delete

echo '===== Fixing shebangs =====' 2>&1
# Find executables with /usr/bin/env shebangs in the examples, and fix them.
find . -type f -perm /0111 -exec gawk \
    '/^#!\/usr\/bin\/env[[:blank:]]/ { print FILENAME }; { nextfile }' \
    '{}' '+' |
  xargs -r sed -r -i '1{s|^(#!/usr/bin/)env[[:blank:]]+([^[:blank:]]+)|\1\2|}'

echo '===== Fixing hard-coded C++ standard =====' 2>&1
# We need to adjust the C++ standard to avoid abseil-related linker errors. For
# the main C++ build, we can use CMAKE_CXX_STANDARD. For extensions, examples,
# etc., we must patch.
sed -r -i 's/(std=c\+\+)14/\1%{cpp_std}/g' \
    setup.py Rakefile \
    examples/cpp/*/Makefile \
    examples/cpp/*/CMakeLists.txt \
    tools/run_tests/artifacts/artifact_targets.py \
    tools/distrib/python/grpcio_tools/setup.py

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
    -DgRPC_PROTOBUF_PACKAGE_TYPE:STRING='MODULE' \
    -DgRPC_BENCHMARK_PROVIDER:STRING='package' \
    -DgRPC_ABSL_PROVIDER:STRING='package' \
    -DgRPC_USE_PROTO_LITE:BOOL=OFF \
    -DgRPC_BUILD_GRPC_CPP_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_CSHARP_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_NODE_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_OBJECTIVE_C_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_PHP_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_PYTHON_PLUGIN:BOOL=ON \
    -DgRPC_BUILD_GRPC_RUBY_PLUGIN:BOOL=ON \
    -GNinja
cmake --build "%{_vpath_builddir}" -j${RPM_BUILD_NCPUS} --target \
    address_sorting \
    gpr \
    grpc \
    grpc++ \
    grpc++_alts \
    grpc++_error_details \
    grpc++_reflection \
    grpc++_unsecure \
    grpc_plugin_support \
    grpc_unsecure \
    grpcpp_channelz \
    grpc_cpp_plugin \
    grpc_csharp_plugin \
    grpc_node_plugin \
    grpc_objective_c_plugin \
    grpc_php_plugin \
    grpc_python_plugin \
    grpc_ruby_plugin \
    grpc_cli
%if %{with core_tests}
cmake --build "%{_vpath_builddir}" -j${RPM_BUILD_NCPUS}
%endif
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
export GRPC_PYTHON_DISABLE_LIBC_COMPATIBILITY='True'
export GRPC_PYTHON_ENABLE_DOCUMENTATION_BUILD='False'
export GRPC_PYTHON_CFLAGS="$(
  pkg-config --cflags protobuf
) -std=c++%{cpp_std} -fvisibility=hidden -fno-wrapv -fno-exceptions"
export GRPC_PYTHON_LDFLAGS="$(pkg-config --libs protobuf)"
%py3_build
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
%py3_build
find . -type f -name protoc.py -execdir sed -r -i '1{/^#!/d}' '{}' '+'
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
  %py3_build
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
%py3_install
pushd "tools/distrib/python/grpcio_tools/" >/dev/null
%py3_install
popd >/dev/null
for suffix in channelz health_checking reflection status testing
do
  pushd "src/python/grpcio_${suffix}/" >/dev/null
  %py3_install
  popd >/dev/null
done
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
%oreon_autofiles python3-grpcio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-grpcio-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-grpcio-channelz usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-grpcio-health-checking usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-grpcio-reflection usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-grpcio-status usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-grpcio-testing usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifarch %{ix86}
cat <<'EOF'
Since the following changes are accepted for F37:
https://fedoraproject.org/wiki/Changes/RetireARMv7
https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
…we still build for i686 since this is not a leaf packages, but skip tests so
we do not have to keep track of 32-bit-specific issues.
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
%ifarch s390x
address_sorting
%endif
%ifarch s390x
alts_crypt
%endif
%ifarch s390x
alts_crypter
%endif
%ifarch s390x
alts_concurrent_connectivity
%endif
%ifarch s390x
alts_frame_protector
%endif
%ifarch s390x
alts_grpc_record_protocol
%endif
%ifarch s390x
alts_iovec_record_protocol
%endif
%ifarch s390x
alts_zero_copy_grpc_protector
%endif
client_ssl
%ifarch s390x riscv64
test_core_security_credentials
%endif
%ifarch x86_64 aarch64
examine_stack
%endif
%ifarch s390x
goaway_server
%endif
%ifarch aarch64 x86_64 ppc64le s390x riscv64
grpc_tool
%endif
%ifarch s390x
murmur_hash
%endif
%ifarch ppc64le
rls_end2end
%endif
%ifarch ppc64le
service_config
%endif
%ifarch x86_64 aarch64
stack_tracer
%endif
%ifarch aarch64 x86_64 ppc64le
test_core_security_credentials
%endif
%ifarch aarch64 x86_64 ppc64le s390x riscv64
tls_key_export
%endif
EOF
} | xargs -r chmod -v a-x
%{__python3} tools/run_tests/start_port_server.py
find %{_vpath_builddir} -type f -perm /0111 -name '*_test' | sort |
  while read -r testexe
  do
    echo "==== $(date -u --iso-8601=ns): $(basename "${testexe}") ===="
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
    test_lite \
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

%files -f %{oreon_filedir}/main.list
%files -n grpc-data -f %{oreon_filedir}/grpc-data.list
%files -n grpc-doc -f %{oreon_filedir}/grpc-doc.list
%files -n grpc-cpp -f %{oreon_filedir}/grpc-cpp.list
%files -n grpc-plugins -f %{oreon_filedir}/grpc-plugins.list
%files -n grpc-cli -f %{oreon_filedir}/grpc-cli.list
%files -n grpc-devel -f %{oreon_filedir}/grpc-devel.list
%files -n python3-grpcio -f %{oreon_filedir}/python3-grpcio.list
%files -n python3-grpcio-tools -f %{oreon_filedir}/python3-grpcio-tools.list
%files -n python3-grpcio-channelz -f %{oreon_filedir}/python3-grpcio-channelz.list
%files -n python3-grpcio-health-checking -f %{oreon_filedir}/python3-grpcio-health-checking.list
%files -n python3-grpcio-reflection -f %{oreon_filedir}/python3-grpcio-reflection.list
%files -n python3-grpcio-status -f %{oreon_filedir}/python3-grpcio-status.list
%files -n python3-grpcio-testing -f %{oreon_filedir}/python3-grpcio-testing.list
