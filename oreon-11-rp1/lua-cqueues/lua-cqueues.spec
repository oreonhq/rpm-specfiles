%global source0_hash 45b4a0105c096eee5840b69e8e0078eb7b5d61a23aeca30db710f1caac3ec399
%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}
%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%global luapkgname cqueues
Name:           lua-%{luapkgname}
Version:        20200603
Release:        1%{?dist}
Summary:        Stackable Continuation Queues for the Lua Programming Language
License:        MIT
URL:            https://github.com/wahern/%{luapkgname}
Source0:        https://github.com/wahern/%{luapkgname}/archive/rel-%{version}/%{name}-%{version}.tar.gz
Patch0:         lua-cqueues-20200603-lua-5.4.patch
Requires:       lua(abi) = %{luaver}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
cqueues is a type of event loop for Lua. It doesn't use callbacks but instead
you communicate with an event controller by the yielding and resumption of
Lua coroutines using objects.

cqueues are stackable. Each instantiated cqueue is a poll-able object which
can be polled from another cqueue, or another event loop system entirely.
The design is meant to be non-intrusive, composable, and embeddable within
existing applications.

cqueues includes a sockets library with DNS, buffering, end-of-line
translation, SSL/TLS, and descriptor passing support builtin.
Domain querying, connection establishment, and SSL negotiation are handled
transparently as part of a state machine entered with every I/O operation,
so users can read and write immediately upon instantiating the object,
as if opening a regular file.

cqueues also includes modules for handling signals, threads, and file change
notifications using native kernel facilities and accessible through easy
to use interfaces which abstract the different kernel facilities.

%package doc
Summary:        Documentation for the Stackable Continuation Queues library
BuildArch:      noarch
Requires:       %{name} == %{version}
%description doc
Documentation for the Stackable Continuation Queues library
for the Lua Programming Language

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{luapkgname}-rel-%{version}
%patch -P0 -p1 -b .lua54

%build

export CFLAGS="%{?optflags} -fPIC"
export LDFLAGS="%{?build_ldflags}"
make LUA_APIS="%{luaver}" %{?_smp_mflags} prefix=%{_prefix} libdir=%{_libdir}
%install
make install LUA_APIS="%{luaver}" DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -r -t %{buildroot}%{_pkgdocdir} doc/cqueues.pdf examples
sed -i '1 s|^#!/.*$|#!/usr/bin/lua|' %{buildroot}%{_pkgdocdir}/examples/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lua-cqueues-doc -f %{oreon_filedir}/lua-cqueues-doc.list

%changelog

%autochangelog
