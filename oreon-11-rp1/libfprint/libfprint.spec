%global source0_hash edc90e02f330a7595ceaf37f2c6ec32ed43541347fe936d3273b0bb2524fd19c
Name:           libfprint
Version:        1.94.100
Release:        1%{?dist}
Summary:        Toolkit for fingerprint scanner
License:        LGPL-2.1-or-later AND NIST-PD
URL:            http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source0:        https://gitlab.freedesktop.org/libfprint/libfprint/-/archive/v%{version}/libfprint-v%{version}.tar.gz
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libgudev-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  python3-cairo
BuildRequires:  python3-gobject
BuildRequires:  systemd
BuildRequires:  umockdev
# /oreon:deps
%description
libfprint offers support for consumer fingerprint reader devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tests
Summary:        Tests for the %{name} package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libfprint-v%{version}
%oreon_prep
%build

%meson -Ddrivers=all
%meson_build
%install
%meson_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libfprint-devel -f %{oreon_filedir}/libfprint-devel.list
%files -n libfprint-tests -f %{oreon_filedir}/libfprint-tests.list

%changelog

%autochangelog
