%global source0_hash b7e8c4821c88b95582ca69234a1d233f87e44182c42e121f740efb0bec1142e0
%bcond check 0
%global debug_package %{nil}
%global crate input-linux
Name:           rust-input-linux
Version:        0.7.1
Release:        1%{?dist}
Summary:        Evdev and uinput
License:        MIT
URL:            https://crates.io/crates/input-linux
Source0:        https://static.crates.io/crates/input-linux/input-linux-%{version}.crate
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
Summary:        Evdev and uinput
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Evdev and uinput
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+codec-devel
Summary:        Evdev and uinput
BuildArch:      noarch
%description -n %{name}+codec-devel

This package contains library source intended for building other packages which
use the "codec" feature of the "%{crate}" crate.

%package     -n %{name}+dox-devel
Summary:        Evdev and uinput
BuildArch:      noarch
%description -n %{name}+dox-devel

This package contains library source intended for building other packages which
use the "dox" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Evdev and uinput
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-0_6-devel
Summary:        Evdev and uinput
BuildArch:      noarch
%description -n %{name}+tokio-util-0_6-devel

This package contains library source intended for building other packages which
use the "tokio-util-0_6" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-util-0_7-devel
Summary:        Evdev and uinput
BuildArch:      noarch
%description -n %{name}+tokio-util-0_7-devel

This package contains library source intended for building other packages which
use the "tokio-util-0_7" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Evdev and uinput
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
%files -n rust-input-linux-devel -f %{oreon_filedir}/rust-input-linux-devel.list

%changelog

%autochangelog
