%global with_tests 1

Name:          cogl
Version:       1.22.8
Release:       17%{?dist}
Summary:       A library for using 3D graphics hardware to draw pretty pictures

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.clutter-project.org/
Source0:       http://download.gnome.org/sources/cogl/1.22/cogl-%{version}.tar.xz

# Vaguely related to https://bugzilla.gnome.org/show_bug.cgi?id=772419
# but on the 1.22 branch, and the static inline in the header is gross
# ajax promises he'll clean this up.
Patch0: 0001-egl-Use-eglGetPlatformDisplay-not-eglGetDisplay.patch

# "GL_ARB_shader_texture_lod" is used to do lod biased texturing. It
# make achieve faster blurring of images instead of using large blur radius.
Patch1: 0002-add-GL_ARB_shader_texture_lod-support.patch

# "copy_sub_image" is used to implement feature similar with kwin blur
# effect by being abel to copy partial of framebuffer contents as texture
# and do post blurring.
Patch2: 0003-texture-support-copy_sub_image.patch
# oreon url source checksums begin
%global source0_sha256 a805b2b019184710ff53d0496f9f0ce6dcca420c141a0f4f6fcc02131581d759
%global source0_file cogl-1.22.8.tar.xz
# oreon url source checksums end

BuildRequires: chrpath
BuildRequires: pkgconfig(cairo)
BuildRequires: mesa-libEGL-devel
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk-doc)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xrandr)

BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: make

%description
Cogl is a small open source library for using 3D graphics hardware to draw
pretty pictures. The API departs from the flat state machine style of
OpenGL and is designed to make it easy to write orthogonal components that
can render without stepping on each others toes.

As well aiming for a nice API, we think having a single library as opposed
to an API specification like OpenGL has a few advantages too; like being
able to paper over the inconsistencies/bugs of different OpenGL
implementations in a centralized place, not to mention the myriad of OpenGL
extensions. It also means we are in a better position to provide utility
APIs that help software developers since they only need to be implemented
once and there is no risk of inconsistency between implementations.

Having other backends, besides OpenGL, such as drm, Gallium or D3D are
options we are interested in for the future.

%package devel
Summary:       %{name} development environment
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for building and developing apps with %{name}.

%package       doc
Summary:       Documentation for %{name}
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description   doc
This package contains documentation for %{name}.

%if 0%{?with_tests}
%package       tests
Requires:      %{name} = %{version}-%{release}
Summary:       Tests for %{name}

%description   tests
This package contains the installable tests for %{name}.
%endif

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/cogl-1.22.8.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a805b2b019184710ff53d0496f9f0ce6dcca420c141a0f4f6fcc02131581d759" || { echo "oreon: Source0 SHA256 mismatch for cogl-1.22.8.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
CFLAGS="$RPM_OPT_FLAGS -fPIC -std=gnu17"
%configure \
  --enable-cairo=yes \
  --enable-cogl-pango=yes \
  --enable-gdk-pixbuf=yes \
  --enable-glx=yes \
  --enable-gtk-doc \
  --enable-introspection=yes \
  --enable-kms-egl-platform \
  --enable-wayland-egl-platform \
  --enable-wayland-egl-server \
  --enable-xlib-egl-platform \
  %{?with_tests:--enable-installed-tests}

make %{?_smp_mflags} V=1

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

# This gets installed by mistake
rm %{buildroot}%{_datadir}/cogl/examples-data/crate.jpg

# Remove lib64 rpaths
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libcogl-path.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libcogl-pango.so

%find_lang %{name}

%check
# make check

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc NEWS README
%{_libdir}/libcogl*.so.20*
%{_libdir}/girepository-1.0/Cogl*.typelib

%files devel
%{_includedir}/cogl
%{_libdir}/libcogl*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Cogl*.gir

%files doc
%{_datadir}/gtk-doc/html/cogl
%{_datadir}/gtk-doc/html/cogl-2.0-experimental

%if 0%{?with_tests}
%files tests
%{_datadir}/installed-tests/%{name}
%{_libexecdir}/installed-tests/%{name}
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.22.8-17
- Prepare for Oreon 11 (RP1)
