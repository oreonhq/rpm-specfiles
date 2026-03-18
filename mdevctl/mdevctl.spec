%bcond_without check

%global crate mdevctl

Name:           mdevctl
Version:        1.4.0
Release:        4%{?dist}
Summary:        A mediated device management utility for Linux

License:        LGPL-2.1-only
URL:            https://crates.io/crates/mdevctl
Source:         %{crates_source}
Source1:        https://github.com/mdevctl/mdevctl/releases/download/v%{version}/mdevctl-%{version}-vendor.tar.gz

# Patches >=1000 are only applied when using system Rust dependencies:
# - Update nix dev-dependency to 0.31
#   https://github.com/mdevctl/mdevctl/pull/132
Patch1000:      mdevctl-fix-metadata.diff

BuildRequires: make systemd python3-docutils
BuildRequires: sed
%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  rust-packaging >= 21
%endif
Requires(post,postun): %{_sbindir}/udevadm

%description
mdevctl is a utility for managing and persisting devices in the
mediated device device framework of the Linux kernel.  Mediated
devices are sub-devices of a parent device (ex. a vGPU) which
can be dynamically created and potentially used by drivers like
vfio-mdev for assignment to virtual machines.

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1 %{?rhel:-a1 -N}
sed  -e 's/SBINDIR=/SBINDIR\?=/' -i Makefile.in
%if 0%{?rhel}
%autopatch -p1 -M999
%cargo_prep -v vendor
%else
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
%endif

%build
%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?rhel}
%cargo_vendor_manifest
%endif

%install
%make_install SBINDIR=%{_sbindir}

%if %{with check}
%check
%cargo_test
%endif

%files
%license COPYING
%license LICENSE.dependencies
%if 0%{?rhel}
%license cargo-vendor.txt
%endif
%doc README.md
%{_sbindir}/mdevctl
%{_sbindir}/lsmdev
%{_udevrulesdir}/60-mdevctl.rules
%dir %{_sysconfdir}/mdevctl.d
%dir %{_prefix}/lib/mdevctl/
%dir %{_prefix}/lib/mdevctl/scripts.d/
%dir %{_prefix}/lib/mdevctl/scripts.d/callouts
%dir %{_prefix}/lib/mdevctl/scripts.d/notifiers
%{_mandir}/man8/mdevctl.8*
%{_mandir}/man8/lsmdev.8*
%{_datadir}/bash-completion/completions/mdevctl
%{_datadir}/bash-completion/completions/lsmdev

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.0-4
- Prepare for Oreon 11 (RP1)
