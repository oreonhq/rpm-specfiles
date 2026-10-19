%global source0_hash 0c460d4fa06223667240720ab69a8045133755ae6dfbe100cf481b95e3a014f1
%bcond check 1
%global crate inferno
Name:           rust-inferno
Version:        0.12.8
Release:        1%{?dist}
Summary:        Rust port of the FlameGraph performance profiling tool suite
License:        CDDL-1.0
URL:            https://crates.io/crates/inferno
Source0:        https://static.crates.io/crates/inferno/inferno-%{version}.crate
Patch:          inferno-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Rust port of the FlameGraph performance profiling tool suite
License:        %{shrink:
    CDDL-1.0 AND
    MIT AND
    (Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT) AND
    (Zlib OR Apache-2.0 OR MIT)
}
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-channel-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+crossbeam-channel-devel

This package contains library source intended for building other packages which
use the "crossbeam-channel" feature of the "%{crate}" crate.

%package     -n %{name}+crossbeam-utils-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+crossbeam-utils-devel

This package contains library source intended for building other packages which
use the "crossbeam-utils" feature of the "%{crate}" crate.

%package     -n %{name}+dashmap-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+dashmap-devel

This package contains library source intended for building other packages which
use the "dashmap" feature of the "%{crate}" crate.

%package     -n %{name}+env_logger-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+env_logger-devel

This package contains library source intended for building other packages which
use the "env_logger" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+multithreaded-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+multithreaded-devel

This package contains library source intended for building other packages which
use the "multithreaded" feature of the "%{crate}" crate.

%package     -n %{name}+nameattr-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+nameattr-devel

This package contains library source intended for building other packages which
use the "nameattr" feature of the "%{crate}" crate.

%package     -n %{name}+rle-decode-fast-devel
Summary:        Rust port of the FlameGraph performance profiling tool suite
BuildArch:      noarch
%description -n %{name}+rle-decode-fast-devel

This package contains library source intended for building other packages which
use the "rle-decode-fast" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -- -- %{shrink:
    --skip test_collapse_multi_dtrace
    --skip test_collapse_multi_dtrace_simple
    --skip test_collapse_multi_perf
    --skip test_collapse_multi_perf_simple
    --skip test_multiple_skip_after
    --skip test_one_skip_after
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n inferno -f %{oreon_filedir}/inferno.list
%files -n rust-inferno-devel -f %{oreon_filedir}/rust-inferno-devel.list

%changelog

%autochangelog
