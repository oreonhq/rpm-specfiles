%global source0_hash 891efababe418670775f199f0d233d84843c227a0949a883ce15b37c78d6629d
%bcond bootstrap 1
%bcond check %{without bootstrap}
%global debug_package %{nil}
%global crate rustix
Name:           rust-rustix
Version:        1.1.5
Release:        1%{?dist}
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/rustix
Source0:        https://static.crates.io/crates/rustix/rustix-%{version}.crate
Patch:          rustix-fix-metadata-auto.diff
Patch:          rustix-fix-metadata.diff
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
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-apis-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+all-apis-devel

This package contains library source intended for building other packages which
use the "all-apis" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+event-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+event-devel

This package contains library source intended for building other packages which
use the "event" feature of the "%{crate}" crate.

%package     -n %{name}+fs-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+fs-devel

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%package     -n %{name}+io_uring-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+io_uring-devel

This package contains library source intended for building other packages which
use the "io_uring" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+libc_errno-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+libc_errno-devel

This package contains library source intended for building other packages which
use the "libc_errno" feature of the "%{crate}" crate.

%package     -n %{name}+linux_4_11-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+linux_4_11-devel

This package contains library source intended for building other packages which
use the "linux_4_11" feature of the "%{crate}" crate.

%package     -n %{name}+linux_5_1-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+linux_5_1-devel

This package contains library source intended for building other packages which
use the "linux_5_1" feature of the "%{crate}" crate.

%package     -n %{name}+linux_5_11-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+linux_5_11-devel

This package contains library source intended for building other packages which
use the "linux_5_11" feature of the "%{crate}" crate.

%package     -n %{name}+linux_latest-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+linux_latest-devel

This package contains library source intended for building other packages which
use the "linux_latest" feature of the "%{crate}" crate.

%package     -n %{name}+mm-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+mm-devel

This package contains library source intended for building other packages which
use the "mm" feature of the "%{crate}" crate.

%package     -n %{name}+mount-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+mount-devel

This package contains library source intended for building other packages which
use the "mount" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+param-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+param-devel

This package contains library source intended for building other packages which
use the "param" feature of the "%{crate}" crate.

%package     -n %{name}+pipe-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+pipe-devel

This package contains library source intended for building other packages which
use the "pipe" feature of the "%{crate}" crate.

%package     -n %{name}+process-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+process-devel

This package contains library source intended for building other packages which
use the "process" feature of the "%{crate}" crate.

%package     -n %{name}+pty-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+pty-devel

This package contains library source intended for building other packages which
use the "pty" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+runtime-devel

This package contains library source intended for building other packages which
use the "runtime" feature of the "%{crate}" crate.

%package     -n %{name}+shm-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+shm-devel

This package contains library source intended for building other packages which
use the "shm" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+stdio-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+stdio-devel

This package contains library source intended for building other packages which
use the "stdio" feature of the "%{crate}" crate.

%package     -n %{name}+system-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+system-devel

This package contains library source intended for building other packages which
use the "system" feature of the "%{crate}" crate.

%package     -n %{name}+termios-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+termios-devel

This package contains library source intended for building other packages which
use the "termios" feature of the "%{crate}" crate.

%package     -n %{name}+thread-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+thread-devel

This package contains library source intended for building other packages which
use the "thread" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+try_close-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+try_close-devel

This package contains library source intended for building other packages which
use the "try_close" feature of the "%{crate}" crate.

%package     -n %{name}+use-explicitly-provided-auxv-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+use-explicitly-provided-auxv-devel

This package contains library source intended for building other packages which
use the "use-explicitly-provided-auxv" feature of the "%{crate}" crate.

%package     -n %{name}+use-libc-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+use-libc-devel

This package contains library source intended for building other packages which
use the "use-libc" feature of the "%{crate}" crate.

%package     -n %{name}+use-libc-auxv-devel
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls
BuildArch:      noarch
%description -n %{name}+use-libc-auxv-devel

This package contains library source intended for building other packages which
use the "use-libc-auxv" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -a -- -- --exact %{shrink:
    --skip buffer::tests::test_slice
    --skip buffer::tests::test_slice_uninit
    --skip buffer::tests::test_spare_capacity
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rustix-devel -f %{oreon_filedir}/rust-rustix-devel.list

%changelog

%autochangelog
