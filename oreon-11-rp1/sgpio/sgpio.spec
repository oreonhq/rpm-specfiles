%global source0_hash 9bf8c42acaa247efd9321bdb1fc2390022f0c554d77fbbd4a7363d990fc0270b

Summary: SGPIO captive backplane tool
Name: sgpio
Version: 1.2.0.10
Release: 40%{?dist}
License: GPL-2.0-or-later
URL: https://sourceware.org/lvm2/wiki/DMRAID_Eventing
Source:        sgpio-1.2-0.10-src.tar.gz
# there is no official download link for the latest package
#Source: http://sources.redhat.com/lvm2/wiki/DMRAID_Eventing?action=AttachFile&do=get&target=sgpio-1.2.tgz
Patch0: sgpio-1.2-makefile.patch
Patch1: sgpio-1.2-coverity.patch
Patch2: sgpio-1.2-buffer-overflow.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: dos2unix

%description
Intel SGPIO enclosure management utility

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n sgpio
dos2unix --keepdate Makefile README
%patch -P0 -p1 -b .makefile
%patch -P1 -p1 -b .coverity
%patch -P2 -p1 -b .buffer-overflow
chmod a-x *

%build
#@@@ workaround for #474755 - remove with next update
make clean
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
%make_install SBIN_DIR=$RPM_BUILD_ROOT%{_sbindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}

%files
%doc README
%{_sbindir}/sgpio
%{_mandir}/man1/sgpio.*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0.10-40
- Import
