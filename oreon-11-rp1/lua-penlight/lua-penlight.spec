%global source0_hash b7a2c3e65799a649d29e9927a337f99cca2a5fc46367a0ce101435be74e53b39
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:		lua-penlight
Version:	1.15.0
Release:        1%{?dist}
Summary:        Penlight Lua Libraries
License:	MIT
URL:		https://github.com/lunarmodules/Penlight
Source0:        https://github.com/lunarmodules/Penlight/archive/%{version}/Penlight-%{version}.tar.gz
%global luaver 5.4
%global luapkgdir %{_datadir}/lua/%{luaver}
%bcond_without docs
BuildArch:	noarch
%if %{with docs}
%endif # with docs
Requires:	lua >= %{luaver}
Requires:	lua-filesystem
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global __requires_exclude_from %{_docdir}
# oreon:deps
BuildRequires:  lua
BuildRequires:  lua-filesystem
BuildRequires:  lua-ldoc
BuildRequires:  lua-markdown
# /oreon:deps
%description
A set of pure Lua libraries focusing on input data handling (such as
reading configuration files), functional programming (such as map,
reduce, placeholder expressions, etc.), and OS path management. Much
of the functionality is inspired by the Python standard libraries.

%if %{with docs}
%package doc
Summary:	API docs for lua-penlight
Requires:	%{name} = %{version}-%{release}
%description doc
%{summary}
%endif # with docs

%package examples
Summary:	Examples of lua-penlight usage
Requires:	%{name} = %{version}-%{release}
%description examples
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Penlight-%{version}

%build

%install
mkdir -p %{buildroot}%{luapkgdir}
cp -av lua/pl %{buildroot}%{luapkgdir}
chmod -x %{buildroot}%{luapkgdir}/pl/dir.lua
mkdir -p %{buildroot}%{_pkgdocdir}
markdown.lua {README,CHANGELOG,CONTRIBUTING,LICENSE}.md
cp -av {README,CHANGELOG,CONTRIBUTING}.html %{buildroot}%{_pkgdocdir}
%if %{with docs}
ldoc .
cp -av docs %{buildroot}%{_pkgdocdir}
%endif # with docs
cp -av examples %{buildroot}%{_pkgdocdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n lua-penlight-doc -f %{oreon_filedir}/lua-penlight-doc.list
%files -n lua-penlight-examples -f %{oreon_filedir}/lua-penlight-examples.list

%changelog

%autochangelog
