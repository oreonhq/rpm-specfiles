%global source0_hash 74523f3a35e05aba87a1d978330aef40f67b0304ac79c1c00b294c9830543db6
%bcond check 1
%global debug_package %{nil}
%global crate nix
Name:           rust-nix0.30
Version:        0.30.1
Release:        1%{?dist}
Summary:        Rust friendly bindings to *nix APIs
License:        MIT
URL:            https://crates.io/crates/nix
Source0:        https://static.crates.io/crates/nix/nix-%{version}.crate
Patch:          nix-fix-metadata-auto.diff
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
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+acct-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+acct-devel

This package contains library source intended for building other packages which
use the "acct" feature of the "%{crate}" crate.

%package     -n %{name}+aio-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+aio-devel

This package contains library source intended for building other packages which
use the "aio" feature of the "%{crate}" crate.

%package     -n %{name}+dir-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+dir-devel

This package contains library source intended for building other packages which
use the "dir" feature of the "%{crate}" crate.

%package     -n %{name}+env-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+env-devel

This package contains library source intended for building other packages which
use the "env" feature of the "%{crate}" crate.

%package     -n %{name}+event-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+event-devel

This package contains library source intended for building other packages which
use the "event" feature of the "%{crate}" crate.

%package     -n %{name}+fanotify-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+fanotify-devel

This package contains library source intended for building other packages which
use the "fanotify" feature of the "%{crate}" crate.

%package     -n %{name}+feature-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+feature-devel

This package contains library source intended for building other packages which
use the "feature" feature of the "%{crate}" crate.

%package     -n %{name}+fs-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+fs-devel

This package contains library source intended for building other packages which
use the "fs" feature of the "%{crate}" crate.

%package     -n %{name}+hostname-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+hostname-devel

This package contains library source intended for building other packages which
use the "hostname" feature of the "%{crate}" crate.

%package     -n %{name}+inotify-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+inotify-devel

This package contains library source intended for building other packages which
use the "inotify" feature of the "%{crate}" crate.

%package     -n %{name}+ioctl-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+ioctl-devel

This package contains library source intended for building other packages which
use the "ioctl" feature of the "%{crate}" crate.

%package     -n %{name}+kmod-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+kmod-devel

This package contains library source intended for building other packages which
use the "kmod" feature of the "%{crate}" crate.

%package     -n %{name}+memoffset-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+memoffset-devel

This package contains library source intended for building other packages which
use the "memoffset" feature of the "%{crate}" crate.

%package     -n %{name}+mman-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+mman-devel

This package contains library source intended for building other packages which
use the "mman" feature of the "%{crate}" crate.

%package     -n %{name}+mount-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+mount-devel

This package contains library source intended for building other packages which
use the "mount" feature of the "%{crate}" crate.

%package     -n %{name}+mqueue-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+mqueue-devel

This package contains library source intended for building other packages which
use the "mqueue" feature of the "%{crate}" crate.

%package     -n %{name}+net-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+net-devel

This package contains library source intended for building other packages which
use the "net" feature of the "%{crate}" crate.

%package     -n %{name}+personality-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+personality-devel

This package contains library source intended for building other packages which
use the "personality" feature of the "%{crate}" crate.

%package     -n %{name}+pin-utils-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+pin-utils-devel

This package contains library source intended for building other packages which
use the "pin-utils" feature of the "%{crate}" crate.

%package     -n %{name}+poll-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+poll-devel

This package contains library source intended for building other packages which
use the "poll" feature of the "%{crate}" crate.

%package     -n %{name}+process-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+process-devel

This package contains library source intended for building other packages which
use the "process" feature of the "%{crate}" crate.

%package     -n %{name}+pthread-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+pthread-devel

This package contains library source intended for building other packages which
use the "pthread" feature of the "%{crate}" crate.

%package     -n %{name}+ptrace-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+ptrace-devel

This package contains library source intended for building other packages which
use the "ptrace" feature of the "%{crate}" crate.

%package     -n %{name}+quota-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+quota-devel

This package contains library source intended for building other packages which
use the "quota" feature of the "%{crate}" crate.

%package     -n %{name}+reboot-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+reboot-devel

This package contains library source intended for building other packages which
use the "reboot" feature of the "%{crate}" crate.

%package     -n %{name}+resource-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+resource-devel

This package contains library source intended for building other packages which
use the "resource" feature of the "%{crate}" crate.

%package     -n %{name}+sched-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+sched-devel

This package contains library source intended for building other packages which
use the "sched" feature of the "%{crate}" crate.

%package     -n %{name}+signal-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+signal-devel

This package contains library source intended for building other packages which
use the "signal" feature of the "%{crate}" crate.

%package     -n %{name}+socket-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+socket-devel

This package contains library source intended for building other packages which
use the "socket" feature of the "%{crate}" crate.

%package     -n %{name}+syslog-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+syslog-devel

This package contains library source intended for building other packages which
use the "syslog" feature of the "%{crate}" crate.

%package     -n %{name}+term-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+term-devel

This package contains library source intended for building other packages which
use the "term" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+ucontext-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+ucontext-devel

This package contains library source intended for building other packages which
use the "ucontext" feature of the "%{crate}" crate.

%package     -n %{name}+uio-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+uio-devel

This package contains library source intended for building other packages which
use the "uio" feature of the "%{crate}" crate.

%package     -n %{name}+user-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+user-devel

This package contains library source intended for building other packages which
use the "user" feature of the "%{crate}" crate.

%package     -n %{name}+zerocopy-devel
Summary:        Rust friendly bindings to *nix APIs
BuildArch:      noarch
%description -n %{name}+zerocopy-devel

This package contains library source intended for building other packages which
use the "zerocopy" feature of the "%{crate}" crate.

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
    --skip sys::test_aio::test_aio_suspend
    --skip sys::test_resource::test_self_cpu_time
    --skip sys::test_socket::test_af_alg_cipher
    --skip sys::test_socket::test_recvmm2
    --skip sys::test_socket::test_recvmsg_rxq_ovfl
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-nix0.30-devel -f %{oreon_filedir}/rust-nix0.30-devel.list

%changelog

%autochangelog
