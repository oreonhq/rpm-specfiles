%global source0_hash 429b4fe9c3511f461938413194605e6312464f9b2a44367c931308e16763d3d8

# Review at https://bugzilla.redhat.com/show_bug.cgi?id=540328
#

# F37 nautilus is based on GTK4, incompatible with GTK3 nautilus extensions
%bcond nautilus %[!(0%{?fedora} > 36 || 0%{?rhel} > 9 || 0%{?flatpak})]

%bcond nemo %{undefined flatpak}

%bcond thunar %{undefined flatpak}

%bcond caja %{undefined flatpak}

Name:           gtkhash
Version:        1.4
Release:        15%{?dist}
Summary:        GTK+ utility for computing message digests or checksums

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/tristanheaven/gtkhash
Source0:        https://github.com/tristanheaven/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  mhash-devel
BuildRequires:  libb2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  automake
BuildRequires:  libtool
%if %{with nautilus}
BuildRequires:  pkgconfig(libnautilus-extension)
%endif
%if %{with caja}
BuildRequires:  pkgconfig(libcaja-extension)
%endif
%if %{with nemo}
BuildRequires:  pkgconfig(libnemo-extension)
%endif
%if %{with thunar}
BuildRequires:  pkgconfig(thunarx-3)
%endif
BuildRequires:  libappstream-glib
BuildRequires: make

Provides:       gtkhash3 = %{version}-%{release}
Obsoletes:      gtkhash3 < 1.1.1
%if %{without nautilus}
Obsoletes:      %{name}-nautilus <= 1.4
%endif
%if %{without nemo}
Obsoletes:      %{name}-nemo <= 1.4
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
GtkHash is a GTK+ utility for computing message digests or checksums. Currently
supported hash functions include
* MD2, MD4 and MD5
* SHA1, SHA224, SHA256, SHA384 and SHA512,
* RIPEMD128, RIPEMD160, RIPEMD256 and RIPEMD320
* TIGER128, TIGER160 and TIGER192
* HAVAL128-3, HAVAL160-3, HAVAL192-3, HAVAL224-3 and HAVAL256-3
* SNEFRU128 and SNEFRU256
* ADLER32, CRC32, GOST and WHIRLPOOL

This package contains the GTK+3 version of the program.

%package        nautilus
Summary:        GtkHash extension for nautilus
Requires:       nautilus
Requires:       %{name}3 = %{version}
Requires:       GConf2

%description    nautilus
GtkHash extension for the nautilus file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%package        thunar
Summary:        GtkHash extension for Thunar
Requires:       Thunar
Requires:       %{name} = %{version}

%description    thunar
GtkHash extension for the Thunar file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%package        nemo
Summary:        GtkHash extension for Nemo
Requires:       nemo
Requires:       %{name} = %{version}

%description    nemo
GtkHash extension for the Nemo file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%package        caja
Summary:        GtkHash extension for Caja
Requires:       caja
Requires:       %{name} = %{version}

%description    caja
GtkHash extension for the Caja file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --with-gtk=3.0 \
  --enable-linux-crypto \
  --enable-gcrypt \
  --enable-glib-checksums \
  --enable-mhash \
%if %{with thunar}
  --enable-thunar \
%endif
%if %{with nautilus}
  --enable-nautilus \
%endif
%if %{with nemo}
  --enable-nemo \
%endif
%if %{with caja}
  --enable-caja \
%endif
  --disable-schemas-compile \

%make_build

%install

%make_install

%find_lang %{name}

# generic
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%if %{with nautilus} || %{with thunar} || %{with nemo} || %{with caja}
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.metainfo.xml
%endif
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/applications/org.%{name}.%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml
%if %{with nautilus} || %{with thunar} || %{with nemo} || %{with caja}
%{_datadir}/glib-2.0/schemas/org.%{name}.plugin.gschema.xml
%endif
%{_datadir}/icons/hicolor/*/apps/org.%{name}.%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/org.%{name}.%{name}.svg
%{_metainfodir}/org.%{name}.%{name}.appdata.xml

%if %{with nautilus}
%files nautilus
%{_libdir}/nautilus/extensions-3.0/libgtkhash-properties-nautilus.so
%{_metainfodir}/org.gtkhash.nautilus.metainfo.xml
%endif

%if %{with thunar}
%files thunar
%{_libdir}/thunarx-3/libgtkhash-properties-thunar.so
%{_metainfodir}/org.gtkhash.thunar.metainfo.xml
%endif

%if %{with nemo}
%files nemo
%{_libdir}/nemo/extensions-3.0/libgtkhash-properties-nemo.so
%{_metainfodir}/org.gtkhash.nemo.metainfo.xml
%endif

%if %{with caja}
%files caja
%{_libdir}/caja/extensions-2.0/libgtkhash-properties-caja.so
%{_datadir}/caja/extensions/libgtkhash-properties-caja.caja-extension
%{_metainfodir}/org.gtkhash.caja.metainfo.xml
%endif

%changelog
%autochangelog
