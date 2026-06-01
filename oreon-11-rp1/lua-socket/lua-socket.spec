%global source0_hash bf033aeb9e62bcaa8d007df68c119c966418e8c9ef7e4f2d7e96bddeca9cca6e

%{!?lua_compat_version: %global lua_compat_version 5.1}
%{!?lua_compat_libdir: %global lua_compat_libdir %{_libdir}/lua/%{lua_compat_version}}
%{!?lua_compat_pkgdir: %global lua_compat_pkgdir %{_datadir}/lua/%{lua_compat_version}}
%{!?lua_compat_builddir: %global lua_compat_builddir %{_builddir}/compat-lua-%{name}-%{version}-%{release}}

Summary:        Network support for the Lua language
Name:           lua-socket
Version:        3.1.0
Release:        9%{?dist}
License:        MIT
URL:            https://lunarmodules.github.io/luasocket/
Source0:        https://github.com/lunarmodules/luasocket/archive/v%{version}/luasocket-%{version}.tar.gz#/lua-socket-3.1.0.tar.gz
Requires:       lua(abi) = %{lua_version}
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
Obsoletes:      lua-socket-devel < 3.0.0-1

%description
LuaSocket is a Lua extension library that is composed by two parts: The C
core that provides support for the TCP and UDP transport layers, and the
set of Lua modules that add support for functionality commonly needed by
applications that deal with the Internet.

Among the support modules, the most commonly used implement the SMTP, HTTP
and FTP. In addition there are modules for MIME, URL handling and LTN12.

%if 0%{?fedora} || (0%{?oreon} >= 11)
%package -n lua%{lua_compat_version}-socket
Summary:        Network support for the Lua %{lua_compat_version} language
Obsoletes:      lua-socket-compat < 3.0-0.28.rc1
Provides:       lua-socket-compat = %{version}-%{release}
Provides:       lua-socket-compat%{?_isa} = %{version}-%{release}
Requires:       lua(abi) = %{lua_compat_version}
BuildRequires:  compat-lua >= %{lua_compat_version}
BuildRequires:  compat-lua-devel >= %{lua_compat_version}

%description -n lua%{lua_compat_version}-socket
LuaSocket is a Lua %{lua_compat_version} extension library that is composed by two parts: The
C core that provides support for the TCP and UDP transport layers, and the
set of Lua %{lua_compat_version} modules that add support for functionality commonly needed by
applications that deal with the Internet.

Among the support modules, the most commonly used implement the SMTP, HTTP
and FTP. In addition there are modules for MIME, URL handling and LTN12.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n luasocket-%{version}

%if 0%{?fedora} || (0%{?oreon} >= 11)
rm -rf %{lua_compat_builddir}
cp -a . %{lua_compat_builddir}
%endif

%build
%make_build linux \
  LUAV=%{lua_version} \
  CFLAGS_linux="$RPM_OPT_FLAGS -fPIC -I%{_includedir} -DLUASOCKET_NODEBUG -DLUA_COMPAT_APIINTCASTS" \
  LDFLAGS_linux="$RPM_LD_FLAGS -shared -o "

%if 0%{?fedora} || (0%{?oreon} >= 11)
pushd %{lua_compat_builddir}
%make_build linux \
  LUAV=%{lua_compat_version} \
  CFLAGS_linux="$RPM_OPT_FLAGS -fPIC -I%{_includedir}/lua-%{lua_compat_version} -DLUASOCKET_NODEBUG -DLUA_COMPAT_APIINTCASTS" \
  LDFLAGS_linux="$RPM_LD_FLAGS -shared -o "
popd
%endif

%install
make install-unix INSTALL_DATA='install -p -m 644' \
  INSTALL_TOP=$RPM_BUILD_ROOT \
  INSTALL_TOP_CDIR=$RPM_BUILD_ROOT%{lua_libdir} \
  INSTALL_TOP_LDIR=$RPM_BUILD_ROOT%{lua_pkgdir}

%if 0%{?fedora} || (0%{?oreon} >= 11)
pushd %{lua_compat_builddir}
make install-unix INSTALL_DATA='install -p -m 644' \
  INSTALL_TOP=$RPM_BUILD_ROOT \
  INSTALL_TOP_CDIR=$RPM_BUILD_ROOT%{lua_compat_libdir} \
  INSTALL_TOP_LDIR=$RPM_BUILD_ROOT%{lua_compat_pkgdir}
popd
%endif

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   dofile("test/hello.lua");'

%if 0%{?fedora} || (0%{?oreon} >= 11)
lua-%{lua_compat_version} -e \
  'package.cpath="%{buildroot}%{lua_compat_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_compat_pkgdir}/?.lua;"..package.path;
   dofile("test/hello.lua");'
%endif

%files
%license LICENSE
%doc CHANGELOG.md README.md docs/*.html docs/*.css docs/*.png
%{lua_libdir}/mime/
%{lua_libdir}/socket/
%{lua_pkgdir}/*.lua
%{lua_pkgdir}/socket/

%if 0%{?fedora} || (0%{?oreon} >= 11)
%files -n lua%{lua_compat_version}-socket
%license LICENSE
%doc CHANGELOG.md README.md docs/*.html docs/*.css docs/*.png
%{lua_compat_libdir}/mime/
%{lua_compat_libdir}/socket/
%{lua_compat_pkgdir}/*.lua
%{lua_compat_pkgdir}/socket/
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.0-9
- Import
