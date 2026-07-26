%global source0_hash 04427fdb444eace5a54c07a0f981e18416858ef0667d863dec5e6287b648a92a

Name:    oz
Version: 0.18.1
Release: 25%{?dist}
Summary: Library and utilities for automated guest OS installs
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2
URL:     http://github.com/clalancette/oz

# libguestfs is not built on i686
ExcludeArch: %{ix86}

Source0: https://github.com/clalancette/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# All upstream patches to current master
Patch: 0001-Move-oz-examples.1-to-man-page-section-5-instead.patch
Patch: 0002-Enable-USB-controller-and-keyboard-for-aarch64-for-a.patch
Patch: 0003-Revert-Don-t-write-kickstart-so-initial-setup-won-t-.patch
Patch: 0004-Don-t-abort-when-the-data-in-_wait_for_install_finis.patch
Patch: 0005-Fix-for-running-on-python3-and-building-on-EL8-or-hi.patch
Patch: 0006-Fix-RHEL-templates-to-pass-required-useuefi-paramete.patch
Patch: 0007-Use-discard-unmap-for-images.patch
Patch: 0008-Don-t-write-kickstart-so-initial-setup-won-t-think-r.patch
Patch: 0009-Wait-for-boot-even-in-case-of-missing-IP.patch
Patch: 0010-Python-3-compat-fixes-py.test-and-ConfigParser.patch
Patch: 0011-Unpick-unnecessary-useuefi-arg-on-the-Guest-classes.patch
Patch: 0012-Python-compat-Callable-is-in-collections.abc-since-P.patch
Patch: 0013-Tests-multiple-fixes-to-expected-guest-XML.patch
Patch: 0014-Add-testing-instructions-to-README.patch
Patch: 0015-Add-monotonic-to-requirements.patch
Patch: 0016-Update-oz.spec.in-to-match-current-Fedora.patch
Patch: 0017-tests-handle-libvirt_type-not-being-kvm.patch
Patch: 0018-tests-handle-guest-image-path-being-the-system-one.patch
Patch: 0019-Update-pylint-and-flake8-commands-in-Makefile.patch
Patch: 0020-Add-ability-to-run-the-unit-tests-in-Fedora-and-EL7-.patch
Patch: 0021-Add-a-Github-Action-workflow-to-run-CI-checks.patch
Patch: 0022-Allow-image-size-specification-using-any-SI-or-IEC-u.patch
Patch: 0023-Replace-M2Crypto-with-cryptography.patch
Patch: 0024-CI-use-sudo-assume-docker-present-use-diff-quality-c.patch
Patch: 0025-CI-convert-EL-7-test-to-an-EL-8-test-using-Alma.patch

# https://github.com/clalancette/oz/pull/312
# Fix tests in mock environment
Patch: 0026-tests-mock-network-functions-so-tests-work-with-no-n.patch

# https://github.com/clalancette/oz/pull/316
# Rename a man page (missed in 0001-Move-oz-examples.1-to-man-page-section-5-instead.patch )
Patch: 0001-Really-rename-oz-examples.1-to-oz-examples.5.patch

# https://github.com/clalancette/oz/pull/318
# Avoid monotonic dependency
Patch: 0001-Switch-to-time.monotonic.patch

# Enable RISC-V arch
Patch: 0027-Enable-riscv64-arch.patch

BuildArch: noarch

BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# test dependencies
BuildRequires: python3-requests
BuildRequires: python3-cryptography
BuildRequires: python3-libvirt
BuildRequires: python3-lxml
BuildRequires: python3-libguestfs
BuildRequires: python3-pytest
BuildRequires: libvirt-daemon
BuildRequires: libvirt-daemon-kvm
BuildRequires: libvirt-daemon-qemu
BuildRequires: libvirt-daemon-config-network
BuildRequires: python3-pytest
Requires: python3
Requires: python3-lxml
Requires: python3-libguestfs >= 1.18
Requires: python3-libvirt
Requires: python3-cryptography
Requires: python3-requests
# in theory, oz doesn't really require libvirtd to be local to operate
# properly.  However, because of the libguestfs manipulations, in practice
# it really does.  Make it depend on libvirt (so we get libvirtd) for now,
# unless/until we are able to make it really be remote.
Requires: libvirt-daemon-kvm
Requires: libvirt-daemon-qemu
Requires: libvirt-daemon-config-network
Requires: genisoimage
Requires: mtools
Requires: openssh-clients

%description
Oz is a set of libraries and utilities for doing automated guest OS
installations, with minimal input from the user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%py3_build

%install
%py3_install

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/isocontent/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/isos/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/floppycontent/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/floppies/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/icicletmp/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/jeos/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/kernels/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/screenshots/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/oz
cp oz.cfg $RPM_BUILD_ROOT%{_sysconfdir}/oz

%post
if [ ! -f %{_sysconfdir}/oz/id_rsa-icicle-gen ]; then
   ssh-keygen -t rsa -b 2048 -N "" -f %{_sysconfdir}/oz/id_rsa-icicle-gen >& /dev/null
fi

%check
libvirtd -d
%pytest tests/

%files
%license COPYING
%doc README examples
%dir %attr(0755, root, root) %{_sysconfdir}/oz/
%config(noreplace) %{_sysconfdir}/oz/oz.cfg
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/isocontent/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/isos/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/floppycontent/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/floppies/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/icicletmp/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/jeos/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/kernels/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/screenshots/
%{_bindir}/oz-install
%{_bindir}/oz-generate-icicle
%{_bindir}/oz-customize
%{_bindir}/oz-cleanup-cache
%{_mandir}/man1/*
%{_mandir}/man5/*
%{python3_sitelib}/oz
%{python3_sitelib}/%{name}*.egg-info

%changelog
%autochangelog
