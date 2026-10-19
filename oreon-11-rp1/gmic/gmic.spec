%global source0_hash c6771c48693ed615b2e85d1db7a9626358d4606eb2c75dcf009b2924f396da59
%global gimpplugindir %(%___build_pre; gimptool --gimpplugindir)/plug-ins
%global use_system_cimg 1
%global zart_version 20231127gitd014169
%global gmic_qt_version 20260318git6e59612
%global gmic_community_version 20260320gitc4150dc4
Summary:        GREYC's Magic for Image Computing
Name:    gmic
Version: 4.0.5
%global shortver %(foo=%{version}; echo ${foo//./})
Release:        1%{?dist}
Source0:        https://gmic.eu/files/source/%{name}_%{version}.tar.gz
Source1: zart-%{zart_version}.tar.gz
Source2: gmic-qt-%{gmic_qt_version}.tar.gz
Source3: gmic-community-%{gmic_community_version}.tar.gz
License: ( CECILL-2.1 OR CECILL-C ) AND GPL-3.0-or-later
Url: http://gmic.eu/
Provides: bundled(zart) = %{zart_version}
Provides: bundled(gmic-qt) = %{gmic_qt_version}
Provides: bundled(gmic-community) = %{gmic_community_version}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:     gmic-static <= 2.1.8
ExcludeArch:    s390x
# oreon:deps
BuildRequires:  CImg-devel
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gimp-devel-tools
BuildRequires:  hdf5-devel
BuildRequires:  ilmbase-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  opencv-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
G'MIC is an open and full-featured framework for image processing, providing
several different user interfaces to convert/manipulate/filter/visualize
generic image datasets, from 1d scalar signals to 3d+t sequences of
multi-spectral volumetric images.

%package devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Summary: Development files for G'MIC
%package gimp
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: G'MIC plugin for GIMP
%package libs
Summary: G'MIC shared libraries
%description devel
G'MIC is an open and full-featured framework for image processing, providing
several different user interfaces to convert/manipulate/filter/visualize
generic image datasets, from 1d scalar signals to 3d+t sequences of
multi-spectral volumetric images.

Provides files for building applications against the G'MIC API

%description gimp
G'MIC is an open and full-featured framework for image processing, providing
several different user interfaces to convert/manipulate/filter/visualize
generic image datasets, from 1d scalar signals to 3d+t sequences of
multi-spectral volumetric images.

Provides a plugin for using G'MIC from GIMP

%description libs
G'MIC is an open and full-featured framework for image processing, providing
several different user interfaces to convert/manipulate/filter/visualize
generic image datasets, from 1d scalar signals to 3d+t sequences of
multi-spectral volumetric images.

Provides G'MIC shared libraries

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1 -a 3

# gmic bundles 'qt', but we don't assume they have the latest
# version, so remove it and provide our own
rm -rf gmic-qt
tar zxvf %{SOURCE2}

cd gmic-qt
# no longer needed
#%%patch 1 -p1
#%%patch 2 -p1
#%%patch 3 -p1

# remove stash-file (thanks Wolfgang Lieff <Wolfgang.Lieff@airborneresearch.org.au>)
rm -f zart/.qmake.stash

%build

cd src
ln -fs ../gmic-community/libcgmic/gmic_libc.cpp .
ln -fs ../gmic-community/libcgmic/gmic_libc.h .
ln -fs ../gmic-community/libcgmic/use_libcgmic.c .
mv CImg.h CImg.h.bak
cp /usr/include/CImg.h CImg.h
make OPT_CFLAGS="%{optflags} -g" NOSTRIP=1 PREFIX=%{_prefix} LIB=%{_lib} cli lib libc
cd ../gmic-qt
%{qmake_qt5} CONFIG+=release GMIC_PATH=../src HOST=gimp gmic_qt.pro && %{make_build}
%{qmake_qt5} CONFIG+=release GMIC_PATH=../src HOST=none gmic_qt.pro && %{make_build}
cd ../zart
%{qmake_qt5} CONFIG+=release GMIC_PATH=../src zart.pro && %{make_build}
%install
mv gmic-qt/COPYING COPYING-gmic-qt
mv gmic-community/libcgmic/COPYING COPYING-libcgmic
iconv -f iso8859-1 -t utf-8 COPYING > COPYING.conv && mv -f COPYING.conv COPYING
iconv -f iso8859-1 -t utf-8 COPYING-libcgmic > COPYING-libcgmic.conv && mv -f COPYING-libcgmic.conv COPYING-libcgmic
cd src
make DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIB=%{_lib} install
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/gmic_qt.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/zart.desktop
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
mv $RPM_BUILD_ROOT/%{_datadir}/bash-completion/completions/gmic $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/gmic
rm -rf $RPM_BUILD_ROOT/%{_datadir}/bash-completion/completions/
chmod -x $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/gmic
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/gmic
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libcgmic.so.%{shortver}
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libgmic.so.%{shortver}
%ldconfig_scriptlets libs
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
%postun

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%pretrans -p <lua> gimp

path = "%{gimpplugindir}/gmic_gimp_qt"
st = posix.stat(path)
if st and st.type == "regular" then
  os.remove(path)
end
path = "%{gimpplugindir}/gmic_gimp_qt/gmic_gimp_qt"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
%posttrans

/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n gmic-devel -f %{oreon_filedir}/gmic-devel.list
%files -n gmic-gimp -f %{oreon_filedir}/gmic-gimp.list
%files -n gmic-libs -f %{oreon_filedir}/gmic-libs.list

%changelog

%autochangelog
