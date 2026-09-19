%global source0_hash 05d3d28a672475e5490c7b7ba39e1808794b6ae1443a7ec219974b50beddbeea

%global _hardened_build 1
%ifarch ppc64le
%if 0%{?el7}
# Works around https://bugs.centos.org/view.php?id=13779 / https://bugzilla.redhat.com/show_bug.cgi?id=1489712
# Compilation failure on PPC64LE due to a compiler bug.
# REMEMBER TO REMOVE ONCE DOWNSTREAM FIXES THE ISSUE!
%global __global_cflags %{__global_cflags} -mno-vsx
%global __global_cxxflags %{__global_cxxflags} -mno-vsx
%endif
%endif

Name:           nx-libs
Version:        3.5.99.27
Release:        9%{?dist}
Summary:        NX X11 protocol compression libraries

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/ArcticaProject/nx-libs
Source0:        https://github.com/ArcticaProject/nx-libs/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  expat-devel
BuildRequires:  imake
BuildRequires:  make
BuildRequires:  quilt
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libxml2-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXfixes-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  libXfont2-devel
%else
BuildRequires:  libXfont-devel
%endif
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  pixman-devel
%if 0%{?fedora}
BuildRequires:  xkbcomp-devel
%else
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:  xorg-x11-xkb-utils-devel
%endif
%endif
# For imake
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  zlib-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python3-devel
%else
BuildRequires:  python-rpm-macros
%endif
%if !(0%{?fedora} >= 38 || 0%{?rhel} >= 8)
BuildRequires:  /usr/bin/pathfix.py
%endif

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
# For /usr/share/X11/xkb
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     xkeyboard-config
%else
Requires:       xkeyboard-config
%endif
# For /usr/share/X11/fonts
%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} <= 8 )
Requires:       xorg-x11-font-utils
%endif
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
# _hardened_build not working for EL6, at least define __global_ldflags for now
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro -Wl,-z,now}
export SHLIBGLOBALSFLAGS="%{__global_ldflags}"
export LOCAL_LDFLAGS="%{__global_ldflags}"
export CDEBUGFLAGS="%{optflags}"
IMAKE_DEFINES="-DUseTIRPC=YES"
# parallel make failed
make VERBOSE=1 CONFIGURE="$PWD/my_configure" LIBDIR=%{_libdir} CDEBUGFLAGS="${CDEBUGFLAGS}" LOCAL_LDFLAGS="${LOCAL_LDFLAGS}" SHLIBGLOBALSFLAGS="${SHLIBGLOBALSFLAGS}" IMAKE_DEFINES="${IMAKE_DEFINES}"

%install
%make_install \
        PREFIX=%{_prefix} \
        LIBDIR=%{_libdir} SHLIBDIR=%{_libdir} \
        INSTALL_DIR="install -dm0755" \
        INSTALL_FILE="install -pm0644" \
        INSTALL_PROGRAM="install -pm0755"

ln -s ../X11/fonts %{buildroot}%{_datadir}/nx/fonts

