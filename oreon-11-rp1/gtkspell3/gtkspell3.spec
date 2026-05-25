Name:           gtkspell3
Version:        3.0.10
Release:        24%{?dist}
Summary:        On-the-fly spell checking for GtkTextView widgets

License:        GPL-2.0-or-later
URL:            https://gtkspell.sourceforge.net/
Source0:        https://downloads.sourceforge.net/gtkspell/gtkspell3-%{version}.tar.xz

BuildRequires:  enchant2-devel
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  make
BuildRequires:  vala

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-enchant2
BuildRequires: mingw32-gettext
BuildRequires: mingw32-gtk3

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-enchant2
BuildRequires: mingw64-gettext
BuildRequires: mingw64-gtk3

Requires:       iso-codes

%description
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use GtkSpell API version 3.0.


%package -n mingw32-%{name}
Summary:       MinGW Windows GtkSpell3 library
Obsoletes:     mingw32-%{name}-static
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows GtkSpell3 library.


%package -n mingw64-%{name}
Summary:       MinGW Windows GtkSpell3 library
Obsoletes:     mingw64-%{name}-static
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows GtkSpell3 library.


%{?mingw_debug_package}


%prep
%autosetup -p1


%build
# Native build
mkdir build_native
pushd build_native
%global _configure ../configure
%configure --disable-static --enable-vala --enable-gtk-doc
%make_build V=1
popd

# MinGW build
%mingw_configure --disable-static
%mingw_make_build


%install
%make_install -C build_native
%mingw_make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang gtkspell3
cat gtkspell3.lang | grep -v mingw32 > gtkspell3_native.lang
%mingw_find_lang %{name}


%mingw_debug_install_post


%files -f gtkspell3_native.lang
%doc AUTHORS README
%license COPYING
%{_libdir}/girepository-1.0/GtkSpell-3.0.typelib
%{_libdir}/libgtkspell3-3.so.*

%files devel
%doc %{_datadir}/gtk-doc/
%{_includedir}/gtkspell-3.0/
%{_libdir}/libgtkspell3-3.so
%{_libdir}/pkgconfig/gtkspell3-3.0.pc
%{_datadir}/gir-1.0/GtkSpell-3.0.gir
%{_datadir}/vala/vapi/gtkspell3-3.0.vapi
%{_datadir}/vala/vapi/gtkspell3-3.0.deps

%files -n mingw32-%{name} -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/libgtkspell3-3-0.dll
%{mingw32_includedir}/gtkspell-3.0/
%{mingw32_libdir}/libgtkspell3-3.dll.a
%{mingw32_libdir}/pkgconfig/gtkspell3-3.0.pc

%files -n mingw64-%{name} -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/libgtkspell3-3-0.dll
%{mingw64_includedir}/gtkspell-3.0/
%{mingw64_libdir}/libgtkspell3-3.dll.a
%{mingw64_libdir}/pkgconfig/gtkspell3-3.0.pc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.10-24
- Import
