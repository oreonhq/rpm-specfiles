%global source0_hash 9f92ce04827905276e3082deab03fb086219aa009e3a13c8b27f5b58d2cbee2b
%global __brp_mangle_shebangs_exclude_from ^%{_prefix}/lib/dracut/modules.d/.*$
%global desc \
The KIWI Image System provides an operating system image builder \
for Linux supported hardware platforms as well as for virtualization \
and cloud systems like Xen, KVM, VMware, EC2 and more.
%bcond check 1
Name:           kiwi
Version:        11.0.2
Release:        1%{?dist}
URL:            http://osinside.github.io/kiwi/
Summary:        Flexible operating system image builder
License:        GPL-3.0-or-later
Source0:        https://files.pythonhosted.org/packages/source/k/%{name}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Patch1001:      1001-Use-buildah-by-default-for-OCI-image-builds.patch
Patch1002:      1002-Use-isomd5sum-by-default-for-tagging-ISO-files.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.2.0
Requires:       python3-kiwi = %{version}-%{release}
# /oreon:deps
%description %{desc}

%package systemdeps-core
Summary:        KIWI - Core host system dependencies
Provides:       kiwi-image-tbz-requires = %{version}-%{release}
Obsoletes:      kiwi-image-tbz-requires < %{version}-%{release}
Provides:       kiwi-image:tbz
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
Requires:       dnf5
Provides:       kiwi-packagemanager:dnf5
%endif
Recommends:     distribution-gpg-keys
Requires:       file
Requires:       lsof
Requires:       mtools
Requires:       rsync
Requires:       sed
Requires:       screen
Requires:       tar >= 1.2.7
Requires:       openssl
Requires:       xz
Obsoletes:      python2-%{name} < %{version}-%{release}
Obsoletes:      %{name}-tools < %{version}-%{release}
%description systemdeps-core
This metapackage installs the necessary system dependencies
to run KIWI.

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

%package systemdeps-iso-media
Summary:        KIWI - host requirements for live and install iso images
Provides:       kiwi-image:iso
Provides:       kiwi-image-iso-requires = %{version}-%{release}
Obsoletes:      kiwi-image-iso-requires < %{version}-%{release}
Requires:       xorriso
Requires:       isomd5sum
%ifarch %{ix86} x86_64
Requires:       syslinux
%endif
%ifarch x86_64
Requires:       grub2-efi-x64-cdboot
%endif
%ifarch aarch64
Requires:       grub2-efi-aa64-cdboot
%endif
Requires:       kiwi-systemdeps-core = %{version}-%{release}
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-bootloaders = %{version}-%{release}
%description systemdeps-iso-media
Host setup helper to pull in all packages required/useful on
the build host to build live and install iso images.

%package systemdeps-bootloaders
Summary:        KIWI - host requirements for configuring bootloaders
%ifnarch s390 s390x
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
%endif
%ifarch %{ix86} x86_64
Requires:       grub2-pc
Requires:       grub2-pc-modules
%endif
%ifarch aarch64
Requires:       grub2-efi-aa64-modules
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
Requires:       kiwi-systemdeps-containers = %{version}-%{release}
%endif
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-disk-images = %{version}-%{release}
Requires:       kiwi-systemdeps-iso-media = %{version}-%{release}
%description systemdeps
Host setup helper to pull in all packages required/useful to
leverage all functionality in KIWI.

%package -n python3-%{name}
Summary:        KIWI - Python 3 implementation
Requires:       kiwi-systemdeps-core = %{version}-%{release}
Recommends:     kiwi-systemdeps = %{version}-%{release}
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

# Drop shebang for kiwi/xml_parse.py, as we don't intend to use it as an independent script
sed -e "s|#!/usr/bin/env python||" -i kiwi/xml_parse.py

%build

