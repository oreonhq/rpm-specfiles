%global source0_hash 77a5ccb89ead03645e387c4ec90a4058bc152b78065004c4db533bddbeb73d3b

# Disable mangling shebangs for dracut module files as it breaks initramfs
%global __brp_mangle_shebangs_exclude_from ^%{_prefix}/lib/dracut/modules.d/.*$

%global desc \
The KIWI Image System provides an operating system image builder \
for Linux supported hardware platforms as well as for virtualization \
and cloud systems like Xen, KVM, VMware, EC2 and more.

%if 0%{?rhel} && 0%{?rhel} < 10
%bcond check 0
%else
%bcond check 1
%endif

Name:           kiwi
Version:        10.3.0
Release:        1%{?dist}
URL:            http://osinside.github.io/kiwi/
Summary:        Flexible operating system image builder
License:        GPL-3.0-or-later
# We must use the version uploaded to pypi, as it contains all the required files.
Source0:        https://files.pythonhosted.org/packages/source/k/%{name}/%{name}-%{version}.tar.gz
# qemu-img dependency is not available
ExcludeArch:    %{ix86}

# Backports from upstream

# Proposed upstream

# Fedora-specific patches
## Use buildah instead of umoci by default for OCI image builds
## TODO: Consider getting umoci into Fedora?
Patch1001:      1001-Use-buildah-by-default-for-OCI-image-builds.patch
## Use isomd5sum instead of checkmedia by default for tagging ISO files
## TODO: Consider getting checkmedia into Fedora?
Patch1002:      1002-Use-isomd5sum-by-default-for-tagging-ISO-files.patch

BuildRequires:  bash-completion
BuildRequires:  dracut
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  shadow-utils
# doc build requirements
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%if %{with check}
# for tests
BuildRequires:  python3dist(pytest) >= 7
%if 0%{?fedora}
BuildRequires:  python3dist(pytest-xdist)
%endif
%endif

%description %{desc}

%package systemdeps-core
Summary:        KIWI - Core host system dependencies
Provides:       kiwi-image-tbz-requires = %{version}-%{release}
Obsoletes:      kiwi-image-tbz-requires < %{version}-%{release}
Provides:       kiwi-image:tbz
# tools used by kiwi
# For building Fedora, RHEL/CentOS, and Mageia based images
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 11
Requires:       dnf5
Provides:       kiwi-packagemanager:dnf5
%endif
%if 0%{?fedora} || (0%{?rhel} >= 8 && 0%{?rhel} < 11)
%if 0%{?rhel}
# Backward compatibility for OBS
Requires:       dnf
%endif
Requires:       dnf4
Provides:       kiwi-packagemanager:dnf
Provides:       kiwi-packagemanager:dnf4
Provides:       kiwi-packagemanager:yum
%endif
%if (0%{?rhel} >= 8 && 0%{?rhel} < 11)
# For building Fedora, RHEL/CentOS, and Mageia based minimal images
Requires:       microdnf
Provides:       kiwi-packagemanager:microdnf
%endif
# Offers GPG public keys for various RPM distros and third party repositories
Recommends:     distribution-gpg-keys
%if 0%{?fedora} || 0%{?rhel} >= 8
# For building Debian/Ubuntu based images
Recommends:     apt
Recommends:     dpkg
Recommends:     gnupg2
# Keyrings for bootstrap
Recommends:     debian-keyring
Recommends:     ubu-keyring
%endif
%if 0%{?fedora}
# For building Arch based images
Recommends:     pacman
Recommends:     archlinux-keyring
%endif
Requires:       file
Requires:       lsof
Requires:       mtools
Requires:       rsync
Requires:       sed
Requires:       screen
Requires:       tar >= 1.2.7
Requires:       openssl
Requires:       xz
# Python 2 module is no longer available
Obsoletes:      python2-%{name} < %{version}-%{release}
# legacy kiwi initramfs tools are no longer available
Obsoletes:      %{name}-tools < %{version}-%{release}

%description systemdeps-core
This metapackage installs the necessary system dependencies
to run KIWI.

%if 0%{?fedora}
%package systemdeps-pkgmgr-zypper
Summary:        KIWI - Zypper package manager support
# For building (open)SUSE based images
Requires:       zypper
Provides:       kiwi-packagemanager:zypper
Requires:       %{name}-systemdeps-core = %{version}-%{release}

