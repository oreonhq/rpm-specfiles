%global source0_hash 2387431c0e83c4189cccb35b989141a3280d735cb5d42bacf3451af9869bebf7

Name:		lua-penlight
Version:	1.14.0
Release:	4%{?dist}
Summary:	Penlight Lua Libraries
License:	MIT
URL:		https://github.com/lunarmodules/Penlight
Source0:	https://github.com/lunarmodules/Penlight/archive/%{version}/Penlight-%{version}.tar.gz

%global luaver 5.4
%global luapkgdir %{_datadir}/lua/%{luaver}

# there's a circular (build) dependency with lua-ldoc
%bcond_without docs

BuildArch:	noarch
BuildRequires:	lua >= %{luaver}
BuildRequires:	lua-filesystem
BuildRequires:	lua-markdown
%if %{with docs}
BuildRequires:	lua-ldoc
%endif # with docs
Requires:	lua >= %{luaver}
Requires:	lua-filesystem

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global __requires_exclude_from %{_docdir}

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
# nothing to do here

%install
mkdir -p %{buildroot}%{luapkgdir}
cp -av lua/pl %{buildroot}%{luapkgdir}

# fix scripts
chmod -x %{buildroot}%{luapkgdir}/pl/dir.lua

# build and install README etc.
mkdir -p %{buildroot}%{_pkgdocdir}
markdown.lua {README,CHANGELOG,CONTRIBUTING,LICENSE}.md
cp -av {README,CHANGELOG,CONTRIBUTING}.html %{buildroot}%{_pkgdocdir}

%if %{with docs}
# build and install docs
ldoc .
cp -av docs %{buildroot}%{_pkgdocdir}
%endif # with docs

# install examples
cp -av examples %{buildroot}%{_pkgdocdir}

%check
# currently disabled: missing luacov
# LUA_PATH="%%{buildroot}%%{luapkgdir}/?/init.lua;%%{buildroot}%%{luapkgdir}/?.lua;;" \
# lua run.lua tests

%files
%dir %{_pkgdocdir}
%license LICENSE.html
%{_pkgdocdir}/README.html
%{_pkgdocdir}/CHANGELOG.html
%{_pkgdocdir}/CONTRIBUTING.html
%{luapkgdir}/pl

%if %{with docs}
%files doc
%{_pkgdocdir}/docs
%endif # with docs

%files examples
%{_pkgdocdir}/examples

%changelog
%autochangelog
