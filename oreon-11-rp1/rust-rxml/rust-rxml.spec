%global source0_hash a98f186c7a2f3abbffb802984b7f1dfd65dac8be1aafdaabbca4137f53f0dff7
%bcond check 0
%global debug_package %{nil}
%global crate rxml
Name:           rust-rxml
Version:        0.9.1
Release:        1%{?dist}
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
License:        MIT
URL:            https://crates.io/crates/rxml
Source0:        https://static.crates.io/crates/rxml/rxml-%{version}.crate
Patch:          rxml-fix-metadata.diff
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
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+mt-devel
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+mt-devel

This package contains library source intended for building other packages which
use the "mt" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-lite-devel
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+pin-project-lite-devel

This package contains library source intended for building other packages which
use the "pin-project-lite" feature of the "%{crate}" crate.

%package     -n %{name}+rxml_proc-devel
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+rxml_proc-devel

This package contains library source intended for building other packages which
use the "rxml_proc" feature of the "%{crate}" crate.

%package     -n %{name}+shared_ns-devel
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+shared_ns-devel

This package contains library source intended for building other packages which
use the "shared_ns" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+weak-table-devel
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features
BuildArch:      noarch
%description -n %{name}+weak-table-devel

This package contains library source intended for building other packages which
use the "weak-table" feature of the "%{crate}" crate.

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
%files -n rust-rxml-devel -f %{oreon_filedir}/rust-rxml-devel.list

%changelog

%autochangelog
