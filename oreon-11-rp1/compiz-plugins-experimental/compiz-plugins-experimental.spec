%global source0_hash 695d0985e9745be8a76df0758a16628cc2d058a2570c2aae54882b57911f2d27
%global  basever 0.8.18
Name:    compiz-plugins-experimental
Epoch:   1
Version: %{basever}
Release:        1%{?dist}
Summary:        Additional plugins for Compiz
License: GPL-2.0-or-later
URL:     https://gitlab.com/compiz/%{name}
Source0:        https://gitlab.com/compiz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
ExcludeArch: s390 s390x
Requires: compiz >= %{basever}
Requires: compiz-plugins-main%{?_isa} >= %{basever}
Requires: compiz-plugins-extra%{?_isa} >= %{basever}
Provides: compiz-plugins-unsupported%{?_isa} = %{epoch}:%{version}-%{release}
Provides: compiz-plugins-unsupported = %{epoch}:%{version}-%{release}
Obsoletes: compiz-plugins-unsupported < %{epoch}:%{version}-%{release}
Patch0: compiz-plugins-experimental-0.8.18-gcc-14-fix.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  compiz-bcop
BuildRequires:  compiz-plugins-extra-devel
BuildRequires:  compiz-plugins-main-devel
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
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
Requires: compiz-plugins-extra-devel%{?_isa} >= %{basever}
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Provides: compiz-plugins-unsupported-devel%{?_isa} = %{epoch}:%{version}-%{release}
Provides: compiz-plugins-unsupported-devel = %{epoch}:%{version}-%{release}
Obsoletes: compiz-plugins-unsupported-devel < %{epoch}:%{version}-%{release}
%description devel
This package contain development files required for developing other plugins

%prep

%autosetup -p1 -n %{name}-v%{version}
chmod -x src/cubemodel/fileParser.c src/cubemodel/cubemodel.c src/cubemodel/cubemodel-internal.h

%build

./autogen.sh
%configure
make %{?_smp_mflags} V=1
%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
%find_lang %{name}
%oreon_autofiles compiz-plugins-experimental-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n compiz-plugins-experimental-devel -f %{oreon_filedir}/compiz-plugins-experimental-devel.list

%changelog

%autochangelog
