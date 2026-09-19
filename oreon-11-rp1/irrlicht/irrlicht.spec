%global source0_hash none

%global irrxml_version 1.8.5
%global irrlicht_version 1.8.5

Name:		irrlicht
Summary: 	A high performance realtime 3D engine
Version:	%{irrlicht_version}
Release:	11%{?dist}
License:	zlib
Source0:	http://downloads.sourceforge.net/irrlicht/%{name}-%{irrlicht_version}.zip
# Various fixes, optflags, system libraries/headers
# http://irrlicht.sourceforge.net/phpBB2/viewtopic.php?t=24076&highlight=
Patch0:		irrlicht-1.8-optflags.patch
# Get the code compiling
Patch1:		irrlicht-1.8-glext.patch
# Use system libaesgm
Patch2:		irrlicht18-libaesgm.patch
# Use improved fastatof from assimp
# Upstream applied a modified version of most of this.
# Patch3:	irrlicht18-fastatof-improvements-typefixes.patch
# Make libIrrXML.so
Patch4:		irrlicht-1.8-irrXML-shared-library.patch
# Fix issue with definition of LOCALE_DECIMAL_POINTS
Patch5:		irrlicht-1.8-fix-locale-decimal-points.patch
# Fix build with Mesa 10
Patch6:		irrlicht-1.8.1-mesa10.patch
# Use RPM_LD_FLAGS
Patch7:		irrlicht-1.8.4-ldflags.patch

URL:		http://irrlicht.sourceforge.net/
BuildRequires:  gcc-c++
BuildRequires:	libXxf86vm-devel, mesa-libGL-devel, mesa-libGLU-devel
BuildRequires:	libjpeg-devel, zlib-devel, libaesgm-devel
BuildRequires:	libpng-devel, bzip2-devel
BuildRequires: make
Provides:	irrlicht18 = %{version}-%{release}
Obsoletes:	irrlicht18 <= 1.8-0.4.svn3629%{?dist}

%description
The Irrlicht Engine is an open source high performance realtime 3D engine 
written and usable in C++ and also available for .NET languages. It is 
completely cross-platform, using D3D, OpenGL and its own software renderer, 
and has all of the state-of-the-art features which can be found in 
commercial 3d engines.

%package devel
Summary:	Development headers and libraries for irrlicht
Requires:	%{name}%{?_isa} = %{irrlicht_version}-%{release}
Requires:	mesa-libGL-devel, mesa-libGLU-devel, libXxf86vm-devel
Requires:	libjpeg-devel, zlib-devel, libpng-devel
Requires:	irrXML-devel%{?_isa} = %{irrxml_version}
Provides:	irrlicht18-devel = %{version}-%{release}
Obsoletes:	irrlicht18-devel <= 1.8-0.4.svn3629%{?dist}

%description devel
Development headers and libraries for irrlicht.

%package -n irrXML
Summary:	Simple and fast XML parser for C++
Version:	%{irrxml_version}
Provides:	irrXML18 = %{irrxml_version}-%{release}
Obsoletes:	irrXML18 <= 1.8-0.4.svn3629%{?dist}

%description -n irrXML
irrXML is a simple and fast open source xml parser for C++.

%package -n irrXML-devel
Summary:	Development headers and libraries for irrXML
Version:	%{irrxml_version}
Requires:	irrXML%{?_isa} = %{irrxml_version}-%{release}
Provides:	irrXML18-devel = %{irrxml_version}-%{release}
Obsoletes:	irrXML18-devel <= 1.8-0.4.svn3629%{?dist}

%description -n irrXML-devel
Development headers and libraries for irrXML.

%prep
%setup -q
%patch -P0 -p1 -b .optflags
%patch -P1 -p1 -b .glext
%patch -P2 -p1 -b .libaesgm
# %patch3 -p1 -b .fastatof
%patch -P4 -p1 -b .irrXML
%patch -P5 -p1 -b .fix-locale-decimal-points
%patch -P6 -p1 -b .mesa10
%patch -P7 -p1 -b .ldflags

# Upstream forgot to increment VERSION_RELEASE to 1 in 1.8.1
sed -i 's|VERSION_RELEASE = 0|VERSION_RELEASE = 1|g' source/Irrlicht/Makefile

sed -i 's/\r//' readme.txt
iconv -o readme.txt.iso88591 -f iso88591 -t utf8 readme.txt
mv readme.txt.iso88591 readme.txt
# We don't use any of this. Deleting it so the debuginfo doesn't pick it up.
rm -rf source/Irrlicht/jpeglib source/Irrlicht/zlib source/Irrlicht/libpng source/Irrlicht/aesGladman

for i in include/*.h doc/upgrade-guide.txt source/Irrlicht/*.cpp source/Irrlicht/*.h; do
  	sed -i 's/\r//' $i
	chmod -x $i
	touch -r changes.txt $i
done

# https://bugzilla.redhat.com/show_bug.cgi?id=1035757
sed -i -e '/_IRR_MATERIAL_MAX_TEXTURES_/s/4/8/' include/IrrCompileConfig.h

%build
cd source/Irrlicht
%make_build sharedlib

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}
make -C source/Irrlicht INSTALL_DIR=%{buildroot}%{_libdir} install 
cp -a include/*.h %{buildroot}%{_includedir}/%{name}/
pushd %{buildroot}%{_libdir}
ln -s libIrrlicht.so.%{irrlicht_version} libIrrlicht.so.1
ln -s libIrrXML.so.%{irrlicht_version} libIrrXML.so.1
popd

%ldconfig_scriptlets

%ldconfig_scriptlets -n irrXML

%files
%doc readme.txt
%{_libdir}/libIrrlicht.so.*

%files devel
%doc doc/upgrade-guide.txt
%{_includedir}/%{name}/
%exclude %{_includedir}/%{name}/fast_atof.h
%exclude %{_includedir}/%{name}/heapsort.h
%exclude %{_includedir}/%{name}/irrArray.h
%exclude %{_includedir}/%{name}/irrString.h
%exclude %{_includedir}/%{name}/irrTypes.h
%exclude %{_includedir}/%{name}/irrXML.h
%{_libdir}/libIrrlicht.so

%files -n irrXML
%doc readme.txt
%{_libdir}/libIrrXML.so.*

%files -n irrXML-devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/fast_atof.h
%{_includedir}/%{name}/heapsort.h
%{_includedir}/%{name}/irrArray.h
%{_includedir}/%{name}/irrString.h
%{_includedir}/%{name}/irrTypes.h
%{_includedir}/%{name}/irrXML.h
%{_libdir}/libIrrXML.so

%changelog
%autochangelog
