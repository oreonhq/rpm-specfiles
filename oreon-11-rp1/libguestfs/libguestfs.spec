%global source0_hash none

%global source7_key_fpr F7774FB1AD074A7E8C8767EA91738F73E1B768A0

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Architectures on which golang works.
#% global golang_arches aarch64 % {arm} % {ix86} x86_64
# In theory the above, in practice golang is so often broken that
# I now disable it:
%global golang_arches NONE

# Architectures that we run the basic sanity-check test.
#
# The full test suite is done after the package has been built.  Here
# we only do a sanity check that kernel/qemu/libvirt/appliance is not
# broken.  To perform the full test suite, see instructions here:
# https://www.redhat.com/archives/libguestfs/2015-September/msg00078.html
%global test_arches aarch64 %{power64} s390x x86_64

# Trim older changelog entries.
# https://lists.fedoraproject.org/pipermail/devel/2013-April/thread.html#181627
%global _changelog_trimtime %(date +%s -d "2 years ago")

# Verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# The source directory.
%global source_directory 1.59-development

# Filter perl provides.
%{?perl_default_filter}

# Unbreak the linker.
%undefine _strict_symbol_defs_build

Summary:       Access and modify virtual machine disk images
Name:          libguestfs
Epoch:         1
Version:       1.59.4
Release:       1%{?dist}
License:       LGPL-2.1-or-later

# Build only for architectures that have a kernel
ExclusiveArch: %{kernel_arches}
%if 0%{?rhel}
# No qemu-kvm on POWER (RHBZ#1946532).
ExcludeArch: %{power64}
%endif

# Source and patches.
URL:           http://libguestfs.org/
Source0:        http://libguestfs.org/download/%{source_directory}/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:        http://libguestfs.org/download/%{source_directory}/%{name}-%{version}.tar.gz.sig
%endif

# Replacement README file.
Source4:       README-replacement.in

# Guestfish colour prompts.
Source5:       guestfish.sh

# Used to build the supermin appliance in Koji.
Source6:       yum.conf.in

# Keyring used to verify tarball signature.
%if 0%{verify_tarball_signature}
Source7:       libguestfs.keyring
%endif

# Maintainer script which helps with handling patches.
Source8:       copy-patches.sh

BuildRequires: autoconf, automake, libtool, gettext-devel

# Basic build requirements.
BuildRequires: gcc, gcc-c++
BuildRequires: make
BuildRequires: rpcgen
BuildRequires: libtirpc-devel
BuildRequires: supermin-devel >= 5.1.18
BuildRequires: hivex-devel >= 1.3.10
BuildRequires: ocaml-hivex-devel
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Pod::Man)
BuildRequires: /usr/bin/pod2text
BuildRequires: po4a
BuildRequires: augeas-devel >= 1.7.0
BuildRequires: ocaml-augeas-devel >= 0.6
BuildRequires: readline-devel
BuildRequires: xorriso
BuildRequires: libxml2-devel
BuildRequires: createrepo_c
BuildRequires: glibc-static
BuildRequires: libselinux-utils
BuildRequires: libselinux-devel
BuildRequires: fuse, fuse-devel
BuildRequires: pcre2-devel
BuildRequires: libvirt-devel >= 11.10.0
BuildRequires: gperf
BuildRequires: rpm-devel
BuildRequires: cpio
BuildRequires: libconfig-devel
%if !0%{?rhel}
BuildRequires: zip
BuildRequires: unzip
%endif
BuildRequires: systemd-units
BuildRequires: netpbm-progs
BuildRequires: icoutils
BuildRequires: libvirt-daemon-kvm
%if !0%{?rhel}
BuildRequires: perl(Expect)
%endif
BuildRequires: libacl-devel
BuildRequires: libcap-devel
%if !0%{?rhel}
BuildRequires: libldm-devel
%endif
BuildRequires: json-c-devel
BuildRequires: systemd-devel
BuildRequires: bash-completion
%if 0%{?fedora} || 0%{?rhel} >= 11
BuildRequires: bash-completion-devel
%endif
BuildRequires: /usr/bin/ping
BuildRequires: curl
BuildRequires: xz
BuildRequires: zstd
BuildRequires: libzstd-devel
BuildRequires: qemu-img >= 7.2.0

