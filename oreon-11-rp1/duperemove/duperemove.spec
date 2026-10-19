%global source0_hash 27809aa91b7b9b7d0810e5329614bf80af2c48e917781e682a3fbcf61fa274da
%define _legacy_common_support 1
Name:           duperemove
Version:        0.15.2
Release:        1%{?dist}
Summary:        Tools for deduping file systems
License:        GPL-2.0-only
URL:            https://github.com/markfasheh/%{name}
Source0:        https://github.com/markfasheh/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libatomic
BuildRequires:  libgcrypt-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  xxhash-devel
# /oreon:deps
%description
Duperemove is a simple tool for finding duplicated extents and
submitting them for deduplication. When given a list of files it will
hash their contents on a block by block basis and compare those hashes
to each other, finding and categorizing extents that match each other.

When given the -d option, duperemove will submit those extents for
deduplication using the btrfs-extent-same ioctl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Fix prefix
sed -i 's@^PREFIX ?= /usr/local$@PREFIX ?= /usr@' Makefile
# Get rid of bundled libraries
rm -f xxhash.h
ln -s /usr/include/xxhash.h

%build

%set_build_flags
export PREFIX=/usr
export VERSION=%{version}
export IS_RELEASE=1
%make_build
%install
%make_install SBINDIR=%{_sbindir} MANDIR=%{_mandir}
rm -f %{buildroot}%{_mandir}/man8/show-shared-extents*.8*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
