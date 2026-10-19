%global source0_hash 93ca320b706279ebca53760da89d4c3f2bbc547f4723967140a34346d9f04c24
%global debug_package %{nil}
%define _legacy_common_support 1
%global _lto_cflags %nil
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] ||
d=%{_sysconfdir}/rpm; echo $d)
Name:           gnustep-make
Version:        2.9.3
Release:        1%{?dist}
Summary:        GNUstep makefile package
License:        GPL-3.0-or-later
URL:            https://www.gnustep.org/
Source0:        https://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
Source1:        %{name}-macros.gnustep
Requires:       gnustep-filesystem%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-objc
BuildRequires:  latex2html
BuildRequires:  make
BuildRequires:  tetex-dvips
BuildRequires:  tetex-latex
BuildRequires:  texi2html
BuildRequires:  texinfo-tex
# /oreon:deps
%description
The makefile package is a simple, powerful and extensible way to write
makefiles for a GNUstep-based project.  It allows the user to write a
project without having to deal with the complex issues associated with
configuration, building, installation, and packaging.  It also allows
the user to easily create cross-compiled binaries.

%package -n     gnustep-filesystem
Summary:        The basic directory layout for GNUstep packages
License:        LicenseRef-Not-Copyrightable
%description -n gnustep-filesystem
The gnustep-filesystem package contains the basic directory layout for
GNUstep packages.

%package        doc
Summary:        Documentation for %{name}
License:        GPL-3.0-or-later
BuildArch:      noarch
Requires:       gnustep-filesystem = %{version}-%{release}
%description    doc
The makefile package is a simple, powerful and extensible way to write
makefiles for a GNUstep-based project.  It allows the user to write a
project without having to deal with the complex issues associated with
configuration, building, installation, and packaging.  It also allows
the user to easily create cross-compiled binaries.
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

cp %{SOURCE1} macros.gnustep

sed -i "s|/@libdir@|/%{_lib}|g" FilesystemLayouts/fhs-system
sed -i "s|/@libdir@|/%{_lib}|g" FilesystemLayouts/fhs

# /usr/share/GNUstep/Makefiles/config-noarch.make and
# /usr/share/GNUstep/Makefiles/ix86/linux-gnu/gnu-gnu-gnu/config.make
# are spoiling a pure /usr/share install
sed -i "s|=/share/GNUstep/Makefiles|=/%{_lib}/GNUstep/Makefiles|" \
    FilesystemLayouts/fhs-system

# Fix files location except GNUSTEP_LOCAL_*
sed -i "67,77!s|=/local|=|" FilesystemLayouts/fhs-system 

%build

%configure --with-layout=fhs-system --enable-flattened
%make_build V=1
%install
%make_install GNUSTEP_INSTALLATION_DOMAIN=SYSTEM
%make_install -C Documentation GNUSTEP_INSTALLATION_DOMAIN=SYSTEM GNUSTEP_MAKEFILES=%{buildroot}%{_libdir}/GNUstep/Makefiles
%make_install -C Documentation GNUSTEP_INSTALLATION_DOMAIN=SYSTEM GNUSTEP_MAKEFILES=%{buildroot}%{_libdir}/GNUstep/Makefiles
for i in Applications WebApplications; do
    mkdir -p %{buildroot}%{_prefix}{,/local}/lib{,64}/GNUstep/$i
done
mkdir -p %{buildroot}%{_prefix}{,/local}/share/GNUstep/Documentation/Developer
install -d %{buildroot}%{macrosdir}
install -p -m 644 macros.gnustep %{buildroot}%{macrosdir}
%oreon_autofiles gnustep-filesystem usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnustep-filesystem -f %{oreon_filedir}/gnustep-filesystem.list
%files -n gnustep-make-doc -f %{oreon_filedir}/gnustep-make-doc.list

%changelog

%autochangelog
