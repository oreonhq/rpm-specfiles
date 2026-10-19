%global source0_hash 74a2ef0dcadc525825942e37d0bd28c5cfdbd8e4cd83c028f90f3a3731983216
Summary:        Utilities for configuring the linux ethernet bridge
Name:           bridge-utils
Version:        1.7.1
Release:        15%{?dist}
License:        GPL-2.0-or-later
URL:            https://wiki.linuxfoundation.org/networking/bridge
Source0:        https://git.kernel.org/pub/scm/network/bridge/%{name}.git/snapshot/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libsysfs-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This package contains utilities for configuring the linux ethernet
bridge. The linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

The bridge-utils package is deprecated, the bridge command from the
iproute package should preferably be used for linux ethernet bridges.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

autoconf
%configure
%make_build
%install
%make_install SUBDIRS="brctl doc"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
