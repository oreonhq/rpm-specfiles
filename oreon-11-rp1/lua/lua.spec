%global source0_hash none
%global source2_hash 4f18ddae154e793e46eeab727c59ef1c0c0c2b744e7b94219710d76f530629ae
%global source3_hash 5e47bbfad7db2965d69580e918ee64edeb8d8d32de404b8dae9ce5c6d76a1472

%global major_version 5.5
# Normally, this is the same as version, but... not always.
%global test_version 5.5.0
# If you are incrementing major_version, enable bootstrapping and adjust accordingly.
# Version should be the latest prior build. If you don't do this, RPM will break and
# everything will grind to a halt.
%global bootstrap 1
%global bootstrap_major_version 5.4
%global bootstrap_version %{bootstrap_major_version}.8

# Place rpm-macros into proper location.
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)


Name:           lua
Version:        %{major_version}.0
Release:        1%{?dist}
Summary:        Powerful light-weight programming language
License:        MIT
URL:            https://www.lua.org/
Source0:        https://www.lua.org/ftp/lua-%{version}.tar.gz
# copied from doc/readme.html on 2014-07-18
Source1:        mit.txt
%if 0%{?bootstrap}
Source2:        https://www.lua.org/ftp/lua-5.4.8.tar.gz
%endif
Source3:        https://www.lua.org/tests/lua-5.5.0-tests.tar.gz
# multilib
Source4:        luaconf.h
Patch0:         %{name}-5.5.0-autotoolize.patch
Patch1:         %{name}-5.4.6-idsize.patch
#Patch2:         %%{name}-5.3.0-luac-shared-link-fix.patch
Patch3:         %{name}-5.2.2-configure-linux.patch
Patch4:         %{name}-5.3.0-configure-compat-module.patch
%if 0%{?bootstrap}
Patch5:         %{name}-5.4.8-autotoolize.patch
Patch6:		%{name}-5.4.8-luac-shared-link-fix.patch
Patch7:		%{name}-5.4.8-bug1.patch
Patch8:		%{name}-5.4.8-bug2.patch
Patch9:		%{name}-5.4.8-bug3.patch
%endif
# https://www.lua.org/bugs.html
Patch10:	lua-5.5.0-bug1.patch
Patch11:	lua-5.5.0-bug2.patch

BuildRequires:  automake autoconf libtool readline-devel ncurses-devel
BuildRequires:  make
Requires:       lua-libs = %{version}-%{release}

%description
Lua is a powerful light-weight programming language designed for
extending applications. Lua is also frequently used as a
general-purpose, stand-alone language. Lua is free software.
Lua combines simple procedural syntax with powerful data description
constructs based on associative arrays and extensible semantics. Lua
is dynamically typed, interpreted from bytecodes, and has automatic
memory management with garbage collection, making it ideal for
configuration, scripting, and rapid prototyping.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# The RPM related dependencies bring nothing to a non-RPM Lua developer
# But we want them when packages BuildRequire lua-devel
Requires:       (lua-rpm-macros if rpm-build)
Requires:       pkgconfig

%description devel
This package contains development files for %{name}.

%package libs
Summary:        Libraries for %{name}
Provides:       lua(abi) = %{major_version}

%description libs
This package contains the shared libraries for %{name}.

%package static
Summary:        Static library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description static
This package contains the static version of liblua for %{name}.

%if 0%{?bootstrap}
%package -n %{name}%{bootstrap_major_version}-libs
Summary:        Compat libraries for %{name}%{bootstrap_major_version}
Provides:       lua(abi) = %{bootstrap_major_version}

%description -n %{name}%{bootstrap_major_version}-libs
This package contains compatibility libraries for lua %{bootstrap_major_version}..
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; })
%(test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; })
%if 0%{?bootstrap}
%setup -q -a 2 -a 3 -n %{name}-%{version}
%else
%setup -q -a 3
%endif
cp %{SOURCE1} .
mv src/luaconf.h src/luaconf.h.template.in
%patch -P0 -p1 -E -z .autoxxx
%patch -P1 -p1 -z .idsize
#%% patch -P2 -p1 -z .luac-shared
%patch -P3 -p1 -z .configure-linux

# Bug patches here
%patch -P10 -p1 -b .bug1
%patch -P11 -p1 -b .bug2

