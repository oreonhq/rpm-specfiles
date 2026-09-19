%global source0_hash a9915e17d49c5499edd3df69ffeac0b7ba24f8b38ddf7509712b48eb3c21f1ff

Name: dx
Version: 4.4.4
Release: 73%{?dist}
Summary: Open source version of IBM's Visualization Data Explorer
License: IPL-1.0
URL: http://www.opendx.org/

Source0: http://opendx.informatics.jax.org/source/dx-%{version}.tar.gz
Source1: %{name}.desktop
Patch1: 0001-dx-rpm.patch
Patch2: 0002-dx-open.patch
Patch3: 0003-dx-gcc43.patch
# fixes http://www.opendx.org/bugs/view.php?id=236
Patch4: 0004-dx-errno.patch
# fix NULL pointer dereference when running dxexec over ssh
# without X forwarding
Patch5: 0005-dx-null.patch
# remove calls to non-public ImageMagick function to fix linking
Patch6: 0006-dx-magick.patch
# fix -Werror=format-security errors
Patch7: 0007-dx-format-security.patch
# fix gcc-6.0 -Warrowing errors
Patch8: 0008-dx-narrowing.patch
# fix gcc-7.0 incompatibilites
Patch9: 0009-gcc7.0-compatibility.patch
Patch10: dx-c99.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: bison
BuildRequires: desktop-file-utils
BuildRequires: flex
BuildRequires: hdf-static, hdf-devel
BuildRequires: ImageMagick-devel
#FIXME doesn't build currently
#BuildRequires: java-devel
BuildRequires: motif-devel
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: libtool
BuildRequires: libXinerama-devel
BuildRequires: libXpm-devel
BuildRequires: netcdf-devel
BuildRequires: openssh-clients
BuildRequires: make
Requires: openssh-clients

%description
OpenDX is a uniquely powerful, full-featured software package for the
visualization of scientific, engineering and analytical data: Its open
system design is built on familiar standard interface environments. And its
sophisticated data model provides users with great flexibility in creating
visualizations.

%package libs
Summary: OpenDX shared libraries

%description libs
This package contains the shared libraries from OpenDX.

%package devel
Summary: OpenDX module development headers and libraries
Requires: %{name}-libs = %{version}-%{release}

%description devel
If you want to write a module to use in the Data Explorer Visual Program
Editor, or in the scripting language, you will need this package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1

# fix debuginfo rpmlint warnings
chmod a-x src/exec/{dxmods,dpexec,hwrender}/*.{c,h}

%build
autoreconf --force --install

# The sources aren't ready for modern c++
# As a work-around, use c++11 and c11
%configure \
	--disable-static \
	--enable-shared \
	--with-jni-path=%{java_home}/include \
	--without-javadx \
	--disable-dependency-tracking \
	--enable-smp-linux \
	--enable-new-keylayout \
	--with-rsh=%{_bindir}/ssh \
	CXXFLAGS="-std=c++11 $RPM_OPT_FLAGS" \
	CFLAGS="-std=c11 $RPM_OPT_FLAGS"

%{make_build}

%install
%{make_install}

ln -s ../../%{_lib}/dx/bin_linux $RPM_BUILD_ROOT%{_datadir}/dx/

mv $RPM_BUILD_ROOT%{_libdir}/arch.mak $RPM_BUILD_ROOT%{_includedir}/dx/

install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
sed -e 's/"R. c #b4b4b4",/"R. c none",/' src/uipp/ui/icon50.xpm > $RPM_BUILD_ROOT%{_datadir}/pixmaps/dx.xpm
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

# cleanup buildroot
rm -rf $RPM_BUILD_ROOT%{_datadir}/dx/doc
rm     $RPM_BUILD_ROOT%{_datadir}/dx/lib/outboard.c
rm     $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets libs

%files
%doc AUTHORS ChangeLog NEWS doc/README*
%license LICENSE
%{_bindir}/*
%{_libdir}/dx
%{_datadir}/dx
%{_mandir}/*/*
%{_datadir}/pixmaps/*.xpm
%{_datadir}/applications/%{name}.desktop

%files libs
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/dx
%{_includedir}/*.h
%{_libdir}/lib*.so

%changelog
%autochangelog
