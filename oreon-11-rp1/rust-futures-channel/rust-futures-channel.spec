%global source0_hash b1f9e3d69d39e4862ffed03ed071a76f9a13ba1d9109d355b0f0aa6b15e393c4
%bcond check 0
%global debug_package %{nil}
%global crate futures-channel
Name:           rust-futures-channel
Version:        0.3.34
Release:        1%{?dist}
Summary:        Channels for asynchronous communication using futures-rs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/futures-channel
Source0:        https://static.crates.io/crates/futures-channel/futures-channel-%{version}.crate
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
Summary:        Channels for asynchronous communication using futures-rs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Channels for asynchronous communication using futures-rs
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+cfg-target-has-atomic-devel
Summary:        Channels for asynchronous communication using futures-rs
BuildArch:      noarch
%description -n %{name}+cfg-target-has-atomic-devel

This package contains library source intended for building other packages which
use the "cfg-target-has-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+futures-sink-devel
Summary:        Channels for asynchronous communication using futures-rs
BuildArch:      noarch
%description -n %{name}+futures-sink-devel

This package contains library source intended for building other packages which
use the "futures-sink" feature of the "%{crate}" crate.

%package     -n %{name}+sink-devel
Summary:        Channels for asynchronous communication using futures-rs
BuildArch:      noarch
%description -n %{name}+sink-devel

This package contains library source intended for building other packages which
use the "sink" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Channels for asynchronous communication using futures-rs
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Channels for asynchronous communication using futures-rs
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-futures-channel-devel -f %{oreon_filedir}/rust-futures-channel-devel.list

%changelog

%autochangelog
