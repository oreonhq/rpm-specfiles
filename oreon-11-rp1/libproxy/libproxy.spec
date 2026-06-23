%global source0_hash a1fa55991998b80a567450a9e84382421a7176a84446c95caaa8b72cf09fa86f

%global _privatelibs libpxbackend-1.0[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

Name:           libproxy
Version:        0.5.12
Release:        3%{?dist}
Summary:        A library handling all the details of proxy configuration

License:        LGPL-2.1-or-later
URL:            https://libproxy.github.io/libproxy/
Source0:        https://github.com/libproxy/%{name}/archive/refs/tags/%{version}.tar.gz#/libproxy-0.5.12.tar.gz
# https://github.com/libproxy/libproxy/issues/343
Patch0:         libproxy-0.5.12-optional-static.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  /usr/bin/gi-docgen
BuildRequires:  /usr/bin/vapigen

BuildRequires:  pkgconfig(duktape)
BuildRequires:  pkgconfig(gio-2.0) >= 2.71.3
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  python3-devel
# For config-gnome
BuildRequires:  pkgconfig(gsettings-desktop-schemas)


%description
libproxy offers the following features:

    * extremely small core footprint
    * minimal dependencies within libproxy core
    * only 4 functions in the stable-ish external API
    * dynamic adjustment to changing network topology
    * a standard way of dealing with proxy settings across all scenarios
    * a sublime sense of joy and accomplishment


%package        bin
Summary:        Binary to test %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    bin
The %{name}-bin package contains the proxy binary for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
%meson \
  -Dconfig-gnome=true \
  -Dconfig-kde=true \
  -Dconfig-osx=false \
  -Dconfig-windows=false \
  -Dintrospection=true \
  -Dtests=true \
  -Dvapi=true
%meson_build


%install
%meson_install
ln -sf libproxy/proxy.h %{buildroot}%{_includedir}/proxy.h


%check
%meson_test

%ldconfig_scriptlets


%files
%doc README.md
%license COPYING
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Libproxy-1.0.typelib
%{_libdir}/libproxy.so.*
%dir %{_libdir}/libproxy
%{_libdir}/libproxy/libpxbackend-1.0.so

%files bin
%{_bindir}/proxy
%{_mandir}/man8/proxy.8*

%files devel
%{_docdir}/libproxy-1.0/
%{_includedir}/proxy.h
%{_includedir}/libproxy/
%{_libdir}/libproxy.so
%{_libdir}/pkgconfig/libproxy-1.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Libproxy-1.0.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/libproxy-1.0.deps
%{_datadir}/vala/vapi/libproxy-1.0.vapi


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.12-2
- Prepare for Oreon 11 (RP1)
