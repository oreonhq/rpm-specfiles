Name:    libsigsegv
Version: 2.15
Release: 2%{?dist}
Summary: Library for handling page faults in user mode

License: GPL-2.0-or-later
URL:     https://www.gnu.org/software/libsigsegv/
Source0: http://ftp.gnu.org/gnu/libsigsegv/libsigsegv-%{version}.tar.gz

BuildRequires: automake libtool
BuildRequires: gcc
BuildRequires: make

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
%autosetup -p1


%build
# for patch1, rpaths
autoreconf -ivf

%configure \
  --enable-shared \
  --disable-silent-rules \
  --enable-static

%make_build


%install
%make_install

# remove libtool archives
find %{buildroot} -type f -name "*.la" -delete


%check
make check


%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libsigsegv.so.2*

%files devel
%{_libdir}/libsigsegv.so
%{_includedir}/sigsegv.h

%files static
%{_libdir}/libsigsegv.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.15-2
- Prepare for Oreon 11 (RP1)
