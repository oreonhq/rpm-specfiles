%global source0_hash b9cc4a2acd74509435892823607d966d424bd9ad5d0b00938f27240a1bfa878a
%global ubuntu_release 16.04
%global with_tests 0
%bcond_without gtk2
Name:       libdbusmenu
Version:    %{ubuntu_release}.0
Release:        1%{?dist}
Summary:        Library for passing menus over DBus
License:    (LGPL-3.0-only OR LGPL-2.1-only) AND GPL-3.0-only
URL:        https://launchpad.net/libdbusmenu
Source0:        https://launchpad.net/%{name}/%{ubuntu_release}/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:     00-no-werror.patch
%if %{with gtk2}
%endif
%if 0%{?with_tests}
%endif
# oreon:deps
BuildRequires:  atk-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  glibc-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  vala
# /oreon:deps
%description
This is a small library designed to make sharing and displaying of menu
structures over DBus simple and easy to use. It works for both QT and GTK+ and
makes building menus simple.

%package devel
Summary:    %{summary} - Development files
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with gtk2}
%package gtk2
Summary:    %{summary} - GTK+2 version
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description gtk2
Shared libraries for the %{name}-gtk2 library.
%endif

%package gtk3
Summary:    %{summary} - GTK+3 version
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description gtk3
Shared libraries for the %{name}-gtk3 library.

%if %{with gtk2}
%package gtk2-devel
Summary:    Development files for %{name}-gtk2
Requires:   %{name}-gtk2%{?_isa} = %{version}-%{release}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   gtk2-devel
%description gtk2-devel
The %{name}-gtk2-devel package contains libraries and header files for
developing applications that use %{name}-gtk2.
%endif

%package gtk3-devel
Summary:    Development files for %{name}-gtk3
Requires:   %{name}-gtk3%{?_isa} = %{version}-%{release}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   gtk3-devel
%description gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.

%package jsonloader
Summary:    Test lib development files
Requires:   %{name}-devel%{?_isa} = %{version}-%{release}
Requires:   libdbusmenu = %{version}-%{release}
%description jsonloader
Test library for %{name}.

%package jsonloader-devel
Summary:    Test lib development files for %{name}
Requires:   %{name}-jsonloader%{?_isa} = %{version}-%{release}
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description jsonloader-devel
The %{name}-jsonloader-devel package contains libraries and header files for
developing applications that use %{name}-jsonloader.

%package    doc
Summary:    Document files for %{name}
BuildArch:  noarch
%description doc
The %{name}-doc package contains documents for developing applications that
use %{name}.

%package    tools
Summary:    Development tools for the dbusmenu libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description tools
The %{name}-tools package contains helper tools for developing applications
that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version} -c

export ACLOCAL_PATH=/usr/share/gettext/m4/
pushd %{name}-%{version}
%patch 0 -p1
autoreconf -fiv
popd

cp -a %{name}-%{version}/{README,COPYING,COPYING.2.1,COPYING-GPL3,AUTHORS,ChangeLog} .
cp -a %{name}-%{version} %{name}-gtk3-%{version}

%build

build(){
%configure --disable-static --disable-dumper --enable-introspection $*
%make_build
}
pushd %{name}-gtk3-%{version}
sed -i -e 's@^#!.*python$@#!/usr/bin/python2@' tools/dbusmenu-bench
build --with-gtk=3
popd
%if %{with gtk2}
pushd %{name}-%{version}
sed -i -e 's@^#!.*python$@#!/usr/bin/python2@' tools/dbusmenu-bench
build --with-gtk=2
popd
%endif
%install
pushd %{name}-gtk3-%{version}
%make_install
find %{buildroot} -name '*.la' -delete
popd
%if %{with gtk2}
pushd %{name}-%{version}
%make_install
find %{buildroot} -name '*.la' -delete
popd
%endif
rm -fr %{buildroot}%{_docdir}/%{name}
rm %{buildroot}/%{_libexecdir}/dbusmenu-bench
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*
%if 0%{?with_tests}
%check

for variant in %{name}-gtk3-%{version} %{name}-%{version}; do
    pushd $variant
        make check V=1
    popd
done
%endif
%ldconfig_scriptlets
%if %{with gtk2}
%ldconfig_scriptlets gtk2
%endif
%ldconfig_scriptlets gtk3
%ldconfig_scriptlets jsonloader
%files -f %{oreon_filedir}/main.list
%files -n libdbusmenu-devel -f %{oreon_filedir}/libdbusmenu-devel.list
%files -n libdbusmenu-gtk2 -f %{oreon_filedir}/libdbusmenu-gtk2.list
%files -n libdbusmenu-gtk3 -f %{oreon_filedir}/libdbusmenu-gtk3.list
%files -n libdbusmenu-gtk2-devel -f %{oreon_filedir}/libdbusmenu-gtk2-devel.list
%files -n libdbusmenu-gtk3-devel -f %{oreon_filedir}/libdbusmenu-gtk3-devel.list
%files -n libdbusmenu-jsonloader -f %{oreon_filedir}/libdbusmenu-jsonloader.list
%files -n libdbusmenu-jsonloader-devel -f %{oreon_filedir}/libdbusmenu-jsonloader-devel.list
%files -n libdbusmenu-doc -f %{oreon_filedir}/libdbusmenu-doc.list
%files -n libdbusmenu-tools -f %{oreon_filedir}/libdbusmenu-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{ubuntu_release}.0-31
- Prepare for Oreon 11 (RP1)
