%global source0_hash 4469cd74c8c7f51d3b9ce802d2239ba2b09d3d3a11273c3a5abdf273a0a53531

%global luaver 5.4
%global luapkgdir %{_datadir}/lua/%{luaver}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		lua-ldoc
Version:	1.5.0
Release:	8%{?dist}
BuildArch:	noarch
Summary:	Lua documentation generator
# the included css code is BSD licensed
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:		https://github.com/lunarmodules/ldoc
Source0:	https://github.com/lunarmodules/ldoc/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	lua >= %{luaver}
BuildRequires:	lua-markdown
BuildRequires:	lua-penlight >= 1.4.0
BuildRequires:	make
Requires:	lua >= %{luaver}
Requires:	lua-markdown
Requires:	lua-penlight >= 1.4.0

%global __requires_exclude_from %{_docdir}

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

%autosetup -p1 -n ldoc-%{version}

%build
# nothing to do here

%install
mkdir -p %{buildroot}%{luapkgdir}
mkdir -p %{buildroot}%{_bindir}
make install \
  "LUA_SHAREDIR=%{luapkgdir}" \
  "LUA_BINDIR=%{_bindir}" \
  "DESTDIR=%{buildroot}"

# fix scripts
sed -i %{buildroot}%{_bindir}/ldoc -e '1i#!/bin/sh'
sed -i %{buildroot}%{luapkgdir}/ldoc.lua -e '1{/^#!/d}'

# create documentation
lua ldoc.lua .
markdown.lua README.md > README.html
markdown.lua CHANGELOG.md > CHANGELOG.html

# fix permissions
chmod u=rwX,go=rX -R public

# fix line-endings
sed -i 's/\r//' COPYRIGHT

# we depend on lua-markdown instead
rm %{buildroot}%{luapkgdir}/ldoc/markdown.lua

# cleanup
rm %{buildroot}%{luapkgdir}/ldoc/SciTE.properties \
   %{buildroot}%{luapkgdir}/ldoc/config.ld

# install docs
mkdir -p %{buildroot}%{_pkgdocdir}
cp -av %{!?_licensedir:COPYRIGHT} README.html CHANGELOG.html public/* \
  %{buildroot}%{_pkgdocdir}

%files
%dir %{_pkgdocdir}
%license COPYRIGHT
%{_pkgdocdir}/README.html
%{_bindir}/ldoc
%{luapkgdir}/ldoc
%{luapkgdir}/ldoc.lua

%files doc
%{_pkgdocdir}/index.html
%{_pkgdocdir}/ldoc_new.css
%{_pkgdocdir}/examples
%{_pkgdocdir}/manual
%{_pkgdocdir}/programs
%{_pkgdocdir}/CHANGELOG.html

%changelog
%autochangelog
