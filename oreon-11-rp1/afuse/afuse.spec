%global source0_hash c6e0555a65d42d3782e0734198bbebd22486386e29cb00047bc43c3eb726dca8

Name:		afuse
Summary:	An automounter implemented with FUSE
Version:	0.4.1
Release:	30%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Source0:	https://afuse.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		afuse-0.4.1-strcpy-buffer-overflow-fix.patch
URL:		https://github.com/pcarrier/afuse/
BuildRequires:	gcc
BuildRequires:	fuse-devel
BuildRequires:	make

%description
Afuse is an automounting file system implemented in user-space using FUSE.
Afuse currently implements the most basic functionality that can be expected
by an automounter; that is it manages a directory of virtual directories. If
one of these virtual directories is accessed and is not already automounted,
afuse will attempt to mount a filesystem onto that directory. If the mount
succeeds the requested access proceeds as normal, otherwise it will fail
with an error.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .strcpy-buffer-overflow-fix

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/afuse
%{_bindir}/afuse-avahissh

%changelog
%autochangelog
