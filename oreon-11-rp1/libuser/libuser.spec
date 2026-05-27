%global source0_hash none

%bcond ldaptests %{undefined rhel}

Name: libuser
Version: 0.64
Release: 17%{?dist}
License: LGPL-2.0-or-later
URL: https://pagure.io/libuser
Source: libuser-%{version}.tar.gz
# https://pagure.io/libuser/pull-request/71
Patch: 0001-tests-use-crypt_r-with-Python-3.13.patch
Patch1:  libuser-0.64-editlocation.patch

BuildRequires: glib2-devel
BuildRequires: linuxdoc-tools
BuildRequires: pam-devel
BuildRequires: popt-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: libselinux-devel
BuildRequires: libxcrypt-devel
BuildRequires: openldap-devel
BuildRequires: python3-devel
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 11 || 0%{?oreon}
BuildRequires: python3dist(crypt-r)
%endif
# To make sure the configure script can find it
BuildRequires: gcc
# For %%check
%if %{with ldaptests}
BuildRequires: openldap-clients
BuildRequires: openldap-servers
%endif
BuildRequires: openssl
BuildRequires: make
BuildRequires: bison
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: gtk-doc
BuildRequires: audit-libs-devel
Provides: deprecated()

Summary: A user and group account administration library

%global __provides_exclude_from ^(%{_libdir}/%{name}|%{python3_sitearch})/.*$

%description
The libuser library implements a standardized interface for manipulating
and administering user and group accounts.  The library uses pluggable
back-ends to interface to its data sources.

Sample applications modeled after those included with the shadow password
suite are included.

%package devel
Summary: Files needed for developing applications which use libuser
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa}
Provides: deprecated()

%description devel
The libuser-devel package contains header files, static libraries, and other
files useful for developing applications with libuser.

%package -n python3-libuser
Summary: Python 3 bindings for the libuser library
Requires: libuser%{?_isa} = %{version}-%{release}
Provides: libuser-python3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: libuser-python3%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: libuser-python3 < 0.63-4
%{?python_provide:%python_provide python3-libuser}
Provides: deprecated()

%description -n python3-libuser
The python3-libuser package contains the Python bindings for
the libuser library, which provides a Python 3 API for manipulating and
administering user and group accounts.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p 1

%build
./autogen.sh
%configure --with-selinux --with-ldap --with-audit \
           --enable-gtk-doc --with-html-dir=%{_datadir}/gtk-doc/html \
           PYTHON=%{python3}
make


%install
%make_install

%find_lang %{name}

%check
%make_build check || { cat test-suite.log; false; }

# Verify that all python modules load, just in case.
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir}:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch}
export PYTHONPATH
%{python3} -c "import libuser"


%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README TODO docs/*.txt
%config(noreplace) %{_sysconfdir}/libuser.conf

%attr(0755,root,root) %{_bindir}/*
%{_libdir}/*.so.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%attr(0755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%exclude %{_libdir}/*.la
%exclude %{_libdir}/%{name}/*.la

%files -n python3-libuser
%doc python/modules.txt
%{python3_sitearch}/*.so
%exclude %{python3_sitearch}/*.la

%files devel
%{_includedir}/libuser
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.64-17
- Import
