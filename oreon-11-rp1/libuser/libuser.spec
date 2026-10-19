%global source0_hash e383cbdabb782ea8e8f6df1351ecd491f3b62f4f9b171c44e03cce9e1cec4658
%bcond ldaptests %{undefined rhel}
Name: libuser
Version: 0.64
Release:        17%{?dist}
License: LGPL-2.0-or-later
URL: https://pagure.io/libuser
Source0:        https://deb.debian.org/debian/pool/main/libu/libuser/libuser_0.64+git20241106~dfsg.orig.tar.gz#/libuser-%{version}.tar.gz
Patch: 0001-tests-use-crypt_r-with-Python-3.13.patch
Patch1:  libuser-0.64-editlocation.patch
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 11 || (0%{?oreon} >= 11)
%endif
%if %{with ldaptests}
%endif
Provides: deprecated()
Summary:        A user and group account administration library
%global __provides_exclude_from ^(%{_libdir}/%{name}|%{python3_sitearch})/.*$
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  linuxdoc-tools
BuildRequires:  make
BuildRequires:  openldap-clients
BuildRequires:  openldap-devel
BuildRequires:  openldap-servers
BuildRequires:  openssl
BuildRequires:  pam-devel
BuildRequires:  popt-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(crypt-r)
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure --with-selinux --with-ldap --with-audit \
           --enable-gtk-doc --with-html-dir=%{_datadir}/gtk-doc/html \
           PYTHON=%{python3}
make
%install
%make_install
%find_lang %{name}
%oreon_autofiles python3-libuser usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check || { cat test-suite.log; false; }
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir}:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch}
export PYTHONPATH
%{python3} -c "import libuser"
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libuser-devel -f %{oreon_filedir}/libuser-devel.list
%files -n python3-libuser -f %{oreon_filedir}/python3-libuser.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.64-17
- Import
