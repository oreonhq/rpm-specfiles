%global source0_hash b040f63836b347eb344f5542443dc254621805072f7141d49c067ecb5a375732
Name:           gtkspell3
Version:        3.0.10
Release:        1%{?dist}
Summary:        On-the-fly spell checking for GtkTextView widgets
License:        GPL-2.0-or-later
URL:            https://gtkspell.sourceforge.net/
Source0:        https://downloads.sourceforge.net/gtkspell/gtkspell3-%{version}.tar.xz
Requires:       iso-codes
# oreon:deps
BuildRequires:  enchant2-devel
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  make
BuildRequires:  mingw32-enchant2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-enchant2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-gtk3
BuildRequires:  vala
# /oreon:deps
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
BuildArch:     noarch
Obsoletes:     mingw32-%{name}-static < %{version}-%{release}
%description -n mingw32-%{name}
MinGW Windows GtkSpell3 library.

%package -n mingw64-%{name}
Summary:       MinGW Windows GtkSpell3 library
BuildArch:     noarch
Obsoletes:     mingw64-%{name}-static < %{version}-%{release}
%description -n mingw64-%{name}
MinGW Windows GtkSpell3 library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

mkdir build_native
pushd build_native
%global _configure ../configure
%configure --disable-static --enable-vala --enable-gtk-doc
%make_build V=1
popd
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtkspell3-devel -f %{oreon_filedir}/gtkspell3-devel.list
%files -n mingw32-gtkspell3 -f %{oreon_filedir}/mingw32-gtkspell3.list
%files -n mingw64-gtkspell3 -f %{oreon_filedir}/mingw64-gtkspell3.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.10-24
- Import
