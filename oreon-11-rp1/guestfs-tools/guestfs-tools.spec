%global source1_hash 5c1ca743455ea8d0fe4d6ebccaf7aaa66fb1d32468b854aae90217c06d98a933
%global source0_hash 1b326502208bfddfc98ed9ab45632e300d8db22872ff7cae09f45e0a62162825
%global source2_key_fpr F7774FB1AD074A7E8C8767EA91738F73E1B768A0
%global test_arches x86_64
%global verify_tarball_signature 1
%global source_directory 1.55-development
%{?perl_default_filter}
Summary:        Tools to access and modify virtual machine disk images
Name:          guestfs-tools
Version:       1.55.9
Release:        1%{?dist}
License:       GPL-2.0-or-later AND LGPL-2.0-or-later
ExclusiveArch: %{kernel_arches}
URL:           http://libguestfs.org/
Source0:        http://download.libguestfs.org/%{name}/%{source_directory}/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:        http://download.libguestfs.org/guestfs-tools/%{source_directory}/%{name}-%{version}.tar.gz.sig
%endif
%if 0%{verify_tarball_signature}
Source2:       libguestfs.keyring
%endif
%ifarch x86_64
%endif
%if 0%{verify_tarball_signature}
%endif
Requires:      libguestfs%{?_isa} >= 1:1.57.6-1
Requires:      curl
Requires:      gnupg2
Requires:      /usr/bin/qemu-img
Requires:      xz
Suggests:      osinfo-db
Recommends:    hwdata
Recommends:    libguestfs-xfs
Suggests:      perl
Provides:      libguestfs-tools-c = 1:%{version}-%{release}
Obsoletes:     libguestfs-tools-c <= 1:1.45.2-1
# oreon:deps
BuildRequires:  /usr/bin/pod2text
BuildRequires:  /usr/bin/qemu-img
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash-completion-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glibc-utils
BuildRequires:  gnupg2
BuildRequires:  hwdata-devel
BuildRequires:  json-c-devel
BuildRequires:  libguestfs-devel
BuildRequires:  libguestfs-xfs
BuildRequires:  libosinfo-devel
BuildRequires:  libtool
BuildRequires:  libvirt-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-gettext-devel
BuildRequires:  ocaml-libguestfs-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl(Locale::TextDomain)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Sys::Guestfs)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Win::Hivex)
BuildRequires:  perl(Win::Hivex::Regedit)
BuildRequires:  perl-generators
BuildRequires:  po4a
BuildRequires:  xorriso
BuildRequires:  xz-devel
# /oreon:deps
%description
guestfs-tools is a set of tools that can be used to make batch
configuration changes to guests, get disk used/free statistics
(virt-df), perform backups and guest clones, change
registry/UUID/hostname info, build guests from scratch (virt-builder)
and much more.

Virt-alignment-scan scans virtual machines looking for partition
alignment problems.

Virt-builder is a command line tool for rapidly making disk images
of popular free operating systems.

Virt-cat is a command line tool to display the contents of a file in a
virtual machine.

Virt-customize is a command line tool for customizing virtual machine
disk images.

Virt-df is a command line tool to display free space on virtual
machine filesystems.  Unlike other tools, it doesn’t just display the
amount of space allocated to a virtual machine, but can look inside
the virtual machine to see how much space is really being used.  It is
like the df(1) command, but for virtual machines, except that it also
works for Windows virtual machines.

Virt-diff shows the differences between virtual machines.

Virt-drivers detects the bootloader, kernel and drivers inside a guest.

Virt-edit is a command line tool to edit the contents of a file in a
virtual machine.

Virt-filesystems is a command line tool to display the filesystems,
partitions, block devices, LVs, VGs and PVs found in a disk image
or virtual machine.  It replaces the deprecated programs
virt-list-filesystems and virt-list-partitions with a much more
capable tool.

Virt-format is a command line tool to erase and make blank disks.

Virt-get-kernel extracts a kernel/initrd from a disk image.

Virt-inspector examines a virtual machine and tries to determine the
version of the OS, the kernel version, what drivers are installed,
whether the virtual machine is fully virtualized (FV) or
para-virtualized (PV), what applications are installed and more.

Virt-log is a command line tool to display the log files from a
virtual machine.

Virt-ls is a command line tool to list out files in a virtual machine.

Virt-make-fs is a command line tool to build a filesystem out of
a collection of files or a tarball.

Virt-resize can resize existing virtual machine disk images.

Virt-sparsify makes virtual machine disk images sparse (thin-provisioned).

Virt-sysprep lets you reset or unconfigure virtual machines in
preparation for cloning them.

Virt-tail follows (tails) a log file within a guest, like 'tail -f'.

%package -n virt-win-reg
Summary:       Access and modify the Windows Registry of a Windows VM
License:       GPL-2.0-or-later
BuildArch:     noarch
Provides:      libguestfs-tools = 1:%{version}-%{release}
Obsoletes:     libguestfs-tools <= 1:1.45.2-1
%description -n virt-win-reg
Virt-win-reg lets you look at and modify the Windows Registry of
Windows virtual machines.

%package bash-completion
Summary:       Bash tab-completion scripts for %{name}
BuildArch:     noarch
Requires:      bash-completion >= 2.0
Requires:      %{name} = %{version}-%{release}
%description bash-completion
Install this package if you want intelligent bash tab-completion
for the virt-* tools.

%package man-pages-ja
Summary:       Japanese (ja) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}
%description man-pages-ja
%{name}-man-pages-ja contains Japanese (ja) man pages
for %{name}.

%package man-pages-uk
Summary:       Ukrainian (uk) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}
%description man-pages-uk
%{name}-man-pages-uk contains Ukrainian (uk) man pages
for %{name}.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q
%autopatch -p1

%build

autoreconf -fiv
%{configure} INSTALL='/usr/bin/install -p'
make -j1 -C builder index-parse.c
make V=1 %{?_smp_mflags}
%check

%ifarch %{test_arches}
if grep CONFIG_DEBUG_MUTEXES=y /lib/modules/*/config ; then
    echo "Skipping tests because debug kernel is installed"
    exit 0
fi
export LIBGUESTFS_DEBUG=1
export LIBGUESTFS_TRACE=1
export SKIP_TEST_MACHINE_READABLE_SH=1
export SKIP_TEST_VIRT_FORMAT_SH=1
export SKIP_TEST_VIRT_RESIZE_PL=1
if ! make check -k ; then
    for f in `find -name test-suite.log | xargs grep -l ^FAIL:`; do
        echo '*****' $f '*****'
        cat $f
        echo
    done
    exit 1
fi
%endif
%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -delete
mv $RPM_BUILD_ROOT%{_docdir}/%{name} installed-docs
gzip --best installed-docs/*.xml
%find_lang %{name}
%oreon_autofiles virt-win-reg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pretrans -p <lua>

path = "/etc/virt-builder"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end
%files -f %{oreon_filedir}/main.list
%files -n virt-win-reg -f %{oreon_filedir}/virt-win-reg.list
%files -n guestfs-tools-bash-completion -f %{oreon_filedir}/guestfs-tools-bash-completion.list
%files -n guestfs-tools-man-pages-ja -f %{oreon_filedir}/guestfs-tools-man-pages-ja.list
%files -n guestfs-tools-man-pages-uk -f %{oreon_filedir}/guestfs-tools-man-pages-uk.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.55.5-2
- Prepare for Oreon 11 (RP1)
