%global source0_hash a805b2b019184710ff53d0496f9f0ce6dcca420c141a0f4f6fcc02131581d759
%global with_tests 1
Name:          cogl
Version:       1.22.8
Release:        1%{?dist}
Summary:        A library for using 3D graphics hardware to draw pretty pictures
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.clutter-project.org/
Source0:        http://download.gnome.org/sources/cogl/1.22/cogl-%{version}.tar.xz
Patch0: 0001-egl-Use-eglGetPlatformDisplay-not-eglGetDisplay.patch
Patch1: 0002-add-GL_ARB_shader_texture_lod-support.patch
Patch2: 0003-texture-support-copy_sub_image.patch
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
find %{buildroot} -name '*.la' -delete
rm %{buildroot}%{_datadir}/cogl/examples-data/crate.jpg
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libcogl-path.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libcogl-pango.so
%find_lang %{name}
%oreon_autofiles cogl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cogl-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cogl-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n cogl-devel -f %{oreon_filedir}/cogl-devel.list
%files -n cogl-doc -f %{oreon_filedir}/cogl-doc.list
%files -n cogl-tests -f %{oreon_filedir}/cogl-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.22.8-17
- Prepare for Oreon 11 (RP1)
