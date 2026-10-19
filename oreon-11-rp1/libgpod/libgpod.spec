%global source0_hash 638a7959d04e95f1e62abad02bd33702e4e8dfef98485ac7d9d50395c37e955d
%global with_gtk3 0
%ifarch %{mono_arches}
%global with_mono 1
%else
%global with_mono 0
%endif
Summary:        Library to access the contents of an iPod
Name: libgpod
Version: 0.8.3
Release:        1%{?dist}
License: LGPL-2.1-or-later
URL: http://www.gtkpod.org/libgpod.html
Source0:        https://downloads.sourceforge.net/gtkpod/%{name}-%{version}.tar.bz2
Patch0:  libgpod-0.8.2-pkgconfig_overlinking.patch
Patch1:  libgpod-fixswig.patch
Patch2:  libgpod-0.8.3-mono4.patch
Patch3:  libgpod-playcounts.patch
Patch4:  libgpod-udev.patch
Patch5:  0001-configure.ac-Add-support-for-libplist-2.2.patch
Patch6:  libgpod-0.8.3-no-plist_dict_insert_item.patch
Patch99: libgpod-0.8.3-implicit-int.patch
Patch100: pointer-types.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  docbook-style-xsl
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libimobiledevice-devel
BuildRequires:  libplist-devel
BuildRequires:  libtool
BuildRequires:  libusbx-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  sg3_utils-devel
BuildRequires:  sqlite-devel
BuildRequires:  swig
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
Requires: %{name} = %{version}-%{release}
%description doc
Libgpod is a library to access the contents of an iPod. It supports playlists,
smart playlists, playcounts, ratings, podcasts, album artwork, photos, etc.

This package contains the API documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure --without-hal --enable-udev --with-temp-mount-dir=/run/%{name} --with-python=no
make %{?_smp_mflags} V=1
%install
make DESTDIR=%{buildroot} install
%find_lang %{name}
mkdir -p %{buildroot}/%{_libdir}/libgpod
rm -f %{buildroot}/%{_libdir}/pkgconfig/%{name}-sharp.pc
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "D /run/%{name} - - - -" > %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m 0755 %{buildroot}/run/%{name}/
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libgpod-devel -f %{oreon_filedir}/libgpod-devel.list
%files -n libgpod-doc -f %{oreon_filedir}/libgpod-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.3-56
- Prepare for Oreon 11 (RP1)