%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

# For language bindings.
BuildRequires: ocaml >= 4.08
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-findlib-devel
%if !0%{?rhel}
BuildRequires: lua
BuildRequires: lua-devel
%endif
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-macros
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::Pod::Coverage) >= 1.00
BuildRequires: perl(Module::Build)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Locale::TextDomain)
BuildRequires: python3-devel
BuildRequires: python3-libvirt
%if !0%{?rhel}
BuildRequires: ruby-devel
BuildRequires: rubygem-rake
# json is not pulled in automatically, see RHBZ#1325022
BuildRequires: rubygem(json)
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(irb)
BuildRequires: php-devel
%endif
%ifarch %{golang_arches}
BuildRequires: golang
%endif

# Build requirements for the appliance.
#
# Get the initial list by doing:
#   for f in `cat appliance/packagelist`; do echo $f; done | sort -u
# However you have to edit the list down to packages which exist in
# current Fedora, since supermin ignores non-existent packages.

BuildRequires: acl
BuildRequires: attr
BuildRequires: augeas-libs
BuildRequires: bash
BuildRequires: binutils
%if !0%{?rhel}
BuildRequires: btrfs-progs
%endif
BuildRequires: bzip2
BuildRequires: clevis-luks
BuildRequires: coreutils
BuildRequires: cpio
BuildRequires: cryptsetup
BuildRequires: dhcpcd
BuildRequires: diffutils
BuildRequires: dosfstools
BuildRequires: e2fsprogs
BuildRequires: file
BuildRequires: findutils
BuildRequires: gawk
%if !0%{?rhel}
BuildRequires: gdisk
BuildRequires: gfs2-utils
%endif
BuildRequires: grep
BuildRequires: gzip
%if !0%{?rhel}
%ifnarch ppc
BuildRequires: hfsplus-tools
%endif
%endif
BuildRequires: hivex-libs
BuildRequires: iproute
BuildRequires: iputils
BuildRequires: kernel
BuildRequires: kmod
BuildRequires: less
BuildRequires: libcap
%if !0%{?rhel}
BuildRequires: libldm
%endif
BuildRequires: libselinux
BuildRequires: libxml2
BuildRequires: lsof
BuildRequires: lsscsi
BuildRequires: lvm2
BuildRequires: lzop
BuildRequires: mdadm
%if !0%{?rhel}
BuildRequires: ntfs-3g ntfsprogs ntfs-3g-system-compression
%endif
BuildRequires: openssh-clients
BuildRequires: parted
BuildRequires: pciutils
BuildRequires: pcre2
BuildRequires: policycoreutils
BuildRequires: procps
BuildRequires: psmisc
BuildRequires: rpm-libs
BuildRequires: rsync
BuildRequires: scrub
BuildRequires: sed
%if !0%{?rhel}
BuildRequires: sleuthkit
BuildRequires: squashfs-tools
%endif
BuildRequires: strace
%if !0%{?rhel}
%ifarch %{ix86} x86_64
BuildRequires: syslinux syslinux-extlinux
%endif
%endif
BuildRequires: systemd
BuildRequires: tar
BuildRequires: udev
BuildRequires: util-linux
BuildRequires: vim-minimal
BuildRequires: xfsprogs
BuildRequires: xz
%if !0%{?rhel}
BuildRequires: zerofree
%endif
BuildRequires: zstd

# Main package requires the appliance.  This allows the appliance to
# be replaced if there exists a package called
# "libguestfs-noappliance".  This package is not provided anywhere,
# you have to provide the dependency or make the package yourself.  If
# you do then libguestfs won't install the appliance and you are free
# to replace it with (eg) a fixed appliance.
Requires:      (%{name}-appliance = %{epoch}:%{version}-%{release} or %{name}-noappliance)