# Put proper version in configure.ac, patch0 hardcodes 5.5.0
sed -i 's|5.5.0|%{version}|g' configure.ac
autoreconf -ifv


%if 0%{?bootstrap}
cd lua-%{bootstrap_version}/
mv src/luaconf.h src/luaconf.h.template.in
%patch -P5 -p1 -b .autoxxx
%patch -P1 -p1 -b .idsize
%patch -P3 -p1 -z .configure-linux
%patch -P4 -p1 -z .configure-compat-all
%patch -P6 -p1 -b .luac-shared-link-fix
%patch -P7 -p1 -b .54bug1
%patch -P8 -p1 -b .54bug2
%patch -P9 -p1 -b .54bug3
autoreconf -i
cd ..
%endif


%build
%configure --with-readline --with-compat-module
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# Autotools give me a headache sometimes.
sed -i 's|@pkgdatadir@|%{_datadir}|g' src/luaconf.h.template

# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles
%make_build LIBS="-lm -ldl"
# only /usr/bin/lua links with readline now #luac_LDADD="liblua.la -lm -ldl"

%if 0%{?bootstrap}
pushd lua-%{bootstrap_version}
%configure --with-readline --with-compat-module
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# Autotools give me a headache sometimes.
sed -i 's|@pkgdatadir@|%{_datadir}|g' src/luaconf.h.template

# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles
%make_build LIBS="-lm -ldl" luac_LDADD="liblua.la -lm -ldl"
popd
%endif

%check
cd ./lua-%{test_version}-tests/

# Dont skip the fully portable or ram-hungry tests:
# sed -i.orig -e '
#     /attrib.lua/d;
#     /files.lua/d;
#     /db.lua/d;
#     /errors.lua/d;
#     ' all.lua
# LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%%{_libdir} $RPM_BUILD_ROOT/%%{_bindir}/lua all.lua

# Removing tests that fail under mock/koji
sed -i.orig -e '
    /db.lua/d;
    /errors.lua/d;
    ' all.lua
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir} $RPM_BUILD_ROOT/%{_bindir}/lua -e"_U=true" all.lua

%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_libdir}/lua/%{major_version}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/lua/%{major_version}

# Rename luaconf.h to luaconf-<arch>.h to avoid file conflicts on
# multilib systems and install luaconf.h wrapper
mv %{buildroot}%{_includedir}/luaconf.h %{buildroot}%{_includedir}/luaconf-%{_arch}.h
install -p -m 644 %{SOURCE4} %{buildroot}%{_includedir}/luaconf.h

%if 0%{?bootstrap}
pushd lua-%{bootstrap_version}
mkdir $RPM_BUILD_ROOT/installdir
make install DESTDIR=$RPM_BUILD_ROOT/installdir
cp -a $RPM_BUILD_ROOT/installdir/%{_libdir}/liblua-%{bootstrap_major_version}.so $RPM_BUILD_ROOT%{_libdir}/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/lua/%{bootstrap_major_version}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/lua/%{bootstrap_major_version}
rm -rf $RPM_BUILD_ROOT/installdir
popd
%endif

%files
%doc README doc/*.html doc/*.css doc/*.png
%{_bindir}/lua
%{_bindir}/luac
%{_mandir}/man1/lua*.1*

%files libs
%{!?_licensedir:%global license %%doc}
%license mit.txt

%dir %{_libdir}/lua
%dir %{_libdir}/lua/%{major_version}
%{_libdir}/liblua-%{major_version}.so
%dir %{_datadir}/lua
%dir %{_datadir}/lua/%{major_version}

%if 0%{?bootstrap}
%files -n %{name}%{bootstrap_major_version}-libs
%license mit.txt
%dir %{_libdir}/lua/%{bootstrap_major_version}
%{_libdir}/liblua-%{bootstrap_major_version}.so
%dir %{_datadir}/lua/%{bootstrap_major_version}
%endif

%files devel
%{_includedir}/l*.h
%{_includedir}/l*.hpp
%{_libdir}/liblua.so
%{_libdir}/pkgconfig/*.pc

%files static
%{_libdir}/*.a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{major_version}.0-1
- Prepare for Oreon 11 (RP1)
