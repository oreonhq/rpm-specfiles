%global source0_hash b6eaed83a873e254d448e24b524e3210d3d24ce6707e9f611d5a8ad8d11c1166
Name:		zonefs-tools
Version:	1.6.0
Release:        1%{?dist}
Summary:        Provides user utilities for the zonefs file system
License:	GPL-2.0-or-later
URL:		https://github.com/westerndigitalcorporation/%{name}
Source0:        https://github.com/westerndigitalcorporation/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libblkid-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
# /oreon:deps
%description
This package provides the mkzonefs (and mkfs.zonefs) user utility
to format zoned block devices for use with the zonefs file system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

sh autogen.sh
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