# The daemon dependencies are not included automatically, because it
# is buried inside the appliance, so list them here.
Requires:      augeas-libs%{?_isa} >= 1.7.0
Requires:      json-c%{?_isa}
Requires:      libacl%{?_isa}
Requires:      libcap%{?_isa}
Requires:      libselinux%{?_isa}
Requires:      hivex-libs%{?_isa} >= 1.3.10
Requires:      pcre2%{?_isa}
Requires:      rpm-libs%{?_isa} >= 4.16.1.3
Requires:      systemd-libs%{?_isa}

# For core mount-local (FUSE) API.
Requires:      fuse

# For core APIs:
Requires:      qemu-img
Requires:      coreutils
Requires:      grep
Requires:      tar

# libguestfs-make-fixed-appliance requires xz.
Requires:      xz

# For qemu direct and libvirt backends.
Requires:      qemu-kvm-core >= 7.2.0
%if !0%{?rhel}
Suggests:      qemu-block-curl
Suggests:      qemu-block-iscsi
%endif
Suggests:      qemu-block-rbd
%if !0%{?rhel}
Suggests:      qemu-block-ssh
%endif
Recommends:    libvirt-daemon-config-network
Requires:      libvirt-daemon-driver-qemu >= 11.10.0
Requires:      libvirt-daemon-driver-secret
Requires:      libvirt-daemon-driver-storage-core
Requires:      passt
Requires:      (selinux-policy >= 3.11.1-63 if selinux-policy)

%ifarch aarch64
Requires:      edk2-aarch64
%endif

# For guestfish.
#Requires:      /usr/bin/emacs #theoretically, but too large
Requires:      /usr/bin/hexedit
Requires:      /usr/bin/less
Requires:      /usr/bin/man
Requires:      /usr/bin/vi

%if !0%{?rhel}
# Someone managed to install libguestfs-winsupport (from RHEL!) on
# Fedora, which breaks everything.  Thus:
Conflicts:     libguestfs-winsupport
%else
Conflicts:     libguestfs-winsupport < 7.2
%endif


%description
Libguestfs is a library for accessing and modifying virtual machine
disk images.  http://libguestfs.org

Libguestfs uses Linux kernel and qemu code, and can access any type of
guest filesystem that Linux and qemu can, including but not limited
to: ext2/3/4, btrfs, FAT and NTFS, LVM, many different disk partition
schemes, qcow, qcow2, vmdk.

For enhanced features, install:

%if !0%{?rhel}
     libguestfs-forensics  adds filesystem forensics support
          libguestfs-gfs2  adds Global Filesystem (GFS2) support
       libguestfs-hfsplus  adds HFS+ (Mac filesystem) support
%endif
 libguestfs-inspect-icons  adds support for inspecting guest icons
        libguestfs-rescue  enhances virt-rescue shell with more tools
         libguestfs-rsync  rsync to/from guest filesystems
%if !0%{?rhel}
           libguestfs-ufs  adds UFS (BSD) support
%endif
           libguestfs-xfs  adds XFS support

For developers:

         libguestfs-devel  C/C++ header files and library

Language bindings:

%ifarch %{golang_arches}
           golang-guestfs  Go language bindings
%endif
%if !0%{?rhel}
              lua-guestfs  Lua bindings
%endif
   ocaml-libguestfs-devel  OCaml bindings
         perl-Sys-Guestfs  Perl bindings
%if !0%{?rhel}
           php-libguestfs  PHP bindings
%endif
       python3-libguestfs  Python 3 bindings
%if !0%{?rhel}
          ruby-libguestfs  Ruby bindings
%endif


%package appliance
Summary:       Appliance for %{name}
License:       GPL-2.0-or-later AND LGPL-2.1-or-later
Requires:      supermin >= 5.1.18


%description appliance
%{name}-appliance provides the appliance used by libguestfs.


