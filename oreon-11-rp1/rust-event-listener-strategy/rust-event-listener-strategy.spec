%global source0_hash 8be9f3dfaaffdae2972880079a491a1a8bb7cbed0b8dd7a347f668b4150a3b93
%bcond check 0
%global debug_package %{nil}
%global crate event-listener-strategy
Name:           rust-event-listener-strategy
Version:        0.5.4
Release:        1%{?dist}
Summary:        Block or poll on event_listener easily
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/event-listener-strategy
Source0:        https://static.crates.io/crates/event-listener-strategy/event-listener-strategy-%{version}.crate
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
Summary:        Block or poll on event_listener easily
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+loom-devel
Summary:        Block or poll on event_listener easily
BuildArch:      noarch
%description -n %{name}+loom-devel

This package contains library source intended for building other packages which
use the "loom" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-devel
Summary:        Block or poll on event_listener easily
BuildArch:      noarch
%description -n %{name}+portable-atomic-devel

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Block or poll on event_listener easily
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-event-listener-strategy-devel -f %{oreon_filedir}/rust-event-listener-strategy-devel.list

%changelog

%autochangelog