%set_build_flags
%pyproject_wheel
make -C doc man
%install
%set_build_flags
%pyproject_install
make buildroot=%{buildroot}/ install
make buildroot=%{buildroot}/ install_dracut
rm -rf %{buildroot}%{_docdir}/packages
mv %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi-ng-3
ln -sr %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi
ln -sr %{buildroot}%{_bindir}/kiwi-ng-3 %{buildroot}%{_bindir}/kiwi-ng
%ifarch %{ix86} x86_64
for i in KIWI pxelinux.cfg image upload boot; do \
    mkdir -p %{buildroot}%{_sharedstatedir}/tftpboot/$i ;\
done
%fdupes %{buildroot}%{_sharedstatedir}/tftpboot
%oreon_autofiles dracut-kiwi-lib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dracut-kiwi-oem-repart usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dracut-kiwi-oem-dump usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dracut-kiwi-live usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dracut-kiwi-overlay usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dracut-kiwi-verity usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/kiwi* usr/lib64/python3*/site-packages/kiwi* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%post cli

if [ -x /usr/sbin/semanage -a -x /usr/sbin/restorecon ]; then
    semanage fcontext --add --type install_exec_t        '%{_bindir}/kiwi'               2> /dev/null || :
    semanage fcontext --add --type install_exec_t        '%{_bindir}/kiwi-ng(.*)'        2> /dev/null || :
    restorecon -r %{_bindir}/kiwi %{_bindir}/kiwi-ng* || :
fi
%postun cli

if [ $1 -eq 0 ]; then
    if [ -x /usr/sbin/semanage ]; then
        semanage fcontext --delete --type install_exec_t        '%{_bindir}/kiwi'               2> /dev/null || :
        semanage fcontext --delete --type install_exec_t        '%{_bindir}/kiwi-ng(.*)'        2> /dev/null || :
    fi
fi
%if %{with check}
%check

pushd test/unit
%pytest %{?fedora:-n auto} --ignore markup/any_test.py -k \
  "not test_process_image_info_print_yaml and not test_process_image_info_print_toml \
   and not test_config_sections_defaults and not test_config_sections_invalid"
popd
%endif
%files
%files -n kiwi-systemdeps-core -f %{oreon_filedir}/kiwi-systemdeps-core.list
%files -n kiwi-systemdeps-containers -f %{oreon_filedir}/kiwi-systemdeps-containers.list
%files -n kiwi-systemdeps-iso-media -f %{oreon_filedir}/kiwi-systemdeps-iso-media.list
%files -n kiwi-systemdeps-bootloaders -f %{oreon_filedir}/kiwi-systemdeps-bootloaders.list
%files -n kiwi-systemdeps-filesystems -f %{oreon_filedir}/kiwi-systemdeps-filesystems.list
%files -n kiwi-systemdeps-disk-images -f %{oreon_filedir}/kiwi-systemdeps-disk-images.list
%files -n kiwi-systemdeps-image-validation -f %{oreon_filedir}/kiwi-systemdeps-image-validation.list
%files -n kiwi-systemdeps -f %{oreon_filedir}/kiwi-systemdeps.list
%files -n python3-kiwi -f %{oreon_filedir}/python3-kiwi.list
%files -n dracut-kiwi-lib -f %{oreon_filedir}/dracut-kiwi-lib.list
%files -n dracut-kiwi-oem-repart -f %{oreon_filedir}/dracut-kiwi-oem-repart.list
%files -n dracut-kiwi-oem-dump -f %{oreon_filedir}/dracut-kiwi-oem-dump.list
%files -n dracut-kiwi-live -f %{oreon_filedir}/dracut-kiwi-live.list
%files -n dracut-kiwi-overlay -f %{oreon_filedir}/dracut-kiwi-overlay.list
%files -n dracut-kiwi-verity -f %{oreon_filedir}/dracut-kiwi-verity.list
%files -n kiwi-cli -f %{oreon_filedir}/kiwi-cli.list

%changelog

%autochangelog
