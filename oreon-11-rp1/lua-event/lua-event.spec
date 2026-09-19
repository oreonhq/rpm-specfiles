%global source0_hash dd12babb252115895618c1243557534decde289bf0c255ffebf0dcd14a18705d

%global enable_docs 1

# ikiwiki is not available on EPEL
%{?rhel:%global enable_docs 0}

Summary:        Bindings of libevent to Lua
Name:           lua-event
Version:        0.4.6
Release:        18%{?dist}
License:        MIT
URL:            https://github.com/harningt/luaevent/
Source0:        https://github.com/harningt/luaevent/archive/v%{version}/luaevent-%{version}.tar.gz

# Make sure CFLAGS/LDFLAGS are respected.
Patch0:         %{name}-0.4.3-respect-cflags.patch
# Conditionalize env calls which are gone in modern lua
Patch1:         luaevent-0.4.3-envfix.patch

Requires:       lua(abi) = %{lua_version}
Requires:       lua-socket
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  libevent-devel >= 1.4

%description
Lua bindings for libevent, an asynchronous event notification library
that provides a mechanism to execute a callback function when a specific
event occurs on a file descriptor or after a timeout has been reached.

%if 0%{?enable_docs}
%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  ikiwiki

%description doc
This package contains documentation for developing applications that
use Lua bindings for libevent, an asynchronous event notification library
that provides a mechanism to execute a callback function when a specific
event occurs on a file descriptor or after a timeout has been reached.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n luaevent-%{version}
%patch -P0 -p1
%patch -P1 -p1 -b .envfix
# Remove 0-byte file.
rm -f doc/modules/luaevent.mdwn

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export LDFLAGS="$RPM_LD_FLAGS -shared"
%make_build

%if 0%{?enable_docs}
/bin/sh makeDocs.sh
%endif

%install
%make_install \
  INSTALL_DIR_LUA=%{lua_pkgdir} \
  INSTALL_DIR_BIN=%{lua_libdir}

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   dofile("test/basic.lua");'

%files
%license doc/COPYING
%doc CHANGELOG README doc/COROUTINE_MANAGEMENT doc/PLAN
%dir %{lua_libdir}/luaevent/
%{lua_libdir}/luaevent/core.so
%{lua_pkgdir}/luaevent.lua

%if 0%{?enable_docs}
%files doc
%doc html/*
%endif

%changelog
%autochangelog
