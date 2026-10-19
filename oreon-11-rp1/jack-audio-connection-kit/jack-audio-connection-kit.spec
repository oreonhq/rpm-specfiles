%global source0_hash 1e42b9fc4ad7db7befd414d45ab2f8a159c0b30fcd6eee452be662298766a849
%global bootstrap 0
%global groupname jackuser
%global pagroup   pulse-rt
%define _lto_cflags %{nil}
Summary:        The Jack Audio Connection Kit
Name:          jack-audio-connection-kit
Version:       1.9.22
Release:        1%{?dist}
License:       GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           https://www.jackaudio.org
Source0:        https://github.com/jackaudio/jack2/archive/refs/tags/v%{version}.tar.gz#/jack2-%{version}.tar.gz
Source1:       %{name}-README.Fedora
Source2:       %{name}-script.pa
Source3:       %{name}-limits.conf
Patch0:        jack2-py312.patch
Patch1:        jack-realtime-compat.patch
%ifnarch s390 s390x
%endif
Requires:      pam
Obsoletes:     %{name}-example-clients < 1.9.22
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  dbus-devel
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  libdb-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  ncurses-devel
BuildRequires:  opus-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
# /oreon:deps
%description
JACK is a low-latency audio server, written primarily for the Linux operating
system. It can connect a number of different applications to an audio device, as
well as allowing them to share audio between themselves. Its clients can run in
their own processes (i.e. as a normal application), or can they can run within a
JACK server (i.e. a "plugin").

JACK is different from other audio server efforts in that it has been designed
from the ground up to be suitable for professional audio work. This means that
it focuses on two key areas: synchronous execution of all clients, and low
latency operation.

%package dbus
Summary:       Jack D-Bus launcher
Requires:      %{name} = %{version}-%{release}
%description dbus
Launcher to start Jack through D-Bus.

%package devel
Summary:       Header files for Jack
Requires:      %{name} = %{version}-%{release}
%description devel
Header files for the Jack Audio Connection Kit.

%package example-clients
Summary:       Example clients that use Jack 
%description example-clients
Small example clients that use the Jack Audio Connection Kit.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jack2-%{version}

# Create a sysusers.d config file
cat >jack-audio-connection-kit.sysusers.conf <<EOF
g jackuser -
EOF

%build

%set_build_flags
export PREFIX=%{_prefix}
python3 ./waf configure \
   --mandir=%{_mandir}/man1 \
   --libdir=%{_libdir} \
   --doxygen \
   --dbus \
   --db \
   --classic \
%ifnarch s390 s390x
%endif
   --alsa \
   --clients 256 \
   --ports-per-application=2048
python3 ./waf build %{?_smp_mflags} -v
%install
python3 ./waf --destdir=%{buildroot} install
mv %{buildroot}%{_datadir}/jack-audio-connection-kit/reference .
rm -rf %{buildroot}%{_datadir}/jack-audio-connection-kit
mkdir -p %{buildroot}%{_sysconfdir}/security/limits.d
sed -e 's,@groupname@,%groupname,g; s,@pagroup@,%pagroup,g;' \
    %{SOURCE3} > %{buildroot}%{_sysconfdir}/security/limits.d/95-jack.conf
install -p -m644 %{SOURCE1} README.Fedora
install -p -m644 %{SOURCE2} jack.pa
chmod 755 %{buildroot}%{_libdir}/jack/*.so %{buildroot}%{_libdir}/libjack*.so.*.*.*
install -m0644 -D jack-audio-connection-kit.sysusers.conf %{buildroot}%{_sysusersdir}/jack-audio-connection-kit.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jack-audio-connection-kit-dbus -f %{oreon_filedir}/jack-audio-connection-kit-dbus.list
%files -n jack-audio-connection-kit-devel -f %{oreon_filedir}/jack-audio-connection-kit-devel.list
%files -n jack-audio-connection-kit-example-clients -f %{oreon_filedir}/jack-audio-connection-kit-example-clients.list

%changelog

%autochangelog

