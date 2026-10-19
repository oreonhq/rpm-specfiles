%global source0_hash 3266d0aab787a9328bbb0ed561a371e19f1ff077273e6684ca92a90fedb2fe24
Name:           bindfs
Version:        1.18.4
Release:        1%{?dist}
Summary:        Fuse filesystem to mirror a directory
License:        GPL-2.0-or-later
URL:            http://bindfs.org/
Source0:        http://bindfs.org/downloads/bindfs-%{version}.tar.gz
Requires:       fuse3
# oreon:deps
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  valgrind
# /oreon:deps
%description
Bindfs allows you to mirror a directory and also change the the permissions in
the mirror directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
