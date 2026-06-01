%global source0_hash d15ac0ebff651fa19a984835b9621e442a7febafcc0b67aafa6a3e80438d0ac9

%global source2_key_fpr F7774FB1AD074A7E8C8767EA91738F73E1B768A0



%global _hardened_build 1

%ifarch %{kernel_arches}
# ppc64le broken in rawhide:
# https://bugzilla.redhat.com/show_bug.cgi?id=2006709
# riscv64 tests fail with
# qemu-system-riscv64: invalid accelerator kvm
# qemu-system-riscv64: falling back to tcg
# qemu-system-riscv64: unable to find CPU model 'host'
# This seems to require changes in libguestfs and/or qemu to support
# -cpu max or -cpu virt.
# s390x builders can't run libguestfs
%ifnarch %{power64} riscv64 s390 s390x
%global have_libguestfs 1
%endif
%endif

# We can only compile the OCaml plugin on platforms which have native
# OCaml support (not bytecode).
%ifarch %{ocaml_native_compiler}
%global have_ocaml 1
%endif

# libblkio was broken on i686: https://bugzilla.redhat.com/2229372
# but somehow "fixed itself", keep an eye on it.
%global have_blkio 1

# Enable mingw subpackage on Fedora only.
%if 0%{?fedora} || (0%{?oreon} >= 11)
%global have_mingw 1
%endif

# Enable nbdkit-selinux package.
%global with_selinux 1
%global modulename nbdkit
%global selinuxtype targeted

# Architectures where we run the complete test suite including
# the libguestfs tests.
#
# On all other architectures, a simpler test suite must pass.  This
# omits any tests that run full qemu, since running qemu under TCG is
# often broken on non-x86_64 arches.
%global complete_test_arches x86_64

# If the test suite is broken on a particular architecture, document
# it as a bug and add it to this list.
%global broken_test_arches NONE

# If we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# The source directory.
%global source_directory 1.47-development

Name:           nbdkit
Version:        1.47.9
Release:        1%{?dist}
Summary:        NBD server

License:        BSD-3-Clause
URL:            https://gitlab.com/nbdkit/nbdkit

%if 0%{?rhel} >= 8 || (0%{?oreon} >= 11)
# On RHEL 8+, we cannot build the package on i686 (no virt stack).
ExcludeArch:    i686
%endif

Source0:        http://libguestfs.org/download/nbdkit/%{source_directory}/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:        http://libguestfs.org/download/nbdkit/%{source_directory}/%{name}-%{version}.tar.gz.sig
# Keyring used to verify tarball signature.
Source2:        https://gitlab.com/nbdkit/nbdkit/-/raw/HEAD/libguestfs.keyring
%endif

# Maintainer script which helps with handling patches.
Source3:        https://gitlab.com/nbdkit/nbdkit/-/raw/HEAD/copy-patches.sh

# For automatic RPM Provides generation.
# See: https://rpm-software-management.github.io/rpm/manual/dependency_generators.html
Source4:        https://gitlab.com/nbdkit/nbdkit/-/raw/HEAD/nbdkit.attr
Source5:        https://gitlab.com/nbdkit/nbdkit/-/raw/HEAD/nbdkit-find-provides

# For nbdkit-selinux package:
Source6:        %{modulename}.te
Source7:        %{modulename}.if
Source8:        %{modulename}.fc

# For applying the patches:
BuildRequires:  git

# For rebuilding autoconf cruft:
BuildRequires:  autoconf, automake, libtool

BuildRequires:  make
BuildRequires:  libxcrypt-devel
BuildRequires:  gcc, gcc-c++
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libselinux)
%if !0%{?rhel} && 0%{?have_libguestfs} || (0%{?oreon} >= 11)
BuildRequires:  pkgconfig(libguestfs)
%endif
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
%if !0%{?rhel} || (0%{?oreon} >= 11)
BuildRequires:  pkgconfig(zlib-ng)
%endif
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnbd)
%if !0%{?rhel} || (0%{?oreon} >= 11)
# We require libnfs >= 6, but the internal version is >= 16
BuildRequires:  pkgconfig(libnfs) >= 16
%endif
BuildRequires:  pkgconfig(libssh)
BuildRequires:  e2fsprogs
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(com_err)
%if !0%{?rhel} || (0%{?oreon} >= 11)
BuildRequires:  xorriso
BuildRequires:  pkgconfig(libtorrent-rasterbar)
%endif
%if 0%{?have_blkio}
BuildRequires:  pkgconfig(blkio)
%endif
%if !0%{?rhel} || (0%{?oreon} >= 11)
BuildRequires:  pkgconfig(OpenCL)
%endif
BuildRequires:  bash-completion
%if 0%{?fedora} || 0%{?rhel} >= 11 || (0%{?oreon} >= 11)
BuildRequires:  bash-completion-devel
%endif
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils::Embed)
%if 0%{?rhel} == 8 || (0%{?oreon} >= 11)
BuildRequires:  platform-python-devel
%else
BuildRequires:  python3-devel
%endif
%if !0%{?rhel} || (0%{?oreon} >= 11)
BuildRequires:  python3-boto3
%endif
%if !0%{?rhel} || (0%{?oreon} >= 11)
%if 0%{?have_ocaml}
BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-ocamldoc
%endif
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(lua)
%endif
%if 0%{verify_tarball_signature}
BuildRequires:  gnupg2
%endif

