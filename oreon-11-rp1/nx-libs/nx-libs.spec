%global source0_hash 05d3d28a672475e5490c7b7ba39e1808794b6ae1443a7ec219974b50beddbeea
%global _hardened_build 1
%ifarch ppc64le
%if 0%{?el7}
%global __global_cflags %{__global_cflags} -mno-vsx
%global __global_cxxflags %{__global_cxxflags} -mno-vsx
%endif
%endif
Name:           nx-libs
Version:        3.5.99.27
Release:        9%{?dist}
Summary:        NX X11 protocol compression libraries
License:        GPL-2.0-or-later
URL:            https://github.com/ArcticaProject/nx-libs
Source0:        https://github.com/ArcticaProject/nx-libs/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      nx < 3.5.0-19
Provides:       nx = %{version}-%{release}
Provides:       nx%{?_isa} = %{version}-%{release}
Obsoletes:      libNX_Xau < 3.5.99.1
Obsoletes:      libNX_Xcomposite < 3.5.99.1
Obsoletes:      libNX_Xdamage < 3.5.99.1
Obsoletes:      libNX_Xdmcp < 3.5.99.1
Obsoletes:      libNX_Xext < 3.5.99.1
Obsoletes:      libNX_Xfixes < 3.5.99.1
Obsoletes:      libNX_Xinerama < 3.5.99.1
Obsoletes:      libNX_Xpm < 3.5.99.1
Obsoletes:      libNX_Xrandr < 3.5.99.1
Obsoletes:      libNX_Xrender < 3.5.99.1
Obsoletes:      libNX_Xtst < 3.5.99.1
Obsoletes:      libXcompext < 3.5.99.3
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  imake
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXfont-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pixman-devel
BuildRequires:  python-rpm-macros
BuildRequires:  quilt
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

%package -n libNX_X11
Summary:        Core NX protocol client library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n libNX_X11
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

%package -n libNX_X11-devel
Summary:        Development files for the Core NX protocol library
Requires:       libNX_X11%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}
%description -n libNX_X11-devel
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

This package contains all necessary include files and libraries
needed to develop applications that require these.

%package -n libXcomp-devel
Summary:        Development files for the NX differential compression library
Requires:       libXcomp%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel = %{version}-%{release}
Obsoletes:      libXcompext-devel < 3.5.99.3
%description -n libXcomp-devel
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The NX differential compression library's development files.

%package -n libXcomp
Summary:        NX differential compression library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n libXcomp
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package contains the NX differential compression library for X11.

%package -n libXcompshad-devel
Summary:        Development files for the NX session shadowing library
Requires:       libXcompshad%{?_isa} = %{version}-%{release}
Requires:       libNX_X11-devel%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description -n libXcompshad-devel
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

The NX session shadowing library's development files.

%package -n libXcompshad
Summary:        NX session shadowing Library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n libXcompshad
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package provides the session shadowing library.

%package devel
Summary:        Include files and libraries for NX development
Requires:       libNX_X11-devel%{?_isa} = %{version}-%{release}
Requires:       nx-proto-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      libNX_Xau-devel < 3.5.99.1
Obsoletes:      libNX_Xdmcp-devel < 3.5.0.32-2
Obsoletes:      libNX_Xext-devel < 3.5.99.1
Obsoletes:      libNX_Xfixes-devel < 3.5.99.1
Obsoletes:      libNX_Xpm-devel < 3.5.0.32-2
Obsoletes:      libNX_Xrender-devel < 3.5.99.1
%description devel
NX is a software suite from NoMachine which implements very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, especially a slow one.

This package contains all necessary include files and libraries
needed to develop nx-X11 applications that require these.

%package -n nx-proto-devel
Summary:        Include files for NX development
%description -n nx-proto-devel
This package contains all necessary include files and libraries
for the nx_X11 wire protocol.

%package -n nxagent
Summary:        NX Agent
Requires:       xkeyboard-config
Obsoletes:      nx < 3.5.0-19
Provides:       nx = %{version}-%{release}
Provides:       nx%{?_isa} = %{version}-%{release}
Obsoletes:      nxauth < 3.5.99.1
%description -n nxagent
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
applications over a network, especially a slow one.

nxagent is an agent providing NX transport of X sessions. The
application is based on the well-known Xnest server. nxagent, like
Xnest, is an X server for its own clients, and at the same time, an X
client for a system's local X server.

The main scope of nxagent is to eliminate X round-trips or transform
them into asynchronous replies. nxagent works together with nxproxy.
nxproxy itself does not make any effort to minimize round-trips by
itself, this is demanded of nxagent.

