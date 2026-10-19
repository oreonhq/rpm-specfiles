%global source0_hash 4469cd74c8c7f51d3b9ce802d2239ba2b09d3d3a11273c3a5abdf273a0a53531
%global luaver 5.4
%global luapkgdir %{_datadir}/lua/%{luaver}
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:		lua-ldoc
Version:	1.5.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Lua documentation generator
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:		https://github.com/lunarmodules/ldoc
Source0:        https://github.com/lunarmodules/ldoc/archive/refs/tags/v%{version}.tar.gz
Requires:	lua >= %{luaver}
Requires:	lua-markdown
Requires:	lua-penlight >= 1.4.0
%global __requires_exclude_from %{_docdir}
# oreon:deps
BuildRequires:  lua
BuildRequires:  lua-markdown
BuildRequires:  lua-penlight
BuildRequires:  make
# /oreon:deps
%description
LDoc is a second-generation documentation tool that can be used as a
replacement for LuaDoc. It is mostly compatible with LuaDoc, except
that certain workarounds are no longer needed. For instance, it is not
so married to the idea that Lua modules should be defined using the
module function.

%package doc
Summary:	Docs for lua-ldoc
Requires:	%{name} = %{version}-%{release}
%description doc
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ldoc-%{version}
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{luapkgdir}
mkdir -p %{buildroot}%{_bindir}
make install \
  "LUA_SHAREDIR=%{luapkgdir}" \
  "LUA_BINDIR=%{_bindir}" \
  "DESTDIR=%{buildroot}"
sed -i %{buildroot}%{_bindir}/ldoc -e '1i#!/bin/sh'
sed -i %{buildroot}%{luapkgdir}/ldoc.lua -e '1{/^#!/d}'
lua ldoc.lua .
markdown.lua README.md > README.html
markdown.lua CHANGELOG.md > CHANGELOG.html
chmod u=rwX,go=rX -R public
sed -i 's/\r//' COPYRIGHT
rm %{buildroot}%{luapkgdir}/ldoc/markdown.lua
rm %{buildroot}%{luapkgdir}/ldoc/SciTE.properties \
   %{buildroot}%{luapkgdir}/ldoc/config.ld
mkdir -p %{buildroot}%{_pkgdocdir}
cp -av %{!?_licensedir:COPYRIGHT} README.html CHANGELOG.html public/* \
  %{buildroot}%{_pkgdocdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lua-ldoc-doc -f %{oreon_filedir}/lua-ldoc-doc.list

%changelog

%autochangelog
