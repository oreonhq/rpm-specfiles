%global source0_hash 97012ffc1aa7b850e95cf688b81a30d5c109f934684bf31d5dcb09c4a38df937

# Don't build the debugging utils by default.
%bcond_with utils

Name:		mISDN
Version:	2.0.22
Release:	18%{?dist}
Summary:	Userspace part of Modular ISDN stack

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://www.misdn.org/
Source0:	https://github.com/ISDN4Linux/mISDNuser/archive/v2.0.22.tar.gz
Source1:        mISDN.rules

Patch0:         mISDNuser-2.0.22-error.patch
Patch1:         %{name}-gcc11.patch

BuildRequires: make
BuildRequires: automake libtool autoconf
BuildRequires: flex

%{?ldconfig:Requires(post): %ldconfig}

%package devel
Summary:	Development files Modular ISDN stack
Requires:	mISDN = %{version}-%{release}

%package utils
Summary:	Debugging utilities for Modular ISDN stack

BuildRequires:  gcc
%description
mISDN (modular ISDN) is intended to be the new ISDN stack for the
Linux 2.6 kernel, from the maintainer of the existing isdn4linux
code. This package contains the userspace libraries required to
interface directly to mISDN.

%description devel
mISDN (modular ISDN) is intended to be the new ISDN stack for the
Linux 2.6 kernel, from the maintainer of the existing isdn4linux
code. This package contains the development files for userspace
libraries required to interface to mISDN, needed for compiling
applications which use mISDN directly such as OpenPBX.

%description utils
mISDN (modular ISDN) is intended to be the new ISDN stack for the
Linux 2.6 kernel, from the maintainer of the existing isdn4linux
code. This package contains test utilities for mISDN.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mISDNuser-%{version}
%patch -P0 -p1
%patch -P1 -p1

# Create a sysusers.d config file
cat >misdn.sysusers.conf <<EOF
u misdn 31 'Modular ISDN' - -
EOF

%build
aclocal
libtoolize --force --automake --copy
automake --add-missing --copy
autoconf

%configure
make CFLAGS="$RPM_OPT_FLAGS"

%install
make install DESTDIR=${RPM_BUILD_ROOT}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d
install -m0644 %SOURCE1 $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d/mISDN.rules
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d/45-misdn.rules

install -m0644 -D misdn.sysusers.conf %{buildroot}%{_sysusersdir}/misdn.conf

%post 
%{?ldconfig}

%ldconfig_postun

%files 
%_libdir/*.so.*
%doc COPYING.LIB LICENSE
%config(noreplace) %{_sysconfdir}/udev/rules.d/mISDN.rules
%exclude %{_sysconfdir}/misdnlogger.conf
%exclude %_bindir/*
%exclude %_sbindir/*
%{_sysusersdir}/misdn.conf

%files devel
%_includedir/mISDN
%_libdir/*.so
%exclude %_libdir/*.a
%exclude %_libdir/*.la

%if 0%{?with_utils}
%files utils
%config(noreplace) %{_sysconfdir}/misdnlogger.conf
%_bindir/*
%_sbindir/*
%endif

%changelog
%autochangelog
