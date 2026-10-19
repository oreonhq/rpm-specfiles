%global source0_hash 519165d378b97752ca44bbe15047d5d3409e875f39327546b42ac81d7e18c1b6
%bcond check 0
%global debug_package %{nil}
%global crate rustix
Name:           rust-rustix0.37
Version:        0.37.28
Release:        1%{?dist}
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/rustix
Source0:        https://static.crates.io/crates/rustix/rustix-%{version}.crate
Patch:          rustix-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-apis-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+all-apis-devel

This package contains library source intended for building other packages which
use the "all-apis" feature of the "%{crate}" crate.

%package     -n %{name}+all-impls-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+all-impls-devel

This package contains library source intended for building other packages which
use the "all-impls" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+compiler_builtins-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+compiler_builtins-devel

This package contains library source intended for building other packages which
use the "compiler_builtins" feature of the "%{crate}" crate.

%package     -n %{name}+core-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+core-devel

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%package     -n %{name}+fs-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+fs-devel

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%package     -n %{name}+fs-err-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+fs-err-devel

This package contains library source intended for building other packages which
use the "fs-err" feature of the "%{crate}" crate.

%package     -n %{name}+io-lifetimes-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+io-lifetimes-devel

This package contains library source intended for building other packages which
use the "io-lifetimes" feature of the "%{crate}" crate.

%package     -n %{name}+io_uring-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+io_uring-devel

This package contains library source intended for building other packages which
use the "io_uring" feature of the "%{crate}" crate.

%package     -n %{name}+itoa-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+itoa-devel

This package contains library source intended for building other packages which
use the "itoa" feature of the "%{crate}" crate.

%package     -n %{name}+linux_4_11-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+linux_4_11-devel

This package contains library source intended for building other packages which
use the "linux_4_11" feature of the "%{crate}" crate.

%package     -n %{name}+linux_latest-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+linux_latest-devel

This package contains library source intended for building other packages which
use the "linux_latest" feature of the "%{crate}" crate.

%package     -n %{name}+mm-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+mm-devel

This package contains library source intended for building other packages which
use the "mm" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+os_pipe-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+os_pipe-devel

This package contains library source intended for building other packages which
use the "os_pipe" feature of the "%{crate}" crate.

%package     -n %{name}+param-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+param-devel

This package contains library source intended for building other packages which
use the "param" feature of the "%{crate}" crate.

%package     -n %{name}+process-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+process-devel

This package contains library source intended for building other packages which
use the "process" feature of the "%{crate}" crate.

%package     -n %{name}+procfs-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+procfs-devel

This package contains library source intended for building other packages which
use the "procfs" feature of the "%{crate}" crate.

%package     -n %{name}+pty-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+pty-devel

This package contains library source intended for building other packages which
use the "pty" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+runtime-devel

This package contains library source intended for building other packages which
use the "runtime" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+rustc-dep-of-std-devel

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+termios-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+termios-devel

This package contains library source intended for building other packages which
use the "termios" feature of the "%{crate}" crate.

%package     -n %{name}+thread-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+thread-devel

This package contains library source intended for building other packages which
use the "thread" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+use-libc-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+use-libc-devel

This package contains library source intended for building other packages which
use the "use-libc" feature of the "%{crate}" crate.

%package     -n %{name}+use-libc-auxv-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls
BuildArch:      noarch
%description -n %{name}+use-libc-auxv-devel

This package contains library source intended for building other packages which
use the "use-libc-auxv" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rustix0.37-devel -f %{oreon_filedir}/rust-rustix0.37-devel.list

%changelog

%autochangelog