%description systemdeps-pkgmgr-zypper
This metapackage exposes support for Zypper as a package
manager for image builds in KIWI.
%endif

%ifnarch ppc64 %{ix86}
%package systemdeps-containers
Summary:        KIWI - host requirements for container images
Provides:       kiwi-image:docker
Provides:       kiwi-image:oci
Provides:       kiwi-image:appx
Provides:       kiwi-image:wsl
Provides:       kiwi-image-docker-requires = %{version}-%{release}
Obsoletes:      kiwi-image-docker-requires < %{version}-%{release}
Provides:       kiwi-image-wsl-requires = %{version}-%{release}
Obsoletes:      kiwi-image-wsl-requires < %{version}-%{release}
Requires:       buildah
Requires:       skopeo
Requires:       appx-util

%description systemdeps-containers
Host setup helper to pull in all packages required/useful on
the build host to build container images e.g docker, wsl.
%endif

%if 0%{?fedora}
%package systemdeps-enclaves
Summary:        KIWI - host requirements for enclave images
Provides:       kiwi-image:enclave
Requires:       eif_build

%description systemdeps-enclaves
Host setup helper to pull in all packages required/useful on
the build host to build secure enclave images (e.g. AWS Nitro).
%endif

%package systemdeps-iso-media
Summary:        KIWI - host requirements for live and install iso images
Provides:       kiwi-image:iso
Provides:       kiwi-image-iso-requires = %{version}-%{release}
Obsoletes:      kiwi-image-iso-requires < %{version}-%{release}
Requires:       xorriso
Requires:       isomd5sum
%ifarch %{ix86} x86_64
# Pull in syslinux when it's x86
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       syslinux-nonlinux
%endif
Requires:       syslinux
%endif
%ifarch x86_64
Requires:       grub2-efi-x64-cdboot
%if ! 0%{?rhel}
Requires:       grub2-efi-ia32-cdboot
%endif
%endif
%ifarch aarch64
Requires:       grub2-efi-aa64-cdboot
%endif
%if ! 0%{?rhel}
%ifarch %{arm}
Requires:       grub2-efi-arm-cdboot
%endif
%endif
Requires:       kiwi-systemdeps-core = %{version}-%{release}
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-bootloaders = %{version}-%{release}

%description systemdeps-iso-media
Host setup helper to pull in all packages required/useful on
the build host to build live and install iso images.

%package systemdeps-bootloaders
Summary:        KIWI - host requirements for configuring bootloaders
%if ! 0%{?rhel}
%ifarch %{arm} aarch64
Requires:       uboot-tools
%endif
%endif
%ifnarch s390 s390x
# grub isn't available on s390(x) systems
Requires:       grub2-tools
Requires:       grub2-tools-extra
Requires:       grub2-tools-minimal
%endif
%ifarch x86_64
Requires:       grub2-tools-efi
%endif
%ifarch x86_64
Requires:       grub2-efi-x64
Requires:       grub2-efi-x64-modules
%if ! 0%{?rhel}
Requires:       grub2-efi-ia32
Requires:       grub2-efi-ia32-modules
%endif
%endif
%ifarch %{ix86} x86_64
Requires:       grub2-pc
Requires:       grub2-pc-modules
%endif
%ifarch aarch64
Requires:       grub2-efi-aa64-modules
%endif
%if ! 0%{?rhel}
# grub-efi for armv7hl is not available in RHEL
%ifarch %{arm}
Requires:       grub2-efi-arm
Requires:       grub2-efi-arm-modules
%endif
%endif
%ifarch s390 s390x
Requires:       s390utils
%endif
Requires:       kiwi-systemdeps-core = %{version}-%{release}

%description systemdeps-bootloaders
Host setup helper to pull in all packages required/useful on
the build host for configuring bootloaders on images.

