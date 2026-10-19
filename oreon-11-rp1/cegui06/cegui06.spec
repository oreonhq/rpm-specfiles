%global source0_hash 0b49884c643a9652a855bcb9ce3eb6e8aed323f38c499ab99638b7237fcea7c8
Name:           cegui06
Version:        0.6.2
Release:        51%{?dist}
Summary:        CEGUI library 0.6 for apps which need this specific version
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.cegui.org.uk
Source0:        CEGUI-0.6.2b-clean.tar.gz
Patch1:         cegui-0.6.0-release-as-so-ver.patch
Patch2:         cegui-0.6.0-userverso.patch
Patch3:         cegui-0.6.2-new-DevIL.patch
Patch4:         cegui-0.6.2-new-tinyxml.patch
Patch5:         cegui-0.6.2-gcc46.patch
Patch6:         cegui-0.6.2-pcre2.patch
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  freeimage-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libGLU-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  make
BuildRequires:  pcre2-devel
# /oreon:deps
%description
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines. This package contains the older version 0.6 for
apps which cannot be easily ported to 0.7. As such this version has been build
without additional image codecs or xml parsers.

%package devel
Summary:        Development files for cegui06
Requires:       %{name} = %{version}-%{release}
Requires:       libGLU-devel
%description devel
Development files for cegui06

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n CEGUI-%{version}

# Permission fixes for debuginfo RPM
chmod -x include/falagard/*.h

# Encoding fixes
iconv -f iso8859-1 AUTHORS -t utf8 > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 TODO -t utf8 > TODO.conv && mv -f TODO.conv TODO
iconv -f iso8859-1 README -t utf8 > README.conv && mv -f README.conv README

# Make makefile happy even though we've removed the (unused) included copy of
# GLEW due to license reasons
mkdir -p RendererModules/OpenGLGUIRenderer/GLEW/GL
touch RendererModules/OpenGLGUIRenderer/GLEW/GL/glew.h
touch RendererModules/OpenGLGUIRenderer/GLEW/GL/glxew.h
touch RendererModules/OpenGLGUIRenderer/GLEW/GL/wglew.h
touch RendererModules/OpenGLGUIRenderer/GLEW/GLEW-LICENSE

%build

sed -i 's|libpcre|libpcre2-8|g' configure
%configure --disable-static --disable-samples --disable-lua-module \
    --disable-corona --disable-devil --disable-silly \
    --disable-irrlicht-renderer --disable-directfb-renderer \
    --disable-xerces-c --disable-libxml --disable-tinyxml \
    --with-default-xml-parser=ExpatParser \
    --with-default-image-codec=FreeImageImageCodec \
    --with-pic
sed -i 's|-L%{_libdir}||g' RendererModules/OpenGLGUIRenderer/Makefile
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mkdir -p %{buildroot}/%{_libdir}/CEGUI-0.6
for i in libCEGUIBase libCEGUIExpatParser libCEGUIFalagardWRBase \
         libCEGUIOpenGLRenderer libCEGUITGAImageCodec \
         libCEGUIFreeImageImageCodec; do
    rm %{buildroot}/%{_libdir}/$i.so
    ln -s ../$i-%{version}.so %{buildroot}/%{_libdir}/CEGUI-0.6/$i.so
done
mv %{buildroot}/%{_includedir}/CEGUI %{buildroot}/%{_includedir}/CEGUI-0.6
mv %{buildroot}/%{_datadir}/CEGUI %{buildroot}/%{_datadir}/CEGUI-0.6
sed -e 's|/CEGUI|/CEGUI-0.6|g' \
    -e 's|libdir=%{_libdir}|libdir=%{_libdir}/CEGUI-0.6|g' \
    -i %{buildroot}/%{_libdir}/pkgconfig/*.pc
for i in %{buildroot}/%{_libdir}/pkgconfig/*.pc; do
    mv $i `echo $i | sed 's|\.pc\$|-0.6.pc|'`
done
%ldconfig_scriptlets
%oreon_autofiles cegui06-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cegui06-devel -f %{oreon_filedir}/cegui06-devel.list

%changelog

%autochangelog