%package devel
Summary:       Development tools and libraries for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:      pkgconfig


%description devel
%{name}-devel contains development tools and libraries
for %{name}.


%if !0%{?rhel}
%package forensics
Summary:       Filesystem forensics support for %{name}
License:       GPL-2.0-or-later
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description forensics
This adds filesystem forensics support to %{name}.  Install it if you
want to forensically analyze disk images using The Sleuth Kit.
%endif


%if !0%{?rhel}
%package gfs2
Summary:       GFS2 support for %{name}
License:       GPL-2.0-or-later
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description gfs2
This adds GFS2 support to %{name}.  Install it if you want to process
disk images containing GFS2.
%endif


%if !0%{?rhel}
%ifnarch ppc
%package hfsplus
Summary:       HFS+ support for %{name}
License:       GPL-2.0-or-later
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description hfsplus
This adds HFS+ support to %{name}.  Install it if you want to process
disk images containing HFS+ / Mac OS Extended filesystems.
%endif
%endif


%package rescue
Summary:       virt-rescue shell
License:       GPL-2.0-or-later
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description rescue
This adds the virt-rescue shell which is a "rescue disk" for virtual
machines, and additional tools to use inside the shell such as ssh,
network utilities, editors and debugging utilities.


%package rsync
Summary:       rsync support for %{name}
License:       GPL-2.0-or-later
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description rsync
This adds rsync support to %{name}.  Install it if you want to use
rsync to upload or download files into disk images.


%if !0%{?rhel}
%package ufs
Summary:       UFS (BSD) support for %{name}
License:       GPL-2.0-or-later
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description ufs
This adds UFS support to %{name}.  Install it if you want to process
disk images containing UFS (BSD filesystems).
%endif


%package xfs
Summary:       XFS support for %{name}
License:       GPL-2.0-or-later
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description xfs
This adds XFS support to %{name}.  Install it if you want to process
disk images containing XFS.


%package inspect-icons
Summary:       Additional dependencies for inspecting guest icons
License:       LGPL-2.1-or-later
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

Requires:      netpbm-progs
Requires:      icoutils


%description inspect-icons
%{name}-inspect-icons is a metapackage that pulls in additional
dependencies required by libguestfs to pull icons out of non-Linux
guests.  Install this package if you want libguestfs to be able to
inspect non-Linux guests and display icons from them.

The only reason this is a separate package is to avoid core libguestfs
having to depend on Perl.  See https://bugzilla.redhat.com/1194158


%package bash-completion
Summary:       Bash tab-completion scripts for %{name} tools
License:       GPL-2.0-or-later
BuildArch:     noarch
Requires:      bash-completion >= 2.0


%description bash-completion
Install this package if you want intelligent bash tab-completion
for guestfish, guestmount and various virt-* tools.


%package -n ocaml-%{name}
Summary:       OCaml bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}


%description -n ocaml-%{name}
ocaml-%{name} contains OCaml bindings for %{name}.

This is for toplevel and scripting access only.  To compile OCaml
programs which use %{name} you will also need ocaml-%{name}-devel.


%package -n ocaml-%{name}-devel
Summary:       OCaml bindings for %{name}
Requires:      ocaml-%{name}%{?_isa} = %{epoch}:%{version}-%{release}


%description -n ocaml-%{name}-devel
ocaml-%{name}-devel contains development libraries
required to use the OCaml bindings for %{name}.


%package -n perl-Sys-Guestfs
Summary:       Perl bindings for %{name} (Sys::Guestfs)
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}


%description -n perl-Sys-Guestfs
perl-Sys-Guestfs contains Perl bindings for %{name} (Sys::Guestfs).


%package -n python3-%{name}
Summary:       Python 3 bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}


%description -n python3-%{name}
python3-%{name} contains Python 3 bindings for %{name}.


%if !0%{?rhel}
%package -n ruby-%{name}
Summary:       Ruby bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:      ruby(release)
Requires:      ruby
Provides:      ruby(guestfs) = %{version}

