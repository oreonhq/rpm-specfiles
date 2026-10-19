%global source0_hash 393bb8352cf72066cb2644d41c194f4c97f7341d8d65961deefe55cde29f94d0
Name:           exif
Version:        0.6.22
Release:        1%{?dist}
Summary:        Utility to show EXIF information hidden in JPEG files
Summary(fr):    Outil pour afficher les informations EXIF masquées dans les fichiers JPEG
License:        LGPL-2.1-or-later
URL:            http://libexif.sourceforge.net/
Source0:        https://github.com/libexif/exif/archive/exif-0_6_22-release/%{name}-%{version}.tar.gz
Patch0:         f6334d9d32437ef13dc902f0a88a2be0063d9d1c.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libexif-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  popt-devel
# /oreon:deps
%description
Small command-line utility to show EXIF information hidden
in JPEG files.

%description -l fr
Petit utilitaire en ligne de commande pour afficher les informations
EXIF masquées dans les fichiers JPEG.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qnexif-exif-0_6_22-release

%patch -P0 -p1

# Convert to UTF8 AUTHORS doc file :
iconv -f iso-8859-1 -t utf8 AUTHORS >AUTHORS.tmp
touch -r AUTHORS AUTHORS.tmp
mv AUTHORS.tmp AUTHORS

%build

autoreconf -if
%configure
%make_build
%install
%make_install
%find_lang %{name}
%ifnarch s390x
%oreon_autofiles main

%check

make check
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
