%global source0_hash 207384deb196198ac4764c5b42bb558f7c661494302b380afc09447678538386
%ifarch %{golang_arches}
%bcond man 1
%endif
Name:           composefs
Version:        1.0.8
Release:        1%{?dist}
Summary:        Tools to handle creating and mounting composefs images
License:        LGPL-2.0-or-later AND Apache-2.0
URL:            https://github.com/containers/composefs
Source0:        https://github.com/containers/composefs/releases/download/v%{version}/%{name}-%{version}.tar.xz
%if %{with man}
%endif
Requires:       %{name}-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  openssl-devel
# /oreon:deps
%description
Tools to handle creating and mounting composefs images. The composefs
project combines several underlying Linux features to provide a very
flexible mechanism to support read-only mountable filesystem trees,
stacking on top of an underlying "lower" Linux filesystem.

Please see https://github.com/containers/composefs for more information.

%package        devel
Summary:        Devel files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
Devel files for %{name}.

%package        libs
Summary:        Libraries for %{name}
License:        LGPL-2.1-or-later AND (GPL-2.0-only OR Apache-2.0)
%description    libs
Library files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson --default-library=shared -Dfuse=enabled \
%if %{with man}
  -Dman=enabled 
%endif
%meson_build
%install
%meson_install
rm -v $RPM_BUILD_ROOT/%{_libdir}/libcomposefs*.a
%oreon_autofiles composefs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles composefs-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n composefs-devel -f %{oreon_filedir}/composefs-devel.list
%files -n composefs-libs -f %{oreon_filedir}/composefs-libs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.8-5
- Prepare for Oreon 11 (RP1)