%package systemdeps-filesystems
Summary:        KIWI - host requirements for filesystems
Provides:       kiwi-image:pxe
Provides:       kiwi-image:kis
Provides:       kiwi-image:erofs
%if ! (0%{?rhel} >= 8)
Provides:       kiwi-filesystem:btrfs
%endif
Provides:       kiwi-filesystem:erofs
Provides:       kiwi-filesystem:ext2
Provides:       kiwi-filesystem:ext3
Provides:       kiwi-filesystem:ext4
Provides:       kiwi-filesystem:squashfs
Provides:       kiwi-filesystem:xfs
Provides:       kiwi-image-pxe-requires = %{version}-%{release}
Obsoletes:      kiwi-image-pxe-requires < %{version}-%{release}
Provides:       kiwi-filesystem-requires = %{version}-%{release}
Obsoletes:      kiwi-filesystem-requires < %{version}-%{release}
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       erofs-utils
Requires:       xfsprogs
%if ! (0%{?rhel} >= 8)
Requires:       btrfs-progs
%endif
Requires:       squashfs-tools
Requires:       qemu-img
Requires:       kiwi-systemdeps-core = %{version}-%{release}

%description systemdeps-filesystems
Host setup helper to pull in all packages required/useful on
the build host to build filesystem images

%package systemdeps-disk-images
Summary:        KIWI - host requirements for disk images
Provides:       kiwi-image:oem
Provides:       kiwi-image:vmx
Provides:       kiwi-image-oem-requires = %{version}-%{release}
Obsoletes:      kiwi-image-oem-requires < %{version}-%{release}
Provides:       kiwi-image-vmx-requires = %{version}-%{release}
Obsoletes:      kiwi-image-vmx-requires < %{version}-%{release}
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-bootloaders = %{version}-%{release}
Requires:       kiwi-systemdeps-iso-media = %{version}-%{release}
Requires:       gdisk
Requires:       lvm2
Requires:       parted
Requires:       kpartx
Requires:       cryptsetup
Requires:       mdadm
Requires:       open-vmdk
Requires:       util-linux

%description systemdeps-disk-images
Host setup helper to pull in all packages required/useful on
the build host to build disk images

%package systemdeps-image-validation
Summary:        KIWI - host requirements for handling image descriptions better
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     jing
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       python3-solv
%endif
%if ! (0%{?rhel} && 0%{?rhel} < 8)
Recommends:     python3-anymarkup
%endif

%description systemdeps-image-validation
Host setup helper to pull in all packages required/useful on
the build host to handling image descriptions better. This also
includes reading of image descriptions for different markup
languages

%package systemdeps
Summary:        KIWI - Host system dependencies
Requires:       kiwi-systemdeps-core = %{version}-%{release}
Requires:       kiwi-systemdeps-bootloaders = %{version}-%{release}
%ifnarch ppc64 %{ix86}
# buildah isn't available on ppc64 or x86_32
Requires:       kiwi-systemdeps-containers = %{version}-%{release}
%endif
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-disk-images = %{version}-%{release}
Requires:       kiwi-systemdeps-iso-media = %{version}-%{release}
%if ! 0%{?rhel}
Requires:       kiwi-systemdeps-image-validation = %{version}-%{release}
%endif
%if 0%{?fedora}
Requires:       kiwi-systemdeps-enclaves = %{version}-%{release}
Recommends:     kiwi-systemdeps-pkgmgr-zypper = %{version}-%{release}
%endif

%description systemdeps
Host setup helper to pull in all packages required/useful to
leverage all functionality in KIWI.

%package -n python3-%{name}
Summary:        KIWI - Python 3 implementation
# Only require core dependencies, and allow OBS to pull the rest through magic Provides
Requires:       kiwi-systemdeps-core = %{version}-%{release}
# Retain default expectation for local installations
Recommends:     kiwi-systemdeps = %{version}-%{release}
# Enable support for alternative markups
Recommends:     python%{python3_version}dist(anymarkup-core) >= 0.8.0
Recommends:     python%{python3_version}dist(xmltodict) >= 0.12.0

BuildArch:      noarch
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python 3 library of the KIWI Image System. Provides an operating system
image builder for Linux supported hardware platforms as well as for
virtualization and cloud systems like Xen, KVM, VMware, EC2 and more.

%ifarch %{ix86} x86_64
%package pxeboot
Summary:        KIWI - PXE boot structure
Requires:       syslinux
Requires:       tftp-server

%description pxeboot
This package contains the basic PXE directory structure which is
needed to serve kiwi built images via PXE.
%endif

