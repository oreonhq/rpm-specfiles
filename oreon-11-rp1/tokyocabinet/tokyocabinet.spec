%global source0_hash a003f47c39a91e22d76bc4fe68b9b3de0f38851b160bbb1ca07a4f6441de1f90
Summary:        A modern implementation of a DBM
Name:		tokyocabinet
Version:	1.4.48
Release:        30%{?dist}
License:	LGPL-2.1-or-later
URL:		https://dbmx.net/tokyocabinet/
Source0:        https://dbmx.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		tokyocabinet-fedora.patch
Patch1:		tokyocabinet-manhelp.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
# /oreon:deps
%description
Tokyo Cabinet is a library of routines for managing a database. It is the 
successor of QDBM. Tokyo Cabinet runs very fast. For example, the time required
to store 1 million records is 1.5 seconds for a hash database and 2.2 seconds
for a B+ tree database. Moreover, the database size is very small and can be up
to 8EB. Furthermore, the scalability of Tokyo Cabinet is great.

Kyoto Cabinet is the designated successor of Tokyo Cabinet, and Tkrzw is the
designated successor to Kyoto Cabinet.

%package devel
Summary:	Headers for developing programs that will use %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
%description devel
This package contains the libraries and header files needed for
developing with %{name}.

%package devel-doc
Summary:	Documentation files for developing programs that will use %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
BuildArch:	noarch
%description devel-doc
This package contains documentation files for the libraries and header files
needed for developing with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p0 -b .fedora
%patch -P1 -p1 -b .manhelp

%build

autoconf
%configure --enable-off64 CFLAGS="$CFLAGS"
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_libdir}/lib%{name}.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifnarch x86_64
make check
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n tokyocabinet-devel -f %{oreon_filedir}/tokyocabinet-devel.list
%files -n tokyocabinet-devel-doc -f %{oreon_filedir}/tokyocabinet-devel-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.48-30
- Prepare for Oreon 11 (RP1)
