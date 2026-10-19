%global source0_hash 413247bf598be9ab6f35154861cbc27def26c89936a67036fb57e59185a88077
%bcond nautilus %[!(0%{?fedora} > 36 || 0%{?rhel} > 9 || 0%{?flatpak})]
%bcond nemo %{undefined flatpak}
%bcond thunar %{undefined flatpak}
%bcond caja %{undefined flatpak}
Name:           gtkhash
Version:        1.5
Release:        1%{?dist}
Summary:        GTK+ utility for computing message digests or checksums
License:        GPL-2.0-or-later
URL:            https://github.com/tristanheaven/gtkhash
Source0:        https://github.com/tristanheaven/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
%if %{with nautilus}
%endif
%if %{with caja}
%endif
%if %{with nemo}
%endif
%if %{with thunar}
%endif
Provides:       gtkhash3 = %{version}-%{release}
Obsoletes:      gtkhash3 < 1.1.1
%if %{without nautilus}
Obsoletes:      %{name}-nautilus <= 1.5
%endif
%if %{without nemo}
Obsoletes:      %{name}-nemo <= 1.5
%endif
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libb2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mhash-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:  pkgconfig(libnemo-extension)
BuildRequires:  pkgconfig(thunarx-3)
# /oreon:deps
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
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%if %{with nautilus} || %{with thunar} || %{with nemo} || %{with caja}
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.metainfo.xml
%endif
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtkhash-nautilus -f %{oreon_filedir}/gtkhash-nautilus.list
%files -n gtkhash-thunar -f %{oreon_filedir}/gtkhash-thunar.list
%files -n gtkhash-nemo -f %{oreon_filedir}/gtkhash-nemo.list
%files -n gtkhash-caja -f %{oreon_filedir}/gtkhash-caja.list

%changelog

%autochangelog
