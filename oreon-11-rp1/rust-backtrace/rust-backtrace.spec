%global source0_hash bb531853791a215d7c62a30daf0dde835f381ab5de4589cfe7c649d2cbe92bd6
%bcond check 0
%global debug_package %{nil}
%global crate backtrace
Name:           rust-backtrace
Version:        0.3.76
Release:        1%{?dist}
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/backtrace
Source0:        https://static.crates.io/crates/backtrace/backtrace-%{version}.crate
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
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+coresymbolication-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+coresymbolication-devel

This package contains library source intended for building other packages which
use the "coresymbolication" feature of the "%{crate}" crate.

%package     -n %{name}+cpp_demangle-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+cpp_demangle-devel

This package contains library source intended for building other packages which
use the "cpp_demangle" feature of the "%{crate}" crate.

%package     -n %{name}+dbghelp-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+dbghelp-devel

This package contains library source intended for building other packages which
use the "dbghelp" feature of the "%{crate}" crate.

%package     -n %{name}+dl_iterate_phdr-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+dl_iterate_phdr-devel

This package contains library source intended for building other packages which
use the "dl_iterate_phdr" feature of the "%{crate}" crate.

%package     -n %{name}+dladdr-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+dladdr-devel

This package contains library source intended for building other packages which
use the "dladdr" feature of the "%{crate}" crate.

%package     -n %{name}+kernel32-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+kernel32-devel

This package contains library source intended for building other packages which
use the "kernel32" feature of the "%{crate}" crate.

%package     -n %{name}+libunwind-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+libunwind-devel

This package contains library source intended for building other packages which
use the "libunwind" feature of the "%{crate}" crate.

%package     -n %{name}+ruzstd-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+ruzstd-devel

This package contains library source intended for building other packages which
use the "ruzstd" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-serde-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+serialize-serde-devel

This package contains library source intended for building other packages which
use the "serialize-serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unix-backtrace-devel
Summary:        A library to acquire a stack trace (backtrace) at runtime in a Rust p...
BuildArch:      noarch
%description -n %{name}+unix-backtrace-devel

This package contains library source intended for building other packages which
use the "unix-backtrace" feature of the "%{crate}" crate.

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
%files -n rust-backtrace-devel -f %{oreon_filedir}/rust-backtrace-devel.list

%changelog

%autochangelog
