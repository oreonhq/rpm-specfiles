%global source0_hash 81f2533f3be42fffe3b5e63b71aeca416c1c3bc33e4e27be018521e76b1f38fb
%bcond check 0
%global debug_package %{nil}
%global crate interprocess
Name:           rust-interprocess1
Version:        1.2.1
Release:        1%{?dist}
Summary:        Interprocess communication toolkit
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/interprocess
Source0:        https://static.crates.io/crates/interprocess/interprocess-%{version}.crate
Patch:          interprocess-fix-metadata-auto.diff
Patch:          interprocess-fix-metadata.diff
Patch:          0001-port-from-to_method-To-to-std-convert-TryFrom.patch
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
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+blocking-devel

This package contains library source intended for building other packages which
use the "blocking" feature of the "%{crate}" crate.

%package     -n %{name}+doc_cfg-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+doc_cfg-devel

This package contains library source intended for building other packages which
use the "doc_cfg" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+nonblocking-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+nonblocking-devel

This package contains library source intended for building other packages which
use the "nonblocking" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio_support-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+tokio_support-devel

This package contains library source intended for building other packages which
use the "tokio_support" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} %{SOURCE2} .
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
%files -n rust-interprocess1-devel -f %{oreon_filedir}/rust-interprocess1-devel.list

%changelog

%autochangelog
