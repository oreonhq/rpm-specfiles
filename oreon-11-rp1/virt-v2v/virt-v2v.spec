%global source0_hash none

%global source2_key_fpr F7774FB1AD074A7E8C8767EA91738F73E1B768A0

# If we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# The source directory.
%global source_directory 2.11-development

%if !0%{?rhel}
# Optional features enabled in this build for Fedora.
%global with_block_driver     1
%global with_glance           1
%global with_ovirt            1
%global with_xen              1

# libguestfs hasn't been built on i686 for a while since there is no
# kernel built for this architecture any longer and libguestfs rather
# fundamentally depends on the kernel.  Therefore we must exclude this
# arch.  Note there is no bug filed for this because we do not ever
# expect that libguestfs or virt-v2v will be available on i686 so
# there is nothing that needs fixing.
ExcludeArch:   %{ix86}

# Version extra string for Fedora.
%global version_extra         fedora=%{fedora},release=%{release}

%else

# Optional features enabled in this build for RHEL.
%global with_block_driver     0
%global with_glance           0
%global with_ovirt            0
%global with_xen              0

# Architectures where virt-v2v is shipped on RHEL:
#
# not on aarch64 because it is not useful there
# not on %%{power64} because of RHBZ#1287826
# not on s390x because it is not useful there
ExclusiveArch: x86_64

# Version extra string for RHEL.
%global version_extra         rhel=%{rhel},release=%{release}

%endif

Name:          virt-v2v
Epoch:         1
Version:       2.11.3
Release:       2%{?dist}
Summary:       Convert a virtual machine to run on KVM

License:       GPL-2.0-or-later AND LGPL-2.0-or-later
URL:           https://github.com/libguestfs/virt-v2v

Source0:        http://download.libguestfs.org/virt-v2v/%{source_directory}/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:        http://download.libguestfs.org/virt-v2v/%{source_directory}/%{name}-%{version}.tar.gz.sig
# Keyring used to verify tarball signature.
Source2:       libguestfs.keyring
%endif

# Maintainer script which helps with handling patches.
Source3:       copy-patches.sh

BuildRequires: autoconf, automake, libtool
BuildRequires: make
BuildRequires: /usr/bin/pod2man
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IPC::Run3)
BuildRequires: gcc
BuildRequires: ocaml >= 4.08

BuildRequires: libguestfs-devel >= 1:1.59.2-1
BuildRequires: augeas-devel
BuildRequires: bash-completion
%if 0%{?fedora} || 0%{?rhel} >= 11
BuildRequires: bash-completion-devel
%endif
BuildRequires: file
BuildRequires: gettext-devel
BuildRequires: json-c-devel
BuildRequires: libnbd-devel >= 1.24
BuildRequires: libosinfo-devel
BuildRequires: libvirt-daemon-kvm
BuildRequires: libvirt-devel
BuildRequires: libxcrypt-devel
BuildRequires: libxml2-devel
BuildRequires: pcre2-devel
BuildRequires: perl(Sys::Guestfs)
BuildRequires: po4a
BuildRequires: /usr/bin/virsh
BuildRequires: xorriso

BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-libguestfs-devel
BuildRequires: ocaml-libvirt-devel
BuildRequires: ocaml-libnbd-devel
BuildRequires: ocaml-fileutils-devel
BuildRequires: ocaml-gettext-devel

# These are for running our limited test.
BuildRequires: glibc-utils
BuildRequires: %{_bindir}/qemu-nbd
BuildRequires: %{_bindir}/nbdcopy
BuildRequires: %{_bindir}/nbdinfo
BuildRequires: nbdkit-server >= 1.46.1
BuildRequires: nbdkit-file-plugin
BuildRequires: nbdkit-null-plugin
BuildRequires: nbdkit-cow-filter
BuildRequires: mingw-srvany-redistributable >= 1.1-6
%ifarch x86_64
BuildRequires: glibc-static
%endif

%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

Requires:      libguestfs%{?_isa} >= 1:1.59.2-1
Requires:      guestfs-tools >= 1.54

# XFS is the default filesystem in Fedora and RHEL.
Requires:      libguestfs-xfs

%if 0%{?rhel} && ! 0%{?eln}
# For Windows conversions on RHEL.
Requires:      libguestfs-winsupport >= 7.2
%endif

Requires:      curl
Requires:      gawk
Requires:      gzip
Requires:      openssh-clients >= 8.8p1
Requires:      %{_bindir}/openssl
Requires:      unzip
Requires:      %{_bindir}/virsh

# Ensure the UEFI firmware is available, to properly convert
# EFI guests (RHBZ#1429643).
%ifarch x86_64
Requires:      edk2-ovmf
%endif
%ifarch aarch64
Requires:      edk2-aarch64
%endif

%if !%{with_ovirt}
Requires:      /usr/bin/python3
%endif
Requires:      libnbd >= 1.24
Requires:      %{_bindir}/qemu-nbd
Requires:      %{_bindir}/nbdcopy
Requires:      %{_bindir}/nbdinfo
Requires:      nbdkit-server >= 1.46.1
Requires:      nbdkit-curl-plugin
Requires:      nbdkit-file-plugin
Requires:      nbdkit-nbd-plugin
Requires:      nbdkit-null-plugin
%if !%{with_ovirt}
Requires:      nbdkit-python-plugin
%endif
Requires:      nbdkit-ssh-plugin
%ifarch x86_64
Requires:      nbdkit-vddk-plugin
%endif
Requires:      nbdkit-blocksize-filter
Requires:      nbdkit-count-filter
Requires:      nbdkit-cow-filter
Requires:      nbdkit-multi-conn-filter
Requires:      nbdkit-rate-filter
Requires:      nbdkit-retry-filter

