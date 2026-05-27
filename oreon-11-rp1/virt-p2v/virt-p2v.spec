%global source0_hash 20ff7bec5ed630ae1928da026e6e6e471e8eb1869222762fd9ab4681975b98c5

# Verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# So far there are no ELF binaries in this package, so the list
# of files in the debuginfo package will be empty, triggering
# an RPM failure.
%global debug_package %{nil}

Summary:       Convert a physical machine to run on KVM
Name:          virt-p2v
Epoch:         1
Version:       1.42.4
Release:       4%{?dist}
License:       GPL-2.0-or-later AND LGPL-2.0-or-later

# virt-p2v works only on x86_64 at the moment.  It requires porting
# to properly detect the hardware on other architectures, and furthermore
# virt-v2v requires porting too.
ExclusiveArch: x86_64

# Source and patches.
URL:           http://libguestfs.org/
Source0:       http://download.libguestfs.org/%{name}/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:       http://download.libguestfs.org/%{name}/%{name}-%{version}.tar.gz.sig
%endif

# Keyring used to verify tarball signature.
%if 0%{verify_tarball_signature}
Source2:       libguestfs.keyring
%endif

# Basic build requirements.
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Pod::Man)
BuildRequires: perl(List::MoreUtils)
BuildRequires: /usr/bin/pod2text
BuildRequires: libxml2-devel
BuildRequires: pcre2-devel
BuildRequires: bash-completion-devel
BuildRequires: xz
BuildRequires: gtk3-devel
BuildRequires: dbus-devel
BuildRequires: m4
%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

# Test suite requirements.
BuildRequires: nbdkit

Requires:      gawk
Requires:      gzip

# virt-p2v-make-disk runs virt-builder:
Requires:      guestfs-tools

# virt-p2v-make-kickstart runs strip:
Requires:      binutils


%description
Virt-p2v converts (virtualizes) physical machines so they can be run
as virtual machines under KVM.

This package contains the tools needed to make a virt-p2v boot CD or
USB key which is booted on the physical machine to perform the
conversion.  You also need virt-v2v installed somewhere else to
complete the conversion.

To convert virtual machines from other hypervisors, see virt-v2v.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1


%build
%configure \
  --with-extra="fedora=%{fedora},release=%{release}"

%make_build


%check
if ! make check; then
    cat test-suite.log
    exit 1
fi


%install
%make_install

# Delete the development man pages.
rm $RPM_BUILD_ROOT%{_mandir}/man1/p2v-building.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/p2v-hacking.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/p2v-release-notes.1*


%files
%doc README
%license COPYING
%{_bindir}/virt-p2v-make-disk
%{_bindir}/virt-p2v-make-kickstart
%{_bindir}/virt-p2v-make-kiwi
%{bash_completions_dir}/virt-*
%{_datadir}/virt-p2v
%{_libdir}/virt-p2v
%{_mandir}/man1/virt-p2v-make-disk.1*
%{_mandir}/man1/virt-p2v-make-kickstart.1*
%{_mandir}/man1/virt-p2v-make-kiwi.1*
%{_mandir}/man1/virt-p2v.1*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.42.4-4
- Import
