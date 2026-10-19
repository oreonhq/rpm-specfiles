%global source0_hash 3125ff654b3a422b819d5b5d90406d4efc8fa4c7a66cc4a63efe6597574ad549
%global  basever 0.8.18
Name:    compiz-plugins-main
Version: 0.8.18
Release:        1%{?dist}
Epoch:   1
Summary:        Collection of Compiz Fusion plugins for Compiz
License: GPL-2.0-or-later
URL:     https://gitlab.com/compiz/%{name}
Source0:        https://gitlab.com/compiz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Patch0: compiz-plugins-main-0.8.18-gcc-14-fix.patch
Requires: compiz%{?_isa} >= %{basever}
# oreon:deps
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  compiz-bcop
BuildRequires:  compiz-devel
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libXrender-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pango-devel
BuildRequires:  perl(XML::Parser)
# /oreon:deps
%description
The Compiz Fusion Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
though plugins and themes contributed by the community giving a
rich desktop experience

%package devel
Summary: Development files for Compiz-Fusion
Requires: compiz-devel%{?_isa} >= %{basever}
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: cairo-devel
Requires: pango-devel
%description devel
This package contain development files required for developing other plugins

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

./autogen.sh
%configure
make %{?_smp_mflags} V=1
%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
%find_lang %{name}
%oreon_autofiles compiz-plugins-main-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n compiz-plugins-main-devel -f %{oreon_filedir}/compiz-plugins-main-devel.list

%changelog

%autochangelog
