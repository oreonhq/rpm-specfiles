%global source0_hash c2b671e67e0c288a69fc33dc1b6f1b534d07882c2aceed37004bf48c601afa72
%bcond_without gtk2
Name: libcanberra
Version: 0.30
Release:        39%{?dist}
Summary:        Portable Sound Event Library
Source0:        http://0pointer.de/lennart/projects/libcanberra/libcanberra-%{version}.tar.xz
Patch0: 0001-gtk-Don-t-assume-all-GdkDisplays-are-GdkX11Displays-.patch
License: LGPL-2.1-or-later
Url: http://git.0pointer.de/?p=libcanberra.git;a=summary
%if %{with gtk2}
%endif
Requires: sound-theme-freedesktop
Requires: pulseaudio-libs >= 0.9.15
Requires: libtdb%{?_isa}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libtdb-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
A small and lightweight implementation of the XDG Sound Theme Specification
(http://0pointer.de/public/sound-theme-spec.html).

%if %{with gtk2}
%package gtk2
Summary: Gtk+ 2.x Bindings for libcanberra
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk3%{?_isa} = %{version}-%{release}
%description gtk2
Gtk+ 2.x bindings for libcanberra
%endif

%package gtk3
Summary: Gtk+ 3.x Bindings for libcanberra
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gtk3
Gtk+ 3.x bindings for libcanberra

%package devel
Summary: Development Files for libcanberra Client Development
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk3%{?_isa} = %{version}-%{release}
%if %{with gtk2}
Requires: %{name}-gtk2%{?_isa} = %{version}-%{release}
Requires: gtk2-devel
%endif
%description devel
Development Files for libcanberra Client Development

%post

%systemd_post canberra-system-bootup.service canberra-system-shutdown.service canberra-system-shutdown-reboot.service
%preun

%systemd_preun canberra-system-bootup.service canberra-system-shutdown.service canberra-system-shutdown-reboot.service
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 

%build

%configure \
    --disable-static \
    --enable-pulse \
    --enable-alsa \
%if %{without gtk2}
    --disable-gtk \
%endif
    --enable-null \
    --disable-oss \
    --with-builtin=dso \
    --with-systemdsystemunitdir=/usr/lib/systemd/system
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;
rm $RPM_BUILD_ROOT%{_docdir}/libcanberra/README
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcanberra-gtk2 -f %{oreon_filedir}/libcanberra-gtk2.list
%files -n libcanberra-gtk3 -f %{oreon_filedir}/libcanberra-gtk3.list
%files -n libcanberra-devel -f %{oreon_filedir}/libcanberra-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.30-39
- Prepare for Oreon 11 (RP1)
