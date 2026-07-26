%global source0_hash c5e77dd2e40e14f0e68dd08df1f21cd1378d88d5001e7c1926ceb7c4a977ab86

%global commit bbb2404580e845df2556560112c8aefa27494d66
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           stfl
Version:        0.24
Release:        2.newsboat.git%{shortcommit}%{?dist}
Summary:        The Structured Terminal Forms Language/Library

License:        LGPL-3.0-or-later
URL:            https://github.com/newsboat/stfl
Source0:        https://github.com/newsboat/stfl/archive/%{commit}.tar.gz

# STFL is unmaintained and the bindings are not used within Fedora. Obsolete
# them to reduce the footprint of the package and avoid needing rebuilds for
# language ecosystems unnecessarily.
# https://bugzilla.redhat.com/show_bug.cgi?id=2420468
Obsoletes:      stfl-perl < 0.22-54
Obsoletes:      stfl-ruby < 0.22-54

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  ncurses-devel

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
# building with smp flags causes random failures
export CFLAGS="%{optflags}"
# test with explicit prefix and echo
#make prefix=/usr libdir=%{_lib}

# Parallel build is unstable :/
#make  %{?_smp_mflags}
make

%install
%make_install
# give the shared libraries executable permissions so they get stripped
# also fixes the 0555 permissions on the perl bindings
find %{buildroot} -name '*.so' -exec chmod 755 {} ';'
# fedora doesn't ship static libraries
rm -f %{buildroot}%{_libdir}/libstfl.a

%ldconfig_scriptlets

%files
%doc README COPYING
%{_libdir}/*.so.0*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/stfl.pc

%changelog
%autochangelog
