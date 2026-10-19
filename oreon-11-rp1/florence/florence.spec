%global source0_hash 422992fd07d285be73cce721a203e22cee21320d69b0fda1579ce62944c5091e
%bcond_without  doc
%bcond_without  xtst
%bcond_without  notification
Name:           florence
Version:        0.6.3
Release:        1%{?dist}
Summary:        Extensible scalable on-screen virtual keyboard for GNOME
License:        GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:            http://florence.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0: florence-c99.patch
%if %{with doc}
%endif
%if %{with notification}
%endif
%if %{with xtst}
%endif
%ifarch aarch64 riscv64
%endif
Requires:       control-center
# oreon:deps
BuildRequires:  GConf2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  gstreamer1-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libXext-devel
BuildRequires:  libXtst-devel
BuildRequires:  libnotify-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  scrollkeeper
# /oreon:deps
%description
Florence is an extensible scalable virtual keyboard for GNOME. 
You need it if you can't use a real hardware keyboard, for 
example because you are disabled, your keyboard is broken or 
because you use a tablet PC, but you must be able to use a pointing 
device (as a mouse, a trackball or a touchscreen).

Florence stays out of your way when you don't need it: 
it appears on the screen only when you need it. 
A Timer-based auto-click functionality is available 
to help disabled people having difficulties to click.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i -e 's|Icon=.*|Icon=%{name}|g' -e '/Encoding/d' data/%{name}.desktop.in.in

%build

CFLAGS+=-std=gnu17
%configure  \
%if %{without doc}
            --without-docs \
%endif
%if %{without notification}
            --without-notification \
%endif
%if %{without xtst}
            --without-xtst \
%endif
%if %{without doc}
            --without-docs \
%endif
            --with-panelapplet \
            --without-at-spi \
            --disable-static
make
%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install
find %{buildroot} -name '*.*a' -delete -print
desktop-file-install \
        --delete-original \
        --remove-category="Application" \
        --add-category="Utility" \
        --dir=%{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop
install -pDm0644 data/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
%ifarch aarch64 riscv64
chrpath --delete %{buildroot}/usr/bin/florence
%endif
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n florence-devel -f %{oreon_filedir}/florence-devel.list

%changelog

%autochangelog
