%global source0_hash b8fb9d609e3aedebde7b0efa0c3de3b1fa5c4b61f5493b7f797b496a80f15fd0
Name:           synfig
Version:        1.5.5
Release:        1%{?dist}
Summary:        Vector-based 2D animation rendering backend
License:        GPL-2.0-or-later
URL:            http://synfig.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         synfig-1.5.3-optflags.patch
Patch1:         synfig-1.0.2-ltld.patch
ExcludeArch:    %{ix86}
Requires:       urw-fonts
Recommends:     which
# oreon:deps
BuildRequires:  ETL-devel
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  cairo-devel
BuildRequires:  fftw-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpng-devel
BuildRequires:  libsigc++-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxml++-devel
BuildRequires:  make
BuildRequires:  mlt-devel
BuildRequires:  pango-devel
BuildRequires:  pkgconfig(OpenEXR)
# /oreon:deps
%description
Synfig is a powerful, industrial-strength vector-based 2D animation
software, designed from the ground-up for producing feature-film quality
animation with fewer people and resources.  It is designed to be capable of
producing feature-film quality animation. It eliminates the need for
tweening, preventing the need to hand-draw each frame. Synfig features
spatial and temporal resolution independence (sharp and smoothat any
resolution or framerate), high dynamic range images, and a flexible plugin
system.

This package contains the command-line-based rendering backend.
Install synfigstudio package for GUI-based animation studio.

%package devel
Summary:        Development files for %{name}
Requires:       pkgconfig(OpenEXR) < 3
Requires:       ETL-devel
Requires:       libxml2-devel
Requires:       libxml++-devel
Requires:       libsigc++20-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p0 -b .optflags
%patch -P 1 -p0 -b .ltdl
rm -rf libltdl

%build

autoreconf -if
intltoolize --force
autoreconf
export CXXFLAGS="${RPM_OPT_FLAGS} -std=gnu++11"
%configure --disable-static --with-imagemagick --with-magickpp \
        --without-libavcodec --without-opengl \
        CPPFLAGS='-DMagickLib=MagickCore -I/usr/include/ImageMagick'
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}
touch -r README $RPM_BUILD_ROOT%{_bindir}/synfig-config
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n synfig-devel -f %{oreon_filedir}/synfig-devel.list

%changelog

%autochangelog