%description -n ruby-%{name}
ruby-%{name} contains Ruby bindings for %{name}.


%package -n php-%{name}
Summary:       PHP bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	php(zend-abi)
Requires:	php(api)

%description -n php-%{name}
php-%{name} contains PHP bindings for %{name}.


%package -n lua-guestfs
Summary:       Lua bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:      lua

%description -n lua-guestfs
lua-guestfs contains Lua bindings for %{name}.
%endif



%ifarch %{golang_arches}
%package -n golang-guestfs
Summary:       Golang bindings for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      golang
Provides:      golang(libguestfs.org) = %{epoch}:%{version}-%{release}

%description -n golang-guestfs
golang-%{name} contains Go language bindings for %{name}.
%endif


%package man-pages-ja
Summary:       Japanese (ja) man pages for %{name}
License:       GPL-2.0-or-later
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description man-pages-ja
%{name}-man-pages-ja contains Japanese (ja) man pages
for %{name}.


%package man-pages-uk
Summary:       Ukrainian (uk) man pages for %{name}
License:       GPL-2.0-or-later
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description man-pages-uk
%{name}-man-pages-uk contains Ukrainian (uk) man pages
for %{name}.


%prep
%(test -z "%{source7_key_fpr}" || { f="%{SOURCE7}"; test -f "$f" || { echo "oreon: missing Source7 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source7_key_fpr}" || { echo "oreon: Source7 key fingerprint mismatch" >&2; exit 1; }; })
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE7}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q
%autopatch -p1

# ACLOCAL_PATH is temporarily required to work around
# https://bugzilla.redhat.com/show_bug.cgi?id=2366708
export ACLOCAL_PATH=/usr/share/gettext/m4/
autoreconf -fiv

# For sVirt to work, the local temporary directory we use in the tests
# must be labelled the same way as /tmp.  This doesn't work if either
# the directory is on NFS (no SELinux labels) or if SELinux is
# disabled, hence the tests.
if [ "$(stat -f -L -c %T .)" != "nfs" ] && \
   [ "$(getenforce | tr '[A-Z]' '[a-z]')" != "disabled" ]; then
    chcon --reference=/tmp tmp
fi

# Replace developer-centric README that ships with libguestfs, with
# our replacement file.
mv README README.orig
sed 's/@VERSION@/%{version}/g' < %{SOURCE4} > README


%build
# Test if network is available.
ip addr list ||:
ip route list ||:
if ping -c 3 -w 20 8.8.8.8 && curl http://libguestfs.org -o /dev/null; then
  extra=
else
  mkdir cachedir repo
  # For an explanation of what we are doing here, see:
  # https://lists.fedorahosted.org/archives/list/koji-devel@lists.fedorahosted.org/thread/ZIBY53JAURLT3QRBBJIJJ7EZWLZDE3TI/
  # -n 1 because of RHBZ#980502.
  dirs=
  for d in /var/cache/{dnf,libdnf5,yum} ; do
    if test -d $d ; then dirs="$dirs $d" ; fi
  done
  test -n "$dirs"
  find $dirs -type f -name '*.rpm' -print0 | xargs -0 -n 1 cp -t repo
  createrepo_c repo
  sed -e "s|@PWD@|$(pwd)|" %{SOURCE6} > yum.conf
  extra=--with-supermin-packager-config=$(pwd)/yum.conf
fi

%{configure} \
%if 0%{?rhel}
  QEMU=%{_libexecdir}/qemu-kvm \
%endif
  PYTHON=%{__python3} \
  --with-default-backend=libvirt \
  --enable-appliance-format-auto \
%if !0%{?rhel}
  --with-extra="fedora=%{fedora},release=%{release},libvirt" \
%else
  --with-extra="rhel=%{rhel},release=%{release},libvirt" \
%endif
%if 0%{?rhel}
  --with-qemu="qemu-kvm qemu-system-%{_build_arch} qemu" \
