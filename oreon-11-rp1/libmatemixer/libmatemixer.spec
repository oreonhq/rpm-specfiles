%global source0_hash 5d73b922397f60688e3c9530eb532bce46c30e262db1b5352fa32c40d870a0c7
%global branch 1.28
Name:        libmatemixer
Summary:        Mixer library for MATE desktop
Version:     %{branch}.0
Release:        1%{?dist}
License:     GPL-2.0-or-later
URL:         http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Patch1: libmatemixer_0001-pulse-Don-t-crash-on-failure-to-retrieve-server-info.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
libmatemixer is a mixer library for MATE desktop.
It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

%package devel
Summary:  Development libraries for libmatemixer
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development libraries for libmatemixer

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
        --disable-static \
        --enable-pulseaudio \
        --enable-alsa \
        --enable-udev \
        --enable-gtk-doc
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool
make %{?_smp_mflags} V=1
%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmatemixer-devel -f %{oreon_filedir}/libmatemixer-devel.list

%changelog

%autochangelog
