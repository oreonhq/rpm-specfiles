%global source0_hash 99e935fc73d54a89fff576526c2ccd42bbf8247aae05b358693475b14fd4ff79
%bcond check 0
%global debug_package %{nil}
%global crate pcap
Name:           rust-pcap
Version:        1.3.0
Release:        1%{?dist}
Summary:        A packet capture API around pcap/wpcap
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pcap
Source0:        https://static.crates.io/crates/pcap/pcap-%{version}.crate
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

%package     -n %{name}+all-features-devel
Summary:        A packet capture API around pcap/wpcap
BuildArch:      noarch
%description -n %{name}+all-features-devel

This package contains library source intended for building other packages which
use the "all-features" feature of the "%{crate}" crate.

%package     -n %{name}+capture-stream-devel
Summary:        A packet capture API around pcap/wpcap
BuildArch:      noarch
%description -n %{name}+capture-stream-devel

This package contains library source intended for building other packages which
use the "capture-stream" feature of the "%{crate}" crate.

%package     -n %{name}+etherparse-devel
Summary:        A packet capture API around pcap/wpcap
BuildArch:      noarch
%description -n %{name}+etherparse-devel

This package contains library source intended for building other packages which
use the "etherparse" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        A packet capture API around pcap/wpcap
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+gat-std-devel
Summary:        A packet capture API around pcap/wpcap
BuildArch:      noarch
%description -n %{name}+gat-std-devel

This package contains library source intended for building other packages which
use the "gat-std" feature of the "%{crate}" crate.

%package     -n %{name}+lending-iter-devel
Summary:        A packet capture API around pcap/wpcap
BuildArch:      noarch
%description -n %{name}+lending-iter-devel

This package contains library source intended for building other packages which
use the "lending-iter" feature of the "%{crate}" crate.

%package     -n %{name}+tap-tests-devel
Summary:        A packet capture API around pcap/wpcap
BuildArch:      noarch
%description -n %{name}+tap-tests-devel

This package contains library source intended for building other packages which
use the "tap-tests" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        A packet capture API around pcap/wpcap
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

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
%files -n rust-pcap-devel -f %{oreon_filedir}/rust-pcap-devel.list

%changelog

%autochangelog
