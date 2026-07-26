%global source0_hash 4e9b228e25451b1e875127a57eb40270e38c59cf4d46bc25c208e370d884ba64

%global tomoe_ver 0.6.0

Name:           tomoe-gtk
Version:        %{tomoe_ver}
Release:        47%{?dist}
Summary:        Gtk library for tomoe for Japanese and Chinese handwritten input

License:        LGPL-2.0-or-later
URL:            https://sourceforge.net/projects/tomoe/
Source0:        http://downloads.sourceforge.net/project/tomoe/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.6.0-rpath.patch
Patch1:         %{name}-0.6.0-cflags.patch

Requires:       tomoe >= %{tomoe_ver}
Obsoletes:      libtomoe-gtk < 0.6.0-4
Provides:       libtomoe-gtk = %{version}-%{release}
BuildRequires: make
BuildRequires:  libtool
BuildRequires:  autoconf, automake
BuildRequires:  tomoe-devel >= %{tomoe_ver}, gtk2-devel
# does not currently build with gucharmap-2
#BuildRequires:  gucharmap-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  gettext

%description
Gtk library for tomoe Japanese handwritten input.
This package is used by scim-tomoe or uim-tomoe.

%package devel
Summary:    Gtk library for tomoe Japanese handwritten input
Requires:   %{name} = %{version}-%{release}
Requires:   gtk2-devel, libgnomeui-devel, gucharmap-devel, tomoe-devel
Obsoletes:  libtomoe-gtk-devel < 0.6.0-4
# added for F10
Provides:   libtomoe-gtk-devel = %{version}-%{release}

%description devel
The libtomoe-devel package includes the header files for libtomoe-gtk.
Install this if you want to develop programs which will use libtomoe-gtk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .rpath
%patch -P1 -p0 -b .cflags

%build
autoreconf -ivf
%configure --disable-static --without-gucharmap --disable-dependency-tracking \
  --disable-rpath --with-python=no
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" 
cd po
mkdir -p locale
for p in *.po;do
    loc=$(basename $p .po)
    mkdir -p locale/$loc/LC_MESSAGES
    msgfmt $p -o locale/$loc/LC_MESSAGES/%{name}.mo
done
cd ..

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
cp -R po/locale $RPM_BUILD_ROOT/%{_datadir}

rm $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%ldconfig_scriptlets

%ldconfig_scriptlets devel

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}/

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_includedir}/tomoe/*
%{_datadir}/gtk-doc/html/lib%{name}/

%changelog
%autochangelog
