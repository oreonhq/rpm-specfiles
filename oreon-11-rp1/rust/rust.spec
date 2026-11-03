%global source0_hash 6451598a99e77f07571960f6b21d577399d3a30f33e80cbd2e3a4aae6535d265
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

# Stage0: when Oreon Build Service detects that rust/cargo do not resolve it
# turns on bootstrap through %%oreon_bootstrap, and this build uses the
# upstream stage0 rustc/cargo (sha256 pinned by src/stage0 in the signed
# source tarball). The next build in the chain self-hosts on the result.
%global oreon_stage0 %[%{with bootstrap} || 0%{?bootstrap}]

# Stage0 pinned by src/stage0 in the signed source tarball.
%global stage0_version 1.98.0
%global stage0_date 2026-08-20
%global stage0_url https://static.rust-lang.org/dist/%{stage0_date}
%global rust_triple %{_arch}-unknown-linux-gnu
%global rustlibdir %{_libdir}/rustlib

Name: rust
Version: 1.99.1
Release: 4%{?dist}
Summary: The Rust programming language
License: (Apache-2.0 OR MIT) AND (Artistic-2.0 AND BSD-3-Clause AND ISC AND MIT AND Unicode-DFS-2016)
URL: https://www.rust-lang.org/
Source0: https://static.rust-lang.org/dist/rustc-%{version}-src.tar.xz
Source1: rustc-%{version}-src.tar.xz.asc
Source2: rust-key.asc
%if %{oreon_stage0}
Source100: %{stage0_url}/rustc-%{stage0_version}-x86_64-unknown-linux-gnu.tar.xz
Source101: %{stage0_url}/rust-std-%{stage0_version}-x86_64-unknown-linux-gnu.tar.xz
Source102: %{stage0_url}/cargo-%{stage0_version}-x86_64-unknown-linux-gnu.tar.xz
Source103: %{stage0_url}/rustc-%{stage0_version}-aarch64-unknown-linux-gnu.tar.xz
Source104: %{stage0_url}/rust-std-%{stage0_version}-aarch64-unknown-linux-gnu.tar.xz
Source105: %{stage0_url}/cargo-%{stage0_version}-aarch64-unknown-linux-gnu.tar.xz
%endif
ExclusiveArch: x86_64 aarch64

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: python3
BuildRequires: pkgconf
BuildRequires: patchelf
BuildRequires: file
BuildRequires: llvm-devel >= 20
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
BuildRequires: libcurl-devel
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: rust
BuildRequires: cargo
%endif
Requires: gcc
Requires: rust-std-static%{?_isa} = %{version}-%{release}
Provides: rustc = %{version}-%{release}
Provides: rustc%{?_isa} = %{version}-%{release}

%description
Rust is a systems programming language focused on safety, speed and
concurrency. This package ships rustc, rustdoc and the standard library.

%package -n cargo
Summary: Rust package manager
Requires: rust%{?_isa} = %{version}-%{release}

%description -n cargo
Cargo downloads Rust project dependencies and builds Rust projects.

%package std-static
Summary: Standard library for Rust

%description std-static
The Rust standard library for the host target.

%package src
Summary: Sources for the Rust standard library

%description src
Sources for the Rust standard library, used by IDE tooling.

%package -n rustfmt
Summary: Tool to format Rust code
Requires: cargo%{?_isa} = %{version}-%{release}

%description -n rustfmt
rustfmt formats Rust code according to style guidelines.

%package -n clippy
Summary: Lints to catch common mistakes in Rust code
Requires: cargo%{?_isa} = %{version}-%{release}
Requires: rust%{?_isa} = %{version}-%{release}

%description -n clippy
Clippy is a collection of lints for Rust code.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n rustc-%{version}-src -p1
%if %{oreon_stage0}
%ifarch x86_64
s0="%{SOURCE100} %{SOURCE101} %{SOURCE102}"
cat > stage0.sha256 <<'SUMS'
0e37cb339f447fc44d6d781073bacacebfdc5612f2600e4c7e84c266f5f3aced  %{SOURCE100}
f5022e6c95a5ad23cca2513dc8281200f585fa188de6370aa37b128a43f876a3  %{SOURCE101}
2f512d170d3dd23e16ababcda32ee2e6d5172d861a7af1f504e0b1e270cafab9  %{SOURCE102}
SUMS
%endif
%ifarch aarch64
s0="%{SOURCE103} %{SOURCE104} %{SOURCE105}"
cat > stage0.sha256 <<'SUMS'
00590657f2356d7163ca5ef295283523974c340fa21bb94b420ce794f29b358c  %{SOURCE103}
a36f7ac98af20ef0ba6368aace0345efabbebaef7962eba99f47190fd256162d  %{SOURCE104}
5784379d73ac881d15a9e67eed2882cd58c747c276221c23cdf9aff37e015ff6  %{SOURCE105}
SUMS
%endif
sha256sum -c stage0.sha256
rm -f stage0.sha256
mkdir -p oreon-stage0-src
for t in $s0; do
  tar -C oreon-stage0-src -xJf "$t"