# For rhsrvany.exe, used to install firstboot scripts in Windows guests.
Requires:      mingw-srvany-redistributable >= 1.1-6

# On RHEL, virtio-win should be used to install virtio drivers
# and qemu-ga in converted guests.  (RHBZ#1972644)
%if 0%{?rhel}
Recommends:    virtio-win
%endif


%description
Virt-v2v converts a single guest from a foreign hypervisor to run on
KVM.  It can read Linux and Windows guests running on VMware, Xen,
Hyper-V and some other hypervisors, and convert them to KVM managed by
libvirt, OpenStack, oVirt, Red Hat Virtualisation (RHV) or several
other targets.  It can modify the guest to make it bootable on KVM and
install virtio drivers so it will run quickly.


%package bash-completion
Summary:       Bash tab-completion for %{name}
BuildArch:     noarch
Requires:      bash-completion >= 2.0
Requires:      %{name} = %{epoch}:%{version}-%{release}


%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.


%package man-pages-ja
Summary:       Japanese (ja) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description man-pages-ja
%{name}-man-pages-ja contains Japanese (ja) man pages
for %{name}.


%package man-pages-uk
Summary:       Ukrainian (uk) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description man-pages-uk
%{name}-man-pages-uk contains Ukrainian (uk) man pages
for %{name}.


%prep
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1

# ACLOCAL_PATH is temporarily required to work around
# https://bugzilla.redhat.com/show_bug.cgi?id=2366708
export ACLOCAL_PATH=/usr/share/gettext/m4/
autoreconf -fiv


%build
%configure \
%if %{with_block_driver}
  --enable-block-driver \
%else
  --disable-block-driver \
%endif
%if %{with_glance}
  --enable-glance \
%else
  --disable-glance \
%endif
%if %{with_ovirt}
  --enable-ovirt \
%else
  --disable-ovirt \
%endif
%if %{with_xen}
  --enable-xen \
%else
  --disable-xen \
%endif
  --with-extra="%{version_extra}"

make V=1 %{?_smp_mflags}


%install
%make_install

# Delete libtool crap.
find $RPM_BUILD_ROOT -name '*.la' -delete

%if 0%{?rhel}
# On RHEL move virt-v2v-in-place to libexec since it is not supported,
# and remove the documentation.
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mv $RPM_BUILD_ROOT%{_bindir}/virt-v2v-in-place $RPM_BUILD_ROOT%{_libexecdir}/
rm $RPM_BUILD_ROOT%{_mandir}/man1/virt-v2v-in-place.1*
%endif

# Find locale files.
%find_lang %{name}


%check
# Check that the binary runs and the features match those configured.
./run virt-v2v --version
./run virt-v2v --machine-readable | tee machine-readable.out
grep "virt-v2v-2.0" machine-readable.out
grep "input:disk" machine-readable.out
%if %{with_block_driver}
grep "block-driver-option" machine-readable.out
%endif
%if %{with_glance}
grep "output:glance" machine-readable.out
%endif
%if %{with_ovirt}
grep "output:ovirt$" machine-readable.out
grep "output:ovirt-upload" machine-readable.out
grep "output:vdsm" machine-readable.out
%endif

%ifarch x86_64
# Only run the tests with non-debug (ie. non-Rawhide) kernels.
# XXX This tests for any debug kernel installed.
if grep CONFIG_DEBUG_MUTEXES=y /lib/modules/*/config ; then
    echo "Skipping tests because debug kernel is installed"
    exit 0
fi

# Make sure we can see the debug messages (RHBZ#1230160).
export LIBGUESTFS_DEBUG=1
export LIBGUESTFS_TRACE=1

# The built in tests take a very long time to run under TCG (in Koji),
# so just perform a very simple conversion to check things are
# working.
for f in windows.img fedora.img; do
    make -C test-data/phony-guests $f
    if test -s test-data/phony-guests/$f; then
        ./run virt-v2v -v -x -i disk test-data/phony-guests/$f -o null
    fi
done
%endif


%files -f %{name}.lang
%license COPYING
%doc README
%{_bindir}/virt-v2v
%if !0%{?rhel}
%{_bindir}/virt-v2v-in-place
%else
%{_libexecdir}/virt-v2v-in-place
%endif
%{_bindir}/virt-v2v-inspector
%{_bindir}/virt-v2v-open
%{_mandir}/man1/virt-v2v.1*
%{_mandir}/man1/virt-v2v-hacking.1*
%{_mandir}/man1/virt-v2v-input-vmware.1*
%if %{with_xen}
%{_mandir}/man1/virt-v2v-input-xen.1*
%endif
%if !0%{?rhel}
%{_mandir}/man1/virt-v2v-in-place.1*
%endif
%{_mandir}/man1/virt-v2v-inspector.1*
%{_mandir}/man1/virt-v2v-open.1*
%{_mandir}/man1/virt-v2v-output-local.1*
%{_mandir}/man1/virt-v2v-output-openstack.1*
%if %{with_ovirt}
%{_mandir}/man1/virt-v2v-output-ovirt.1*
%endif
%{_mandir}/man1/virt-v2v-release-notes-1.42.1*
%{_mandir}/man1/virt-v2v-release-notes-2.*.1*
%{_mandir}/man1/virt-v2v-support.1*


%files bash-completion
%license COPYING
%{bash_completions_dir}/virt-v2v


%files man-pages-ja
%license COPYING
%lang(ja) %{_mandir}/ja/man1/*.1*


%files man-pages-uk
%license COPYING
%lang(uk) %{_mandir}/uk/man1/*.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.11.3-2
- Prepare for Oreon 11 (RP1)