# Only for running the test suite:
BuildRequires:  /usr/bin/bc
BuildRequires:  /usr/bin/certtool
BuildRequires:  /usr/bin/cut
BuildRequires:  expect
BuildRequires:  glibc-utils
BuildRequires:  /usr/bin/hexdump
BuildRequires:  /usr/sbin/ip
BuildRequires:  jq
%if !0%{?rhel} || (0%{?oreon} >= 11)
BuildRequires:  /usr/bin/lzip
%endif
BuildRequires:  /usr/bin/nbdcopy
BuildRequires:  /usr/bin/nbdinfo
BuildRequires:  /usr/bin/nbdsh
%ifnarch %{ix86}
BuildRequires:  /usr/bin/qemu-img
BuildRequires:  /usr/bin/qemu-io
BuildRequires:  /usr/bin/qemu-nbd
%endif
BuildRequires:  /usr/sbin/sfdisk
%if !0%{?rhel} || (0%{?oreon} >= 11)
BuildRequires:  /usr/bin/socat
%endif
BuildRequires:  /usr/sbin/ss
BuildRequires:  /usr/bin/stat

# This package has RPM rules that create the automatic Provides: for
# nbdkit plugins and filters.  This means nbdkit build depends on
# itself, but it's a simple noarch package so easy to install.
BuildRequires:  nbdkit-srpm-macros >= 1.30.0

%if 0%{?have_mingw}
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw64-gnutls
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw32-xz
BuildRequires:  mingw64-xz
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
%endif

# nbdkit is a metapackage pulling the server and a useful subset
# of the plugins and filters.
Requires:       nbdkit-server%{?_isa} = %{version}-%{release}
Requires:       nbdkit-basic-plugins%{?_isa} = %{version}-%{release}
Requires:       nbdkit-basic-filters%{?_isa} = %{version}-%{release}

%if 0%{?with_selinux}
# This ensures that the nbdkit-selinux package and all its
# dependencies are not pulled into containers and other systems that
# do not use SELinux.
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif


%description
NBD is a protocol for accessing block devices (hard disks and
disk-like things) over the network.

nbdkit is a toolkit for creating NBD servers.

The key features are:

* Multithreaded NBD server written in C with good performance.

* Minimal dependencies for the basic server.

* Liberal license (BSD) allows nbdkit to be linked to proprietary
  libraries or included in proprietary code.

* Well-documented, simple plugin API with a stable ABI guarantee.
  Lets you to export "unconventional" block devices easily.

* You can write plugins in C or many other languages.

* Filters can be stacked in front of plugins to transform the output.

* Server can run standalone or can be invoked from other programs.

'%{name}' is a meta-package which pulls in the core server and a
useful subset of plugins and filters with minimal dependencies.

If you want just the server, install '%{name}-server'.

To develop plugins, install the '%{name}-devel' package and start by
reading the nbdkit(1) and nbdkit-plugin(3) manual pages.


%package server
Summary:        The %{name} server

%description server
This package contains the %{name} server with only the null plugin
and no filters.  To install a basic set of plugins and filters you
need to install "nbdkit-basic-plugins", "nbdkit-basic-filters" or
the metapackage "nbdkit".


%package basic-plugins
Summary:        Basic plugins for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}


%description basic-plugins
This package contains plugins for %{name} which only depend on simple
C libraries: glibc, gnutls, zlib and zstd.  Other plugins for nbdkit
with more complex dependencies are packaged separately.

nbdkit-data-plugin          Serve small amounts of data from the command line.

nbdkit-eval-plugin          Write a shell script plugin on the command line.

nbdkit-file-plugin          The normal file plugin for serving files.

nbdkit-floppy-plugin        Create a virtual floppy disk from a directory.

nbdkit-full-plugin          A virtual disk that returns ENOSPC errors.

nbdkit-info-plugin          Serve client and server information.

nbdkit-memory-plugin        A virtual memory plugin.

nbdkit-ones-plugin          Fill disk with repeated 0xff or other bytes.

nbdkit-pattern-plugin       Fixed test pattern.

nbdkit-partitioning-plugin  Create virtual disks from partitions.

nbdkit-random-plugin        Random content plugin for testing.

nbdkit-sh-plugin            Write plugins as shell scripts or executables.

nbdkit-sparse-random-plugin Make sparse random disks.

nbdkit-split-plugin         Concatenate one or more files.

nbdkit-zero-plugin          Zero-length plugin for testing.


%package example-plugins
Summary:        Example plugins for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
%if !0%{?rhel} || (0%{?oreon} >= 11)
# example4 is written in Perl.
Requires:       %{name}-perl-plugin
%endif

%description example-plugins
This package contains example plugins for %{name}.


# The plugins below have non-trivial dependencies are so are
# packaged separately.

%if 0%{?have_blkio}
%package blkio-plugin
Summary:        libblkio NVMe, vhost-user, vDPA, VFIO plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description blkio-plugin
This package contains libblkio (NVMe, vhost-user, vDPA, VFIO) support
for %{name}.
%endif


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package cc-plugin
Summary:        Write small inline C plugins and scripts for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       gcc
Requires:       /usr/bin/cat

%description cc-plugin
This package contains support for writing inline C plugins and scripts
for %{name}.  NOTE this is NOT the right package for writing plugins
in C, install %{name}-devel for that.
%endif


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package cdi-plugin
Summary:        Containerized Data Import plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       jq
Requires:       podman

%description cdi-plugin
This package contains Containerized Data Import support for %{name}.
%endif


%package curl-plugin
Summary:        HTTP/FTP (cURL) plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description curl-plugin
This package contains cURL (HTTP/FTP) support for %{name}.


%if !0%{?rhel} || (0%{?oreon} >= 11)
# In theory this is noarch, but because plugins are placed in _libdir
# which varies across architectures, RPM does not allow this.
%package gcs-plugin
Summary:        Gooogle Cloud Storage plugin %{name}
Requires:       %{name}-python-plugin%{?_isa} = %{version}-%{release}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
# XXX Should not need to add this.
Requires:       python3-google-cloud-storage

