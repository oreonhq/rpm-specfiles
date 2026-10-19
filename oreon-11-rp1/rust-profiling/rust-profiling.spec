%global source0_hash 3d595e54a326bc53c1c197b32d295e14b169e3cfeaa8dc82b529f947fba6bcf5
%bcond check 0
%global debug_package %{nil}
%global crate profiling
Name:           rust-profiling
Version:        1.0.18
Release:        1%{?dist}
Summary:        This crate provides a very thin abstraction over other profiler crates.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/profiling
Source0:        https://static.crates.io/crates/profiling/profiling-%{version}.crate
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
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+optick-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+optick-devel

This package contains library source intended for building other packages which
use the "optick" feature of the "%{crate}" crate.

%package     -n %{name}+procmacros-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+procmacros-devel

This package contains library source intended for building other packages which
use the "procmacros" feature of the "%{crate}" crate.

%package     -n %{name}+profile-with-optick-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+profile-with-optick-devel

This package contains library source intended for building other packages which
use the "profile-with-optick" feature of the "%{crate}" crate.

%package     -n %{name}+profile-with-puffin-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+profile-with-puffin-devel

This package contains library source intended for building other packages which
use the "profile-with-puffin" feature of the "%{crate}" crate.

%package     -n %{name}+profile-with-superluminal-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+profile-with-superluminal-devel

This package contains library source intended for building other packages which
use the "profile-with-superluminal" feature of the "%{crate}" crate.

%package     -n %{name}+profile-with-tracing-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+profile-with-tracing-devel

This package contains library source intended for building other packages which
use the "profile-with-tracing" feature of the "%{crate}" crate.

%package     -n %{name}+profile-with-tracy-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+profile-with-tracy-devel

This package contains library source intended for building other packages which
use the "profile-with-tracy" feature of the "%{crate}" crate.

%package     -n %{name}+profiling-procmacros-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+profiling-procmacros-devel

This package contains library source intended for building other packages which
use the "profiling-procmacros" feature of the "%{crate}" crate.

%package     -n %{name}+puffin-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+puffin-devel

This package contains library source intended for building other packages which
use the "puffin" feature of the "%{crate}" crate.

%package     -n %{name}+superluminal-perf-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+superluminal-perf-devel

This package contains library source intended for building other packages which
use the "superluminal-perf" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+tracy-client-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+tracy-client-devel

This package contains library source intended for building other packages which
use the "tracy-client" feature of the "%{crate}" crate.

%package     -n %{name}+type-check-devel
Summary:        This crate provides a very thin abstraction over other profiler crates.
BuildArch:      noarch
%description -n %{name}+type-check-devel

This package contains library source intended for building other packages which
use the "type-check" feature of the "%{crate}" crate.

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
%files -n rust-profiling-devel -f %{oreon_filedir}/rust-profiling-devel.list

%changelog

%autochangelog
