%global source0_hash 0b90722984561004de84847744d566809dbb9daf732a9e503b91a1b5a84e5699

%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro -Wl,-z,now}

Name:		SDL_image
Version:	1.2.12
Release:	42%{?dist}
Summary:	Image loading library for SDL

License:	Zlib
URL:		http://www.libsdl.org/projects/SDL_image/
Source0:	http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz
Patch0:         SDL_image-1.2.12-interlaced-png-warning-fix.patch
Patch1:         pointer-type.patch

BuildRequires:  gcc make
BuildRequires: 	SDL-devel >= 1.2.10
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL surfaces.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.10
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1
%patch -P 1 -p0

%build
# XCF support is crashy in 1.2.4
%configure --disable-dependency-tracking	\
	--enable-tif				\
	--disable-jpg-shared			\
	--disable-png-shared			\
	--disable-tif-shared			\
	--disable-static                        \
	--disable-rpath
# Remove useless /usr/lib64 rpath on 64bit archs
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_bindir}
./libtool --mode=install /usr/bin/install showimage $RPM_BUILD_ROOT%{_bindir}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc README CHANGES
%license COPYING
%{_bindir}/showimage
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/SDL/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
