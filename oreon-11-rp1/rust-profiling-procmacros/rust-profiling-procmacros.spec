%global source0_hash 4488a4a36b9a4ba6b9334a32a39971f77c1436ec82c38707bce707699cc3bbcb
%bcond check 0
%global debug_package %{nil}
%global crate profiling-procmacros
Name:           rust-profiling-procmacros
Version:        1.0.18
Release:        1%{?dist}
Summary:        This crate provides a very thin abstraction over other profiler crates.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/profiling-procmacros
Source0:        https://static.crates.io/crates/profiling-procmacros/profiling-procmacros-%{version}.crate
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
%files -n rust-profiling-procmacros-devel -f %{oreon_filedir}/rust-profiling-procmacros-devel.list

%changelog

%autochangelog
