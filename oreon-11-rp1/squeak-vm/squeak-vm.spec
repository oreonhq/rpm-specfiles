%global source0_hash 3f9b60be9d63a12e002da836901ca410ef46cb8f46c070081225f48acb27534e

%global major   4
%global minor   10
%global patch   2
%global rev     2614
%global vmver   %{major}.%{minor}.%{patch}.%{rev}
%global vmver2   %{major}.%{minor}.%{patch}-%{rev}
%global source  Squeak-%{vmver}-src-no-mp3

Name:           squeak-vm
Version:        %{vmver}
Release:        39%{?dist}
Summary:        The Squeak virtual machine

License:        MIT
URL:            http://squeakvm.org/unix
Source0:        http://squeakvm.org/unix/release/%{source}.tar.gz
Source1:        inisqueak
Source2:        squeak-desktop-files.tar.gz
Patch:          squeak-vm-dprintf.patch
Patch:          alsa-fixes.patch
Patch:          squeak-vm-4.10.2-fix-cmake.patch
Patch:          squeak-vm-4.10.2-squeak-init-fix.patch
Patch:          squeak-vm-4.10.2-format-security.patch
Patch:          squeak-vm-4.10.2-gcc-14-fix.patch
Patch:          squeak-vm-4.10.2-cmake-4-fix.patch

# For clean upgrade path, could be probably dropped in F20 or later
Provides:       %{name}-nonXOplugins = %{version}-%{release}
Obsoletes:      %{name}-nonXOplugins < 4.10.2.2614-1

Requires:       xmessage

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libtheora-devel
BuildRequires:  speex-devel
BuildRequires:  dbus-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pango-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libXext-devel
BuildRequires:  libuuid-devel
BuildRequires:  libffi-devel
BuildRequires:  nas-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libxml2-devel
BuildRequires:  glib2-devel
BuildRequires:  cairo-devel
BuildRequires:  libv4l-devel
BuildRequires:  freetype-devel
ExcludeArch:    %{ix86}

%description
Squeak is a full-featured implementation of the Smalltalk programming
language and environment based on (and largely compatible with) the original
Smalltalk-80 system.

This package contains just the Squeak virtual machine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{source} -a 2

%autopatch -p1

# Fix libdir
sed -i 's|libdir="${prefix}/lib/squeak"|libdir="%{_libdir}/squeak"|' unix/cmake/squeak.in

%build
export CFLAGS="%{build_cflags} -std=gnu17"
%cmake ./unix -DCMAKE_VERBOSE_MAKEFILE=ON -DVM_HOST="%{_host}" -DVM_VERSION="%{vmver2}" -DPLATFORM_SOURCE_VERSION="%{rev}"
%cmake_build

%install
%cmake_install

# these files will be put in std RPM doc location
rm -rf %{buildroot}%{_prefix}/doc/squeak

# install the desktop stuff
install -D --mode=u=rw,go=r squeak.xml %{buildroot}%{_datadir}/mime/packages/squeak.xml
install -D --mode=u=rw,go=r squeak.png %{buildroot}%{_datadir}/pixmaps/squeak.png

%global icons_dir %{buildroot}%{_datadir}/icons/gnome
for size in 16 24 32 48 64 72 96
do
  mkdir -p %{icons_dir}/${size}x${size}/mimetypes
  install -m0644 squeak${size}.png %{icons_dir}/${size}x${size}/mimetypes/application-x-squeak-image.png
  install -m0644 squeaksource${size}.png %{icons_dir}/${size}x${size}/mimetypes/application-x-squeak-source.png
done

# Remove squeak.sh & mysqueak, obsoleted
rm -f %{buildroot}%{_bindir}/squeak.sh

# Install own version of inisqueak
install -m0755 %{SOURCE1} %{buildroot}%{_bindir}/inisqueak

%files
%doc unix/ChangeLog unix/doc/{README*,LICENSE,*RELEASE_NOTES}
%{_bindir}/*
%dir %{_libdir}/squeak
%dir %{_libdir}/squeak/%{vmver2}
%if 0 == 0%{?nonXOplugins}
%{_libdir}/squeak/%{vmver2}/so.FileCopyPlugin
%{_libdir}/squeak/%{vmver2}/so.B3DAcceleratorPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.PseudoTTYPlugin
%{_libdir}/squeak/%{vmver2}/so.UnixOSProcessPlugin
%{_libdir}/squeak/%{vmver2}/so.XDisplayControlPlugin

%{_libdir}/squeak/%{vmver2}/so.AioPlugin
%{_libdir}/squeak/%{vmver2}/so.ClipboardExtendedPlugin
%{_libdir}/squeak/%{vmver2}/so.DBusPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.GStreamerPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.ImmX11Plugin
#%%{_libdir}/squeak/%%{vmver2}/so.KedamaPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.KedamaPlugin2
%{_libdir}/squeak/%{vmver2}/so.MIDIPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.OggPlugin
%{_libdir}/squeak/%{vmver2}/so.RomePlugin
%{_libdir}/squeak/%{vmver2}/so.Squeak3D
%{_libdir}/squeak/%{vmver2}/so.UUIDPlugin
#%%{_libdir}/squeak/%%{vmver2}/so.VideoForLinuxPlugin
%{_libdir}/squeak/%{vmver2}/so.HostWindowPlugin

#%%{_libdir}/squeak/%%{vmver2}/npsqueak.so
#%%{_libdir}/squeak/%%{vmver2}/squeak
%{_libdir}/squeak/%{vmver2}/so.vm-display-X11
%{_libdir}/squeak/%{vmver2}/so.vm-display-fbdev
%{_libdir}/squeak/%{vmver2}/so.vm-display-null
%{_libdir}/squeak/%{vmver2}/so.vm-sound-ALSA
%{_libdir}/squeak/%{vmver2}/so.vm-sound-OSS
%{_libdir}/squeak/%{vmver2}/so.vm-sound-null

#%%{_libdir}/squeak/%%{vmver2}/so.Mpeg3Plugin
%{_libdir}/squeak/%{vmver2}/so.SqueakFFIPrims
%{_libdir}/squeak/%{vmver2}/so.vm-display-custom
%{_libdir}/squeak/%{vmver2}/so.vm-sound-NAS
%{_libdir}/squeak/%{vmver2}/so.vm-sound-custom
%{_libdir}/squeak/%{vmver2}/so.vm-sound-pulse
%{_libdir}/squeak/%{vmver2}/squeakvm

# 4.10 plugins
%{_libdir}/squeak/%{vmver2}/ckformat
%{_libdir}/squeak/%{vmver2}/so.CameraPlugin
%{_libdir}/squeak/%{vmver2}/so.ScratchPlugin
%{_libdir}/squeak/%{vmver2}/so.UnicodePlugin
%{_libdir}/squeak/%{vmver2}/so.WeDoPlugin

%endif
%{_mandir}/man*/*
#%%dir %%{_datadir}/squeak
#%%{_datadir}/squeak/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/gnome/*/mimetypes/*.png

%changelog
%autochangelog
