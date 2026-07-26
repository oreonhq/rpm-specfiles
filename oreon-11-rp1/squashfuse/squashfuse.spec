%global source0_hash db0238c5981dabbd80ee09ae15387f390091668ca060a7bc38047912491443d3

Name:     squashfuse
Version:  0.5.2
Release:  %autorelease
Summary:  FUSE filesystem to mount squashfs archives

License:  BSD-2-Clause
URL:      https://github.com/vasi/squashfuse
Source0:  https://github.com/vasi/squashfuse/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: autoconf, automake, fuse3-devel, gcc, libattr-devel, libtool, libzstd-devel, lz4-devel, xz-devel, zlib-devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Squashfuse lets you mount SquashFS archives in user-space. It supports almost
all features of the SquashFS format, yet is still fast and memory-efficient.
SquashFS is an efficiently compressed, read-only storage format. Support for it
has been built into the Linux kernel since 2009. It is very common on Live CDs
and embedded Linux distributions.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for developing applications that use %{name}.

%package libs
Summary: Libraries for %{name}

%description libs
Libraries for running %{name} applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh
%configure --disable-static --disable-demo
%make_build

%install
%make_install

%files
%license LICENSE
%doc README CONFIGURATION NEWS TODO
%{_bindir}/squashfuse
%{_bindir}/squashfuse_ll
%{_mandir}/man1/squashfuse.1*
%{_mandir}/man1/squashfuse_ll.1*

%files devel
%{_includedir}/squashfuse/
%{_libdir}/pkgconfig/squashfuse.pc
%{_libdir}/pkgconfig/squashfuse_ll.pc
%{_libdir}/libsquashfuse.so
%{_libdir}/libsquashfuse_ll.so

%files libs
%license LICENSE
%{_libdir}/libsquashfuse.so.0*
%{_libdir}/libsquashfuse_ll.so.0*

%changelog
%autochangelog
