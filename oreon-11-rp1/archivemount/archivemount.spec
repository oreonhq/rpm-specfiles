%global source0_hash c529b981cacb19541b48ddafdafb2ede47a40fcaf16c677c1e2cd198b159c5b3

Name:          archivemount
Version:       0.9.1
Release:       16%{?dist}
Summary:       FUSE based filesystem for mounting compressed archives

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.cybernoia.de/software/archivemount/
Source0:       http://www.cybernoia.de/software/archivemount/%{name}-%{version}.tar.gz

Requires:      fuse
BuildRequires: gcc
BuildRequires: fuse-devel
BuildRequires: libarchive-devel
BuildRequires: automake
BuildRequires: make

%description
Archivemount is a piece of glue code between libarchive and FUSE. It can be
used to mount a (possibly compressed) archive (as in .tar.gz or .tar.bz2)
and use it like an ordinary filesystem.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --enable-debug
%make_build

%install
rm -rf $RPM_BUILD_ROOT
rm -f archivemount.1
%make_install

%files
%doc CHANGELOG README
%license COPYING
%{_mandir}/*/*
%{_bindir}/archivemount

%changelog
%autochangelog
