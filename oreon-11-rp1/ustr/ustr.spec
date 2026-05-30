%global source0_hash 3daf6eae9f78de1e872c0b2b83cce35515b94d4bb8a074e48f331fd99e1fc2c4

%define show_all_cmds       1
%define broken_fed_dbg_opts 0
%define multilib_inst       1

%if %{show_all_cmds}
%define policy_cflags_hide HIDE=
%else
%define policy_cflags_hide %{nil}
%endif

%if %{broken_fed_dbg_opts}
# Variable name explains itself.
%define policy_cflags_broken DBG_ONLY_BAD_POLICIES_HAVE_THIS_EMPTY_CFLAGS=
%else
%define policy_cflags_broken %{nil}
%endif

%define policy_cflags %{policy_cflags_hide}  %{policy_cflags_broken}

%if %{multilib_inst}
%define ustr_make_install install-multilib-linux
%else
%define ustr_make_install install
%endif


Name: ustr
Version: 1.0.4
Release: 43%{?dist}
Summary: String library, very low memory overhead, simple to import
# Automatically converted from old format: MIT or LGPLv2+ or BSD - review is highly recommended.
License: LicenseRef-Callaway-MIT OR LicenseRef-Callaway-LGPLv2+ OR LicenseRef-Callaway-BSD
URL: http://www.and.org/ustr/
Source0:        http://www.and.org/ustr/%{version}/%{name}-%{version}.tar.bz2
Patch0: c99-inline.patch
# BuildRequires: make gcc sed

BuildRequires: make
BuildRequires:  gcc
%description
 Micro string library, very low overhead from plain strdup() (Ave. 44% for
0-20B strings). Very easy to use in existing C code. At it's simplest you can
just include a single header file into your .c and start using it.
 This package also distributes pre-built shared libraries.

%package devel
Summary: Development files for %{name}
# This isn't required, but Fedora policy makes it so
Requires: pkgconfig >= 0.14
Requires: %{name} = %{version}-%{release}

%description devel
 Header files for the Ustr string library, and the .so to link with.
 Also includes a %{name}.pc file for pkg-config usage.
 Includes the ustr-import tool, for if you jsut want to include
the code in your projects ... you don't have to link to the shared lib.

%package static
Summary: Static development files for %{name}
Requires: %{name}-devel = %{version}-%{release}

%description static
 Static library for the Ustr string library.

%package debug
Summary: Development files for %{name}, with debugging options turned on
# This isn't required, but Fedora policy makes it so
Requires: pkgconfig >= 0.14
Requires: %{name}-devel = %{version}-%{release}

%description debug
 Header files and dynamic libraries for a debug build of the Ustr string
library.
 Also includes a %{name}-debug.pc file for pkg-config usage.

%package debug-static
Summary: Static development files for %{name}, with debugging options turned on
Requires: %{name}-debug = %{version}-%{release}

%description debug-static
 Static library for the debug build of the Ustr string library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P0 -p1

%build
make %{?_smp_mflags} all-shared CFLAGS="${CFLAGS:-%optflags}  -fgnu89-inline" \
  LDFLAGS="$RPM_LD_FLAGS" %{policy_cflags}

%check
%if %{?chk}%{!?chk:1}
make %{?_smp_mflags} check CFLAGS="${CFLAGS:-%optflags}  -fgnu89-inline"
  LDFLAGS="$RPM_LD_FLAGS" %{policy_cflags}
%endif

%install
rm -rf $RPM_BUILD_ROOT
make $@ %{ustr_make_install} prefix=%{_prefix} \
                bindir=%{_bindir}         mandir=%{_mandir} \
                datadir=%{_datadir}       libdir=%{_libdir} \
                includedir=%{_includedir} libexecdir=%{_libexecdir} \
                DOCSHRDIR=%{_datadir}/doc/ustr-devel \
                DESTDIR=$RPM_BUILD_ROOT LDCONFIG=/bin/true HIDE=

%ldconfig_scriptlets

%ldconfig_scriptlets debug

%files
%{_libdir}/libustr-1.0.so.*
%{!?_licensedir:%global license %%doc}
%license LICENSE*
%doc ChangeLog README NEWS

%files devel
%{_datadir}/ustr-%{version}
%{_bindir}/ustr-import
%if %{multilib_inst}
%{_libexecdir}/ustr-%{version}
%endif
%{_includedir}/ustr.h
%{_includedir}/ustr-*.h
%exclude %{_includedir}/ustr*debug*.h
%{_libdir}/pkgconfig/ustr.pc
%{_libdir}/libustr.so
%{_datadir}/doc/ustr-devel
%{_mandir}/man1/*
%{_mandir}/man3/*

%files static
%{_libdir}/libustr.a

%files debug
%{_libdir}/libustr-debug-1.0.so.*
%{_libdir}/libustr-debug.so
%{_includedir}/ustr*debug*.h
%{_libdir}/pkgconfig/ustr-debug.pc

%files debug-static
%{_libdir}/libustr-debug.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.4-43
- Prepare for Oreon 11 (RP1)
