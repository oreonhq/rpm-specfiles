%global source0_hash bb085f1e127ddd6219092fbcdfdfde5df223d57517999bf92e672d7404ff6776
%bcond_without check
%global crate mdevctl
Name:           mdevctl
Version:        1.4.0
Release:        4%{?dist}
Summary:        A mediated device management utility for Linux
License:        LGPL-2.1-only
URL:            https://crates.io/crates/mdevctl
Source0:        https://static.crates.io/crates/mdevctl/mdevctl-%{version}.crate
Patch1000:      mdevctl-fix-metadata.diff
Requires(post,postun): %{_sbindir}/udevadm
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  make
BuildRequires:  python3-docutils
BuildRequires:  rustc
BuildRequires:  sed
BuildRequires:  systemd
# /oreon:deps
%description
mdevctl is a utility for managing and persisting devices in the
mediated device device framework of the Linux kernel.  Mediated
devices are sub-devices of a parent device (ex. a vGPU) which
can be dynamically created and potentially used by drivers like
vfio-mdev for assignment to virtual machines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version_no_tilde} -p1
sed  -e 's/SBINDIR=/SBINDIR\?=/' -i Makefile.in
%oreon_vendor_cargo
%build

%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%install
%make_install SBINDIR=%{_sbindir}
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.0-4
- Prepare for Oreon 11 (RP1)
