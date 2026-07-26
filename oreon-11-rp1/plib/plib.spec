%global source0_hash 485b22bf6fdc0da067e34ead5e26f002b76326f6371e2ae006415dea6a380a32

Name:           plib
Version:        1.8.5
Release:        41%{?dist}
Summary:        Set of portable libraries especially useful for games
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://plib.sourceforge.net/
Source:         http://plib.sourceforge.net/dist/plib-%{version}.tar.gz
Patch1:         plib-1.8.4-fullscreen.patch
Patch3:         plib-1.8.4-autorepeat.patch
Patch4:         plib-1.8.5-CVE-2011-4620.patch
Patch5:         plib-1.8.5-CVE-2012-4552.patch
Patch6:         plib-freeglut.patch
Patch7:         plib-1.8.5-spelling_errors.patch
Patch8:         plib-1.8.5-dont_break_joystick_system_calibration.patch
Patch9:         plib-1.8.5-CVE-2021-38714.patch
BuildRequires:  gcc gcc-c++ make
BuildRequires:  freeglut-devel libpng-devel libXext-devel libXi-devel
Buildrequires:  libXmu-devel libSM-devel libXxf86vm-devel

%description
This is a set of OpenSource (LGPL) libraries that will permit programmers
to write games and other realtime interactive applications that are 100%
portable across a wide range of hardware and operating systems. Here is
what you need - it's all free and available with LGPL'ed source code on
the web. All of it works well together.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libGL-devel

%description devel
This package contains the header files and libraries needed to write
or compile programs that use plib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# for some reason this file has its x permission sets, which makes rpmlint cry
chmod -x src/sg/sgdIsect.cxx

%build
%configure CXXFLAGS="$RPM_OPT_FLAGS -fPIC -DXF86VIDMODE"
make %{?_smp_mflags} 
# and below is a somewhat dirty hack inspired by debian to build shared libs
# instead of static. Notice that the adding of -fPIC to CXXFLAGS above is part
# of the hack.
dirnames=(util sg ssg fnt js net psl pui puAux pw sl sl ssgAux)
libnames=(ul sg ssg fnt js net psl pu puaux pw sl sm ssgaux)
libdeps=("" \
  "-L../util -lplibul" \
  "-L../util -lplibul -L../sg -lplibsg -lGL" \
  "-L../util -lplibul -L../sg -lplibsg -lGL" \
  "-L../util -lplibul" \
  "-L../util -lplibul" \
  "-L../util -lplibul" \
  "-L../util -lplibul -L../sg -lplibsg -L../fnt -lplibfnt -lGL" \
  "-L../util -lplibul -L../sg -lplibsg -L../fnt -lplibfnt -L../pui -lplibpu -lGL" \
  "-L../util -lplibul -lX11 -lGL -lXxf86vm" \
  "-L../util -lplibul" \
  "-L../util -lplibul" \
  "-L../util -lplibul -L../sg -lplibsg -L../ssg -lplibssg -lGL")

for (( i = 0; i < 13; i++ )) ; do
  pushd src/${dirnames[$i]}
  g++ -shared -Wl,-soname,libplib${libnames[$i]}.so.%{version} \
    -o libplib${libnames[$i]}.so.%{version} `ar t libplib${libnames[$i]}.a` \
    ${libdeps[$i]} -Wl,-z,relro -Wl,-z,now
  ln -s libplib${libnames[$i]}.so.%{version} libplib${libnames[$i]}.so
  popd
done

%install
make install DESTDIR=$RPM_BUILD_ROOT
# we don't want the static libs
rm $RPM_BUILD_ROOT%{_libdir}/*.a
# instead do a DIY install of the shared libs we created
cp -a `find . -name "libplib*.so*"` $RPM_BUILD_ROOT%{_libdir}

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NOTICE README
%license COPYING
%{_libdir}/libplib*.so.%{version}

%files devel
%{_includedir}/*
%{_libdir}/libplib*.so

%changelog
%autochangelog
