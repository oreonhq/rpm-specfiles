%global source0_hash 0db3ebff755db170f65e74a64ec4511812e9ee3185c232eeffeacd274190dfb0

Name:    libatomic_ops
Summary: Atomic memory update operations
Version: 7.10.0
Release: 2%{?dist}

# libatomic_ops MIT, libatomic_ops_gpl GPLv2+
License: GPL-2.0-or-later AND MIT
URL:     https://github.com/ivmai/libatomic_ops/
Source0: https://github.com/ivmai/libatomic_ops/releases/download/v%{version}/libatomic_ops-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

# runtime compatibility with other distros
Provides: libatomic1 = %{version}-%{release}
Provides: libatomic1%{?_isa} = %{version}-%{release}

# from README.md:
# IN NEW CODE, PLEASE USE C11 OR C++14 STANDARD ATOMICS INSTEAD OF THE CORE
# LIBRARY IN THIS PACKAGE.
Provides: deprecated()

%description
Provides implementations for atomic memory update operations on a
number of architectures. This allows direct use of these in reasonably
portable code. Unlike earlier similar packages, this one explicitly
considers memory barrier semantics, and allows the construction of code
that involves minimum overhead across a variety of architectures.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: deprecated()
%description devel
Files for developing with %{name}.

%package static
Summary: Static library files for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Provides: deprecated()
%description static
Files for developing with %{name} and linking statically.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%build
%configure \
  --enable-shared \
  --disable-silent-rules

%make_build


%install
%make_install

# omit dup'd docs
rm -fv %{buildroot}%{_docdir}/libatomic_ops/{COPYING,LICENSE,README*,*.txt}


%check
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/src/.libs/
%make_build check


%files
%license COPYING
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_libdir}/libatomic_ops.so.1*
%{_libdir}/libatomic_ops_gpl.so.1*

%files devel
%doc README_*.txt
%{_includedir}/atomic_ops.h
%{_includedir}/atomic_ops_malloc.h
%{_includedir}/atomic_ops_stack.h
%{_includedir}/atomic_ops/
%{_libdir}/libatomic_ops.so
%{_libdir}/libatomic_ops_gpl.so
%{_libdir}/pkgconfig/atomic_ops.pc

%files static
%{_libdir}/libatomic_ops.a
%{_libdir}/libatomic_ops_gpl.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.10.0-2
- Prepare for Oreon 11 (RP1)
