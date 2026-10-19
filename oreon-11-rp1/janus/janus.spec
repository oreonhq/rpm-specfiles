%global source0_hash cba1e7aac44f4458701c5e14698e791a0eee13ecacbdacc71b4245716c442c08
%global __provides_exclude_from %{_includedir}/%{name}/events/.*\\.so$
%global __provides_exclude_from %{_includedir}/%{name}/loggers/.*\\.so$
%global __provides_exclude_from %{_includedir}/%{name}/plugins/.*\\.so$
%global __provides_exclude_from %{_includedir}/%{name}/transports/.*\\.so$
%global __requires_exclude_from %{_includedir}/%{name}/events/.*\\.so$
%global __requires_exclude_from %{_includedir}/%{name}/loggers/.*\\.so$
%global __requires_exclude_from %{_includedir}/%{name}/plugins/.*\\.so$
%global __requires_exclude_from %{_includedir}/%{name}/transports/.*\\.so$
%global api_version_major 2
%global api_version_minor 0
%global api_version_patch 8
%global api_version %{api_version_major}.%{api_version_minor}.%{api_version_patch}
Name: janus
Version: 1.4.1
Release:        1%{?dist}
Summary:        An open source WebRTC server designed and developed by Meetecho
License: GPL-3.0-only AND MIT AND BSD-3-Clause
URL: https://janus.conf.meetecho.com/
Source0:        https://github.com/meetecho/%{name}-gateway/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.service
Source2: %{name}.sysusers
patch0: janus-dtls.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  duktape-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  jansson-devel
BuildRequires:  libconfig-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libnice-devel
BuildRequires:  libpcap-devel
BuildRequires:  librabbitmq-devel
BuildRequires:  libsrtp-devel
BuildRequires:  libtool
BuildRequires:  libwebsockets-devel
BuildRequires:  lua-devel
BuildRequires:  nanomsg-devel
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  paho-c-devel
BuildRequires:  sofia-sip-devel
BuildRequires:  speexdsp-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  usrsctp-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Janus is an open source WebRTC server designed and developed by Meetecho.

%package devel
Summary: The %{name} header files and test scripts
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development package containing header files and what is required for %{name}
plugin development, as well as some test scripts.

%package eventhandlers-gelf
Summary: GELF event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description eventhandlers-gelf
GELF event handler for %{name}.

%package eventhandlers-mqtt
Summary: MQTT event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description eventhandlers-mqtt
MQTT event handler for %{name}.

%package eventhandlers-nanomsg
Summary: Nanomsg event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description eventhandlers-nanomsg
Nanomsg event handler for %{name}.

%package eventhandlers-rabbitmq
Summary: RabbitMQ event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description eventhandlers-rabbitmq
RabbitMQ event handler for %{name}.

%package eventhandlers-sample
Summary: Sample event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description eventhandlers-sample
Sample event handler for %{name}.

%package eventhandlers-ws
Summary: WebSocket event handler for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description eventhandlers-ws
WebSocket event handler for %{name}.

%package loggers-json
Summary: A logger plugin for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description loggers-json
This is a trivial logger plugin for %{name}.

%package plugins-audiobridge
Summary: An audio conference bridge plugin for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-audiobridge
This is a plugin implementing an audio conference bridge for %{name}, specifically mixing Opus streams.

%package plugins-duktape
Summary: A simple bridge to JavaScript via Duktape for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-duktape
This is a plugin that implements a simple bridge to JavaScript via Duktape for
%{name}.

%package plugins-echotest
Summary: EchoTest plugin for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-echotest
This is a trivial EchoTest plugin for %{name}, just used to showcase the plugin
interface.

%package plugins-lua
Summary: Simple bridge to Lua scripts for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lua-json
Requires: lua-term
%description plugins-lua
This is a plugin that implements a simple bridge to Lua scripts for %{name}.

%package plugins-nosip
Summary: Acts as an RTP bridge for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-nosip
This is quite a basic plugin, as it only takes care of acting as an RTP bridge
for %{name}.

%package plugins-recordplay
Summary: Record and playback of WebRTC messages for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-recordplay
This is a simple application that implements two different features for
%{name}: it allows you to record a message you send with WebRTC and
subsequently replay this recording (or other previously recorded) through
WebRTC as well.

%package plugins-sip
Summary: Allows WebRTC peers to register at a SIP server
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-sip
This is a simple SIP plugin for Janus, allowing WebRTC peers to register at a
SIP server (e.g., Asterisk) and call SIP user agents through %{name}.

%package plugins-streaming
Summary: Streaming plugin for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-streaming
This is a streaming plugin for %{name}, allowing WebRTC peers to watch/listen
to pre-recorded files or media generated by another tool.

%package plugins-textroom
Summary: A DataChannel only text room for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-textroom
This is a plugin implementing a DataChannel only text room for %{name}.

%package plugins-videocall
Summary: Allows two WebRTC peers to call each other through %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-videocall
This is a simple video call plugin for Janus, allowing two WebRTC peers to call
each other through %{name}.

