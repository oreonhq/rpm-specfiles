%global source0_hash 8caddd1ee8d8c7790e4b7fedc9be15d4d76ea23f25b17687fc27218648325885

Summary: Shared memory allocation library
Name: mm
Version: 1.4.2
Release: 38%{?dist}
# Automatically converted from old format: BSD with advertising - review is highly recommended.
License: LicenseRef-Callaway-BSD-with-advertising
Source0: ftp://ftp.ossp.org/pkg/lib/mm/mm-%{version}.tar.gz
URL: http://www.ossp.org/pkg/lib/mm/

BuildRequires: make
BuildRequires:  gcc
%description
OSSP mm is a 2-layer abstraction library which simplifies the usage of
shared memory between forked (and this way strongly related) processes
under Unix platforms. On the first layer it hides all platform dependent
implementation details (allocation and locking) when dealing with shared
memory segments and on the second layer it provides a high-level
malloc(3)-style API for a convenient and well known way to work with
data structures inside those shared memory segments.

%package devel
Summary: Header files and libraries for %{name} development
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and libraries needed
to develop programs that use the %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --enable-debug
%{__make} %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -name "*.la" -exec rm -f {} \;
find %{buildroot} -name "*.a" -exec rm -f {} \;

# Fix permissions, so that find-debuginfo.sh picks up the libraries
find %{buildroot} -name *.so.* -type f -exec chmod 755 {} \;

# Fix the installed mm-config script to remove unnecessary flags and
# prevent a multilib conflict
sed -i -e 's#^mm_libdir=.*#mm_libdir=#; s# -L$mm_libdir##; s# -m[36][24]##' %{buildroot}%{_bindir}/mm-config

%ldconfig_scriptlets

%files
%doc LICENSE THANKS README
%{_libdir}/*.so.*

%files devel
%doc ChangeLog
%defattr(-, root, root)
%{_bindir}/mm-config
%{_libdir}/*.so
%{_includedir}/mm.h
%{_mandir}/man1/mm-config.1*
%{_mandir}/man3/mm.3*

%changelog
%autochangelog
