%global source0_hash 3550702ef94b2f5f16c7db91c6b3282b2aed1340665834a03e47458e09d98d87

Name:          ifuse
Version:       1.1.4
Release:       %autorelease
Summary:       Mount Apple iPhone and iPod touch devices
License:       LGPL-2.1-or-later
URL:           https://www.libimobiledevice.org/
Source:        https://github.com/libimobiledevice/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  fuse-devel
BuildRequires:  libimobiledevice-devel
BuildRequires:  libimobiledevice-glue-devel
BuildRequires:  libplist-devel

Requires:       fuse

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

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
