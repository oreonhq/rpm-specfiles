%global source0_hash 656b45c05d95a5704399aeef6bd0ddec7b2b3531b7c9e900abbf7c4d2190c925
%bcond check 0
%global debug_package %{nil}
%global crate syntect
Name:           rust-syntect
Version:        5.3.0
Release:        1%{?dist}
Summary:        library for high quality syntax highlighting and code intelligence us...
License:        MIT
URL:            https://crates.io/crates/syntect
Source0:        https://static.crates.io/crates/syntect/syntect-%{version}.crate
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
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bincode-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+bincode-devel

This package contains library source intended for building other packages which
use the "bincode" feature of the "%{crate}" crate.

%package     -n %{name}+default-fancy-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+default-fancy-devel

This package contains library source intended for building other packages which
use the "default-fancy" feature of the "%{crate}" crate.

%package     -n %{name}+default-onig-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+default-onig-devel

This package contains library source intended for building other packages which
use the "default-onig" feature of the "%{crate}" crate.

%package     -n %{name}+default-syntaxes-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+default-syntaxes-devel

This package contains library source intended for building other packages which
use the "default-syntaxes" feature of the "%{crate}" crate.

%package     -n %{name}+default-themes-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+default-themes-devel

This package contains library source intended for building other packages which
use the "default-themes" feature of the "%{crate}" crate.

%package     -n %{name}+dump-create-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+dump-create-devel

This package contains library source intended for building other packages which
use the "dump-create" feature of the "%{crate}" crate.

%package     -n %{name}+dump-load-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+dump-load-devel

This package contains library source intended for building other packages which
use the "dump-load" feature of the "%{crate}" crate.

%package     -n %{name}+fancy-regex-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+fancy-regex-devel

This package contains library source intended for building other packages which
use the "fancy-regex" feature of the "%{crate}" crate.

%package     -n %{name}+flate2-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+flate2-devel

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

%package     -n %{name}+fnv-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+fnv-devel

This package contains library source intended for building other packages which
use the "fnv" feature of the "%{crate}" crate.

%package     -n %{name}+html-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+html-devel

This package contains library source intended for building other packages which
use the "html" feature of the "%{crate}" crate.

%package     -n %{name}+metadata-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+metadata-devel

This package contains library source intended for building other packages which
use the "metadata" feature of the "%{crate}" crate.

%package     -n %{name}+onig-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+onig-devel

This package contains library source intended for building other packages which
use the "onig" feature of the "%{crate}" crate.

%package     -n %{name}+parsing-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+parsing-devel

This package contains library source intended for building other packages which
use the "parsing" feature of the "%{crate}" crate.

%package     -n %{name}+plist-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+plist-devel

This package contains library source intended for building other packages which
use the "plist" feature of the "%{crate}" crate.

%package     -n %{name}+plist-load-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+plist-load-devel

This package contains library source intended for building other packages which
use the "plist-load" feature of the "%{crate}" crate.

%package     -n %{name}+regex-fancy-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+regex-fancy-devel

This package contains library source intended for building other packages which
use the "regex-fancy" feature of the "%{crate}" crate.

%package     -n %{name}+regex-onig-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+regex-onig-devel

This package contains library source intended for building other packages which
use the "regex-onig" feature of the "%{crate}" crate.

%package     -n %{name}+regex-syntax-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+regex-syntax-devel

This package contains library source intended for building other packages which
use the "regex-syntax" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-load-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+yaml-load-devel

This package contains library source intended for building other packages which
use the "yaml-load" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-rust-devel
Summary:        library for high quality syntax highlighting and code intelligence us...
BuildArch:      noarch
%description -n %{name}+yaml-rust-devel

This package contains library source intended for building other packages which
use the "yaml-rust" feature of the "%{crate}" crate.

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
%files -n rust-syntect-devel -f %{oreon_filedir}/rust-syntect-devel.list

%changelog

%autochangelog
