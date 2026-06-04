%global source0_hash none

%global	project_name	idxd-config

Name:		accel-config
Version:	4.1.8
Release:	13%{?dist}
Summary:	Configure accelerator subsystem devices
License:	GPL-2.0-only
URL:		https://github.com/intel/%{project_name}
Source0:        https://github.com/intel/idxd-config/archive/refs/tags/accel-config-v4.1.8.tar.gz

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:	gcc
BuildRequires:	autoconf
BuildRequires:	asciidoc
BuildRequires:	xmlto
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libkmod)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	systemd
BuildRequires: make

# accel-config is for configuring Intel DSA (Data-Streaming
# Accelerator) subsystem in the Linux kernel. It supports x86_64 only.
ExclusiveArch:	%{ix86} x86_64

%description
Utility library for configuring the accelerator subsystem.

%package devel
Summary:	Development files for libaccfg
License:	LGPL-2.1-only
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package libs
Summary:	Configuration library for accelerator subsystem devices
License:	LGPL-2.1-only
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description libs
Libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{project_name}-%{name}-v%{version}

%build
echo %{version} > version
./autogen.sh
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
make check

%files
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/accel-config-licenses LICENSE_GPL_2_0
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_sysconfdir}/%{name}/contrib/configs/*

%files libs
%doc README.md
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/accel-config-licenses accfg/lib/LICENSE_LGPL_2_1
%{_libdir}/lib%{name}.so.*

%files devel
%license Documentation/COPYING
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.8-13
- Import