%endif
%ifnarch %{golang_arches}
  --disable-golang \
%endif
  --without-java \
  --disable-erlang \
%if 0%{?rhel}
  --disable-lua \
  --disable-php \
  --disable-ruby \
%endif
  $extra

# 'INSTALLDIRS' ensures that Perl and Ruby libs are installed in the
# vendor dir not the site dir.
%make_build INSTALLDIRS=vendor


%check
%ifarch %{test_arches}
# Only run the tests with non-debug (ie. non-Rawhide) kernels.
# XXX This tests for any debug kernel installed.
if grep CONFIG_DEBUG_MUTEXES=y /lib/modules/*/config ; then
    echo "Skipping tests because debug kernel is installed"
    exit 0
fi

export LIBGUESTFS_DEBUG=1
export LIBGUESTFS_TRACE=1
export LIBVIRT_DEBUG=1

if ! make quickcheck QUICKCHECK_TEST_TOOL_ARGS="-t 1200"; then
    cat $HOME/.cache/libvirt/qemu/log/*
    exit 1
fi

# As libvirt is the default backend, test that the direct backend
# works too.  It's a good place to get test coverage across all the
# architectures.
if ! LIBGUESTFS_BACKEND=direct \
     make quickcheck QUICKCHECK_TEST_TOOL_ARGS="-t 1200"; then
    cat $HOME/.cache/libvirt/qemu/log/*
    exit 1
fi
%endif


%install
# 'INSTALLDIRS' ensures that Perl and Ruby libs are installed in the
# vendor dir not the site dir.
%make_install INSTALLDIRS=vendor

# Delete static libraries.
rm $( find $RPM_BUILD_ROOT -name '*.a' | grep -v /ocaml/ )

# Delete libtool files.
find $RPM_BUILD_ROOT -name '*.la' -delete

# Delete some bogus Perl files.
find $RPM_BUILD_ROOT -name perllocal.pod -delete
find $RPM_BUILD_ROOT -name .packlist -delete
find $RPM_BUILD_ROOT -name '*.bs' -delete
find $RPM_BUILD_ROOT -name 'bindtests.pl' -delete

# debuginfo generation fails with debugedit >= 5.1 unless the files
# are writable:
find $RPM_BUILD_ROOT -name Guestfs.so -exec chmod u+w {} \;

# golang: Ignore what libguestfs upstream installs, and just copy the
# source files to %%{_datadir}/gocode/src.
%ifarch %{golang_arches}
rm -r $RPM_BUILD_ROOT/usr/lib/golang
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gocode/src
cp -a golang/src/libguestfs.org $RPM_BUILD_ROOT%{_datadir}/gocode/src
%endif

# Split up the monolithic packages file in the supermin appliance so
# we can install dependencies in subpackages.
pushd $RPM_BUILD_ROOT%{_libdir}/guestfs/supermin.d

function remove
{
    grep -Ev "^$1$" < packages > packages-t
    mv packages-t packages
}

function move_to
{
    if ! grep -Esq "^$1$" packages; then
        echo "move_to $1: package name not found in packages file"
        exit 1
    fi
    remove "$1"
    echo "$1" >> "$2"
}

%if !0%{?rhel}
move_to sleuthkit       zz-packages-forensics
move_to gfs2-utils      zz-packages-gfs2
move_to hfsplus-tools   zz-packages-hfsplus
%else
remove sleuthkit
remove gfs2-utils
remove hfsplus-tools
%endif
move_to iputils         zz-packages-rescue
move_to lsof            zz-packages-rescue
move_to openssh-clients zz-packages-rescue
move_to pciutils        zz-packages-rescue
move_to strace          zz-packages-rescue
move_to vim-minimal     zz-packages-rescue
move_to rsync           zz-packages-rsync
move_to xfsprogs        zz-packages-xfs

%if !0%{?rhel}
# On Fedora you need kernel-modules-extra to be able to mount
# UFS (BSD) filesystems.
echo "kernel-modules-extra" > zz-packages-ufs
%endif

popd

# If there is a bogus dependency on kernel-*, rename it to 'kernel'
# instead.  This can happen for various reasons:
# - DNF picks kernel-debug instead of kernel.
# - Version of kernel-rt in brew > version of kernel.
# On all known architectures, depending on 'kernel' should
# mean "we need a kernel".
pushd $RPM_BUILD_ROOT%{_libdir}/guestfs/supermin.d
sed -i 's/^kernel-.*/kernel/' packages
popd

