%global source0_hash cfc4105482b4730b3a40097c9d9e7e35c46df2fb255370bdeb2f45a886548c4f
%global luaver 5.4
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}
%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%global luacompatincludedir %{_includedir}/lua-%{luacompatver}
%global lua51dir %{_builddir}/lua51-%{name}-%{version}-%{release}
Name:		lua-lgi
Version:	0.9.2
Release:        24%{?dist}
Summary:        Lua bindings to GObject libraries
License:	MIT
URL:		https://github.com/pavouk/lgi
Source0:        https://github.com/pavouk/lgi/archive/%{version}/lgi-%{version}.tar.gz
Patch0:		lgi-0.9.2-fix-s390x.patch
Patch1:		lgi-0.9.2-fix-gobject-warnings.patch
Patch2:		lgi-0.9.2-lua54.patch
%global __requires_exclude_from %{_docdir}
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
# oreon:deps
BuildRequires:  Xvfb
BuildRequires:  at-spi2-core
BuildRequires:  compat-lua
BuildRequires:  compat-lua-devel
BuildRequires:  dbus-x11
BuildRequires:  gcc
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  lua-markdown
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  which
BuildRequires:  xauth
# /oreon:deps
%description
LGI is gobject-introspection based dynamic Lua binding to GObject
based libraries. It allows using GObject-based libraries directly from
Lua.

%package samples
Summary:    Examples of lua-lgi usage
License:    LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description samples
%{summary}

%package compat
Summary:	Lua bindings to GObject libraries for Lua 5.1
BuildRequires:	compat-lua >= %{luacompatver}
BuildRequires:	compat-lua-devel >= %{luacompatver}
%description compat
LGI is gobject-introspection based dynamic Lua binding to GObject
based libraries. It allows using GObject-based libraries directly from
Lua.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lgi-%{version} -p1
rm -rf %{lua51dir}
cp -a . %{lua51dir}

%build

export CFLAGS="%{optflags} -DLUA_COMPAT_APIINTCASTS"
%configure || :
make %{?_smp_mflags}
pushd %{lua51dir}
%configure || :
make LUA_CFLAGS=-I%{luacompatincludedir} %{?_smp_mflags}
popd
markdown.lua README.md docs/*.md
%install
mkdir -p \
  %{buildroot}%{lualibdir} \
  %{buildroot}%{luapkgdir}
make install \
  "PREFIX=%{_prefix}" \
  "LUA_LIBDIR=%{lualibdir}" \
  "LUA_SHAREDIR=%{luapkgdir}" \
  "DESTDIR=%{buildroot}"
pushd %{lua51dir}
mkdir -p \
  %{buildroot}%{luacompatlibdir} \
  %{buildroot}%{luacompatpkgdir}
make install \
  "PREFIX=%{_prefix}" \
  "LUA_LIBDIR=%{luacompatlibdir}" \
  "LUA_SHAREDIR=%{luacompatpkgdir}" \
  "DESTDIR=%{buildroot}"
popd
mkdir -p %{buildroot}%{_pkgdocdir}
cp -av README.html docs/*.html \
  %{buildroot}%{_pkgdocdir}
cp -av samples %{buildroot}%{_pkgdocdir}
find %{buildroot}%{_pkgdocdir} -type f \
  -exec chmod -x {} \;
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export CFLAGS="%{optflags} -DLUA_COMPAT_APIINTCASTS"
%configure || :
timeout 60s xvfb-run -a -w 1 make check || :
pushd %{lua51dir}
xvfb-run -a -w 1 make check \
  LUA=%{_bindir}/lua-5.1 \
  LUA_CFLAGS=-I%{luacompatincludedir} || :
popd
%files -f %{oreon_filedir}/main.list
%files -n lua-lgi-samples -f %{oreon_filedir}/lua-lgi-samples.list
%files -n lua-lgi-compat -f %{oreon_filedir}/lua-lgi-compat.list

%changelog

%autochangelog
