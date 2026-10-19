%global source0_hash 7e0f1d2f8ad884edd2983eefba294e4df2428c5dbd876dedde46f79e8a4cea1e
Name:           AllegroOGG
Version:        1.0.3
Release:        41%{?dist}
Summary:        Ogg library for use with the Allegro game library
License:        LicenseRef-Callaway-BSD
URL:            http://www.allegro.cc/resource/Libraries/Audio/alogg
Source0:        http://www.hero6.com/filereviver/alogg.zip
Source1:        AllegroOGG.pc.in
# oreon:deps
BuildRequires:  allegro-devel
BuildRequires:  gcc
BuildRequires:  libvorbis-devel
# /oreon:deps
%description
%{name} is an Allegro wrapper for the Ogg Vorbis decoder from the Xiph.org
foundation. This lib lets you play OGGs and convert OGGs to Allegro SAMPLEs
amongst a lot of other capabilites.

%package devel
Summary:        Developmental libraries and include files for AllegroOgg
Requires:       %{name} = %{version}-%{release}
Requires:       allegro-devel
%description devel
Development libraries and include files for developing applications using
the %{name} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
%{__sed} -i 's/\r//' docs/A*.txt
%{__sed} -e "s#@prefix@#%{_prefix}#g" -e "s#@libdir@#%{_libdir}#g" \
  -e "s#@includedir@#%{_includedir}#g" -e "s#@version@#%{version}#g" \
  -e "s#@name@#%{name}#" %{SOURCE1} > %{name}.pc

%build

gcc $RPM_OPT_FLAGS -fPIC -DPIC -Iinclude -c src/alogg.c -o src/alogg.o
gcc -g -shared -Wl,-soname=lib%{name}.so.0 -o lib%{name}.so.0 \
  src/alogg.o -logg -lvorbis -lvorbisfile $(allegro-config --libs)
%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
install -m 755 lib%{name}.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{name}.so.0 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
install -m 644 include/* $RPM_BUILD_ROOT%{_includedir}/%{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n AllegroOGG-devel -f %{oreon_filedir}/AllegroOGG-devel.list

%changelog

%autochangelog