Being an X server, nxagent is able to resolve all the property/atoms
related requests locally, ensuring that the most common source of
round-trips are nearly reduced to zero.

%package -n nxproxy
Summary:        NX Proxy
Obsoletes:      nx < 3.5.0-19
Provides:       nx = %{version}-%{release}
Provides:       nx%{?_isa} = %{version}-%{release}
%description -n nxproxy
This package provides the NX proxy (client) binary.

%package -n nxdialog
Summary:        NX Dialog
%description -n nxdialog
NX is a software suite which implements very efficient compression of
the X11 protocol. This increases performance when using X
pplications over a network, especially a slow one.

This package provides the nxdialog helper script.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Install into /usr
sed -i -e 's,/usr/local,/usr,' nx-X11/config/cf/site.def
# Fix FSF address
find -name LICENSE | xargs sed -i \
  -e 's/59 Temple Place/51 Franklin Street/' -e 's/Suite 330/Fifth Floor/' \
  -e 's/MA  02111-1307/MA  02110-1301/'
# Fix source permissions
find -type f -name '*.[hc]' | xargs chmod -x

# Bundled nx-X11/extras
# Mesa - Used by the X server
# Xcursor - Other code still references files in it

%build

cat >"my_configure" <<'EOF'
%configure --disable-silent-rules "${@}"
EOF
chmod a+x my_configure;
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro -Wl,-z,now}
export SHLIBGLOBALSFLAGS="%{__global_ldflags}"
export LOCAL_LDFLAGS="%{__global_ldflags}"
export CDEBUGFLAGS="%{optflags}"
IMAKE_DEFINES="-DUseTIRPC=YES"
make VERBOSE=1 CONFIGURE="$PWD/my_configure" LIBDIR=%{_libdir} CDEBUGFLAGS="${CDEBUGFLAGS}" LOCAL_LDFLAGS="${LOCAL_LDFLAGS}" SHLIBGLOBALSFLAGS="${SHLIBGLOBALSFLAGS}" IMAKE_DEFINES="${IMAKE_DEFINES}"
%install
%make_install \
        PREFIX=%{_prefix} \
        LIBDIR=%{_libdir} SHLIBDIR=%{_libdir} \
        INSTALL_DIR="install -dm0755" \
        INSTALL_FILE="install -pm0644" \
        INSTALL_PROGRAM="install -pm0755"
ln -s ../X11/fonts %{buildroot}%{_datadir}/nx/fonts
rm %{buildroot}%{_libdir}/*.a
chmod 755  %{buildroot}%{_libdir}/lib*.so*
rm -r %{buildroot}%{_includedir}/GL
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/XK*.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/*Xv*.h
rm -r %{buildroot}%{_includedir}/nx-X11/Xtrans
rm %{buildroot}%{_libdir}/*.la
pathfix.py -pni "%{__python2} %{py2_shbang_opts}" %{buildroot}%{_bindir}/nxdialog
%ldconfig_scriptlets
%ldconfig_scriptlets -n libNX_X11
%ldconfig_scriptlets -n libXcomp
%ldconfig_scriptlets -n libXcompshad
%oreon_autofiles libNX_X11 usr/*/lib*.so.*
%oreon_autofiles libNX_X11-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libXcomp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libXcomp usr/*/lib*.so.*
%oreon_autofiles libXcompshad-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libXcompshad usr/*/lib*.so.*
%oreon_autofiles nx-proto-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles nxagent usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nxproxy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nxdialog usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libNX_X11 -f %{oreon_filedir}/libNX_X11.list
%files -n libNX_X11-devel -f %{oreon_filedir}/libNX_X11-devel.list
%files -n libXcomp-devel -f %{oreon_filedir}/libXcomp-devel.list
%files -n libXcomp -f %{oreon_filedir}/libXcomp.list
%files -n libXcompshad-devel -f %{oreon_filedir}/libXcompshad-devel.list
%files -n libXcompshad -f %{oreon_filedir}/libXcompshad.list
%files -n nx-libs-devel -f %{oreon_filedir}/nx-libs-devel.list
%files -n nx-proto-devel -f %{oreon_filedir}/nx-proto-devel.list
%files -n nxagent -f %{oreon_filedir}/nxagent.list
%files -n nxproxy -f %{oreon_filedir}/nxproxy.list
%files -n nxdialog -f %{oreon_filedir}/nxdialog.list

%changelog

%autochangelog
