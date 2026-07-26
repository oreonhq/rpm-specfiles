%global source0_hash 1b62cb6351835217f3c229faba3182ba2aa0ab395849bb894dab422976dc8cf4

Name:           aiksaurus
Version:        1.2.1
Release:        60%{?dist}
Summary:        An English-language thesaurus library

Epoch:          1
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://aiksaurus.sourceforge.net/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
Patch0:         %{name}-1.2.1-gcc43.patch
Patch1:         %{name}-security.patch
Patch2:         %{name}-configure.c99.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires: make

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

# Remove libtool archives and static libs
find %{buildroot} -type f -name "*.la" -delete

# Add the desktop icon.
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

# Add desktop file.
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}

%ldconfig_scriptlets
%ldconfig_scriptlets gtk

%files
%doc ChangeLog README COPYING AUTHORS
%{_bindir}/%{name}
%{_bindir}/caiksaurus
%{_libdir}/*Aiksaurus-*.so.*
%{_datadir}/%{name}/

%files devel
%dir %{_includedir}/Aiksaurus
%{_includedir}/Aiksaurus/Aiksaurus.h
%{_includedir}/Aiksaurus/AiksaurusC.h
%{_libdir}/*Aiksaurus.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

%files gtk
%{_libdir}/*GTK*.so.*

%files gtk-devel
%{_includedir}/Aiksaurus/AiksaurusGTK*.h
%{_libdir}/*GTK*.so
%{_libdir}/pkgconfig/gaiksaurus-1.0.pc

%files thesaurus
%{_bindir}/gaiksaurus
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