# Guestfish colour prompts.
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

# Remove the .gitignore file from ocaml/html which will be copied to docdir.
rm ocaml/html/.gitignore


# Find locale files.
%find_lang %{name}


%files -f %{name}.lang
%license COPYING COPYING.LIB
%doc README
%{_bindir}/guestfish
%{_bindir}/guestmount
%{_bindir}/guestunmount
%{_bindir}/libguestfs-test-tool
%{_bindir}/virt-copy-in
%{_bindir}/virt-copy-out
%{_bindir}/virt-tar-in
%{_bindir}/virt-tar-out
%{_sbindir}/libguestfs-make-fixed-appliance
%{_libdir}/libguestfs.so.*
%{_mandir}/man1/guestfish.1*
%{_mandir}/man1/guestfs-faq.1*
%{_mandir}/man1/guestfs-performance.1*
%{_mandir}/man1/guestfs-recipes.1*
%{_mandir}/man1/guestfs-release-notes-1*.1*
%{_mandir}/man1/guestfs-release-notes.1*
%{_mandir}/man1/guestfs-security.1*
%{_mandir}/man1/guestmount.1*
%{_mandir}/man1/guestunmount.1*
%{_mandir}/man1/libguestfs-make-fixed-appliance.1*
%{_mandir}/man1/libguestfs-test-tool.1*
%{_mandir}/man1/virt-copy-in.1*
%{_mandir}/man1/virt-copy-out.1*
%{_mandir}/man1/virt-tar-in.1*
%{_mandir}/man1/virt-tar-out.1*
%{_mandir}/man5/libguestfs-tools.conf.5*
%config %{_sysconfdir}/profile.d/guestfish.sh
%config(noreplace) %{_sysconfdir}/libguestfs-tools.conf


%files appliance
%{_libdir}/guestfs/
%exclude %{_libdir}/guestfs/supermin.d/zz-packages-*


