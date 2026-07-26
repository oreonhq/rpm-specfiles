%global source0_hash d95e48d230c104d80fee160314cbe0a16fab64228b9c9f88c867f040391d36de

%define realname ClanLib

Summary:        Cross platform C++ game library
Name:           ClanLib1
Version:        1.0.0
Release:        49%{?dist}
License:        Zlib
URL:            http://www.clanlib.org/
Source0:        http://www.clanlib.org/download/releases-1.0/%{realname}-%{version}.tgz
# Prebuild docs to avoid multilib conflicts. To regenerate, build and install
# ClanLib without passing --disable-docs (requires perl, libxslt) and then:
# mv $RPM_BUILD_ROOT%%{_datadir}/doc/clanlib html
# tar cvfz ClanLib-%%{version}-generated-docs.tar.gz html
Source1:        ClanLib-%{version}-generated-docs.tar.gz
Patch0:         ClanLib-0.8.0-gcc43.patch
Patch1:         ClanLib-1.0.0-fullscreen-viewport.patch
Patch2:         ClanLib-1.0.0-libpng15.patch
Patch3:         ClanLib-1.0.0-gcc6.patch
Patch4:         ClanLib-1.0.0-NULL-not-defined.patch
Patch5:         ClanLib-1.0.0-use-pthread_mutexattr_settype.patch
Patch6:         ClanLib-1.0.0-gcc15.patch
BuildRequires:  make gcc-c++
BuildRequires:  libX11-devel libXi-devel libXmu-devel libGLU-devel libICE-devel
BuildRequires:  libXext-devel libXxf86vm-devel libXt-devel xorg-x11-proto-devel
BuildRequires:  libvorbis-devel mikmod-devel SDL-devel SDL_gfx-devel
BuildRequires:  alsa-lib-devel libpng-devel libjpeg-devel

%description
ClanLib is a cross platform C++ game library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libGLU-devel xorg-x11-proto-devel pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a 1 -n %{realname}-%{version}
iconv -f iso8859-1 -t utf8 NEWS > NEWS.utf8
touch -r NEWS.utf8 NEWS
mv NEWS.utf8 NEWS
iconv -f iso8859-1 -t utf8 CREDITS > CREDITS.utf8
touch -r CREDITS.utf8 CREDITS
mv CREDITS.utf8 CREDITS
# fixup pc files
sed -i 's|libdir=${exec_prefix}/lib|libdir=@libdir@|' pkgconfig/clan*.pc.in
sed -i 's|Libs:   -L${libdir}|Libs:   -L${libdir}/%{realname}-1.0|' \
  pkgconfig/clan*.pc.in

%build
%configure --disable-dependency-tracking --disable-static --enable-dyn \
  --disable-docs
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
# put .so links in a subdir of %%{libdir} so they don't conflict with
# ClanLib06-devel .so links. The pkg-config files are patches to transparently
# handle this for applications using us.
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{realname}-1.0
mv $RPM_BUILD_ROOT%{_libdir}/*.so $RPM_BUILD_ROOT%{_libdir}/%{realname}-1.0
for i in $RPM_BUILD_ROOT%{_libdir}/%{realname}-1.0/*; do
  ln -sf ../`readlink $i` $i
done
# we're API compatible with 0.8, add 0.8 pkgconfig symlinks, so 0.8
# expecting sources can be build against us
for i in $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc; do
  ln -s `basename $i` `echo $i|sed 's/1\.0\.pc/0\.8\.pc/'`
done

%ldconfig_scriptlets

%files
%doc CREDITS NEWS TODO-RSN
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc README* html
%{_libdir}/%{realname}-1.0
%{_includedir}/%{realname}-1.0
%{_libdir}/pkgconfig/clan*.pc

%changelog
%autochangelog
