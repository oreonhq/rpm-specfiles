%global source0_hash 1b62cb6351835217f3c229faba3182ba2aa0ab395849bb894dab422976dc8cf4
Name:           aiksaurus
Version:        1.2.1
Release:        1%{?dist}
Summary:        An English-language thesaurus library
Epoch:          1
License:        GPL-2.0-or-later
URL:            http://aiksaurus.sourceforge.net/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
Patch0:         %{name}-1.2.1-gcc43.patch
Patch1:         %{name}-security.patch
Patch2:         %{name}-configure.c99.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  make
# /oreon:deps
%description
Aiksaurus is an English-language thesaurus library that can be 
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.  A basic command line 
thesaurus program is also included.

%package devel
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        Files for developing with aiksaurus
%description devel
Includes and definitions for developing with aiksaurus.

%package gtk
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        A GTK+ interface for aiksaurus
%description gtk
AiksaurusGTK is a GTK+ interface to the Aiksaurus library.
It provides an attractive thesaurus interface, and can be embedded
in GTK+ projects, notably AbiWord.

%package gtk-devel
Requires:       %{name}-gtk = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       gtk2-devel
Summary:        Files for developing with aiksaurus-gtk
%description gtk-devel
gtk includes and definitions for developing with aiksaurus.

%package thesaurus
Requires:       %{name}-gtk = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        A GTK+ frontend to aiksaurus
%description thesaurus
A standalone thesaurus program base on aiksaurus-gtk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool 
make %{?_smp_mflags}
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
%ldconfig_scriptlets
%ldconfig_scriptlets gtk
%oreon_autofiles aiksaurus-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles aiksaurus-gtk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles aiksaurus-gtk-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles aiksaurus-thesaurus usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n aiksaurus-devel -f %{oreon_filedir}/aiksaurus-devel.list
%files -n aiksaurus-gtk -f %{oreon_filedir}/aiksaurus-gtk.list
%files -n aiksaurus-gtk-devel -f %{oreon_filedir}/aiksaurus-gtk-devel.list
%files -n aiksaurus-thesaurus -f %{oreon_filedir}/aiksaurus-thesaurus.list

%changelog

%autochangelog
