%global source3_hash 8d325ff6a7d606d3359f75445522bf7b66d5961a1030e9f1b1763780ec7b8230
%global source2_hash c6a510f6fab1ec094fc91f3711ca4b656020825d4da4c7982450e037a56e1d75
%global source1_hash 5df5d49d129ed7aac755293ba6c8fc1316a661912ea80de68446384199a418e9
%global source0_hash cf18a8c52138a38541be3478af446c06048108729d7e18476492d62d54baabc4
Name:           libeatmydata
Version:        131
Release:        1%{?dist}
Group:          Development/Tools
License:        GPL-3.0-only
Summary:        Library and utilities designed to disable fsync and friends
Source0:        https://www.flamingspork.com/projects/libeatmydata/%{name}-%{version}.tar.gz
Source1:        https://www.flamingspork.com/projects/libeatmydata/%{name}-%{version}.tar.gz.asc
Source2:        https://flamingspork.com/stewart.gpg
Source3:        https://salsa.debian.org/debian/libeatmydata/-/raw/048c4ea3/debian/eatmydata.1
URL:            https://www.flamingspork.com/projects/libeatmydata/
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  strace
# /oreon:deps
%description
This package contains a small LD_PRELOAD library (libeatmydata) and a couple 
of helper utilities (eatmydata) designed to transparently disable fsync and
friends (like open(O_SYNC)). This has two side-effects: making software that
writes data safely to disk a lot quicker and making this software no longer 
crash safe.

%package -n eatmydata
Summary: Utility to disable fsync() and friends for the command specified 
Requires: %{name}
%description -n eatmydata
The eatmydata script does the heavy lifting of LD_PRELOAD for the command
specified. You can also symlink a command to the eatmydata wrapper and the
wrapper will find the command in PATH and then execute it after setting up
the libeatmydata LD_PRELOAD

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%configure --enable-static=no
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -m444 -p %{SOURCE3} %{buildroot}%{_mandir}/man1/
%oreon_autofiles eatmydata usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__make} check
%files -f %{oreon_filedir}/main.list
%files -n eatmydata -f %{oreon_filedir}/eatmydata.list

%changelog

%autochangelog
