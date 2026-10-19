%global source0_hash 35ce0ee1741ea38def304ddfe84a958901413aa829698357f0bee5bb8f0a223b
Summary:        Library (C API) for accessing CDDB servers
Name:		libcddb
Version:	1.3.2
Release:        47%{?dist}
License:	LGPL-2.0-or-later
URL:		http://libcddb.sourceforge.net/
Source0:        http://downloads.sourceforge.net/libcddb/%{name}-%{version}.tar.bz2
Patch0:		libcddb-1.3.0-multilib.patch
Patch1:		libcddb-1.3.2-rhbz770611.patch
Patch2:         pointer-types.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libcdio-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (e.g http://freedb.org/).

%package devel
Summary:	Development files for libcddb
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (e.g http://freedb.org/).
This package contains development files (static libraries, headers)
for libcddb.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p0
iconv -f ISO_8859-1 -t UTF-8 THANKS > THANKS.tmp
touch -r THANKS THANKS.tmp
mv THANKS.tmp THANKS
iconv -f ISO_8859-1 -t UTF-8 ChangeLog > ChangeLog.tmp
touch -r ChangeLog ChangeLog.tmp
mv ChangeLog.tmp ChangeLog

%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcddb-devel -f %{oreon_filedir}/libcddb-devel.list

%changelog

%autochangelog