%files devel
%doc AUTHORS HACKING TODO README
%doc examples/*.c
%{_libdir}/libguestfs.so
%{_mandir}/man1/guestfs-building.1*
%{_mandir}/man1/guestfs-hacking.1*
%{_mandir}/man1/guestfs-internals.1*
%{_mandir}/man1/guestfs-testing.1*
%{_mandir}/man3/guestfs.3*
%{_mandir}/man3/guestfs-examples.3*
%{_mandir}/man3/libguestfs.3*
%{_includedir}/guestfs.h
%{_libdir}/pkgconfig/libguestfs.pc


%if !0%{?rhel}
%files forensics
%{_libdir}/guestfs/supermin.d/zz-packages-forensics
%endif

%if !0%{?rhel}
%files gfs2
%{_libdir}/guestfs/supermin.d/zz-packages-gfs2
%endif

%if !0%{?rhel}
%ifnarch ppc
%files hfsplus
%{_libdir}/guestfs/supermin.d/zz-packages-hfsplus
%endif
%endif

%files rsync
%{_libdir}/guestfs/supermin.d/zz-packages-rsync

%files rescue
%{_libdir}/guestfs/supermin.d/zz-packages-rescue
%{_bindir}/virt-rescue
%{_mandir}/man1/virt-rescue.1*

%if !0%{?rhel}
%files ufs
%{_libdir}/guestfs/supermin.d/zz-packages-ufs
%endif

%files xfs
%{_libdir}/guestfs/supermin.d/zz-packages-xfs

%files inspect-icons
# no files


%files bash-completion
%if 0%{?fedora} || 0%{?rhel} >= 11
%dir %{bash_completions_dir}
%{bash_completions_dir}/guestfish
%{bash_completions_dir}/guestmount
%{bash_completions_dir}/guestunmount
%{bash_completions_dir}/libguestfs-test-tool
%{bash_completions_dir}/virt-copy-in
%{bash_completions_dir}/virt-copy-out
%{bash_completions_dir}/virt-rescue
%{bash_completions_dir}/virt-tar-in
%{bash_completions_dir}/virt-tar-out
%else
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/guestfish
%{_datadir}/bash-completion/completions/guestmount
%{_datadir}/bash-completion/completions/guestunmount
%{_datadir}/bash-completion/completions/libguestfs-test-tool
%{_datadir}/bash-completion/completions/virt-copy-in
%{_datadir}/bash-completion/completions/virt-copy-out
%{_datadir}/bash-completion/completions/virt-rescue
%{_datadir}/bash-completion/completions/virt-tar-in
%{_datadir}/bash-completion/completions/virt-tar-out
%endif


%files -n ocaml-%{name}
%{_libdir}/ocaml/guestfs
%exclude %{_libdir}/ocaml/guestfs/*.a
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/guestfs/*.cmxa
%exclude %{_libdir}/ocaml/guestfs/*.cmx
%endif
%exclude %{_libdir}/ocaml/guestfs/*.mli
%{_libdir}/ocaml/stublibs/dllmlguestfs.so
%{_libdir}/ocaml/stublibs/dllmlguestfs.so.owner


%files -n ocaml-%{name}-devel
%doc ocaml/examples/*.ml ocaml/html
%{_libdir}/ocaml/guestfs/*.a
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/guestfs/*.cmxa
%{_libdir}/ocaml/guestfs/*.cmx
%endif
%{_libdir}/ocaml/guestfs/*.mli
%{_mandir}/man3/guestfs-ocaml.3*


%files -n perl-Sys-Guestfs
%doc perl/examples/*.pl
%{perl_vendorarch}/*
%{_mandir}/man3/Sys::Guestfs.3pm*
%{_mandir}/man3/guestfs-perl.3*


%files -n python3-%{name}
%doc python/examples/*.py
%{python3_sitearch}/libguestfsmod*.so
%{python3_sitearch}/guestfs.py
%{python3_sitearch}/__pycache__/guestfs*.py*
%{_mandir}/man3/guestfs-python.3*


%if !0%{?rhel}
%files -n ruby-%{name}
%doc ruby/examples/*.rb
%doc ruby/doc/site/*
%{ruby_vendorlibdir}/guestfs.rb
%{ruby_vendorarchdir}/_guestfs.so
%{_mandir}/man3/guestfs-ruby.3*


%files -n php-%{name}
%doc php/README-PHP
%dir %{_sysconfdir}/php.d
%{_sysconfdir}/php.d/guestfs_php.ini
%{_libdir}/php/modules/guestfs_php.so


%files -n lua-guestfs
%doc lua/examples/*.lua
%doc lua/examples/LICENSE
%{_libdir}/lua/*/guestfs.so
%{_mandir}/man3/guestfs-lua.3*
%endif


%ifarch %{golang_arches}
%files -n golang-guestfs
%doc golang/examples/*.go
%doc golang/examples/LICENSE
%{_datadir}/gocode/src/libguestfs.org
%{_mandir}/man3/guestfs-golang.3*
%endif


%files man-pages-ja
%lang(ja) %{_mandir}/ja/man1/*.1*
%lang(ja) %{_mandir}/ja/man3/*.3*
%lang(ja) %{_mandir}/ja/man5/*.5*


%files man-pages-uk
%lang(uk) %{_mandir}/uk/man1/*.1*
%lang(uk) %{_mandir}/uk/man3/*.3*
%lang(uk) %{_mandir}/uk/man5/*.5*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.59.4-1
- Prepare for Oreon 11 (RP1)
