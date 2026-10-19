%global source0_hash 43186959edc87d5c7a1be7b7d2a25efffd22ce5807c7af99067f86f99641bfdf
%global         zig_arches x86_64 aarch64 riscv64 %{mips64}
%global         public_key RWSGOq2NVecA2UPNdBUZykf1CCb147pkmdtYxgb3Ti+JO/wCYvhbAb/U
%if 0%{?fedora} >= 43 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
%global         llvm_compat 20
%endif
%global         llvm_version 20.0.0
%bcond bootstrap 0
%bcond docs      %{without bootstrap}
%bcond macro     %{without bootstrap}
%bcond test      1
%global zig_cache_dir %{_vpath_builddir}/zig-cache
%global zig_build_options %{shrink: \
    --verbose \
    --release=fast \
    --summary all \
    \
    -Dtarget=native \
    -Dcpu=baseline \
    --zig-lib-dir lib \
    --build-id=sha1 \
    \
    --cache-dir "%{zig_cache_dir}" \
    --global-cache-dir "%{zig_cache_dir}" \
    \
    -Dversion-string="%{version}" \
    -Dstatic-llvm=false \
    -Denable-llvm=true \
    -Dno-langref=true \
    -Dstd-docs=false \
    -Dpie \
    -Dconfig_h="%{__cmake_builddir}/config.h" \
}
%global zig_install_options %zig_build_options %{shrink: \
    --prefix "%{_prefix}" \
}
Name:           zig
Version:        0.16.0
Release:        1%{?dist}
Summary:        Programming language for maintaining robust, optimal, and reusable software
%global         archive_name %{name}-%{version}.tar.xz
License:        MIT AND NCSA AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later AND GPL-2.0-or-later WITH GCC-exception-2.0 AND BSD-3-Clause AND Inner-Net-2.0 AND ISC AND LicenseRef-Fedora-Public-Domain AND GFDL-1.1-or-later AND ZPL-2.1
URL:            https://ziglang.org
Source0:        https://%{name}lang.org/download/%{version}/%{archive_name}
Source1:        %{url}/download/%{version}/%{archive_name}.minisig
Source2:        macros.%{name}
Patch0:         0001-remove-native-lib-directories-from-rpath.patch
Patch1:         0002-Remove-unsupported-LLVM-targets-for-EPEL.patch
%if %{without bootstrap}
%endif
%if %{with test}
%endif
Requires:       %{name}-libs = %{version}
Provides: bundled(compiler-rt) = %{llvm_version}
Provides: bundled(glibc) = 2.41
Provides: bundled(libcxx) = %{llvm_version}
Provides: bundled(libcxxabi) = %{llvm_version}
Provides: bundled(libunwind) = %{llvm_version}
Provides: bundled(mingw) = 3839e21b08807479a31d5a9764666f82ae2f0356
Provides: bundled(musl) = 1.2.5
Provides: bundled(wasi-libc) = d03829489904d38c624f6de9983190f1e5e7c9c5
ExclusiveArch: %{zig_arches}
# oreon:deps
BuildRequires:  (zig >= 0.15 with zig < 0.16)
BuildRequires:  clang20-devel
BuildRequires:  cmake
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libstdc++-static
BuildRequires:  libxml2-devel
BuildRequires:  lld20-devel
BuildRequires:  llvm20-devel
BuildRequires:  minisign
BuildRequires:  zlib-devel
# /oreon:deps
%description
Zig is an open-source programming language designed for robustness, optimality,
and clarity. This package provides the zig compiler and the associated runtime.

# The Zig stdlib only contains uncompiled code
%package libs
Summary:        %{name} Standard Library
BuildArch:      noarch
%description libs
%{name} Standard Library

%if %{with docs}
%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}
%description doc
Documentation for %{name}. For more information, visit %{url}
%endif

%if %{with macro}
%package        rpm-macros
Summary:        Common RPM macros for %{name}
Requires:       rpm
BuildArch:      noarch
%description    rpm-macros
This package contains common RPM macros for %{name}.
%endif

%prep

/usr/bin/minisign -V -m %{SOURCE0} -x %{SOURCE1} -P %{public_key} -Q | grep -F "file:%{archive_name}"

%autosetup -N
%patch 0 -p1

%if %{without bootstrap}
# Ensure that the pre-build stage1 binary is not used
rm -f stage1/zig1.wasm
%endif

%build

export CCACHE_DISABLE=1
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
    -DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING="-DNDEBUG -Wno-unused" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="-DNDEBUG -Wno-unused" \
    \
    -DZIG_EXTRA_BUILD_ARGS:STRING="--verbose;--build-id=sha1" \
    -DZIG_SHARED_LLVM:BOOL=true \
    -DZIG_PIE:BOOL=true \
    \
    -DZIG_TARGET_MCPU:STRING=baseline \
    -DZIG_TARGET_TRIPLE:STRING=native \
    \
    -DZIG_VERSION:STRING="%{version}"
%if %{with bootstrap}
%cmake_build --target stage3
%else
%cmake_build --target zigcpp
zig build %{zig_build_options}
help2man --no-discard-stderr --no-info "./zig-out/bin/zig" --version-option=version --output=zig.1
%endif
%if %{with docs}
./zig-out/bin/zig build docs %{zig_build_options}
%endif
%install
%if %{with bootstrap}
%cmake_install
%else
DESTDIR="%{buildroot}" zig build install %{zig_install_options}
install -D -pv -m 0644 -t %{buildroot}%{_mandir}/man1/ zig.1
%endif
%if %{with macro}
install -D -pv -m 0644 %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if %{with test}
%check

"%{buildroot}%{_bindir}/zig" test test/behavior.zig -Itest
%endif
%files -f %{oreon_filedir}/main.list
%files -n zig-libs -f %{oreon_filedir}/zig-libs.list
%files -n zig-doc -f %{oreon_filedir}/zig-doc.list
%files -n zig-rpm-macros -f %{oreon_filedir}/zig-rpm-macros.list

%changelog

%autochangelog
