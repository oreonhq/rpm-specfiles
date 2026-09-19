%global source0_hash 2b31cd8aaed9e22e9b7aee7a72f4c3f0e33c4dfb87404c1981311ce2d338d33f

%global  basever 0.8.18

Name:    compiz-plugins-extra
Version: 0.8.18
Release: 16%{?dist}
Epoch:   1
Summary: Additional Compiz Fusion plugins for Compiz

# Automatically converted from old format: GPLv2+ and MIT - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:     https://gitlab.com/compiz/%{name}
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires: compiz-plugins-main-devel >= %{basever}
BuildRequires: compiz-bcop >= %{basever}
BuildRequires: gettext-devel
BuildRequires: perl(XML::Parser)
BuildRequires: mesa-libGLU-devel
BuildRequires: libXrender-devel
BuildRequires: libnotify-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: gtk2-devel
BuildRequires: automake
BuildRequires: make

Requires: compiz >= %{basever}
Requires: compiz-plugins-main%{?_isa} >= %{basever}
# https://gitlab.com/compiz/compiz-plugins-extra/-/issues/36
Patch0: compiz-plugins-extra-0.8.18-gcc-14-fix.patch

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

%autosetup -p1 -n %{name}-v%{version}

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

%files -f %{name}.lang
%doc COPYING AUTHORS NEWS
%{_libdir}/compiz/*.so
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*.png
%{_datadir}/compiz/icons/hicolor/scalable/apps/*.svg

%files devel
%{_includedir}/compiz/
%{_libdir}/pkgconfig/compiz-*

%changelog
%autochangelog
