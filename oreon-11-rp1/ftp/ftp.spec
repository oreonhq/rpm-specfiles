%global source0_hash 61c913299b81a4671ff089aac821329f7db9bc111aa812993dd585798b700349

Summary: The standard UNIX FTP (File Transfer Protocol) client
Name: ftp
Version: 0.17
Release: 100%{?dist}
License: BSD-4-Clause-UC
# The Upstream of ftp is no longer active.
# The source file for ftp is no longer available anywhere
# else than in Fedora repos.
Source0: netkit-ftp-%{version}.tar.gz
Patch1: netkit-ftp-0.17-pre20000412.pasv-security.patch
Patch2: netkit-ftp-0.17-acct.patch
Patch3: netkit-ftp.usagi-ipv6.patch
Patch4: netkit-ftp-0.17-segv.patch
Patch5: netkit-ftp-0.17-volatile.patch
Patch6: netkit-ftp-0.17-runique_mget.patch
Patch7: netkit-ftp-locale.patch
Patch8: netkit-ftp-0.17-printf.patch
Patch9: netkit-ftp-0.17-longint.patch
Patch10: netkit-ftp-0.17-vsftp165083.patch
Patch11: netkit-ftp-0.17-C-Frame121.patch
Patch12: netkit-ftp-0.17-data.patch
Patch13: netkit-ftp-0.17-multihome.patch
Patch14: netkit-ftp-0.17-longnames.patch
Patch15: netkit-ftp-0.17-multiipv6.patch
Patch16: netkit-ftp-0.17-nodebug.patch
Patch17: netkit-ftp-0.17-stamp.patch
Patch18: netkit-ftp-0.17-sigseg.patch
Patch19: netkit-ftp-0.17-size.patch
Patch20: netkit-ftp-0.17-fdleak.patch
Patch21: netkit-ftp-0.17-fprintf.patch
Patch22: netkit-ftp-0.17-bitrate.patch
Patch23: netkit-ftp-0.17-arg_max.patch
Patch24: netkit-ftp-0.17-case.patch
Patch25: netkit-ftp-0.17-chkmalloc.patch
Patch26: netkit-ftp-0.17-man.patch
Patch27: netkit-ftp-0.17-acct_ovl.patch
Patch28: netkit-ftp-0.17-remove-nested-include.patch
Patch29: netkit-ftp-0.17-linelen.patch
Patch30: netkit-ftp-0.17-active-mode-option.patch
Patch31: netkit-ftp-0.17-commands-leaks.patch
Patch32: netkit-ftp-0.17-lsn-timeout.patch
Patch33: netkit-ftp-0.17-getlogin.patch
Patch34: netkit-ftp-0.17-token.patch
Patch35: netkit-ftp-0.17-linelen-segfault.patch
Patch36: netkit-ftp-0.17-out-of-memory.patch
Patch37: netkit-ftp-0.17-gcc15.patch

BuildRequires: glibc-devel
BuildRequires: readline-devel
BuildRequires: ncurses-devel
BuildRequires: perl-interpreter
BuildRequires: gcc
BuildRequires: make
BuildRequires: git-core

%description
The ftp package provides the standard UNIX command-line FTP (File
Transfer Protocol) client.  FTP is a widely used protocol for
transferring files over the Internet and for archiving files.

If your system is on a network, you should install ftp in order to do
file transfers.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n netkit-ftp-%{version} -S git

%build
sh configure --with-c-compiler=%{__cc} --enable-ipv6
perl -pi -e '
    s,^CC=.*$,CC=cc,;
    s,-O2,\$(RPM_OPT_FLAGS) -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64,;
    s,^LDFLAGS=.*$,LDFLAGS=\$(RPM_LD_FLAGS),;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' MCONFIG

%{make_build}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man5

make INSTALLROOT=${RPM_BUILD_ROOT} install

%files
%{_bindir}/ftp
%{_bindir}/pftp
%{_mandir}/man1/ftp.*
%{_mandir}/man1/pftp.*
%{_mandir}/man5/netrc.*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17-100
- Import
