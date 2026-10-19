%global source0_hash dd12babb252115895618c1243557534decde289bf0c255ffebf0dcd14a18705d
%global enable_docs 1
%{?rhel:%global enable_docs 0}
Summary:        Bindings of libevent to Lua
Name:           lua-event
Version:        0.4.6
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/harningt/luaevent/
Source0:        https://github.com/harningt/luaevent/archive/v%{version}/luaevent-%{version}.tar.gz
Patch0:         %{name}-0.4.3-respect-cflags.patch
Patch1:         luaevent-0.4.3-envfix.patch
Requires:       lua(abi) = %{lua_version}
Requires:       lua-socket
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ikiwiki
BuildRequires:  libevent-devel
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   dofile("test/basic.lua");'
%files -f %{oreon_filedir}/main.list
%files -n lua-event-doc -f %{oreon_filedir}/lua-event-doc.list

%changelog

%autochangelog