%package -n dracut-kiwi-lib
Summary:        KIWI - Dracut kiwi Library
Requires:       bc
# btrfs-progs is not available on RHEL 8+
%if ! (0%{?rhel} >= 8)
Requires:       btrfs-progs
%endif
Requires:       coreutils
Requires:       cryptsetup
Requires:       curl
Requires:       device-mapper
Requires:       dialog
Requires:       dracut
Requires:       e2fsprogs
Requires:       gdisk
Requires:       grep
Requires:       kpartx
Requires:       lvm2
Requires:       mdadm
Requires:       parted
Requires:       pv
Requires:       util-linux
Requires:       xfsprogs
Requires:       xz
BuildArch:      noarch

%description -n dracut-kiwi-lib
This package contains a collection of methods to provide a library
for tasks done in other kiwi dracut modules

%package -n dracut-kiwi-oem-repart
Summary:        KIWI - Dracut module for oem(repart) image type
Requires:       dracut-kiwi-lib = %{version}-%{release}
BuildArch:      noarch

%description -n dracut-kiwi-oem-repart
This package contains the kiwi-repart dracut module which is
used to repartition the oem disk image to the current disk
geometry according to the setup in the kiwi image configuration

%package -n dracut-kiwi-oem-dump
Summary:        KIWI - Dracut module for oem(install) image type
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       gawk
Requires:       kexec-tools
BuildArch:      noarch

%description -n dracut-kiwi-oem-dump
This package contains the kiwi-dump and kiwi-dump-reboot dracut
modules which is used to install an oem image onto a target disk.
It implements a simple installer which allows for user selected
target disk or unattended installation to target. The source of
the image to install could be either from media(CD/DVD/USB) or
from remote.

%package -n dracut-kiwi-live
Summary:        KIWI - Dracut module for iso(live) image type
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       dracut-network
Requires:       device-mapper
Requires:       dialog
Requires:       dracut
Requires:       e2fsprogs
Requires:       util-linux
Requires:       xfsprogs
Requires:       parted
BuildArch:      noarch

%description -n dracut-kiwi-live
This package contains the kiwi-live dracut module which is used
for booting iso(live) images built with KIWI.

%package -n dracut-kiwi-overlay
Summary:        KIWI - Dracut module for vmx(+overlay) image type
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       dracut
Requires:       util-linux
BuildArch:      noarch

%description -n dracut-kiwi-overlay
This package contains the kiwi-overlay dracut module which is used
for booting vmx images built with KIWI and configured to use an
overlay root filesystem.

%package -n dracut-kiwi-verity
Summary:        KIWI - Dracut module for disk with embedded verity metadata
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       dracut

%description -n dracut-kiwi-verity
This package contains the kiwi-verity dracut module which is used
for booting oem images built with KIWI and configured to use an
embedded verity metadata block via the embed_verity_metadata
type attribute.

%package cli
Summary:        Flexible operating system appliance image builder
Provides:       kiwi-schema = 8.2
# So we can reference it by the source package name while permitting this to be noarch
Provides:       %{name} = %{version}-%{release}
Requires:       python3-%{name} = %{version}-%{release}
Requires:       bash-completion
BuildArch:      noarch

