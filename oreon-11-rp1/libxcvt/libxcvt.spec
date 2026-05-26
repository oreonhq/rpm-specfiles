# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 0561690544796e25cfbd71806ba1b0d797ffe464e9796411123e79450f71db38
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:      libxcvt
Version:   0.1.2
Release:   11%{?dist}
Summary:   VESA CVT standard timing modelines generator

URL:       https://gitlab.freedesktop.org/xorg/lib/libxcvt/
Source0:   https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz

License:   MIT AND HPND-sell-variant

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: meson

%description
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.

%package devel
Summary: Development package
Requires: pkgconfig
Requires: libxcvt%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n cvt
Summary: Command line tool to calculate VESA CVT mode lines
Conflicts: xorg-x11-server-Xorg < 1.21
Requires: libxcvt%{?_isa} = %{version}-%{release}

%description -n cvt
A standalone version of the command line tool cvt copied from the Xorg
implementation and is meant to be a direct replacement to the version
provided by the Xorg server.

%prep
%oreon_verify_sources
%autosetup -S git_am -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc COPYING
%{_libdir}/libxcvt.so.*

%files devel
%{_libdir}/pkgconfig/libxcvt.pc
%dir %{_includedir}/libxcvt
%{_includedir}/libxcvt/*.h
%{_libdir}/libxcvt.so

%files -n cvt
%{_bindir}/cvt
%{_mandir}/man1/cvt.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.2-11
- Prepare for Oreon 11 (RP1)