done
for d in oreon-stage0-src/*/; do
  sh "$d/install.sh" --prefix="$PWD/oreon-stage0" --disable-ldconfig --components="$(cat "$d/components" | tr '\n' ',' | sed 's/,$//')"
done
rm -rf oreon-stage0-src
%endif

%build
%if %{oreon_stage0}
rust_root=$PWD/oreon-stage0
%else
rust_root=%{_prefix}
%endif
export CFLAGS="%{_oreon_cflags}" CXXFLAGS="%{_oreon_cflags}" LDFLAGS="%{_oreon_ldflags}"
./configure \
  --build=%{rust_triple} --host=%{rust_triple} --target=%{rust_triple} \
  --prefix=%{_prefix} --libdir=%{_libdir} --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} --mandir=%{_mandir} --docdir=%{_docdir}/rust \
  --local-rust-root="$rust_root" \
  --llvm-root=%{_prefix} --enable-llvm-link-shared --disable-llvm-static-stdcpp \
  --disable-docs --disable-compiler-docs --disable-rpath \
  --enable-extended --tools=cargo,clippy,rustfmt,src \
  --enable-vendor --release-channel=stable \
  --release-description="Oreon %{version}-%{release}" \
  --set build.optimized-compiler-builtins=false \
  --set rust.lld=false --set rust.llvm-tools=false \
  --set rust.codegen-units-std=1 --set rust.debuginfo-level=0 \
  --set build.offline=true
python3 ./x.py build -j %{_oreon_jobs}

%install
DESTDIR=%{buildroot} python3 ./x.py install
rm -f %{buildroot}%{_libdir}/rustlib/{install.log,uninstall.sh,components,rust-installer-version}
rm -f %{buildroot}%{_libdir}/rustlib/manifest-*
rm -rf %{buildroot}%{_docdir}/rust %{buildroot}%{_docdir}/cargo %{buildroot}%{_docdir}/clippy %{buildroot}%{_docdir}/rustfmt
rm -f %{buildroot}%{_sysconfdir}/target-spec-json-schema.json
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done

%files
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%{_bindir}/rustc
%{_bindir}/rustdoc
%{_bindir}/rust-gdb
%{_bindir}/rust-gdbgui
%{_bindir}/rust-lldb
%{_libdir}/librustc_driver-*.so
%dir %{rustlibdir}
%{rustlibdir}/etc/
%{_mandir}/man1/rustc.1*
%{_mandir}/man1/rustdoc.1*

%files std-static
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%dir %{rustlibdir}
%dir %{rustlibdir}/%{rust_triple}
%dir %{rustlibdir}/%{rust_triple}/lib
%{rustlibdir}/%{rust_triple}/lib/*.rlib
%{rustlibdir}/%{rust_triple}/lib/*.rmeta
%{rustlibdir}/%{rust_triple}/lib/*.so

%files src
%dir %{rustlibdir}
%{rustlibdir}/src/

%files -n cargo
%license src/tools/cargo/LICENSE-APACHE src/tools/cargo/LICENSE-MIT src/tools/cargo/LICENSE-THIRD-PARTY
%{_bindir}/cargo
%{_mandir}/man1/cargo*.1*
%{_sysconfdir}/bash_completion.d/cargo
%{_datadir}/zsh/site-functions/_cargo

%files -n rustfmt
%license src/tools/rustfmt/LICENSE-APACHE src/tools/rustfmt/LICENSE-MIT
%{_bindir}/rustfmt
%{_bindir}/cargo-fmt

%files -n clippy
%license src/tools/clippy/LICENSE-APACHE src/tools/clippy/LICENSE-MIT
%{_bindir}/cargo-clippy
%{_bindir}/clippy-driver