# Remove static libs
rm %{buildroot}%{_libdir}/*.a

# Fix permissions on shared libraries
chmod 755  %{buildroot}%{_libdir}/lib*.so*

# Remove extras, GL, and other unneeded headers
rm -r %{buildroot}%{_includedir}/GL
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/XK*.h
rm -r %{buildroot}%{_includedir}/nx-X11/extensions/*Xv*.h
rm -r %{buildroot}%{_includedir}/nx-X11/Xtrans

#Remove our shared libraries' .la files before wrapping up the packages
rm %{buildroot}%{_libdir}/*.la

# Fix python scripts
%if 0%{?fedora} || 0%{?rhel} >= 8
%py3_shebang_fix %{buildroot}%{_bindir}/nxdialog
%else
pathfix.py -pni "%{__python2} %{py2_shbang_opts}" %{buildroot}%{_bindir}/nxdialog
%endif

%ldconfig_scriptlets
%ldconfig_scriptlets -n libNX_X11
%ldconfig_scriptlets -n libXcomp
%ldconfig_scriptlets -n libXcompshad

%files
%license COPYING LICENSE LICENSE.nxcomp
%doc ChangeLog
%dir %{_libdir}/nx
%dir %{_datadir}/nx
%dir %{_datadir}/nx/X11
%{_datadir}/nx/SecurityPolicy
%{_datadir}/nx/X11/XErrorDB
%{_datadir}/nx/X11/Xcms.txt

%files -n libNX_X11
%{_libdir}/libNX_X11.so.6*

%files -n libNX_X11-devel
%{_libdir}/libNX_X11.so
%{_libdir}/pkgconfig/nx-x11.pc
%dir %{_includedir}/nx-X11
%{_includedir}/nx-X11/ImUtil.h
%{_includedir}/nx-X11/Xauth.h
%{_includedir}/nx-X11/XKBlib.h
%{_includedir}/nx-X11/Xcms.h
%{_includedir}/nx-X11/Xlib.h
%{_includedir}/nx-X11/XlibConf.h
%{_includedir}/nx-X11/Xlibint.h
%{_includedir}/nx-X11/Xlocale.h
%{_includedir}/nx-X11/Xregion.h
%{_includedir}/nx-X11/Xresource.h
%{_includedir}/nx-X11/Xutil.h
%{_includedir}/nx-X11/cursorfont.h

%files -n libXcomp-devel
%{_libdir}/libXcomp.so
%{_libdir}/pkgconfig/nxcomp.pc
%dir %{_includedir}/nx
%{_includedir}/nx/MD5.h
%{_includedir}/nx/NX.h
%{_includedir}/nx/NXalert.h
%{_includedir}/nx/NXpack.h
%{_includedir}/nx/NXproto.h
%{_includedir}/nx/NXvars.h

%files -n libXcomp
%license COPYING LICENSE LICENSE.nxcomp
%doc ChangeLog
%_libdir/libXcomp.so.3*

%files -n libXcompshad-devel
%{_libdir}/libXcompshad.so
%{_libdir}/pkgconfig/nxcompshad.pc
%dir %{_includedir}/nx
%{_includedir}/nx/Shadow.h

%files -n libXcompshad
%license COPYING LICENSE LICENSE.nxcomp
%doc ChangeLog
%_libdir/libXcompshad.so.3*

%files devel
%dir %{_includedir}/nx-X11/extensions
%{_includedir}/nx-X11/extensions/panoramiXext.h
%{_includedir}/nx-X11/misc.h
%{_includedir}/nx-X11/os.h

%files -n nx-proto-devel
%dir %{_includedir}/nx-X11
%{_includedir}/nx-X11/DECkeysym.h
%{_includedir}/nx-X11/HPkeysym.h
%{_includedir}/nx-X11/Sunkeysym.h
%{_includedir}/nx-X11/X.h
%{_includedir}/nx-X11/XF86keysym.h
%{_includedir}/nx-X11/Xarch.h
%{_includedir}/nx-X11/Xatom.h
%{_includedir}/nx-X11/Xdefs.h
%{_includedir}/nx-X11/Xfuncproto.h
%{_includedir}/nx-X11/Xfuncs.h
%{_includedir}/nx-X11/Xmd.h
%{_includedir}/nx-X11/Xos.h
%{_includedir}/nx-X11/Xos_r.h
%{_includedir}/nx-X11/Xosdefs.h
%{_includedir}/nx-X11/Xpoll.h
%{_includedir}/nx-X11/Xproto.h
%{_includedir}/nx-X11/Xprotostr.h
%{_includedir}/nx-X11/Xthreads.h
%{_includedir}/nx-X11/keysym.h
%{_includedir}/nx-X11/keysymdef.h
%{_includedir}/nx-X11/extensions/Xdbeproto.h
%{_includedir}/nx-X11/extensions/XI.h
%{_includedir}/nx-X11/extensions/XIproto.h
%{_includedir}/nx-X11/extensions/XResproto.h
%{_includedir}/nx-X11/extensions/bigreqstr.h
%{_includedir}/nx-X11/extensions/composite.h
%{_includedir}/nx-X11/extensions/compositeproto.h
%{_includedir}/nx-X11/extensions/damagewire.h
%{_includedir}/nx-X11/extensions/damageproto.h
%{_includedir}/nx-X11/extensions/dpms.h
%{_includedir}/nx-X11/extensions/dpmsstr.h
%{_includedir}/nx-X11/extensions/panoramiXproto.h
%{_includedir}/nx-X11/extensions/randr.h
%{_includedir}/nx-X11/extensions/randrproto.h
%{_includedir}/nx-X11/extensions/record*.h
%{_includedir}/nx-X11/extensions/render.h
%{_includedir}/nx-X11/extensions/renderproto.h
%{_includedir}/nx-X11/extensions/saver.h
%{_includedir}/nx-X11/extensions/saverproto.h
%{_includedir}/nx-X11/extensions/security.h
%{_includedir}/nx-X11/extensions/securstr.h
%{_includedir}/nx-X11/extensions/shapeconst.h
%{_includedir}/nx-X11/extensions/sync.h
%{_includedir}/nx-X11/extensions/syncstr.h
%{_includedir}/nx-X11/extensions/xcmiscstr.h
%{_includedir}/nx-X11/extensions/xf86bigfont.h
%{_includedir}/nx-X11/extensions/xf86bigfproto.h
%{_includedir}/nx-X11/extensions/xfixesproto.h
%{_includedir}/nx-X11/extensions/xfixeswire.h
%{_includedir}/nx-X11/extensions/xtestconst.h
%{_includedir}/nx-X11/extensions/xteststr.h

%files -n nxagent
%doc doc/nxagent/README.keystrokes
%dir %{_sysconfdir}/nxagent
%config(noreplace) %{_sysconfdir}/nxagent/keystrokes.cfg
%{_bindir}/nxagent
%dir %{_libdir}/nx
%dir %{_libdir}/nx/bin
%{_libdir}/nx/bin/nxagent
%dir %{_libdir}/nx/X11
%{_libdir}/nx/X11/libX11.so.6*
%dir %{_datadir}/nx
%{_datadir}/nx/fonts
%{_datadir}/nx/VERSION.nxagent
%{_mandir}/man1/nxagent.1*

%files -n nxproxy
%{_bindir}/nxproxy
%dir %{_libdir}/nx
%dir %{_libdir}/nx/bin
%dir %{_datadir}/nx
%{_datadir}/nx/VERSION.nxproxy
%{_mandir}/man1/nxproxy.1*

%files -n nxdialog
%doc nxdialog/README.md
%{_bindir}/nxdialog
%{_mandir}/man1/nxdialog.1*

%changelog
%autochangelog