%description gcs-plugin
This package lets you open disk images stored in Google
Cloud Storage using %{name}.
%endif


%if !0%{?rhel} && 0%{?have_libguestfs} || (0%{?oreon} >= 11)
%package guestfs-plugin
Summary:        libguestfs plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description guestfs-plugin
This package is a libguestfs plugin for %{name}.
%endif


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package iso-plugin
Summary:        Virtual ISO 9660 plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       xorriso

%description iso-plugin
This package is a virtual ISO 9660 (CD-ROM) plugin for %{name}.
%endif


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package libvirt-plugin
Summary:        Libvirt plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description libvirt-plugin
This package is a libvirt plugin for %{name}.  It lets you access
libvirt guest disks readonly.  It is implemented using the libvirt
virDomainBlockPeek API.
%endif


%package linuxdisk-plugin
Summary:        Virtual Linux disk plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
# for mke2fs
Requires:       e2fsprogs

%description linuxdisk-plugin
This package is a virtual Linux disk plugin for %{name}.


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package lua-plugin
Summary:        Lua plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description lua-plugin
This package lets you write Lua plugins for %{name}.
%endif


%package nbd-plugin
Summary:        NBD proxy / forward plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description nbd-plugin
This package lets you forward NBD connections from %{name}
to another NBD server.


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package nfs-plugin
Summary:        NFS (Network File Server) plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description nfs-plugin
This package contains Network File Server (NFS) support for %{name}.
%endif


%if !0%{?rhel} && 0%{?have_ocaml} || (0%{?oreon} >= 11)
%package ocaml-plugin
Summary:        OCaml plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description ocaml-plugin
This package lets you run OCaml plugins for %{name}.

To compile OCaml plugins you will also need to install
%{name}-ocaml-plugin-devel.


%package ocaml-plugin-devel
Summary:        OCaml development environment for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       %{name}-ocaml-plugin%{?_isa} = %{version}-%{release}

%description ocaml-plugin-devel
This package lets you write OCaml plugins for %{name}.
%endif


%package ondemand-plugin
Summary:        Create filesystems on demand for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
# For mkfs and mke2fs (defaults).
Requires:       util-linux, e2fsprogs
# For other filesystems.
Suggests:       xfsprogs
%if !0%{?rhel} || (0%{?oreon} >= 11)
Suggests:       ntfsprogs, dosfstools
%endif

%description ondemand-plugin
This package is a plugin to create filesystems on demand for %{name}.


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package perl-plugin
Summary:        Perl plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description perl-plugin
This package lets you write Perl plugins for %{name}.
%endif


%package python-plugin
Summary:        Python 3 plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description python-plugin
This package lets you write Python 3 plugins for %{name}.


%if !0%{?rhel} || (0%{?oreon} >= 11)
# In theory this is noarch, but because plugins are placed in _libdir
# which varies across architectures, RPM does not allow this.
%package S3-plugin
Summary:        Amazon S3 and Ceph plugin for %{name}
Requires:       %{name}-python-plugin%{?_isa} = %{version}-%{release}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
# XXX Should not need to add this.
Requires:       python3-boto3

%description S3-plugin
This package lets you open disk images stored in Amazon S3
or Ceph using %{name}.
%endif


%package ssh-plugin
Summary:        SSH plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description ssh-plugin
This package contains SSH support for %{name}.


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package tcl-plugin
Summary:        Tcl plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description tcl-plugin
This package lets you write Tcl plugins for %{name}.
%endif


%package tmpdisk-plugin
Summary:        Remote temporary filesystem disk plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
# For mkfs and mke2fs (defaults).
Requires:       util-linux, e2fsprogs
# For other filesystems.
Suggests:       xfsprogs
%if !0%{?rhel} || (0%{?oreon} >= 11)
Suggests:       ntfsprogs, dosfstools
%endif

%description tmpdisk-plugin
This package is a remote temporary filesystem disk plugin for %{name}.


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package torrent-plugin
Summary:        BitTorrent plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description torrent-plugin
This package is a BitTorrent plugin for %{name}.
%endif


%ifarch x86_64
%package vddk-plugin
Summary:        VMware VDDK plugin for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
# https://bugzilla.redhat.com/show_bug.cgi?id=1931818
Requires:       libxcrypt-compat%{?_isa}

%description vddk-plugin
This package is a plugin for %{name} which connects to
VMware VDDK for accessing VMware disks and servers.
%endif


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package vram-plugin
Summary:        use GPU Video RAM as a network block device
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Recommends:     %{_bindir}/clinfo

%description vram-plugin
This package contains GPU Video RAM support for %{name}.
%endif


%package basic-filters
Summary:        Basic filters for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description basic-filters
This package contains filters for %{name} which only depend on simple
C libraries: glibc, gnutls, zlib and zstd.  Other filters for nbdkit
with more complex dependencies are packaged separately.

nbdkit-blocksize-filter    Adjust block size of requests sent to plugins.

nbdkit-blocksize-policy-filter  Set block size constraints and policy.

nbdkit-cache-filter        Server-side cache.

nbdkit-checkwrite-filter   Check writes match contents of plugin.

nbdkit-count-filter        Count bytes read, written, zeroed and trimmed.

nbdkit-cow-filter          Copy-on-write overlay for read-only plugins.

nbdkit-ddrescue-filter     Filter for serving from ddrescue dump.

nbdkit-delay-filter        Inject read and write delays.

nbdkit-error-filter        Inject errors.

nbdkit-evil-filter         Add random data corruption to reads.

nbdkit-exitlast-filter     Exit on last client connection.

nbdkit-exitwhen-filter     Exit gracefully when an event occurs.

