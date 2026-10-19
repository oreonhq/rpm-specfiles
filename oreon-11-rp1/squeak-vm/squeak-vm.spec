%global source0_hash a7b384a3c0c593d43606456b0d8e894c45f953ada448727527a22735aff4b106
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
Provides:       %{name}-nonXOplugins = %{version}-%{release}
Obsoletes:      %{name}-nonXOplugins < 4.10.2.2614-1
Requires:       xmessage
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libffi-devel
BuildRequires:  libtheora-devel
BuildRequires:  libuuid-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  nas-devel
BuildRequires:  pango-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  speex-devel
# /oreon:deps
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
rm -rf %{buildroot}%{_prefix}/doc/squeak
install -D --mode=u=rw,go=r squeak.xml %{buildroot}%{_datadir}/mime/packages/squeak.xml
install -D --mode=u=rw,go=r squeak.png %{buildroot}%{_datadir}/pixmaps/squeak.png
%global icons_dir %{buildroot}%{_datadir}/icons/gnome
for size in 16 24 32 48 64 72 96
do
  mkdir -p %{icons_dir}/${size}x${size}/mimetypes
  install -m0644 squeak${size}.png %{icons_dir}/${size}x${size}/mimetypes/application-x-squeak-image.png
  install -m0644 squeaksource${size}.png %{icons_dir}/${size}x${size}/mimetypes/application-x-squeak-source.png
done
rm -f %{buildroot}%{_bindir}/squeak.sh
install -m0755 %{SOURCE1} %{buildroot}%{_bindir}/inisqueak
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
