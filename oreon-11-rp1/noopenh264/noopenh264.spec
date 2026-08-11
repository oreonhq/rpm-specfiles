%global source0_hash eccc175a7a11b8f7d36cb90c9907e8b8aca380dfac73af554bed667116a69edf

%global soversion 8

Name:           noopenh264
Version:        2.6.0
Release:        %autorelease
Summary:        Fake implementation of the OpenH264 library

License:        BSD-2-Clause and LGPL-2.1-or-later
URL:            https://codeberg.org/distro-openh264/noopenh264
Source:         %{url}/archive/v%{version}.tar.gz#/noopenh264-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson

# Explicitly conflict with openh264 that ships the actual
# non-dummy version of the library.
Conflicts:      openh264%{?_isa}

%description
Fake implementation of the OpenH264 library we can link from
regardless of the actual library being available.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Explicitly conflict with openh264-devel that ships the actual
# non-dummy version of the library.
Conflicts:      openh264-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

%build
%meson
%meson_build

%install
%meson_install

# Remove static library
rm $RPM_BUILD_ROOT%{_libdir}/*.a

%files
%license COPYING*
%doc README
%{_libdir}/libopenh264.so.%{soversion}
%{_libdir}/libopenh264.so.%{version}

%files devel
%{_includedir}/wels/
%{_libdir}/libopenh264.so
%{_libdir}/pkgconfig/openh264.pc

%changelog
%autochangelog
