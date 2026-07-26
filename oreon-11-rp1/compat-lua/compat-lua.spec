%global source0_hash 2640fc56a795f29d28ef15e13c34a47e223960b0240e8cb0a82d9b0738695333

Name:           compat-lua
Version:        5.1.5
Release:        31%{?dist}
Summary:        Powerful light-weight programming language (compat version)
License:        MIT
URL:            http://www.lua.org/
Source0:        http://www.lua.org/ftp/lua-%{version}.tar.gz
Patch0:         lua-5.1.4-autotoolize.patch
Patch1:         lua-5.1.4-lunatic.patch
Patch2:         lua-5.1.4-idsize.patch
Patch3:         lua-5.1.4-pc-compat.patch
BuildRequires:  readline-devel ncurses-devel libtool
BuildRequires: make
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       lua = 5.1
Provides:       lua5.1 = %{version}-%{release}
Provides:       lua5.1%{?_isa} = %{version}-%{release}

%description
This package contains a compatibility version of the lua-5.1 binaries.

%package libs
Summary:        Powerful light-weight programming language (compat version)
Provides:       lua(abi) = 5.1
Provides:       lua5.1-libs = %{version}-%{release}
Provides:       lua5.1-libs%{?_isa} = %{version}-%{release}

%description libs
This package contains a compatibility version of the lua-5.1 libraries.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       lua5.1-devel = %{version}-%{release}
Provides:       lua5.1-devel%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for compat-lua-libs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lua-%{version}
%patch -P0 -p1 -E -z .autoxxx
%patch -P1 -p0 -z .lunatic
%patch -P2 -p1 -z .idsize
%patch -P3 -p1
# fix perms on auto files
chmod u+x autogen.sh config.guess config.sub configure depcomp install-sh missing
# Avoid make doing auto-reconf itself, killing our rpath removal in the process
autoreconf -i -f

%build
%configure --with-readline
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles
make %{?_smp_mflags} LIBS="-lm -ldl" luac_LDADD="liblua.la -lm -ldl"
# also remove readline from lua.pc
sed -i 's/-lreadline -lncurses //g' etc/lua.pc

%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/liblua.{a,la}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/lua/5.1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/lua/5.1
# Rename some files to avoid conflicts with 5.2
mv $RPM_BUILD_ROOT%{_bindir}/lua $RPM_BUILD_ROOT%{_bindir}/lua-5.1
mv $RPM_BUILD_ROOT%{_bindir}/luac $RPM_BUILD_ROOT%{_bindir}/luac-5.1
mv $RPM_BUILD_ROOT%{_mandir}/man1/lua.1 \
  $RPM_BUILD_ROOT%{_mandir}/man1/lua-5.1.1
mv $RPM_BUILD_ROOT%{_mandir}/man1/luac.1 \
  $RPM_BUILD_ROOT%{_mandir}/man1/luac-5.1.1
mkdir -p $RPM_BUILD_ROOT%{_includedir}/lua-5.1
mv $RPM_BUILD_ROOT%{_includedir}/l*h* $RPM_BUILD_ROOT%{_includedir}/lua-5.1
rm $RPM_BUILD_ROOT%{_libdir}/liblua.so
mv $RPM_BUILD_ROOT%{_libdir}/pkgconfig/lua.pc \
  $RPM_BUILD_ROOT%{_libdir}/pkgconfig/lua-5.1.pc

%ldconfig_scriptlets libs

%files
%{_bindir}/lua-5.1
%{_bindir}/luac-5.1
%{_mandir}/man1/lua*5.1.1*

%files libs
%doc COPYRIGHT HISTORY README doc/*.html doc/*.css doc/*.gif doc/*.png
%{_libdir}/liblua-5.1.so
%dir %{_libdir}/lua
%dir %{_libdir}/lua/5.1
%dir %{_datadir}/lua
%dir %{_datadir}/lua/5.1

%files devel
%{_includedir}/lua-5.1/
%{_libdir}/pkgconfig/lua-5.1.pc

%changelog
%autochangelog
