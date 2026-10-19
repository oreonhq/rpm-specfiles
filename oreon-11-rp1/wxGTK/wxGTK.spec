%global source0_hash 6a129015bce2e914e4bf61ec4411854ad962801d47e92f2eb8340adb6a90af08
%global srcname wxWidgets
%global wxbasename wxBase
%global gtk3dir bld_gtk3
%global sover 0
%bcond_without tests
Name:           wxGTK
Version:        3.2.11
Release:        1%{?dist}
Summary:        GTK port of the wxWidgets GUI library
License:        LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:            https://www.wxwidgets.org/
Source0:        https://github.com/%{srcname}/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.bz2
Source10:       wx-config
Patch0:         %{name}-3.1.6-abicheck.patch
Patch1:         tests-no-deprecated-copy-dtor.patch
%if %{with tests}
%endif
Provides:       wxGTK3 = %version-%{release}
Obsoletes:      wxGTK3 < %version-%{release}
Obsoletes:      compat-wxGTK3-gtk2 < %version-%{release}
Obsoletes:      compat-wxGTK3-gtk2-devel < %version-%{release}
Obsoletes:      compat-wxGTK3-gtk2-gl < %version-%{release}
Obsoletes:      compat-wxGTK3-gtk2-media < %version-%{release}
Obsoletes:      wxBase3 < %version-%{release}
Obsoletes:      wxBase3-devel < %version-%{release}
Obsoletes:      wxGTK3-devel < %version-%{release}
Obsoletes:      wxGTK3-docs < %version-%{release}
Obsoletes:      wxGTK3-gl < %version-%{release}
Obsoletes:      wxGTK3-i18n < %version-%{release}
Obsoletes:      wxGTK3-media < %version-%{release}
Obsoletes:      wxGTK3-webview < %version-%{release}
Provides:       %{srcname} = %{version}-%{release}
Provides:       bundled(scintilla) = 3.7.2
Requires:       %{wxbasename}%{?_isa} = %{version}-%{release}
Requires:       %{name}-i18n = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  autoconf
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glibc-langpack-en
BuildRequires:  graphviz
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gtk3-devel
BuildRequires:  libGLU-devel
BuildRequires:  libSM-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmspack-devel
BuildRequires:  libpng-devel
BuildRequires:  libsecret-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  mesa-libEGL
BuildRequires:  python3-httpbin
BuildRequires:  vulkan-loader
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  xclock
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  zlib-devel
# /oreon:deps
%description
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package -n     %{wxbasename}-devel
Summary:        Development files for the wxBase3 library
Requires:       %{wxbasename}%{?_isa} = %{version}-%{release}
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
%description -n %{wxbasename}-devel
This package include files needed to link with the wxBase3 library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package        devel
Summary:        Development files for the wxGTK library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gl = %{version}-%{release}
Requires:       %{name}-media = %{version}-%{release}
Requires:       %{name}-webview = %{version}-%{release}
Requires:       %{wxbasename} = %{version}-%{release}
Requires:       %{wxbasename}-devel%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel
Requires:       libGLU-devel
Provides:       %{srcname}-devel = %{version}-%{release}
%description devel
This package include files needed to link with the wxGTK library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package        gl
Summary:        OpenGL add-on for the wxWidgets library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description gl
OpenGL (a 3D graphics API) add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package        i18n
Summary:        i18n message catalogs for the wxWidgets library
BuildArch:      noarch
%description i18n
i18n message catalogs for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package        media
Summary:        Multimedia add-on for the wxWidgets library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description media
Multimedia add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package        webview
Summary:        WebView add-on for the wxWidgets library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description webview
WebView add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.

%package -n     %{wxbasename}
Summary:        Non-GUI support classes from the wxWidgets library
%description -n %{wxbasename}
Every wxWidgets application must link against this library. It contains
mandatory classes that any wxWidgets code depends on (like wxString) and
portability classes that abstract differences between platforms. wxBase can
be used to develop console mode applications -- it does not require any GUI
libraries or the X Window System.

%package        docs
Summary:        Documentation for the wxGTK library
Requires:       %{name} = %{version}-%{release}
Provides:       %{srcname}-docs = %{version}-%{release}
BuildArch:      noarch
%description docs
This package provides documentation for the %{srcname} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

# patch some installed files to avoid conflicts with 2.8.*
sed -i -e 's|aclocal)|aclocal/wxwin32.m4)|' Makefile.in

# fix plugin dir for 64-bit
sed -i -e 's|/usr/lib\b|/usr/%{_lib}|' wx-config.in configure
sed -i -e 's|/lib|/%{_lib}|' src/unix/stdpaths.cpp