nbdkit-exportname-filter   Adjust export names between client and plugin.

nbdkit-extentlist-filter   Place extent list over a plugin.

nbdkit-fua-filter          Modify flush behaviour in plugins.

nbdkit-gzip-filter         Decompress a .gz file

nbdkit-indexed-gzip-filter Access .gz contents efficiently.

nbdkit-ip-filter           Filter clients by IP address.

nbdkit-limit-filter        Limit nr clients that can connect concurrently.

nbdkit-log-filter          Log all transactions to a file.

nbdkit-luks-filter         Read and write LUKS-encrypted disks.

nbdkit-map-filter          Remap disk blocks.

nbdkit-multi-conn-filter   Enable, emulate or disable multi-conn.

nbdkit-nocache-filter      Disable cache requests in the underlying plugin.

nbdkit-noextents-filter    Disable extents in the underlying plugin.

nbdkit-nofilter-filter     Passthrough filter.

nbdkit-noparallel-filter   Serialize requests to the underlying plugin.

nbdkit-nozero-filter       Adjust handling of zero requests by plugins.

nbdkit-offset-filter       Serve an offset and range.

nbdkit-openonce-filter     Open the underlying plugin once.

nbdkit-partition-filter    Serve a single partition.

nbdkit-pause-filter        Pause NBD requests.

nbdkit-protect-filter      Write-protect parts of a plugin.

%if !0%{?rhel} || (0%{?oreon} >= 11)
nbdkit-qcow2dec-filter     Decode qcow2 files.

%endif
nbdkit-rate-filter         Limit bandwidth by connection or server.

nbdkit-readahead-filter    Prefetch data when reading sequentially.

nbdkit-readonly-filter     Switch a plugin between read-only and writable.

nbdkit-retry-filter        Reopen connection on error.

nbdkit-retry-request-filter Retry single requests on error.

nbdkit-rotational-filter   Set if a plugin is rotational or not.

nbdkit-scan-filter         Prefetch data ahead of sequential reads.

nbdkit-spinning-filter     Add seek delays to simulate a spinning hard disk.

nbdkit-swab-filter         Filter for swapping byte order.

nbdkit-time-limit-filter   Set an overall time limit for each connection.

nbdkit-tls-fallback-filter TLS protection filter.

nbdkit-truncate-filter     Truncate, expand, round up or round down size.

nbdkit-xor-filter          Obfuscate contents of a plugin with XOR..


%package bzip2-filter
Summary:        BZip2 filter for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description bzip2-filter
This package is a bzip2 filter for %{name}.


%if !0%{?rhel} || (0%{?oreon} >= 11)
%package ext2-filter
Summary:        ext2, ext3 and ext4 filesystem support for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description ext2-filter
This package contains ext2, ext3 and ext4 filesystem support for
%{name}.
%endif


%package stats-filter
Summary:        Statistics filter for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description stats-filter
Display statistics about operations.


%package tar-filter
Summary:        Tar archive filter for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       tar

%description tar-filter
This package is a tar archive filter for %{name}.


%package xz-filter
Summary:        XZ and lzip filters for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description xz-filter
This package contains the xz and lzip filters for %{name}.


%package devel
Summary:        Development files and documentation for %{name}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains development files and documentation
for %{name}.  Install this package if you want to develop
plugins for %{name}.


%package srpm-macros
Summary:       RPM Provides rules for %{name} plugins and filters
BuildArch:     noarch

%description srpm-macros
This package contains RPM rules that create the automatic Provides:
for %{name} plugins and filters found in the plugins directory.


%package bash-completion
Summary:       Bash tab-completion for %{name}
BuildArch:     noarch
Requires:      bash-completion >= 2.0
Requires:      %{name}-server = %{version}-%{release}

%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.


%if 0%{?with_selinux}
%package selinux
Summary:       %{name} SELinux policy
BuildArch:     noarch
Requires:      selinux-policy-%{selinuxtype}
Requires(post):selinux-policy-%{selinuxtype}
BuildRequires: selinux-policy-devel
%{?selinux_requires}

%description selinux
%{name} SELinux policy module.
%endif


%if 0%{?have_mingw}
%package -n mingw32-%{name}
Summary:       nbdkit binary, plugins, filters, development files for Windows
BuildArch:     noarch
Requires:      mingw32-filesystem
Requires:      pkgconfig

%description -n mingw32-%{name}
NBD is a protocol for accessing block devices (hard disks and
disk-like things) over the network.

nbdkit is a toolkit for creating NBD servers.

This package contains the nbdkit binary, plugins, filters and
development kit for 32 bit versions of Windows.


%package -n mingw64-%{name}
Summary:       nbdkit binary, plugins, filters, development files for Windows
BuildArch:     noarch
Requires:      mingw64-filesystem
Requires:      pkgconfig

%description -n mingw64-%{name}
NBD is a protocol for accessing block devices (hard disks and
disk-like things) over the network.

nbdkit is a toolkit for creating NBD servers.

This package contains the nbdkit binary, plugins, filters and
development kit for 64 bit versions of Windows.


%{?mingw_debug_package}
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1 -S git
autoreconf -i


%build
mkdir build_native
pushd build_native
%global _configure ../configure

# Golang bindings are not enabled in the build since they don't
# need to be.  Most people would use them by copying the upstream
# package into their vendor/ directory.
export PYTHON=%{__python3}
%configure \
    --disable-static \
    --with-extra='%{name}-%{version}-%{release}' \
    --with-tls-priority=@NBDKIT,SYSTEM \
    --with-bash-completions \
    --with-curl \
    --with-gnutls \
    --with-liblzma \
    --with-libnbd \
    --with-manpages \
    --with-selinux \
    --with-ssh \
    --with-zlib \
