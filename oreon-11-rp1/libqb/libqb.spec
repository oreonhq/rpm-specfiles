%global source0_hash 61a83753199c86a47a69f615778e81b56ac0a58d07751230444e76500b6b210b

%bcond_with check

Name:           libqb
Version:        2.0.9
Release:        2%{?dist}
Summary:        Library providing high performance logging, tracing, ipc, and poll

License:        LGPL-2.1-or-later
URL:            https://github.com/ClusterLabs/libqb
Source0:        https://github.com/ClusterLabs/libqb/releases/download/v2.0.9/libqb-2.0.9.tar.xz


BuildRequires:  autoconf automake libtool
BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  procps
# for ipc.test only (part of check scriptlet)
BuildRequires:  pkgconfig(glib-2.0)
# git-style patch application
BuildRequires:  git-core
# For doxygen2man
BuildRequires:  libxml2-devel
BuildRequires: make

%description
A "Quite Boring" library that provides high-performance, reusable features for client-server
architecture, such as logging, tracing, inter-process communication (IPC),
and polling.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}

%build
./autogen.sh
%configure --disable-static
%{make_build}

%if 0%{?with_check}
%check
make check V=1
%endif

%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -delete
rm -rf $RPM_BUILD_ROOT/%{_docdir}/*

%ldconfig_scriptlets

%files
%license COPYING
%{_sbindir}/qb-blackbox
%{_libdir}/libqb.so.*
%{_mandir}/man8/qb-blackbox.8*

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files          devel
%doc README.markdown
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3*


%package -n     doxygen2man
Summary:        Program to create nicely-formatted man pages from Doxygen XML files
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description -n doxygen2man
This package contains a program to create nicely-formatted man pages from Doxygen XML files

%files -n       doxygen2man
%{_bindir}/doxygen2man
%{_mandir}/man1/doxygen2man.1.gz


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.9-2
- Prepare for Oreon 11 (RP1)
