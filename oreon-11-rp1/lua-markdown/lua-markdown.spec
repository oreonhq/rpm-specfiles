%global source1_hash 2f4c07d0123fc3d682bae9927469dbaca146ce1184f8a9dc865f6d861a41c68b
%global source0_hash d24d35f249229c2a0ab2370dab96fd6fa6cf62719deac217d15a37c6703730c0
%global luaver 5.4
%global luapkgdir %{_datadir}/lua/%{luaver}
Name:		lua-markdown
Version:	0.32
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Markdown module for Lua
License:	MIT
URL:		http://www.frykholm.se/files/markdown.lua
Source0:        http://www.frykholm.se/files/markdown.lua
Source1:	http://www.frykholm.se/files/markdown-tests.lua
Patch0:		lua-markdown-0.32-lua-5.2.patch
Requires:	lua >= %{luaver}
# oreon:deps
BuildRequires:  lua
# /oreon:deps
%description
This is an implementation of the popular text markup language Markdown
in pure Lua.  Markdown can convert documents written in a simple and
easy to read text format to well-formatted HTML.

%prep

%setup -c -T
cp -av %{SOURCE0} .
cp -av %{SOURCE1} .
%patch -P0 -p1 -b .lua-52

%build

%install
mkdir -p %{buildroot}%{luapkgdir}
mkdir -p %{buildroot}%{_bindir}
cp -av markdown.lua %{buildroot}%{luapkgdir}
sed -i %{buildroot}%{luapkgdir}/markdown.lua -e '1{/^#!/d}'
echo -en '#!/bin/sh\nlua %{luapkgdir}/markdown.lua "$@"' \
  > %{buildroot}%{_bindir}/markdown.lua
chmod +x %{buildroot}%{_bindir}/markdown.lua
%oreon_autofiles main

%check

lua markdown.lua -t
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
