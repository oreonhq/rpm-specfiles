%global source0_hash de71e20a55f8d8a99f133abb3c7bf13b128f5cc8fbe1629f3c1da337a367edd0
%global commit e9deec8231c0d1f99a8f1615b6cefdd493da4411
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global headerversion 1.35.2
Name:           janet
Version:        1.35.2^20240907git%{shortcommit}
Release:        1%{?dist}
Summary:        A dynamic language and bytecode vm
License:        MIT
URL:            https://janet-lang.org
Source0:        https://github.com/%{name}-lang/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
# /oreon:deps
%description
Janet makes a good system scripting language, or a language
to embed in other programs. It's like Lua and GNU Guile in
that regard. It has more built-in functionality and a richer
core language than Lua, but smaller than GNU Guile or Python.
However, it is much easier to embed and port than Python or
Guile.

There is a REPL for trying out the language, as well as the
ability to run script files. This client program is separate
from the core runtime, so Janet can be embedded in other
programs. Try Janet in your browser at https://janet-lang.org.

%package devel
Summary:   A dynamic language and bytecode vm
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for Janet.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}
rm examples/numarray/.gitignore

%build

%meson --buildtype=release -Ddefault_library=shared
%meson_build
%{_vpath_builddir}/janet tools/gendoc.janet  > doc.html
%install
%meson_install
mkdir -p %{buildroot}/%{_libdir}/janet
install -Dm644 %{_builddir}/%{name}-%{commit}/%{_vpath_builddir}/janet.c \
 %{buildroot}/%{_libdir}/janet/janet.c
install -Dm644 src/conf/janetconf.h %{buildroot}/%{_includedir}/janetconf.h
rm %{buildroot}/%{_libdir}/janet/.keep
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n janet-devel -f %{oreon_filedir}/janet-devel.list

%changelog

%autochangelog
