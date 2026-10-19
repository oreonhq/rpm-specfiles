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
Release:        1%{?dist}
Summary:        String library, very low memory overhead, simple to import
License: LicenseRef-Callaway-MIT OR LicenseRef-Callaway-LGPLv2+ OR LicenseRef-Callaway-BSD
URL: http://www.and.org/ustr/
Source0:        http://www.and.org/ustr/%{version}/%{name}-%{version}.tar.bz2
Patch0: c99-inline.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
 Micro string library, very low overhead from plain strdup() (Ave. 44% for
0-20B strings). Very easy to use in existing C code. At it's simplest you can
just include a single header file into your .c and start using it.
 This package also distributes pre-built shared libraries.

%package devel
Summary: Development files for %{name}
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ustr-devel -f %{oreon_filedir}/ustr-devel.list
%files -n ustr-static -f %{oreon_filedir}/ustr-static.list
%files -n ustr-debug -f %{oreon_filedir}/ustr-debug.list
%files -n ustr-debug-static -f %{oreon_filedir}/ustr-debug-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.4-43
- Prepare for Oreon 11 (RP1)
