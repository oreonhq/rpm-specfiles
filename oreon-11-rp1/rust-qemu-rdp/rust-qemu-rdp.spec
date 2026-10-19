%global source0_hash 7e822e7e5003c67d3705b587caf66d7934b6d5fdf6eda1bc1be3acf149f69752
%bcond check 1
%global crate qemu-rdp
Name:           rust-qemu-rdp
Version:        0.1.1
Release:        1%{?dist}
Summary:        Org.qemu.Display1 RDP server
License:        MIT
URL:            https://crates.io/crates/qemu-rdp
Source0:        https://static.crates.io/crates/qemu-rdp/qemu-rdp-%{version}.crate
Patch:          qemu-rdp-fix-metadata.diff
Patch2:         https://gitlab.com/marcandre.lureau/qemu-display/-/commit/b81e4478eab3ff943899140892a8ecd9fe380e4e.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Org.qemu.Display1 RDP server
License:        # FIXME
%description -n %{crate}

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n qemu-rdp -f %{oreon_filedir}/qemu-rdp.list

%changelog

%autochangelog