%if !0%{?rhel} || (0%{?oreon} >= 11)
    --with-zlib-ng \
%else
    --without-zlib-ng \
%endif
    --enable-linuxdisk \
    --enable-python \
    --disable-golang \
    --disable-rust \
    --disable-valgrind \
%if !0%{?rhel} && 0%{?have_ocaml} || (0%{?oreon} >= 11)
    --enable-ocaml \
%else
    --disable-ocaml \
%endif
%if !0%{?rhel} || (0%{?oreon} >= 11)
    --enable-lua \
    --enable-perl \
    --enable-tcl \
    --enable-torrent \
    --enable-vram \
    --with-ext2 \
    --with-iso \
    --with-libvirt \
%else
    --disable-lua \
    --disable-perl \
    --disable-tcl \
    --disable-torrent \
    --disable-vram \
    --without-ext2 \
    --without-iso \
    --without-libvirt \
%endif
%if 0%{?have_blkio}
    --with-libblkio \
%else
    --without-libblkio \
%endif
%ifarch x86_64
    --enable-vddk \
%else
    --disable-vddk \
%endif
%if !0%{?rhel} && 0%{?have_libguestfs} || (0%{?oreon} >= 11)
    --with-libguestfs \
%else
    --without-libguestfs \
%endif
%ifarch !0%{?rhel} && 0%{?have_libguestfs} && %{complete_test_arches}
    --enable-libguestfs-tests \
%else
    --disable-libguestfs-tests \
%endif
    %{nil}

# Verify that it picked the correct version of Python
# to avoid RHBZ#1404631 happening again silently.
grep '^PYTHON_VERSION = 3' Makefile

%make_build

%if 0%{?with_selinux}
# SELinux policy (originally from selinux-policy-contrib)
# this policy module will override the production module
mkdir selinux
cp -p %{SOURCE6} selinux/
cp -p %{SOURCE7} selinux/
cp -p %{SOURCE8} selinux/

make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif

popd

%if 0%{?have_mingw}
%mingw_configure \
    --disable-static \
    --enable-shared \
    --with-extra='%{name}-%{version}-%{release}' \
    --with-tls-priority=@NBDKIT,SYSTEM \
    --disable-golang \
    --disable-libguestfs-tests \
    --disable-linuxdisk \
    --disable-lua \
    --disable-ocaml \
    --disable-perl \
    --disable-python \
    --disable-rust \
    --disable-tcl \
    --disable-torrent \
    --disable-valgrind \
    --disable-vddk \
    --disable-vram \
    --without-bash-completions \
    --without-curl \
    --without-ext2 \
    --with-gnutls \
    --without-iso \
    --without-libblkio \
    --without-libguestfs \
    --without-libnbd \
    --without-libvirt \
    --with-liblzma \
    --without-manpages \
    --without-selinux \
    --without-ssh \
    --with-zlib \
    %{nil}

%mingw_make %{?_smp_mflags}
%endif


%install
pushd build_native
%make_install

# Delete libtool crap.
find $RPM_BUILD_ROOT -name '*.la' -delete

# If cargo happens to be installed on the machine then the
# rust plugin is built.  Delete it if this happens.
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/nbdkit-rust-plugin.3*

%if 0%{?rhel} || (0%{?oreon} >= 11)
# In RHEL, remove some plugins and filters we cannot --disable.
for f in cc cdi ; do
    rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/nbdkit-$f-plugin.so
    rm -f $RPM_BUILD_ROOT%{_mandir}/man?/nbdkit-$f-plugin.*
done
for f in gcs S3 ; do
    rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/nbdkit-$f-plugin
    rm -f $RPM_BUILD_ROOT%{_mandir}/man1/nbdkit-$f-plugin.1*
done
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/filters/nbdkit-qcow2dec-filter.so
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/nbdkit-qcow2dec-filter.1*
%endif

# Install RPM dependency generator.
mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/
install -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/
install -m 0755 %{SOURCE5} $RPM_BUILD_ROOT%{_rpmconfigdir}/

%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 $RPM_BUILD_ROOT%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 selinux/%{modulename}.if $RPM_BUILD_ROOT%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%endif
popd

%if 0%{?have_mingw}
%mingw_make_install

# Remove .la files
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