# Since we're currently patching configure.in
rm -f configure
./autogen.sh

%build

%global _configure ../configure
mkdir %{gtk3dir}
pushd %{gtk3dir}
%configure \
  --with-gtk=3 \
  --with-opengl \
  --with-sdl \
  --with-libmspack \
  --with-liblzma \
  --enable-intl \
  --disable-rpath \
  --disable-glcanvasegl \
  --enable-ipv6
%make_build
popd
WX_SKIP_DOXYGEN_VERSION_CHECK=1 docs/doxygen/regen.sh html
mv docs/doxygen/out/html .
%install
pushd %{gtk3dir}
%make_install
popd
rm %{buildroot}%{_bindir}/wx-config
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_libexecdir}/%{name}/wx-config
sed -i -e 's|=/usr|=%{_prefix}|' %{buildroot}%{_libexecdir}/%{name}/wx-config
ln -s ../..%{_libexecdir}/%{name}/wx-config %{buildroot}%{_bindir}/wx-config-3.2
touch %{buildroot}%{_bindir}/wx-config
mv %{buildroot}%{_bindir}/wxrc* %{buildroot}%{_libexecdir}/%{name}
ln -s ../..%{_libexecdir}/%{name}/wxrc-3.2 %{buildroot}%{_bindir}/wxrc-3.2
touch %{buildroot}%{_bindir}/wxrc
mkdir %{buildroot}%{_datadir}/bakefile/presets/wx32
mv %{buildroot}%{_datadir}/bakefile/presets/*.* %{buildroot}%{_datadir}/bakefile/presets/wx32
%find_lang wxstd-3.2
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
pushd %{gtk3dir}/tests
make %{?_smp_mflags}
python3 -m httpbin.core &
LD_LIBRARY_PATH=%{buildroot}%{_libdir} TZ=UTC wxUSE_XVFB=1 \
  WX_TEST_WEBREQUEST_URL="http://localhost:5000" xvfb-run -a ./test ~[.] \
%ifarch s390x
  ~wxTextFile::Special ~wxFileName::GetSizeSpecial ~wxFile::Special \
%endif
%ifarch riscv64
  ~wxTextFile::Special ~wxFile::Special ~URLTestCase::GetInputStream ~WebRequest::SSL::Error \
%endif
  ~WebRequest::SSL::Ignore
LD_LIBRARY_PATH=%{buildroot}%{_libdir} wxUSE_XVFB=1 xvfb-run -a \
  ./test_gui ~[.] \
%ifarch i686
  ~ImageTestCase \
%endif
%ifarch ppc64le
  ~VirtListCtrlTestCase \
%endif
%ifarch s390x
  ~WebView \
%endif
%ifarch riscv64
  ~TreeCtrlTestCase ~WebView ~wxImage::Paste \
%endif
%ifarch loongarch64
  ~WebView \
%endif
  ~wxHtmlPrintout::Pagination
popd
%endif
%post -n %{wxbasename}-devel

if [ -f %{_bindir}/wx-config ] && [ ! -h %{_bindir}/wx-config ] ; then
  rm %{_bindir}/wx-config
fi
/usr/sbin/update-alternatives --install %{_bindir}/wx-config \
  wx-config %{_libexecdir}/%{name}/wx-config 25
/usr/sbin/update-alternatives --install %{_bindir}/wxrc \
  wxrc %{_libexecdir}/%{name}/wxrc 25
%postun -n %{wxbasename}-devel

if [ $1 -eq 0 ] ; then
  /usr/sbin/update-alternatives --remove wx-config %{_libexecdir}/%{name}/wx-config
  /usr/sbin/update-alternatives --remove wxrc %{_libexecdir}/%{name}/wxrc
fi
%files -f %{oreon_filedir}/main.list
%files -n wxBase-devel -f %{oreon_filedir}/wxBase-devel.list
%files -n wxGTK-devel -f %{oreon_filedir}/wxGTK-devel.list
%files -n wxGTK-gl -f %{oreon_filedir}/wxGTK-gl.list
%files -n wxGTK-i18n -f %{oreon_filedir}/wxGTK-i18n.list
%files -n wxGTK-media -f %{oreon_filedir}/wxGTK-media.list
%files -n wxGTK-webview -f %{oreon_filedir}/wxGTK-webview.list
%files -n wxBase -f %{oreon_filedir}/wxBase.list
%files -n wxGTK-docs -f %{oreon_filedir}/wxGTK-docs.list

%changelog

%autochangelog

