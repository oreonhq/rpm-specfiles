%global source0_hash 0db3ebff755db170f65e74a64ec4511812e9ee3185c232eeffeacd274190dfb0
Name:    libatomic_ops
Summary:        Atomic memory update operations
Version: 7.10.0
Release:        2%{?dist}
License: GPL-2.0-or-later AND MIT
URL:     https://github.com/ivmai/libatomic_ops/
Source0:        https://github.com/ivmai/libatomic_ops/releases/download/v%{version}/libatomic_ops-%{version}.tar.gz
Provides: libatomic1 = %{version}-%{release}
Provides: libatomic1%{?_isa} = %{version}-%{release}
Provides: deprecated()
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
  --enable-shared \
  --disable-silent-rules
%make_build
%install
%make_install
rm -fv %{buildroot}%{_docdir}/libatomic_ops/{COPYING,LICENSE,README*,*.txt}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/src/.libs/
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libatomic_ops-devel -f %{oreon_filedir}/libatomic_ops-devel.list
%files -n libatomic_ops-static -f %{oreon_filedir}/libatomic_ops-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.10.0-2
- Prepare for Oreon 11 (RP1)
