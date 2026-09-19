%global source0_hash 0b49884c643a9652a855bcb9ce3eb6e8aed323f38c499ab99638b7237fcea7c8

Name:           cegui06
Version:        0.6.2
Release:        51%{?dist}
Summary:        CEGUI library 0.6 for apps which need this specific version
# Automatically converted from old format: MIT and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.cegui.org.uk
# This is
# http://downloads.sourceforge.net/crayzedsgui/CEGUI-0.6.2b.tar.gz
# with the bundled GLEW: RendererModules/OpenGLGUIRenderer/GLEW
# removed as its an older GLEW version which contains
# parts under then non Free SGI OpenGL and GLX licenses
# To regenerate do:
# wget http://downloads.sourceforge.net/crayzedsgui/CEGUI-0.6.2b.tar.gz
# tar xvfz CEGUI-0.6.2b.tar.gz'
# rm -r CEGUI-0.6.2/RendererModules/OpenGLGUIRenderer/GLEW
# tar cvfz CEGUI-0.6.2b-clean.tar.gz
Source0:        CEGUI-0.6.2b-clean.tar.gz
# Both submitted upstream: http://www.cegui.org.uk/mantis/view.php?id=197
Patch1:         cegui-0.6.0-release-as-so-ver.patch
Patch2:         cegui-0.6.0-userverso.patch
# TODO: submit upstream
Patch3:         cegui-0.6.2-new-DevIL.patch
Patch4:         cegui-0.6.2-new-tinyxml.patch
Patch5:         cegui-0.6.2-gcc46.patch
Patch6:         cegui-0.6.2-pcre2.patch
BuildRequires:  gcc-c++
BuildRequires:  expat-devel
BuildRequires:  freetype-devel > 2.0.0
BuildRequires:  libICE-devel
BuildRequires:  libGLU-devel
BuildRequires:  libSM-devel
BuildRequires:  pcre2-devel
BuildRequires:  glew-devel
BuildRequires:  freeimage-devel
BuildRequires:  make

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
# configure part of pcre2 change, easier/cleaner to do with sed
sed -i 's|libpcre|libpcre2-8|g' configure
%configure --disable-static --disable-samples --disable-lua-module \
    --disable-corona --disable-devil --disable-silly \
    --disable-irrlicht-renderer --disable-directfb-renderer \
    --disable-xerces-c --disable-libxml --disable-tinyxml \
    --with-default-xml-parser=ExpatParser \
    --with-default-image-codec=FreeImageImageCodec \
    --with-pic
# We do not want to get linked against a system copy of ourselves!
sed -i 's|-L%{_libdir}||g' RendererModules/OpenGLGUIRenderer/Makefile
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Move some things around to make cegui06-devel co-exist peacefully with
# cegui-devel
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

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/libCEGUI*-%{version}.so

%files devel
%{_libdir}/CEGUI-0.6
%{_libdir}/pkgconfig/CEGUI-OPENGL-0.6.pc
%{_libdir}/pkgconfig/CEGUI-0.6.pc
%{_includedir}/CEGUI-0.6
%{_datadir}/CEGUI-0.6

%changelog
%autochangelog
