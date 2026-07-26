%global source0_hash 27809aa91b7b9b7d0810e5329614bf80af2c48e917781e682a3fbcf61fa274da

%define _legacy_common_support 1

Name:           duperemove
Version:        0.15.2
Release:        3%{?dist}
Summary:        Tools for deduping file systems
License:        GPL-2.0-only
URL:            https://github.com/markfasheh/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  libgcrypt-devel
BuildRequires:  xxhash-devel
BuildRequires:  libatomic
BuildRequires:  libuuid-devel
BuildRequires:  gcc
BuildRequires:  make

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
# This binary doesn't exist anymore
rm -f %{buildroot}%{_mandir}/man8/show-shared-extents*.8*

%files
%doc README.md
%license LICENSE
%{_mandir}/man8/btrfs-extent-same*.8*
%{_mandir}/man8/duperemove*.8*
%{_mandir}/man8/hashstats*.8*
%{_bindir}/btrfs-extent-same
%{_bindir}/duperemove
%{_bindir}/hashstats
%{_datadir}/zsh/site-functions/_duperemove

%changelog
%autochangelog
