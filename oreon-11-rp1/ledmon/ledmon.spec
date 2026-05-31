%global source0_hash 4f626400e41ab1e4317b886db5b5df1afa517e8e4faa80fd4378fd22b0bcd055

Summary: Enclosure LED Utilities
Name: ledmon
Version: 1.1.0
Release: 4%{?dist}
License: GPL-2.0-only AND LGPL-2.1-only
URL: https://github.com/intel/ledmon
Source0:        https://github.com/intel/ledmon/archive/v1.1.0/ledmon-1.1.0.tar.gz

BuildRequires: autoconf automake
BuildRequires: autoconf-archive
BuildRequires: gcc make
BuildRequires: libconfig-devel
BuildRequires: libtool
BuildRequires: pciutils-devel
BuildRequires: sg3_utils-devel
# Needed for pkgconfig usage.
BuildRequires: pkgconfig(systemd)
# Needed for the udev dependency.
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros

Obsoletes: ledctl = 0.1-1
Provides: ledctl = %{version}-%{release}

# 
ExcludeArch: %{ix86}

%description
The ledmon and ledctl are user space applications design to control LED
associated with each slot in an enclosure or a drive bay. There are two
types of system: 2-LED system (Activity LED, Status LED) and 3-LED system
(Activity LED, Locate LED, Fail LED). User must have root privileges to
use this application.

%package        libs
Summary:        Runtime library files for %{name}
Requires:       pciutils-libs
Requires:       sg3_utils-libs

%description    libs
The %{name}-libs package contains runtime libraries for applications
that use %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pciutils-devel
Requires:       sg3_utils-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
autoreconf -fiv

%build
%configure --enable-systemd=yes --enable-library --disable-static
%make_build

%install
%make_install

%post
%systemd_post ledmon.service

%preun
%systemd_preun ledmon.service

%postun
%systemd_postun_with_restart ledmon.service

%files
%doc README.md COPYING
%{_sbindir}/ledctl
%{_sbindir}/ledmon
%{_mandir}/*/*
%{_unitdir}/ledmon.service

%files libs
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-4
- Import
