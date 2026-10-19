%global source0_hash 81300c8058a7747013c8f3e27e76eeceb8226621283d30d787b970019d8404f6
%bcond check 0
%global debug_package %{nil}
%global crate lv2
Name:           rust-lv2
Version:        0.6.0
Release:        1%{?dist}
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lv2
Source0:        https://static.crates.io/crates/lv2/lv2-%{version}.crate
ExcludeArch:    ppc64le s390x
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
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+lv2-atom-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+lv2-atom-devel

This package contains library source intended for building other packages which
use the "lv2-atom" feature of the "%{crate}" crate.

%package     -n %{name}+lv2-core-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+lv2-core-devel

This package contains library source intended for building other packages which
use the "lv2-core" feature of the "%{crate}" crate.

%package     -n %{name}+lv2-midi-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+lv2-midi-devel

This package contains library source intended for building other packages which
use the "lv2-midi" feature of the "%{crate}" crate.

%package     -n %{name}+lv2-state-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+lv2-state-devel

This package contains library source intended for building other packages which
use the "lv2-state" feature of the "%{crate}" crate.

%package     -n %{name}+lv2-sys-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+lv2-sys-devel

This package contains library source intended for building other packages which
use the "lv2-sys" feature of the "%{crate}" crate.

%package     -n %{name}+lv2-time-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+lv2-time-devel

This package contains library source intended for building other packages which
use the "lv2-time" feature of the "%{crate}" crate.

%package     -n %{name}+lv2-units-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+lv2-units-devel

This package contains library source intended for building other packages which
use the "lv2-units" feature of the "%{crate}" crate.

%package     -n %{name}+lv2-urid-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+lv2-urid-devel

This package contains library source intended for building other packages which
use the "lv2-urid" feature of the "%{crate}" crate.

%package     -n %{name}+lv2-worker-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+lv2-worker-devel

This package contains library source intended for building other packages which
use the "lv2-worker" feature of the "%{crate}" crate.

%package     -n %{name}+minimal_plugin-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+minimal_plugin-devel

This package contains library source intended for building other packages which
use the "minimal_plugin" feature of the "%{crate}" crate.

%package     -n %{name}+plugin-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+plugin-devel

This package contains library source intended for building other packages which
use the "plugin" feature of the "%{crate}" crate.

%package     -n %{name}+urid-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+urid-devel

This package contains library source intended for building other packages which
use the "urid" feature of the "%{crate}" crate.

%package     -n %{name}+wmidi-devel
Summary:        Safe, fast, and ergonomic framework to create LV2 plugins
BuildArch:      noarch
%description -n %{name}+wmidi-devel

This package contains library source intended for building other packages which
use the "wmidi" feature of the "%{crate}" crate.

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
%files -n rust-lv2-devel -f %{oreon_filedir}/rust-lv2-devel.list

%changelog

%autochangelog
