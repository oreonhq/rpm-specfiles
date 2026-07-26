%global source0_hash 2f50567225acd05d287e6161ff9540806b1dd9a57e7145e1e3fc5239159f677f

%global shortname graphlcd

Summary:        GraphLCD drivers and tools
Name:           %shortname-base
Version:        2.0.3
Release:        11%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/M-Reimer/graphlcd-base
Source0:        %url/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel
BuildRequires:  perl-interpreter
# makefile requires udev directory to be present to install rule.
BuildRequires:  systemd-udev
BuildRequires:  zlib-devel

%description
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

%package -n glcddrivers
Summary:        GraphLCD shared driver library
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later 
Provides:       libglcddrivers%{?_isa}  = %{version}-%{release}
# While the library doesn't use graphlcd-config directly, it is
# useless without the linked program using it.
# (Anssi) FIXME: What? If the above is true then this is bogus.
Requires:       %shortname-common%{?_isa}  >= %{version}

%description -n glcddrivers
The GraphLCD base is a project to support graphical LC displays. It is
mainly used by the graphlcd plugin for the Video Disc Recorder to
display its information.

This package contains the driver library needed to run programs
dynamically linked with GraphLCD.

%package -n %{shortname}-devel
Summary:        Headers for graphlcd
# Automatically converted from old format: GPLv2+ - review is highly recommended.
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
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Provides:       libglcdgraphics%{?_isa}  = %{version}-%{release}
# While the library doesn't use graphlcd-config directly, it is
# useless without the linked program using it.
# (Anssi) FIXME: See previous fixme.
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
# Automatically converted from old format: GPLv2+ - review is highly recommended.
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

%files -n glcddrivers
%doc README
%license COPYING
%{_libdir}/libglcddrivers.so.2*

%files -n %{shortname}-devel
%doc README
%dir %{_includedir}/glcddrivers
%dir %{_includedir}/glcdgraphics
%dir %{_includedir}/glcdskin
%{_includedir}/glcddrivers/*
%{_includedir}/glcdgraphics/*
%{_includedir}/glcdskin/*
%{_libdir}/libglcddrivers.so
%{_libdir}/libglcdgraphics.so
%{_libdir}/libglcdskin.so

%files -n glcdgraphics
%doc README
%license COPYING
%{_libdir}/libglcdgraphics.so.2*

%files -n glcdskin
%doc README
%license COPYING
%{_libdir}/libglcdskin.so.2*

%files -n graphlcd-common
%doc README HISTORY docs
%license COPYING
%config(noreplace) %{_sysconfdir}/graphlcd.conf
%{_udevrulesdir}/*-%{name}.rules

%files -n graphlcd-tools
%doc README docs/README.*
%license COPYING
%{_bindir}/*

%changelog
%autochangelog
