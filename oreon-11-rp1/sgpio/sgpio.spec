Summary: SGPIO captive backplane tool
Name: sgpio
Version: 1.2.0.10
Release: 40%{?dist}
License: GPL-2.0-or-later
URL: https://sourceware.org/lvm2/wiki/DMRAID_Eventing
Source: sgpio-1.2-0.10-src.tar.gz
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0.10-40
- Prepare for Oreon 11 (RP1)
