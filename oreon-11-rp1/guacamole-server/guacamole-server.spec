%global source0_hash 913b05d19beabed4a3066e6e2be3078783048f55c7a9d2e3a012897a8766c245

%global username guacd

# Manual FFmpeg support override by passing "--with(out)=ffmpeg" to mock/rpmbuild
%if 0%{?fedora} || 0%{?rhel} >= 9
%global _with_ffmpeg 1
%endif

Name:           guacamole-server
Version:        1.6.0
Release:        6%{?dist}
Summary:        Server-side native components that form the Guacamole proxy
License:        Apache-2.0
URL:            https://guacamole.apache.org/

Source0:        https://github.com/apache/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysusersd
# src/libguac/wol.c: inet_pton called with a destination buffer size too small
# https://issues.apache.org/jira/browse/GUACAMOLE-2087
Patch0:         https://github.com/apache/guacamole-server/pull/591.patch#/guacamole-server-1.6.0-correct-struct-sockaddr_in.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libwebsockets-devel
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(freerdp-client2)
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

%{?_with_ffmpeg:
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
}

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

%autosetup -p1

%build
# https://issues.apache.org/jira/browse/GUACAMOLE-2182
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

# Systemd unit files
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/guacd.service
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_sysusersdir}/guacd.conf

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

%files -n libguac
%license LICENSE
%doc README CONTRIBUTING
%{_libdir}/libguac.so.25*
%{_libdir}/libguac-terminal.so.2*

%files -n libguac-devel
%doc html
%{_includedir}/guacamole/
%{_libdir}/libguac.so
%{_libdir}/libguac-terminal.so

# The libguac source code dlopen's these plugins, and they are named without
# the version in the shared object; i.e. "libguac-client-$(PROTOCOL).so".

%files -n libguac-client-kubernetes
%{_libdir}/libguac-client-kubernetes.so
%{_libdir}/libguac-client-kubernetes.so.0*

%files -n libguac-client-rdp
%{_libdir}/libguac-client-rdp.so
%{_libdir}/libguac-client-rdp.so.0*
%{_libdir}/freerdp2/libguac-common-svc-client.so
%{_libdir}/freerdp2/libguacai-client.so

%files -n libguac-client-ssh
%{_libdir}/libguac-client-ssh.so
%{_libdir}/libguac-client-ssh.so.0*

%files -n libguac-client-vnc
%{_libdir}/libguac-client-vnc.so
%{_libdir}/libguac-client-vnc.so.0*

%files -n libguac-client-telnet
%{_libdir}/libguac-client-telnet.so
%{_libdir}/libguac-client-telnet.so.0*

%files -n guacd
%{_bindir}/guaclog
%{?_with_ffmpeg:
%{_bindir}/guacenc
%{_mandir}/man1/guacenc.1*
}
%{_mandir}/man1/guaclog.1*
%{_mandir}/man5/guacd.conf.5*
%{_mandir}/man8/guacd.8*
%{_sbindir}/guacd
%{_unitdir}/guacd.service
%{_sysusersdir}/guacd.conf
%attr(750,%{username},%{username}) %{_sharedstatedir}/guacd/

%changelog
%autochangelog
