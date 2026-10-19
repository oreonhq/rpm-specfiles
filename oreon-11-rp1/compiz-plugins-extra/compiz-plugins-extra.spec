%global source0_hash 2b31cd8aaed9e22e9b7aee7a72f4c3f0e33c4dfb87404c1981311ce2d338d33f
%global  basever 0.8.18
Name:    compiz-plugins-extra
Version: 0.8.18
Release:        1%{?dist}
Epoch:   1
Summary:        Additional Compiz Fusion plugins for Compiz
License: GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:     https://gitlab.com/compiz/%{name}
Source0:        https://gitlab.com/compiz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Requires: compiz >= %{basever}
Requires: compiz-plugins-main%{?_isa} >= %{basever}
Patch0: compiz-plugins-extra-0.8.18-gcc-14-fix.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  compiz-bcop
BuildRequires:  compiz-plugins-main-devel
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libXrender-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  perl(XML::Parser)
# /oreon:deps
%description
The Compiz Fusion Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
though plugins and themes contributed by the community giving a
rich desktop experience.
This package contains additional plugins from the Compiz Fusion Project

%package devel
Summary: Development files for Compiz-Fusion
Requires: compiz-plugins-main-devel%{?_isa} >= %{basever}
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
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
%ldconfig_scriptlets
%oreon_autofiles compiz-plugins-extra-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n compiz-plugins-extra-devel -f %{oreon_filedir}/compiz-plugins-extra-devel.list

%changelog

%autochangelog
