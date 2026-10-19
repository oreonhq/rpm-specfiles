%global source0_hash 913b05d19beabed4a3066e6e2be3078783048f55c7a9d2e3a012897a8766c245
%global username guacd
Name:           guacamole-server
Version:        1.6.0
Release:        1%{?dist}
Summary:        Server-side native components that form the Guacamole proxy
License:        Apache-2.0
URL:            https://guacamole.apache.org/
Source0:        https://github.com/apache/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysusersd
Patch0:         https://github.com/apache/guacamole-server/pull/591.patch#/guacamole-server-1.6.0-correct-struct-sockaddr_in.patch
%{?_with_ffmpeg:
}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libwebsockets-devel
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freerdp-client2)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtelnet)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(winpr2)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Guacamole is an HTML5 remote desktop gateway.

Guacamole provides access to desktop environments using remote desktop protocols
like VNC and RDP. A centralized server acts as a tunnel and proxy, allowing
access to multiple desktops through a web browser.

No browser plugins are needed, and no client software needs to be installed. The
client requires nothing more than a web browser supporting HTML5 and AJAX.

The main web application is provided by the "guacamole-client" package.

%package -n libguac
Summary:        The common library used by all C components of Guacamole
%description -n libguac
libguac is the core library for guacd (the Guacamole proxy) and any protocol
support plugins for guacd. libguac provides efficient buffered I/O of text and
base64 data, as well as somewhat abstracted functions for sending Guacamole
instructions.

%package -n libguac-devel
Summary:        Development files for %{name}
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n libguac-devel
The libguac-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n libguac-client-kubernetes
Summary:        Kubernetes pods terminal support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n libguac-client-kubernetes
libguac-client-kubernetes is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for attaching to terminals of containers running
in Kubernetes pods.

%package -n libguac-client-rdp
Summary:        RDP support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n libguac-client-rdp
libguac-client-rdp is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for RDP, the proprietary remote desktop protocol used by
Windows Remote Deskop / Terminal Services, via the libfreerdp library.

%package -n libguac-client-ssh
Summary:        SSH support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n libguac-client-ssh
libguac-client-ssh is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for SSH, the secure shell.

%package -n libguac-client-vnc
Summary:        VNC support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n libguac-client-vnc
libguac-client-vnc is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for VNC via the libvncclient library (part of
libvncserver).

%package -n libguac-client-telnet
Summary:        Telnet support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n libguac-client-telnet
libguac-client-telnet is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for Telnet via the libtelnet library.

%package -n guacd
Summary:        Proxy daemon for Guacamole
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%{?systemd_requires}
%{?sysusers_requires_compat}
%description -n guacd
guacd is the Guacamole proxy daemon used by the Guacamole web application and
framework to translate between arbitrary protocols and the Guacamole protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="%{optflags} -Wno-error"
autoreconf -vif
%configure \
  --disable-silent-rules \
  --disable-static
%make_build
pushd doc/libguac/
  doxygen Doxyfile
popd
pushd doc/libguac-terminal/
  doxygen Doxyfile
popd
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
mkdir html
cp -a doc/libguac/doxygen-output/html/ html/libguac/
cp -a doc/libguac-terminal/doxygen-output/html/ html/libguac-terminal/
mkdir -p %{buildroot}%{_sharedstatedir}/guacd
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/guacd.service
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_sysusersdir}/guacd.conf
%oreon_autofiles libguac usr/*/lib*.so.*
%oreon_autofiles libguac-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libguac-client-kubernetes usr/*/lib*.so.*
%oreon_autofiles libguac-client-rdp usr/*/lib*.so.*
%oreon_autofiles libguac-client-ssh usr/*/lib*.so.*
%oreon_autofiles libguac-client-vnc usr/*/lib*.so.*
%oreon_autofiles libguac-client-telnet usr/*/lib*.so.*
%oreon_autofiles guacd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre -n guacd

%sysusers_create_compat %{SOURCE2}
%post -n guacd

%systemd_post guacd.service
%preun -n guacd

%systemd_preun guacd.service
%postun -n guacd

%systemd_postun_with_restart guacd.service
%ldconfig_scriptlets -n libguac
%ldconfig_scriptlets -n libguac-client-kubernetes
%ldconfig_scriptlets -n libguac-client-rdp
%ldconfig_scriptlets -n libguac-client-ssh
%ldconfig_scriptlets -n libguac-client-vnc
%ldconfig_scriptlets -n libguac-client-telnet
%files -f %{oreon_filedir}/main.list
%files -n libguac -f %{oreon_filedir}/libguac.list
%files -n libguac-devel -f %{oreon_filedir}/libguac-devel.list
%files -n libguac-client-kubernetes -f %{oreon_filedir}/libguac-client-kubernetes.list
%files -n libguac-client-rdp -f %{oreon_filedir}/libguac-client-rdp.list
%files -n libguac-client-ssh -f %{oreon_filedir}/libguac-client-ssh.list
%files -n libguac-client-vnc -f %{oreon_filedir}/libguac-client-vnc.list
%files -n libguac-client-telnet -f %{oreon_filedir}/libguac-client-telnet.list
%files -n guacd -f %{oreon_filedir}/guacd.list

%changelog

%autochangelog
