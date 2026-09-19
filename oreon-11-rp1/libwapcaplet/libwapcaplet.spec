%global source0_hash 9b2aa1dd6d6645f8e992b3697fdbd87f0c0e1da5721fa54ed29b484d13160c5c

Name: libwapcaplet
Version: 0.4.3
Release: %autorelease
Summary: A string internment library

License: MIT
URL: http://www.netsurf-browser.org/projects/libwapcaplet/
Source: http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz

BuildRequires: gcc
BuildRequires: netsurf-buildsystem
BuildRequires: pkgconfig(check)
BuildRequires: make

%description
LibWapcaplet is a string internment library, written in C. It provides
reference counted string interment and rapid string comparison
functionality. It was developed as part of the NetSurf project and is
available for use by other software under the MIT licence. For further
details, see the readme.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%global make_vars COMPONENT_TYPE=lib-shared PREFIX=%{_prefix} LIBDIR=%{_lib} Q=
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="$RPM_LD_FLAGS"

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

sed -i -e s@-Werror@@ Makefile

%build
make %{?_smp_mflags} %{make_vars} %{build_vars}

%install
make install DESTDIR=%{buildroot} %{make_vars}

%check
make %{?_smp_mflags} test %{make_vars}

%files
%doc README
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
