%global source0_hash d0f47500192605d01b5a2569c605e51ed319f557d24cfcbcb23a26d51d6138c9

Name:           mktorrent
Version:        1.1
Release:        21%{?dist}
Summary:        Command line utility to create BitTorrent metainfo files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/Rudde/mktorrent
Source0:        https://github.com/Rudde/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  openssl-devel

%description
Command line utility to create BitTorrent metainfo files.
See --help option for mktorrent command for details on usage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Use openssl sha1 routine rather than included one.
rm sha1.c sha1.h

%build
%ifarch alpha ia64 ppc64 s390x sparc64 x86_64
%global largefiles 0
%else
%global largefiles 1
%endif

make %{?_smp_mflags} USE_LARGE_FILES=%{largefiles}  USE_PTHREADS=1 \
       USE_OPENSSL=1 USE_LONG_OPTIONS=1  CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
make install USE_LARGE_FILES=%{largefiles}  USE_PTHREADS=1 \
       USE_OPENSSL=1 USE_LONG_OPTIONS=1 CFLAGS="%{optflags}" \
       PREFIX=%{buildroot}%{_prefix} INSTALL="install -p"

%files
%{_bindir}/mktorrent
%doc COPYING README

%changelog
%autochangelog
