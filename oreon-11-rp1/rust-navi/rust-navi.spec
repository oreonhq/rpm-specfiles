%global source0_hash b6cdb5ef0dcae99730ce3692e7f5bc2c93d0a35381ffd5b90986dbd69d34cc79
%bcond check 1
%global crate navi
Name:           rust-navi
Version:        2.20.1
Release:        1%{?dist}
Summary:        Interactive cheatsheet tool for the command-line
License:        Apache-2.0
URL:            https://crates.io/crates/navi
Source0:        https://static.crates.io/crates/navi/navi-%{version}.crate
Patch:          navi-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Interactive cheatsheet tool for the command-line
License:        Apache-2.0 AND CC0-1.0 AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
Requires:       fzf
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Interactive cheatsheet tool for the command-line
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+disable-command-execution-devel
Summary:        Interactive cheatsheet tool for the command-line
BuildArch:      noarch
%description -n %{name}+disable-command-execution-devel

This package contains library source intended for building other packages which
use the "disable-command-execution" feature of the "%{crate}" crate.

%package     -n %{name}+disable-repo-management-devel
Summary:        Interactive cheatsheet tool for the command-line
BuildArch:      noarch
%description -n %{name}+disable-repo-management-devel

This package contains library source intended for building other packages which
use the "disable-repo-management" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n navi -f %{oreon_filedir}/navi.list
%files -n rust-navi-devel -f %{oreon_filedir}/rust-navi-devel.list

%changelog

%autochangelog