%description cli %{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Temporarily switch things back to docopt for everything but Fedora 41+
# FIXME: Drop this hack as soon as we can...
%if ! (0%{?fedora} >= 41 || 0%{?rhel} >= 10)
sed -e 's/docopt-ng.*/docopt = ">=0.6.2"/' -i pyproject.toml
%endif

# Drop shebang for kiwi/xml_parse.py, as we don't intend to use it as an independent script
sed -e "s|#!/usr/bin/env python||" -i kiwi/xml_parse.py

%generate_buildrequires
%pyproject_buildrequires

%build
# Required for some parts
%set_build_flags

%pyproject_wheel

# Build man pages
make -C doc man

%install
# Required for some parts
%set_build_flags

%pyproject_install

# Install man-pages, completion and kiwi default configuration (yes, the slash is needed!)
make buildroot=%{buildroot}/ install

# Install dracut modules (yes, the slash is needed!)
make buildroot=%{buildroot}/ install_dracut

# Get rid of unnecessary doc files
rm -rf %{buildroot}%{_docdir}/packages

# Rename unversioned binaries
mv %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi-ng-3

# Create symlinks for correct binaries
ln -sr %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi
ln -sr %{buildroot}%{_bindir}/kiwi-ng-3 %{buildroot}%{_bindir}/kiwi-ng

# kiwi pxeboot directory structure to be packed in kiwi-pxeboot
%ifarch %{ix86} x86_64
for i in KIWI pxelinux.cfg image upload boot; do \
    mkdir -p %{buildroot}%{_sharedstatedir}/tftpboot/$i ;\
done
%fdupes %{buildroot}%{_sharedstatedir}/tftpboot
%endif

%post cli
if [ -x /usr/sbin/semanage -a -x /usr/sbin/restorecon ]; then
    # file contexts
    semanage fcontext --add --type install_exec_t        '%{_bindir}/kiwi'               2> /dev/null || :
    semanage fcontext --add --type install_exec_t        '%{_bindir}/kiwi-ng(.*)'        2> /dev/null || :
    restorecon -r %{_bindir}/kiwi %{_bindir}/kiwi-ng* || :
fi

%postun cli
if [ $1 -eq 0 ]; then
    if [ -x /usr/sbin/semanage ]; then
        # file contexts
        semanage fcontext --delete --type install_exec_t        '%{_bindir}/kiwi'               2> /dev/null || :
        semanage fcontext --delete --type install_exec_t        '%{_bindir}/kiwi-ng(.*)'        2> /dev/null || :
    fi
fi

%if %{with check}
%check
pushd test/unit
# skipped tests require anymarkup which was retired from Fedora
# we patch the code of default ISO tagging method, hence skip test_config_sections_* too
%pytest %{?fedora:-n auto} --ignore markup/any_test.py -k \
  "not test_process_image_info_print_yaml and not test_process_image_info_print_toml \
   and not test_config_sections_defaults and not test_config_sections_invalid"
popd
%endif

%files -n python3-%{name}
%license LICENSE
%{_bindir}/kiwi-ng-3*
%{python3_sitelib}/kiwi*/
%dir %{_datadir}/kiwi
%{_datadir}/kiwi/xsl_to_v74/

%files cli
%{_bindir}/kiwi
%{_bindir}/kiwi-ng
%{_datadir}/bash-completion/completions/kiwi-ng
%{_mandir}/man8/kiwi*
%config(noreplace) %{_sysconfdir}/kiwi.yml

%ifarch %{ix86} x86_64
%files pxeboot
%license LICENSE
%{_sharedstatedir}/tftpboot/*
%endif

%files -n dracut-kiwi-lib
%license LICENSE
%{_prefix}/lib/dracut/modules.d/59kiwi-lib/

%files -n dracut-kiwi-oem-repart
%license LICENSE
%{_prefix}/lib/dracut/modules.d/55kiwi-repart/

%files -n dracut-kiwi-oem-dump
%license LICENSE
%{_prefix}/lib/dracut/modules.d/55kiwi-dump/
%{_prefix}/lib/dracut/modules.d/59kiwi-dump-reboot/

%files -n dracut-kiwi-live
%license LICENSE
%{_prefix}/lib/dracut/modules.d/55kiwi-live/

%files -n dracut-kiwi-overlay
%license LICENSE
%{_prefix}/lib/dracut/modules.d/55kiwi-overlay/

%files -n dracut-kiwi-verity
%{_usr}/lib/dracut/modules.d/50kiwi-verity
%{_bindir}/kiwi-parse-verity

%files systemdeps-core
# Empty metapackage

%if 0%{?fedora}
%files systemdeps-pkgmgr-zypper
# Empty metapackage
%endif

%files systemdeps-bootloaders
# Empty metapackage

%ifnarch ppc64 %{ix86}
%files systemdeps-containers
# Empty metapackage
%endif

%if 0%{?fedora}
%files systemdeps-enclaves
# Empty metapackage
%endif

%files systemdeps-iso-media
# Empty metapackage

%files systemdeps-filesystems
# Empty metapackage

%files systemdeps-disk-images
# Empty metapackage

%files systemdeps-image-validation
# Empty metapackage

%files systemdeps
# Empty metapackage

%changelog
%autochangelog
