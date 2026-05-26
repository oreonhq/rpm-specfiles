%global with_mingw 0

%if 0%{?fedora}
%global with_mingw 1
%endif

Name:           gcab
Version:        1.6
Release:        10%{?dist}
Summary:        Cabinet file library and tool

License:        LGPL-2.1-or-later
#VCS:           git:git://git.gnome.org/gcab
URL:            http://ftp.gnome.org/pub/GNOME/sources/gcab
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gcab/%{version}/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 2f0c9615577c4126909e251f9de0626c3ee7a152376c15b5544df10fc87e560b
%global source0_file gcab-1.6.tar.xz
# oreon url source checksums end

BuildRequires:  git-core
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  vala
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  zlib-devel
BuildRequires:  meson
BuildRequires:  git

Requires:       libgcab1%{?_isa} = %{version}-%{release}

%if %{with_mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-glib2
BuildRequires: mingw32-glib2
BuildRequires: mingw64-zlib
BuildRequires: mingw32-zlib
%endif

%description
gcab is a tool to manipulate Cabinet archive.

%package -n libgcab1
Summary:        Library to create Cabinet archives

%description -n libgcab1
libgcab is a library to manipulate Cabinet archive using GIO/GObject.

%package -n libgcab1-devel
Summary:        Development files to create Cabinet archives
Requires:       libgcab1%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       pkgconfig

%description -n libgcab1-devel
libgcab is a library to manipulate Cabinet archive.

Libraries, includes, etc. to compile with the gcab library.

%if %{with_mingw}
%package -n mingw32-libgcab1
Summary: MinGW library to create Cabinet archive.
BuildArch: noarch

%description -n mingw32-libgcab1
libgcab is a library to manipulate Cabinet archive.

%package -n mingw64-libgcab1
Summary: MinGW library to create Cabinet archive.
BuildArch: noarch

%description -n mingw64-libgcab1
libgcab is a library to manipulate Cabinet archive.

%{?mingw_debug_package}
%endif

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gcab-1.6.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2f0c9615577c4126909e251f9de0626c3ee7a152376c15b5544df10fc87e560b" || { echo "oreon: Source0 SHA256 mismatch for gcab-1.6.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git_am

%build
%meson
%meson_build

%if %{with_mingw}
%mingw_meson -Dintrospection=false -Ddocs=false
%mingw_ninja
%endif

%check
%meson_test

%install
%meson_install

%find_lang %{name}

%ldconfig_scriptlets -n libgcab1

%if %{with_mingw}
%mingw_ninja_install
%mingw_debug_install_post
%mingw_find_lang %{name}
%endif


%files
%{_bindir}/gcab
%{_mandir}/man1/gcab.1*

%files -n libgcab1 -f %{name}.lang
%license COPYING
%doc NEWS
%{_libdir}/girepository-1.0/GCab-1.0.typelib
%{_libdir}/libgcab-1.0.so.*

%files -n libgcab1-devel
%{_datadir}/gir-1.0/GCab-1.0.gir
%{_datadir}/gtk-doc/html/gcab/*
%{_datadir}/vala/vapi/libgcab-1.0.vapi
%{_datadir}/vala/vapi/libgcab-1.0.deps
%{_includedir}/libgcab-1.0/*
%{_libdir}/libgcab-1.0.so
%{_libdir}/pkgconfig/libgcab-1.0.pc

%if %{with_mingw}
%files -n mingw32-libgcab1 -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/gcab.exe
%{mingw32_bindir}/libgcab-1.0-0.dll
%{mingw32_libdir}/libgcab-1.0.dll.a
%{mingw32_includedir}/libgcab-1.0/
%{mingw32_libdir}/pkgconfig/libgcab-1.0.pc
%{mingw32_mandir}/man1/gcab.1

%files -n mingw64-libgcab1 -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/gcab.exe
%{mingw64_bindir}/libgcab-1.0-0.dll
%{mingw64_libdir}/libgcab-1.0.dll.a
%{mingw64_includedir}/libgcab-1.0/
%{mingw64_libdir}/pkgconfig/libgcab-1.0.pc
%{mingw64_mandir}/man1/gcab.1
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6-10
- Prepare for Oreon 11 (RP1)
