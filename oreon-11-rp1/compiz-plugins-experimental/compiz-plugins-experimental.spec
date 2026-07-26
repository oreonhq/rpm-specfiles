%global source0_hash none

%global  basever 0.8.18

Name:    compiz-plugins-experimental
Epoch:   1
Version: %{basever}
Release: 16%{?dist}
Summary: Additional plugins for Compiz
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://gitlab.com/compiz/%{name}
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# libdrm is not available on these arches
ExcludeArch: s390 s390x

BuildRequires: gcc-c++
BuildRequires: compiz-plugins-main-devel >= %{basever}
BuildRequires: compiz-plugins-extra-devel >= %{basever}
BuildRequires: compiz-bcop >= %{basever}
BuildRequires: perl(XML::Parser)
BuildRequires: intltool
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libtool
BuildRequires: libXScrnSaver-devel
BuildRequires: automake
BuildRequires: make

Requires: compiz >= %{basever}
Requires: compiz-plugins-main%{?_isa} >= %{basever}
Requires: compiz-plugins-extra%{?_isa} >= %{basever}
Provides: compiz-plugins-unsupported%{?_isa} = %{epoch}:%{version}-%{release}
Provides: compiz-plugins-unsupported = %{epoch}:%{version}-%{release}
Obsoletes: compiz-plugins-unsupported < %{epoch}:%{version}-%{release}
# https://gitlab.com/compiz/compiz-plugins-experimental/-/merge_requests/48
Patch0: compiz-plugins-experimental-0.8.18-gcc-14-fix.patch

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

%files -f %{name}.lang
%doc COPYING AUTHORS NEWS
%{_libdir}/compiz/*.so
%dir %{_datadir}/compiz/elements/
%dir %{_datadir}/compiz/fireflies/
%dir %{_datadir}/compiz/snow/
%dir %{_datadir}/compiz/stars/
%dir %{_datadir}/compiz/earth/
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*/*.frag
%{_datadir}/compiz/*/*.png
%{_datadir}/compiz/*/*.svg
%{_datadir}/compiz/*/*.vert
%{_datadir}/compiz/icons/hicolor/scalable/apps/*.svg

%files devel
%{_includedir}/compiz/compiz-elements.h

%changelog
%autochangelog
