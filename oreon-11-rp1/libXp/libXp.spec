%global source0_hash 1f19e3b8e82a34a8fd9889a7d9af0abe8588cb03fb57c37c569634cf3b9df1a4
Summary:        X.Org X11 libXp runtime library
Name: libXp
Version: 1.0.4
Release:        10%{?dist}
License: X11 AND X11-distribute-modifications-variant
URL: http://www.x.org
Source0:        https://www.x.org/releases/individual/lib/libXp-1.0.4.tar.xz
Patch0:        add-proto-files.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libXext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXp runtime library

%package devel
Summary: X.Org X11 libXp development package
Requires: libXau-devel pkgconfig
Requires: %{name} = %{version}-%{release}
BuildRequires: xorg-x11-proto-devel
%description devel
X.Org X11 libXp development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .add-proto-files

%build

CPPFLAGS="$CPPFLAGS -I$RPM_BUILD_ROOT%{_includedir}"
export CPPFLAGS
autoreconf -v --install
%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXp-devel -f %{oreon_filedir}/libXp-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.4-10
- Import