%package plugins-videoroom
Summary: Videoconferencing SFU for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-videoroom
This is a plugin implementing a videoconferencing SFU (Selective Forwarding
Unit) for %{name}, that is an audio/video router.

%package tools
Summary: Janus' helper tools
Requires:%{name}%{?_isa} = %{version}-%{release}
Requires: gstreamer1-plugins-good%{?_isa}
%description tools
Janus' helper tools.

%package transports-http
Summary: RESTs transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}
%description transports-http
This is an implementation of a RESTs transport for the %{name} API, using the
libmicrohttpd library.

%package transports-mqtt
Summary: MQTT transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}
%description transports-mqtt
This is an implementation of a MQTT transport for the %{name} API, using the
Eclipse Paho C Client library.

%package transports-nanomsg
Summary: Nanomsg transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}
%description transports-nanomsg
This is an implementation of a Nanomsg transport for the %{name} API.

%package transports-pfunix
Summary: Unix Sockets transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}
%description transports-pfunix
This is an implementation of a Unix Sockets transport for the %{name} API.

%package transports-rabbitmq
Summary: RabbitMQ transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}
%description transports-rabbitmq
This is an implementation of a RabbitMQ transport for the %{name} API.

%package transports-websockets
Summary: WebSockets transport for the %{name} API
Requires: %{name}%{?_isa} = %{version}-%{release}
%description transports-websockets
This is an implementation of a WebSockets transport for the %{name} API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-gateway-%{version}
%oreon_prep
%build

sh autogen.sh
%configure \
    --enable-docs \
    --enable-json-logger \
    --enable-plugin-audiobridge \
    --enable-plugin-duktape \
    --enable-plugin-lua \
    --enable-post-processing \
    --enable-systemd-sockets
%make_build
%check

make check
%install
%make_install
make DESTDIR=%{buildroot} configs
chmod 755 %{buildroot}%{_datadir}/%{name}/streams/*.sh
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf
rm -fr %{buildroot}%{_docdir}/%{name}-gateway
rm -fr %{buildroot}%{_datadir}/%{name}/html
rm -fr %{buildroot}%{_datadir}/%{name}/javascript
find %{buildroot} -type f -iname '*.la' -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

%sysusers_create_compat %{SOURCE2}
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n janus-devel -f %{oreon_filedir}/janus-devel.list
%files -n janus-eventhandlers-gelf -f %{oreon_filedir}/janus-eventhandlers-gelf.list
%files -n janus-eventhandlers-mqtt -f %{oreon_filedir}/janus-eventhandlers-mqtt.list
%files -n janus-eventhandlers-nanomsg -f %{oreon_filedir}/janus-eventhandlers-nanomsg.list
%files -n janus-eventhandlers-rabbitmq -f %{oreon_filedir}/janus-eventhandlers-rabbitmq.list
%files -n janus-eventhandlers-sample -f %{oreon_filedir}/janus-eventhandlers-sample.list
%files -n janus-eventhandlers-ws -f %{oreon_filedir}/janus-eventhandlers-ws.list
%files -n janus-loggers-json -f %{oreon_filedir}/janus-loggers-json.list
%files -n janus-plugins-audiobridge -f %{oreon_filedir}/janus-plugins-audiobridge.list
%files -n janus-plugins-duktape -f %{oreon_filedir}/janus-plugins-duktape.list
%files -n janus-plugins-echotest -f %{oreon_filedir}/janus-plugins-echotest.list
%files -n janus-plugins-lua -f %{oreon_filedir}/janus-plugins-lua.list
%files -n janus-plugins-nosip -f %{oreon_filedir}/janus-plugins-nosip.list
%files -n janus-plugins-recordplay -f %{oreon_filedir}/janus-plugins-recordplay.list
%files -n janus-plugins-sip -f %{oreon_filedir}/janus-plugins-sip.list
%files -n janus-plugins-streaming -f %{oreon_filedir}/janus-plugins-streaming.list
%files -n janus-plugins-textroom -f %{oreon_filedir}/janus-plugins-textroom.list
%files -n janus-plugins-videocall -f %{oreon_filedir}/janus-plugins-videocall.list
%files -n janus-plugins-videoroom -f %{oreon_filedir}/janus-plugins-videoroom.list
%files -n janus-tools -f %{oreon_filedir}/janus-tools.list
%files -n janus-transports-http -f %{oreon_filedir}/janus-transports-http.list
%files -n janus-transports-mqtt -f %{oreon_filedir}/janus-transports-mqtt.list
%files -n janus-transports-nanomsg -f %{oreon_filedir}/janus-transports-nanomsg.list
%files -n janus-transports-pfunix -f %{oreon_filedir}/janus-transports-pfunix.list
%files -n janus-transports-rabbitmq -f %{oreon_filedir}/janus-transports-rabbitmq.list
%files -n janus-transports-websockets -f %{oreon_filedir}/janus-transports-websockets.list

%changelog

%autochangelog
