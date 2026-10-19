%global source0_hash 036855660225cb3817a190fc00e6764ce7836051bacb48d35e26444b8c1729d9
Name:    libsigsegv
Version: 2.15
Release:        2%{?dist}
Summary:        Library for handling page faults in user mode
License: GPL-2.0-or-later
URL:     https://www.gnu.org/software/libsigsegv/
Source0:        https://mirrors.kernel.org/gnu/libsigsegv/libsigsegv-%{version}.tar.gz
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This is a library for handling page faults in user mode. A page fault
occurs when a program tries to access to a region of memory that is
currently not available. Catching and handling a page fault is a useful
technique for implementing:
  - pageable virtual memory
  - memory-mapped access to persistent databases
  - generational garbage collectors
  - stack overflow handlers
  - distributed shared memory

%package devel
Summary: Development libraries and header files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package static
Summary: Static libraries for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -ivf
%configure \
  --enable-shared \
  --disable-silent-rules \
  --enable-static
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libsigsegv-devel -f %{oreon_filedir}/libsigsegv-devel.list
%files -n libsigsegv-static -f %{oreon_filedir}/libsigsegv-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.15-2
- Prepare for Oreon 11 (RP1)
