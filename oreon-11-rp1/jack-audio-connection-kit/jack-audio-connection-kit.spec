%global source0_hash none

# set bootstrap to 1 in order to break the initial libffado loop
#
# libffado -> PyQt4 -> phonon -> phonon-backend-gstreamer ->
# -> gstreamer-plugins-good -> jack-audio-connection-kit -> libffado
#
%global bootstrap 0

%global groupname jackuser
%global pagroup   pulse-rt

# Disable lto (#1872065, #1869059)
%define _lto_cflags %{nil}

Summary:       The Jack Audio Connection Kit
Name:          jack-audio-connection-kit
Version:       1.9.22
Release:       11%{?dist}
# The entire source (~500 files) is a mixture of these three licenses
# Automatically converted from old format: GPLv2 and GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           https://www.jackaudio.org
Source0:       https://github.com/jackaudio/jack2/archive/v%{version}/v%{version}.tar.gz#/jack2-%{version}.tar.gz
Source1:       %{name}-README.Fedora
Source2:       %{name}-script.pa
Source3:       %{name}-limits.conf
# Build with Python >= 3.12
Patch0:        jack2-py312.patch
# Adjust default priority. RHBZ#795094
Patch1:        jack-realtime-compat.patch

BuildRequires: alsa-lib-devel
BuildRequires: dbus-devel
# Berkeley DB v6 new licence (AGPLv3) is incompatible with GPLv2. https://en.wikipedia.org/wiki/Berkeley_DB#Licensing
BuildRequires: libdb-devel < 6.0.20
BuildRequires: doxygen
BuildRequires: expat-devel
BuildRequires: gcc-c++
%ifnarch s390 s390x
%if !0%{?bootstrap} && !0%{?flatpak} && 0%{?rhel} < 9
BuildRequires: libffado-devel
%endif
%endif
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: ncurses-devel
BuildRequires: opus-devel
BuildRequires: pkgconfig
BuildRequires: python3

Requires:      pam

Obsoletes:     %{name}-example-clients < 1.9.22

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
%if !0%{?bootstrap} && !0%{?flatpak} && 0%{?rhel} < 9
   --firewire \
%endif
%endif
   --alsa \
   --clients 256 \
   --ports-per-application=2048

python3 ./waf build %{?_smp_mflags} -v

%install
python3 ./waf --destdir=%{buildroot} install

# move doxygen documentation to the right place
mv %{buildroot}%{_datadir}/jack-audio-connection-kit/reference .
rm -rf %{buildroot}%{_datadir}/jack-audio-connection-kit

# install our limits to the /etc/security/limits.d
mkdir -p %{buildroot}%{_sysconfdir}/security/limits.d
sed -e 's,@groupname@,%groupname,g; s,@pagroup@,%pagroup,g;' \
    %{SOURCE3} > %{buildroot}%{_sysconfdir}/security/limits.d/95-jack.conf

# prepare README.Fedora for documentation including
install -p -m644 %{SOURCE1} README.Fedora

# install pulseaudio script for jack (as documentation part)
install -p -m644 %{SOURCE2} jack.pa

# Fix permissions of the modules
chmod 755 %{buildroot}%{_libdir}/jack/*.so %{buildroot}%{_libdir}/libjack*.so.*.*.*

install -m0644 -D jack-audio-connection-kit.sysusers.conf %{buildroot}%{_sysusersdir}/jack-audio-connection-kit.conf


%files
%doc ChangeLog.rst README.rst README_NETJACK2
%doc README.Fedora
%doc jack.pa
%license COPYING
%{_bindir}/jackd
%{_libdir}/jack/
%{_libdir}/libjack.so.0*
%{_libdir}/libjacknet.so.0*
%{_libdir}/libjackserver.so.0*
%config(noreplace) %{_sysconfdir}/security/limits.d/*.conf

%{_mandir}/man1/jackd*.1*
%{_sysusersdir}/jack-audio-connection-kit.conf

%files dbus
%{_bindir}/jackdbus
%{_datadir}/dbus-1/services/org.jackaudio.service
%{_bindir}/jack_control

%files devel
%doc reference/html/
%{_includedir}/jack/
%{_libdir}/libjack.so
%{_libdir}/libjacknet.so
%{_libdir}/libjackserver.so
%{_libdir}/pkgconfig/jack.pc

%changelog
%autochangelog

