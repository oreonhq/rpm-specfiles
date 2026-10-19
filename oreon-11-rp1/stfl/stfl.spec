%global source0_hash c5e77dd2e40e14f0e68dd08df1f21cd1378d88d5001e7c1926ceb7c4a977ab86
%global commit bbb2404580e845df2556560112c8aefa27494d66
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           stfl
Version:        0.24
Release:        1%{?dist}
Summary:        The Structured Terminal Forms Language/Library
License:        LGPL-3.0-or-later
URL:            https://github.com/newsboat/stfl
Source0:        https://github.com/newsboat/%{name}/archive/%{commit}.tar.gz
Obsoletes:      stfl-perl < 0.22-54
Obsoletes:      stfl-ruby < 0.22-54
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
STFL is a library which implements a curses-based widget set for text
terminals.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
## ensures that _stfl.so doesn't end up in lib-dynload
## - http://www.rocklinux.net/pipermail/stfl/2009-June/000113.html
sed -i.path \
 -e '/mkdir.*lib-dynload/d' \
 -e '/cp/s|lib-dynload||' \
 python/Makefile.*
## creates an soname symlink for the shared library
## - http://www.rocklinux.net/pipermail/stfl/2009-June/000114.html
## add the new line needed (the part starting with \n) If you know a better way with sed to do it, please educate me
sed -i.soname \
 -e 's|\(.*ln -fs.*/\)\(libstfl\.so\)$|\1\2\n\1\$(SONAME)|' \
 Makefile
## fixes undefined-non-weak-symbol rpmlint warnings
## - http://www.rocklinux.net/pipermail/stfl/2009-October/000116.html
sed -i.ldflags -e 's|\(-shared\)|\1 \$(LDLIBS)|' Makefile
## fixes libdir for other arch than x86 
## - http://www.rocklinux.net/pipermail/stfl/2009-October/000118.html
sed -i.path -e 's|libdir=.*|libdir=%{_libdir}|' stfl.pc.in
sed -i.cflags -e 's|-Os||' Makefile
# fix paths in Makefile.cfg
sed -i.path -e 's|lib$|%{_lib}|' -e 's|/usr/local$|%{_prefix}|' Makefile.cfg

%build

export CFLAGS="%{optflags}"
make
%install
%make_install
find %{buildroot} -name '*.so' -exec chmod 755 {} ';'
rm -f %{buildroot}%{_libdir}/libstfl.a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n stfl-devel -f %{oreon_filedir}/stfl-devel.list

%changelog

%autochangelog
