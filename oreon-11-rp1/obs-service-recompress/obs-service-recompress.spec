%global source0_hash 6341709088e5d18cadaf8f3425a7c512f0eca7539f83885ed41c7ce5170b5efc

%define service recompress

Name:           obs-service-%{service}
Version:        0.5.2
Release:        5%{?dist}
Summary:        An OBS source service: Recompress files
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#./%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gzip
BuildRequires:  bzip2
BuildRequires:  xz
BuildRequires:  zstd
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(File::Copy)
BuildRequires:  /usr/bin/prove
Requires:       bzip2
Requires:       gzip
Requires:       xz
Requires:       zstd

BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It supports to compress, uncompress or recompress files from or to

 none : No Compression
 gz   : Gzip Compression
 bz2  : Bzip2 Compression
 xz   : XZ Compression

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Nothing to build

%install
%make_install

%check
%make_build test

%files
# In lieu of a proper license file: https://github.com/openSUSE/obs-service-recompress/issues/13
%license debian/copyright
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
%autochangelog
