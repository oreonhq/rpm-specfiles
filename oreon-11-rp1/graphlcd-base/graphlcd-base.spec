%global source0_hash 2f50567225acd05d287e6161ff9540806b1dd9a57e7145e1e3fc5239159f677f
%global shortname graphlcd
Summary:        GraphLCD drivers and tools
Name:           %shortname-base
Version:        2.0.3
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/M-Reimer/graphlcd-base
Source0:        https://github.com/M-Reimer/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  systemd-udev
BuildRequires:  zlib-devel
# /oreon:deps
%description
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

%package -n glcddrivers
Summary:        GraphLCD shared driver library
License:        GPL-2.0-or-later 
Provides:       libglcddrivers%{?_isa}  = %{version}-%{release}
Requires:       %shortname-common%{?_isa}  >= %{version}
%description -n glcddrivers
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the driver library needed to run programs
dynamically linked with GraphLCD.

%package -n %{shortname}-devel
Summary:        Headers for graphlcd
License:        GPL-2.0-or-later
Requires:       glcddrivers%{?_isa}  = %{version}
Requires:       glcdgraphics%{?_isa}  = %{version}
Requires:       glcdskin%{?_isa}  = %{version}
Provides:       libglcddrivers-devel%{?_isa}  = %{version}-%{release}
Provides:       glcddrivers-devel%{?_isa}  = %{version}-%{release}
Provides:       libglcdgraphics-devel%{?_isa}  = %{version}-%{release}
Provides:       glcdgraphics-devel%{?_isa}  = %{version}-%{release}
Provides:       graphlcd-devel%{?_isa}  = %{version}-%{release}
%description -n %{shortname}-devel
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the headers that programmers will need to
develop applications which will use graphlcd-base.

%package -n glcdgraphics
Summary:        GraphLCD shared graphics library
License:        GPL-2.0-or-later
Provides:       libglcdgraphics%{?_isa}  = %{version}-%{release}
Requires:       %{shortname}-common%{?_isa}  >= %{version}
%description -n glcdgraphics
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the graphics library needed to run programs
dynamically linked with GraphLCD.

%package -n glcdskin
Summary:        GraphLCD shared skin library
License:        GPL-1.0-or-later
%description -n glcdskin
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the skin library needed to run programs
dynamically linked with libglcdskin.

%package -n graphlcd-common
Summary:        GraphLCD configuration file and documentation
License:        GPL-1.0-or-later
%description -n graphlcd-common
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the GraphLCD configuration file and GraphLCD
documentation.

%package -n graphlcd-tools
Summary:        GraphLCD tools
License:        GPL-2.0-or-later
%description -n graphlcd-tools
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains tools to use with GraphLCD.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# don't strip nor chmod to root
perl -pi -e 's,-o root -g root -s,,' $(find -name Makefile)

## Optimization flags in 'Make.config' file
sed -i \
    -e 's|PREFIX ?= /usr/local|PREFIX ?= %{_prefix}|' \
    -e 's|LIBDIR ?= $(PREFIX)/lib|LIBDIR ?= %{_libdir}|' \
    -e 's|UDEVRULESDIR ?= /etc/udev/rules.d|UDEVRULESDIR ?= %{_udevrulesdir}|' \
    Make.config

# Use group "dialout" for serial devices
sed -i -e 's|uucp|dialout|' 99-graphlcd-base.rules

# W: file-not-utf8
iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY

%build

%make_build
%install
%make_install
install -d -m755 %{buildroot}%{_sysconfdir}
install -m644 graphlcd.conf %{buildroot}%{_sysconfdir}
%oreon_autofiles glcddrivers usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles glcdgraphics usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles glcdskin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles graphlcd-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles graphlcd-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n glcddrivers -f %{oreon_filedir}/glcddrivers.list
%files -n graphlcd-devel -f %{oreon_filedir}/graphlcd-devel.list
%files -n glcdgraphics -f %{oreon_filedir}/glcdgraphics.list
%files -n glcdskin -f %{oreon_filedir}/glcdskin.list
%files -n graphlcd-common -f %{oreon_filedir}/graphlcd-common.list
%files -n graphlcd-tools -f %{oreon_filedir}/graphlcd-tools.list

%changelog

%autochangelog
