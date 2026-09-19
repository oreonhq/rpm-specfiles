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
Release:	24%{?dist}
Summary:	Lua bindings to GObject libraries
# Automatically converted from old format: MIT - review is highly recommended.
License:	MIT
URL:		https://github.com/pavouk/lgi
Source0:	https://github.com/pavouk/lgi/archive/%{version}/lgi-%{version}.tar.gz
# see gh#212 (commit a127f82)
Patch0:		lgi-0.9.2-fix-s390x.patch
# see gh#215
Patch1:		lgi-0.9.2-fix-gobject-warnings.patch
# see gh#249
Patch2:		lgi-0.9.2-lua54.patch
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.10.8
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	lua >= %{luaver}
BuildRequires:	lua-devel >= %{luaver}
BuildRequires:	lua-markdown
# for the testsuite:
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	which
BuildRequires:	Xvfb xauth
BuildRequires:	dbus-x11 at-spi2-core

%global __requires_exclude_from %{_docdir}
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
LGI is gobject-introspection based dynamic Lua binding to GObject
based libraries. It allows using GObject-based libraries directly from
Lua.

%package samples
Summary:    Examples of lua-lgi usage
# gtk-demo is LGPLv2+
# Automatically converted from old format: LGPLv2+ and MIT - review is highly recommended.
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

# generate html documentation
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

# install docs
mkdir -p %{buildroot}%{_pkgdocdir}
cp -av README.html docs/*.html \
  %{buildroot}%{_pkgdocdir}
cp -av samples %{buildroot}%{_pkgdocdir}
find %{buildroot}%{_pkgdocdir} -type f \
  -exec chmod -x {} \;

%check
export CFLAGS="%{optflags} -DLUA_COMPAT_APIINTCASTS"
%configure || :
# report failing tests, don't fail the build
timeout 60s xvfb-run -a -w 1 make check || :

pushd %{lua51dir}
# report failing tests, don't fail the build
xvfb-run -a -w 1 make check \
  LUA=%{_bindir}/lua-5.1 \
  LUA_CFLAGS=-I%{luacompatincludedir} || :
popd

%files
%dir %{_pkgdocdir}
%license LICENSE
%{_pkgdocdir}/*.html
%{luapkgdir}/lgi.lua
%{luapkgdir}/lgi
%{lualibdir}/lgi

%files compat
%license LICENSE
%{luacompatpkgdir}/lgi.lua
%{luacompatpkgdir}/lgi
%{luacompatlibdir}/lgi

%files samples
%{_pkgdocdir}/samples

%changelog
%autochangelog
