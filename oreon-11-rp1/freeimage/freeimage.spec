%global source0_hash 999cec8e3a787d5d4a277587d5f5788913fe3e5450e90d06d8373ded71dde055

# https://bugzilla.redhat.com/show_bug.cgi?id=1676717
%undefine _ld_as_needed

%define major 3
%global svn_rev 1909

Name:           freeimage
Version:        3.19.0
Release:        0.31%{?svn_rev:.svn%svn_rev}%{?dist}
Summary:        Multi-format image decoder library

# freeimage is tripple-licensed, see
# http://freeimage.sourceforge.net/license.html
# https://lists.fedoraproject.org/pipermail/legal/2013-October/002271.html
License:        GPL-2.0-only OR GPL-3.0-only OR MPL-1.0
URL:            http://freeimage.sourceforge.net/
%if 0%{?svn_rev:1}
# Visit https://sourceforge.net/p/freeimage/svn/%{svn_rev}/tarball?path=/FreeImage/trunk
Source:        freeimage-svn-r%{svn_rev}-FreeImage-trunk.zip
%else
Source:        http://downloads.sourceforge.net/%{name}/FreeImage%(echo %{version} | sed 's|\.||g').zip
%endif
# Unbundle bundled libraries
Patch0:         FreeImage_unbundle.patch
# Fix incorrect path in doxyfile
Patch1:         FreeImage_doxygen.patch
# Patch for openexr 3
Patch2:         freeimage-openexr3.patch
# Proposed fix for CVE-2021-33367
Patch4:         CVE-2021-33367.patch
# Downstream fix for CVE-2021-40266
Patch5:         CVE-2021-40266.patch
# Downstream fix for CVE-2020-24292
Patch6:         CVE-2020-24292.patch
# Downstream fix for CVE-2020-24293
Patch7:         CVE-2020-24293.patch
# Downstream fix for CVE-2020-24295
Patch8:         CVE-2020-24295.patch
# Downstream fix for CVE-2021-40263
Patch9:         CVE-2021-40263.patch
# Downstream fix for CVE-2023-47997
Patch10:        CVE-2023-47997.patch
# Downstream fix for CVE-2023-47995
Patch11:        CVE-2023-47995.patch

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  jxrlib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  LibRaw-devel
%if 0%{?fedora} > 34
BuildRequires:  openexr-devel
BuildRequires:  imath-devel
%else
BuildRequires:  OpenEXR-devel
%endif
BuildRequires:  openjpeg2-devel

%description
FreeImage is a library for developers who would like to support popular
graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by
today's multimedia applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        plus
Summary:        C++ wrapper for FreeImage

%description    plus
The %{name}-plus package contains the C++ wrapper library for %{name}.

%package        plus-devel
Summary:        Development files for %{name}-devel
Requires:       %{name}-plus%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    plus-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}-plus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?svn_rev:1}
%setup -n freeimage-svn-r%{svn_rev}-FreeImage-trunk
%else
%setup -n FreeImage
%endif
# sanitize encodings / line endings
for file in `find . -type f -name '*.c' -or -name '*.cpp' -or -name '*.h' -or -name '*.txt' -or -name Makefile`; do
  iconv --from=ISO-8859-15 --to=UTF-8 $file > $file.new && \
  sed -i 's|\r||g' $file.new && \
  touch -r $file $file.new && mv $file.new $file
done

%autopatch -p1

# Fix unbundling patch for flatpak builds, where jxrlib is not in the runtime
if [ %{_prefix} != /usr -a -d %{_includedir}/jxrlib ] ; then
  sed -i -e 's|/usr/include/jxrlib|%{_includedir}/jxrlib|' Makefile.gnu
fi

# remove all included libs to make sure these don't get used during compile
rm -r Source/Lib* Source/ZLib Source/OpenEXR

# clear files which cannot be built due to dependencies on private headers
# (see also unbundle patch)
> Source/FreeImage/PluginG3.cpp
> Source/FreeImageToolkit/JPEGTransform.cpp

%build
sh ./gensrclist.sh
sh ./genfipsrclist.sh
%ifarch %{power64} %{mips32} aarch64 i686 s390x
%make_build -f Makefile.gnu CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LDFLAGS="%{__global_ldflags}"
%make_build -f Makefile.fip CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LDFLAGS="%{__global_ldflags}"
%else
%make_build -f Makefile.gnu CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"
%make_build -f Makefile.fip CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"
%endif

pushd Wrapper/FreeImagePlus/doc
doxygen FreeImagePlus.dox
popd

%install
install -Dpm 755 Dist/lib%{name}-%{version}.so %{buildroot}%{_libdir}/lib%{name}-%{version}.so
ln -s lib%{name}-%{version}.so %{buildroot}%{_libdir}/lib%{name}.so

install -Dpm 755 Dist/lib%{name}plus-%{version}.so %{buildroot}%{_libdir}/lib%{name}plus-%{version}.so
ln -s lib%{name}plus-%{version}.so %{buildroot}%{_libdir}/lib%{name}plus.so

install -Dpm 644 Source/FreeImage.h %{buildroot}%{_includedir}/FreeImage.h
install -Dpm 644 Wrapper/FreeImagePlus/FreeImagePlus.h %{buildroot}%{_includedir}/FreeImagePlus.h

# install missing symlink (was giving no-ldconfig-symlink rpmlint errors)
ldconfig -n %{buildroot}%{_libdir}

%files
%license license-*.txt
%doc Whatsnew.txt
%{_libdir}/lib%{name}-%{version}.so
%{_libdir}/lib%{name}.so.%major

%files devel
%doc Examples
%{_includedir}/FreeImage.h
%{_libdir}/lib%{name}.so

%files plus
%doc Wrapper/FreeImagePlus/WhatsNew_FIP.txt
%{_libdir}/lib%{name}plus-%{version}.so
%{_libdir}/lib%{name}plus.so.%major

%files plus-devel
%doc Wrapper/FreeImagePlus/html
%{_includedir}/FreeImagePlus.h
%{_libdir}/lib%{name}plus.so

%changelog
%autochangelog
