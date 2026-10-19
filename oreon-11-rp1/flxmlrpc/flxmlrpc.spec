%global source0_hash 6f9d5986c6c9dc4d92c88b80ac19ef9376688bb947390d7557ef9c2eaf42aade
Name:           flxmlrpc
Version:        1.0.1
Release:        1%{?dist}
Summary:        An xmlrpc library for the NBEMS suite of programs
License:        LGPL-3.0-or-later
URL:            http://www.w1hkj.com
Source0:        http://www.w1hkj.com/xmlrpc-mods/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This is version %{version} of flxmlrpc, an implementation of the XmlRpc protocol
written in C++, based upon XmlRpc++0.7 and modified to provide additional XmlRpc
Variable types.  It is used in fldigi, flrig, flnet, flmsg, flarq, flamp, fllog;
a suite of programs written for amateur radio emergency communications.

flxmlrpc is designed to make it easy to incorporate xmlrpc client and server
support into C++ applications. Or use both client and server objects in your 
application for easy peer-to-peer support.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

if [ ! -f configure ]
then autoreconf -fi
fi
%configure --disable-static
%make_build
%install
%make_install
find %{buildroot}%{_libdir} -name "*.la" -exec rm -f {} \;
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n flxmlrpc-devel -f %{oreon_filedir}/flxmlrpc-devel.list

%changelog

%autochangelog
