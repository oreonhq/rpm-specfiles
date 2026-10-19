%global source0_hash 89af7c785a7ae3d9a7af6e64a69028829a429f66a14b1b913be22816dc07ddca
%bcond check 1
%global forgeurl https://github.com/WizardMac/ReadStat
Version:        1.1.9
%forgemeta
Name:           readstat
Release:        1%{?dist}
Summary:        Read (and write) data sets from SAS, Stata, and SPSS
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/ReadStat-%{version}.tar.gz
Patch0:         https://github.com/WizardMac/ReadStat/pull/298.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
Originally developed for Wizard, ReadStat is a command-line tool and
MIT-licensed C library for reading files from popular stats packages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
The %{name}-tools package contains tools about %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

autoreconf -fiv
CFLAGS="$CFLAGS -Wno-error=stringop-truncation"
%configure
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

make check
%endif
%files -f %{oreon_filedir}/main.list
%files -n readstat-devel -f %{oreon_filedir}/readstat-devel.list
%files -n readstat-tools -f %{oreon_filedir}/readstat-tools.list

%changelog

%autochangelog
