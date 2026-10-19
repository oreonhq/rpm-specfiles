%global source0_hash eccc175a7a11b8f7d36cb90c9907e8b8aca380dfac73af554bed667116a69edf
%global soversion 8
Name:           noopenh264
Version:        2.6.0
Release:        1%{?dist}
Summary:        Fake implementation of the OpenH264 library
License:        BSD-2-Clause and LGPL-2.1-or-later
URL:            https://codeberg.org/distro-openh264/noopenh264
Source0:        https://codeberg.org/distro-openh264/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Conflicts:      openh264%{?_isa}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  meson
# /oreon:deps
%description
Fake implementation of the OpenH264 library we can link from
regardless of the actual library being available.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      openh264-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
rm $RPM_BUILD_ROOT%{_libdir}/*.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n noopenh264-devel -f %{oreon_filedir}/noopenh264-devel.list

%changelog

%autochangelog