# The .def files aren't interesting for other binaries
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/*.def
rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/*.def

# Remove man pages which duplicate stuff in Fedora already.
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

%mingw_debug_install_post
%endif


%check
%ifnarch %{broken_test_arches}
pushd build_native
function skip_test ()
{
    for f in "$@"; do
        rm -f "$f"
        echo 'exit 77' > "$f"
        chmod +x "$f"
    done
}

# Workaround for broken libvirt (RHBZ#1138604).
mkdir -p $HOME/.cache/libvirt

# tests/test-captive.sh is racy especially on s390x.  We need to
# rethink this test upstream.
skip_test tests/test-captive.sh

%ifarch s390x
# Temporarily kill tests/test-cache-max-size.sh since it fails
# sometimes on s390x for unclear reasons.
skip_test tests/test-cache-max-size.sh
%endif

# Temporarily kill test-nbd-tls.sh and test-nbd-tls-psk.sh
# https://www.redhat.com/archives/libguestfs/2020-March/msg00191.html
skip_test tests/test-nbd-tls.sh tests/test-nbd-tls-psk.sh

# This test fails on RHEL 9 aarch64 & ppc64le with the error:
# nbdkit: error: allocator=malloc: mlock: Cannot allocate memory
# It could be the mlock limit on the builder is too low.
# https://bugzilla.redhat.com/show_bug.cgi?id=2044432
%if 0%{?rhel} || (0%{?oreon} >= 11)
%ifarch aarch64 %{power64}
skip_test tests/test-memory-allocator-malloc-mlock.sh
%endif
%endif

# Make sure we can see the debug messages (RHBZ#1230160).
export LIBGUESTFS_DEBUG=1
export LIBGUESTFS_TRACE=1

%make_build check || {
    cat tests/test-suite.log
    exit 1
  }
popd
%endif


%if 0%{?have_ocaml}
%ldconfig_scriptlets plugin-ocaml
%endif


%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}
# if with_selinux
%endif


%files
# metapackage so empty


%files server
%doc README.md
%license LICENSE
%{_sbindir}/nbdkit
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/nbdkit-null-plugin.so
%dir %{_libdir}/%{name}/filters
%{_mandir}/man1/nbdkit.1*
%{_mandir}/man1/nbdkit-captive.1*
%{_mandir}/man1/nbdkit-client.1*
%{_mandir}/man1/nbdkit-loop.1*
%{_mandir}/man1/nbdkit-null-plugin.1*
%{_mandir}/man1/nbdkit-probing.1*
%{_mandir}/man1/nbdkit-protocol.1*
%{_mandir}/man1/nbdkit-service.1*
%{_mandir}/man1/nbdkit-security.1*
%{_mandir}/man1/nbdkit-tls.1*


%files basic-plugins
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-data-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-eval-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-file-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-floppy-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-full-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-info-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-memory-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-ones-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-partitioning-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-pattern-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-random-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-sh-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-sparse-random-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-split-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-zero-plugin.so
%{_mandir}/man1/nbdkit-data-plugin.1*
%{_mandir}/man1/nbdkit-eval-plugin.1*
%{_mandir}/man1/nbdkit-file-plugin.1*
%{_mandir}/man1/nbdkit-floppy-plugin.1*
%{_mandir}/man1/nbdkit-full-plugin.1*
%{_mandir}/man1/nbdkit-info-plugin.1*
%{_mandir}/man1/nbdkit-memory-plugin.1*
%{_mandir}/man1/nbdkit-ones-plugin.1*
%{_mandir}/man1/nbdkit-partitioning-plugin.1*
%{_mandir}/man1/nbdkit-pattern-plugin.1*
%{_mandir}/man1/nbdkit-random-plugin.1*
%{_mandir}/man3/nbdkit-sh-plugin.3*
%{_mandir}/man1/nbdkit-sparse-random-plugin.1*
%{_mandir}/man1/nbdkit-split-plugin.1*
%{_mandir}/man1/nbdkit-zero-plugin.1*


%files example-plugins
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-example*-plugin.so
%if !0%{?rhel} || (0%{?oreon} >= 11)
%{_libdir}/%{name}/plugins/nbdkit-example4-plugin
%endif
%{_mandir}/man1/nbdkit-example*-plugin.1*


%if 0%{?have_blkio}
%files blkio-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-blkio-plugin.so
%{_mandir}/man1/nbdkit-blkio-plugin.1*
%endif


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files cc-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-cc-plugin.so
%{_mandir}/man3/nbdkit-cc-plugin.3*
%endif


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files cdi-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-cdi-plugin.so
%{_mandir}/man1/nbdkit-cdi-plugin.1*
%endif


%files curl-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-curl-plugin.so
%{_mandir}/man1/nbdkit-curl-plugin.1*


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files gcs-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-gcs-plugin
%{_mandir}/man1/nbdkit-gcs-plugin.1*
%endif


%if !0%{?rhel} && 0%{?have_libguestfs} || (0%{?oreon} >= 11)
%files guestfs-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-guestfs-plugin.so
%{_mandir}/man1/nbdkit-guestfs-plugin.1*
%endif


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files iso-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-iso-plugin.so
%{_mandir}/man1/nbdkit-iso-plugin.1*
%endif


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files libvirt-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-libvirt-plugin.so
%{_mandir}/man1/nbdkit-libvirt-plugin.1*
%endif


%files linuxdisk-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-linuxdisk-plugin.so
%{_mandir}/man1/nbdkit-linuxdisk-plugin.1*


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files lua-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-lua-plugin.so
%{_mandir}/man3/nbdkit-lua-plugin.3*
%endif


%files nbd-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-nbd-plugin.so
%{_mandir}/man1/nbdkit-nbd-plugin.1*


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files nfs-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-nfs-plugin.so
%{_mandir}/man1/nbdkit-nfs-plugin.1*
%endif


%if !0%{?rhel} && 0%{?have_ocaml} || (0%{?oreon} >= 11)
%files ocaml-plugin
%doc README.md
%license LICENSE
%{_libdir}/libnbdkitocaml.so.*

%files ocaml-plugin-devel
%{_libdir}/libnbdkitocaml.so
%{_libdir}/ocaml/NBDKit.*
%{_mandir}/man3/nbdkit-ocaml-plugin.3*
%{_mandir}/man3/NBDKit.3*
%endif


%files ondemand-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-ondemand-plugin.so
%{_mandir}/man1/nbdkit-ondemand-plugin.1*


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files perl-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-perl-plugin.so
%{_mandir}/man3/nbdkit-perl-plugin.3*
%endif


%files python-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-python-plugin.so
%{_mandir}/man3/nbdkit-python-plugin.3*


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files S3-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-S3-plugin
%{_mandir}/man1/nbdkit-S3-plugin.1*
%endif


%files ssh-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-ssh-plugin.so
%{_mandir}/man1/nbdkit-ssh-plugin.1*


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files tcl-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-tcl-plugin.so
%{_mandir}/man3/nbdkit-tcl-plugin.3*
%endif


%files tmpdisk-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-tmpdisk-plugin.so
%{_mandir}/man1/nbdkit-tmpdisk-plugin.1*


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files torrent-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-torrent-plugin.so
%{_mandir}/man1/nbdkit-torrent-plugin.1*
%endif


%ifarch x86_64
%files vddk-plugin
%doc README.md plugins/vddk/README.VDDK
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-vddk-plugin.so
%{_mandir}/man1/nbdkit-vddk-plugin.1*
%endif


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files vram-plugin
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-vram-plugin.so
%{_mandir}/man1/nbdkit-vram-plugin.1*
%endif


%files basic-filters
%doc README.md
%license LICENSE
%{_libdir}/%{name}/filters/nbdkit-blocksize-filter.so
%{_libdir}/%{name}/filters/nbdkit-blocksize-policy-filter.so
%{_libdir}/%{name}/filters/nbdkit-cache-filter.so
%{_libdir}/%{name}/filters/nbdkit-checkwrite-filter.so
%{_libdir}/%{name}/filters/nbdkit-count-filter.so
%{_libdir}/%{name}/filters/nbdkit-cow-filter.so
%{_libdir}/%{name}/filters/nbdkit-ddrescue-filter.so
%{_libdir}/%{name}/filters/nbdkit-delay-filter.so
%{_libdir}/%{name}/filters/nbdkit-error-filter.so
%{_libdir}/%{name}/filters/nbdkit-evil-filter.so
%{_libdir}/%{name}/filters/nbdkit-exitlast-filter.so
%{_libdir}/%{name}/filters/nbdkit-exitwhen-filter.so
%{_libdir}/%{name}/filters/nbdkit-exportname-filter.so
%{_libdir}/%{name}/filters/nbdkit-extentlist-filter.so
%{_libdir}/%{name}/filters/nbdkit-fua-filter.so
%{_libdir}/%{name}/filters/nbdkit-gzip-filter.so
%{_libdir}/%{name}/filters/nbdkit-indexed-gzip-filter.so
%{_libdir}/%{name}/filters/nbdkit-ip-filter.so
%{_libdir}/%{name}/filters/nbdkit-limit-filter.so
%{_libdir}/%{name}/filters/nbdkit-log-filter.so
%{_libdir}/%{name}/filters/nbdkit-luks-filter.so
%{_libdir}/%{name}/filters/nbdkit-map-filter.so
%{_libdir}/%{name}/filters/nbdkit-multi-conn-filter.so
%{_libdir}/%{name}/filters/nbdkit-nocache-filter.so
%{_libdir}/%{name}/filters/nbdkit-noextents-filter.so
%{_libdir}/%{name}/filters/nbdkit-nofilter-filter.so
%{_libdir}/%{name}/filters/nbdkit-noparallel-filter.so
%{_libdir}/%{name}/filters/nbdkit-nozero-filter.so
%{_libdir}/%{name}/filters/nbdkit-offset-filter.so
%{_libdir}/%{name}/filters/nbdkit-openonce-filter.so
%{_libdir}/%{name}/filters/nbdkit-partition-filter.so
%{_libdir}/%{name}/filters/nbdkit-pause-filter.so
%{_libdir}/%{name}/filters/nbdkit-protect-filter.so
%if !0%{?rhel} || (0%{?oreon} >= 11)
%{_libdir}/%{name}/filters/nbdkit-qcow2dec-filter.so
%endif
%{_libdir}/%{name}/filters/nbdkit-rate-filter.so
%{_libdir}/%{name}/filters/nbdkit-readahead-filter.so
%{_libdir}/%{name}/filters/nbdkit-readonly-filter.so
%{_libdir}/%{name}/filters/nbdkit-retry-filter.so
%{_libdir}/%{name}/filters/nbdkit-retry-request-filter.so
%{_libdir}/%{name}/filters/nbdkit-rotational-filter.so
%{_libdir}/%{name}/filters/nbdkit-scan-filter.so
%{_libdir}/%{name}/filters/nbdkit-spinning-filter.so
%{_libdir}/%{name}/filters/nbdkit-swab-filter.so
%{_libdir}/%{name}/filters/nbdkit-time-limit-filter.so
%{_libdir}/%{name}/filters/nbdkit-tls-fallback-filter.so
%{_libdir}/%{name}/filters/nbdkit-truncate-filter.so
%{_libdir}/%{name}/filters/nbdkit-xor-filter.so
%{_mandir}/man1/nbdkit-blocksize-filter.1*
%{_mandir}/man1/nbdkit-blocksize-policy-filter.1*
%{_mandir}/man1/nbdkit-cache-filter.1*
%{_mandir}/man1/nbdkit-checkwrite-filter.1*
%{_mandir}/man1/nbdkit-count-filter.1*
%{_mandir}/man1/nbdkit-cow-filter.1*
%{_mandir}/man1/nbdkit-ddrescue-filter.1*
%{_mandir}/man1/nbdkit-delay-filter.1*
%{_mandir}/man1/nbdkit-error-filter.1*
%{_mandir}/man1/nbdkit-evil-filter.1*
%{_mandir}/man1/nbdkit-exitlast-filter.1*
%{_mandir}/man1/nbdkit-exitwhen-filter.1*
%{_mandir}/man1/nbdkit-exportname-filter.1*
%{_mandir}/man1/nbdkit-extentlist-filter.1*
%{_mandir}/man1/nbdkit-fua-filter.1*
%{_mandir}/man1/nbdkit-gzip-filter.1*
%{_mandir}/man1/nbdkit-indexed-gzip-filter.1*
%{_mandir}/man1/nbdkit-ip-filter.1*
%{_mandir}/man1/nbdkit-limit-filter.1*
%{_mandir}/man1/nbdkit-log-filter.1*
%{_mandir}/man1/nbdkit-luks-filter.1*
%{_mandir}/man1/nbdkit-map-filter.1*
%{_mandir}/man1/nbdkit-multi-conn-filter.1*
%{_mandir}/man1/nbdkit-nocache-filter.1*
%{_mandir}/man1/nbdkit-noextents-filter.1*
%{_mandir}/man1/nbdkit-nofilter-filter.1*
%{_mandir}/man1/nbdkit-noparallel-filter.1*
%{_mandir}/man1/nbdkit-nozero-filter.1*
%{_mandir}/man1/nbdkit-offset-filter.1*
%{_mandir}/man1/nbdkit-openonce-filter.1*
%{_mandir}/man1/nbdkit-partition-filter.1*
%{_mandir}/man1/nbdkit-pause-filter.1*
%{_mandir}/man1/nbdkit-protect-filter.1*
%if !0%{?rhel} || (0%{?oreon} >= 11)
%{_mandir}/man1/nbdkit-qcow2dec-filter.1*
%endif
%{_mandir}/man1/nbdkit-rate-filter.1*
%{_mandir}/man1/nbdkit-readahead-filter.1*
%{_mandir}/man1/nbdkit-readonly-filter.1*
%{_mandir}/man1/nbdkit-retry-filter.1*
%{_mandir}/man1/nbdkit-retry-request-filter.1*
%{_mandir}/man1/nbdkit-rotational-filter.1*
%{_mandir}/man1/nbdkit-scan-filter.1*
%{_mandir}/man1/nbdkit-spinning-filter.1*
%{_mandir}/man1/nbdkit-swab-filter.1*
%{_mandir}/man1/nbdkit-time-limit-filter.1*
%{_mandir}/man1/nbdkit-tls-fallback-filter.1*
%{_mandir}/man1/nbdkit-truncate-filter.1*
%{_mandir}/man1/nbdkit-xor-filter.1*


%files bzip2-filter
%doc README.md
%license LICENSE
%{_libdir}/%{name}/filters/nbdkit-bzip2-filter.so
%{_mandir}/man1/nbdkit-bzip2-filter.1*


%if !0%{?rhel} || (0%{?oreon} >= 11)
%files ext2-filter
%doc README.md
%license LICENSE
%{_libdir}/%{name}/filters/nbdkit-ext2-filter.so
%{_mandir}/man1/nbdkit-ext2-filter.1*
%endif


%files stats-filter
%doc README.md
%license LICENSE
%{_libdir}/%{name}/filters/nbdkit-stats-filter.so
%{_mandir}/man1/nbdkit-stats-filter.1*


%files tar-filter
%doc README.md
%license LICENSE
%{_libdir}/%{name}/filters/nbdkit-tar-filter.so
%{_mandir}/man1/nbdkit-tar-filter.1*


%files xz-filter
%doc README.md
%license LICENSE
%{_libdir}/%{name}/filters/nbdkit-lzip-filter.so
%{_libdir}/%{name}/filters/nbdkit-xz-filter.so
%{_mandir}/man1/nbdkit-lzip-filter.1*
%{_mandir}/man1/nbdkit-xz-filter.1*


%files devel
%doc BENCHMARKING OTHER_PLUGINS README.md SECURITY.md TODO.md
%license LICENSE
# Include the source of the example plugins in the documentation.
%doc plugins/example*/*.c
%if !0%{?rhel} || (0%{?oreon} >= 11)
%doc build_native/plugins/example4/nbdkit-example4-plugin
%doc plugins/lua/example.lua
%endif
%if !0%{?rhel} && 0%{?have_ocaml} || (0%{?oreon} >= 11)
%doc plugins/ocaml/example.ml
%endif
%if !0%{?rhel} || (0%{?oreon} >= 11)
%doc plugins/perl/example.pl
%endif
%doc plugins/python/examples/*.py
%doc plugins/sh/examples/*.sh
%if !0%{?rhel} || (0%{?oreon} >= 11)
%doc plugins/tcl/example.tcl
%endif
%{_includedir}/nbdkit-common.h
%{_includedir}/nbdkit-filter.h
%{_includedir}/nbdkit-plugin.h
%{_includedir}/nbdkit-version.h
%{_includedir}/nbd-protocol.h
%{_mandir}/man3/nbdkit-filter.3*
%{_mandir}/man3/nbdkit-plugin.3*
%{_mandir}/man3/nbdkit_*.3*
%{_mandir}/man1/nbdkit-release-notes-1.*.1*
%{_mandir}/man3/nbdkit-tracing.3*
%{_libdir}/pkgconfig/nbdkit.pc


%files srpm-macros
%license LICENSE
%{_rpmconfigdir}/fileattrs/nbdkit.attr
%{_rpmconfigdir}/nbdkit-find-provides


%files bash-completion
%license LICENSE
%if 0%{?fedora} || 0%{?rhel} >= 11 || (0%{?oreon} >= 11)
%dir %{bash_completions_dir}
%{bash_completions_dir}/nbdkit
%else
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/nbdkit
%endif


%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%endif


%if 0%{?have_mingw}
%files -n mingw32-%{name}
%license LICENSE
%{mingw32_sbindir}/nbdkit.exe
%{mingw32_libdir}/%{name}/
%{mingw32_libdir}/libnbdkit.a
%{mingw32_libdir}/pkgconfig/%{name}.pc
%{mingw32_includedir}/*.h


%files -n mingw64-%{name}
%license LICENSE
%{mingw64_sbindir}/nbdkit.exe
%{mingw64_libdir}/%{name}/
%{mingw64_libdir}/libnbdkit.a
%{mingw64_libdir}/pkgconfig/%{name}.pc
%{mingw64_includedir}/*.h
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.47.9-1
- Import
