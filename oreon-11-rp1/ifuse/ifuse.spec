%global source0_hash 9d490470ba6553f8052b385bb5330462e46fbe82131ebe65be47a1cc1c70e857
Name:          ifuse
Version:       1.2.1
Release:        1%{?dist}
Summary:        Mount Apple iPhone and iPod touch devices
License:       LGPL-2.1-or-later
URL:           https://www.libimobiledevice.org/
Source0:        https://github.com/libimobiledevice/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Requires:       fuse
# oreon:deps
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  libimobiledevice-devel
BuildRequires:  libimobiledevice-glue-devel
BuildRequires:  libplist-devel
BuildRequires:  make
# /oreon:deps
%description
A fuse filesystem for mounting iPhone and iPod touch devices

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
