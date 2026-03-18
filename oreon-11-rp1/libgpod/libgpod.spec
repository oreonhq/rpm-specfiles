# If banshee ever stablizes around gtk3, we need to flip this on.
%global with_gtk3 0

%ifarch %{mono_arches}
%global with_mono 1
%else
%global with_mono 0
%endif
%if 0%{?rhel}
%global with_mono 0
%endif

Summary: Library to access the contents of an iPod
Name: libgpod
Version: 0.8.3
Release: 56%{?dist}
License: LGPL-2.1-or-later
URL: http://www.gtkpod.org/libgpod.html
Source0: http://downloads.sourceforge.net/gtkpod/%{name}-%{version}.tar.bz2

# upstreamable patch: reduce pkgconfig-related overlinking
Patch0:  libgpod-0.8.2-pkgconfig_overlinking.patch
Patch1:  libgpod-fixswig.patch
Patch2:  libgpod-0.8.3-mono4.patch
Patch3:  libgpod-playcounts.patch
Patch4:  libgpod-udev.patch
Patch5:  0001-configure.ac-Add-support-for-libplist-2.2.patch
Patch6:  libgpod-0.8.3-no-plist_dict_insert_item.patch
Patch99: libgpod-0.8.3-implicit-int.patch
Patch100: pointer-types.patch

BuildRequires: automake libtool
BuildRequires: docbook-style-xsl
BuildRequires: glib2-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: libimobiledevice-devel
BuildRequires: libplist-devel
BuildRequires: libusbx-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt
%if %{with_mono}
BuildRequires: mono-devel
%if %{with_gtk3}
BuildRequires: gtk-sharp3-devel
%else
BuildRequires: gtk-sharp2-devel
%endif
%endif
BuildRequires: gtk-doc
BuildRequires: sg3_utils-devel
BuildRequires: sqlite-devel
BuildRequires: swig
BuildRequires: systemd-rpm-macros
BuildRequires: make

%description
Libgpod is a library to access the contents of an iPod. It supports playlists,
smart playlists, playcounts, ratings, podcasts, album artwork, photos, etc.


%package devel
Summary: Development files for the libgpod library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Libgpod is a library to access the contents of an iPod. It supports playlists,
smart playlists, playcounts, ratings, podcasts, album artwork, photos, etc.

This package contains the files required to develop programs that will use
libgpod.


%package doc
Summary: API documentation for the libgpod library
License: GFDL-1.1-or-later
%if 0%{?fedora}
BuildArch: noarch
%endif
Requires: %{name} = %{version}-%{release}

%description doc
Libgpod is a library to access the contents of an iPod. It supports playlists,
smart playlists, playcounts, ratings, podcasts, album artwork, photos, etc.

This package contains the API documentation.


%if %{with_mono}
%package sharp
Summary: C#/.NET library to access iPod content
Requires: %{name}%{?_isa} = %{version}-%{release}

%description sharp
C#/.NET library to access iPod content.  Provides bindings to the libgpod
library.


%package sharp-devel
Summary: Development files for libgpod-sharp
Requires: %{name}-sharp%{?_isa} = %{version}-%{release}

%description sharp-devel
C#/.NET library to access iPod content.  Provides bindings to the libgpod
library.

This package contains the files required to develop programs that will use
libgpod-sharp.
%endif


%prep
%autosetup -p1

%if %{with_gtk3}
sed -i "s#sharp-2.0#sharp-3.0#g" bindings/mono/libgpod-sharp/libgpod-sharp.pc.in
sed -i "s#public DateTime#public System.DateTime#g" bindings/mono/libgpod-sharp/Artwork.cs
%endif

%build
autoreconf -vif
%if %{with_gtk3}
sed -i "s#sharp-2.0#sharp-3.0#g" configure
%endif

%configure --without-hal --enable-udev --with-temp-mount-dir=/run/%{name} --with-python=no
make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install
%find_lang %{name}

mkdir -p %{buildroot}/%{_libdir}/libgpod

%if %{with_mono}
# remove execute perms from some libgpod-sharp files
chmod -x %{buildroot}/%{_libdir}/%{name}/*.dll.config
%else
# remove unwanted file
rm -f %{buildroot}/%{_libdir}/pkgconfig/%{name}-sharp.pc
%endif

# Setup tmpfiles.d config
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "D /run/%{name} - - - -" > %{buildroot}%{_tmpfilesdir}/%{name}.conf

install -d -m 0755 %{buildroot}/run/%{name}/

# remove static libs and libtool archives
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete

%ldconfig_scriptlets


%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog NEWS README*
%{_bindir}/*
%{_libdir}/*.so.*
%dir /run/%{name}/
%{_tmpfilesdir}/%{name}.conf
/lib/udev/iphone-set-info
/lib/udev/ipod-set-info
/lib/udev/rules.d/*.rules
%dir %{_libdir}/libgpod/

%files devel
%{_includedir}/gpod-1.0/
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_libdir}/*.so


%files doc
%{_datadir}/gtk-doc

%if %{with_mono}
%files sharp
%{_libdir}/%{name}/%{name}-sharp*


%files sharp-devel
%{_libdir}/pkgconfig/%{name}-sharp.pc
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.3-56
- Prepare for Oreon 11 (RP1)
