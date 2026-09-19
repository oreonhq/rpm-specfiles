%global source0_hash de71e20a55f8d8a99f133abb3c7bf13b128f5cc8fbe1629f3c1da337a367edd0

%global commit e9deec8231c0d1f99a8f1615b6cefdd493da4411
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global headerversion 1.35.2
Name:           janet
Version:        1.35.2^20240907git%{shortcommit}
Release:        %autorelease
Summary:        A dynamic language and bytecode vm

License:        MIT
URL:            https://janet-lang.org
Source0:        https://github.com/janet-lang/janet/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson

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
# Create HTML documentation file
%{_vpath_builddir}/janet tools/gendoc.janet  > doc.html

%install
%meson_install
# Amalgamated janet.c file is used to embed Janet in C applications
mkdir -p %{buildroot}/%{_libdir}/janet
install -Dm644 %{_builddir}/%{name}-%{commit}/%{_vpath_builddir}/janet.c \
 %{buildroot}/%{_libdir}/janet/janet.c
install -Dm644 src/conf/janetconf.h %{buildroot}/%{_includedir}/janetconf.h
# Do not package hidden file
rm %{buildroot}/%{_libdir}/janet/.keep

%check
%meson_test

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%doc doc.html
%doc examples/
%{_mandir}/man1/janet.1*
%{_bindir}/janet
%{_libdir}/libjanet.so.1.*

%files devel
%{_libdir}/pkgconfig/janet.pc
%{_includedir}/janet.h
%{_includedir}/janetconf.h
%{_libdir}/libjanet.so
%dir %{_includedir}/janet
%{_includedir}/janet/janet.h
%{_includedir}/janet/janet_%{headerversion}.h
%dir %{_libdir}/janet
%{_libdir}/janet/janet.c

%changelog
%autochangelog
