%global source0_hash 25485360a54d6861439d60facef26de713b1e126bf015ec8f98239467a2b82f7
%bcond check 1
%global debug_package %{nil}
%global crate procfs
Name:           rust-procfs
Version:        0.18.0
Release:        1%{?dist}
Summary:        Interface to the linux procfs pseudo-filesystem
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/procfs
Source0:        https://static.crates.io/crates/procfs/procfs-%{version}.crate
Patch:          procfs-fix-metadata.diff
Patch10:        procfs-0.17.0-no-test_procinfo.patch
Patch11:        procfs-0.17.0-no-test_failure.patch
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
Summary:        Interface to the linux procfs pseudo-filesystem
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Interface to the linux procfs pseudo-filesystem
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Interface to the linux procfs pseudo-filesystem
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+flate2-devel
Summary:        Interface to the linux procfs pseudo-filesystem
BuildArch:      noarch
%description -n %{name}+flate2-devel

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Interface to the linux procfs pseudo-filesystem
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde1-devel
Summary:        Interface to the linux procfs pseudo-filesystem
BuildArch:      noarch
%description -n %{name}+serde1-devel

This package contains library source intended for building other packages which
use the "serde1" feature of the "%{crate}" crate.

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

skip="${skip-} --skip _runsinglethread"
skip="${skip-} --skip sys::kernel::random::tests::test_write_wakeup_threshold"
%ifnarch x86_64 %{ix86}
skip="${skip-} --skip tests::test_cpuinfo"
%endif
%ifarch s390x
skip="${skip-} --skip tests::test_kernel_stat"
skip="${skip-} --skip tests::test_meminfo"
%endif
%{cargo_test -- -- ${skip-}}
%ifarch s390x
stskip="${stskip-} --skip process::task::tests::test_task_runsinglethread"
%endif
%{cargo_test -- -- _runsinglethread --test-threads 1 ${stskip-}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-procfs-devel -f %{oreon_filedir}/rust-procfs-devel.list

%changelog

%autochangelog
