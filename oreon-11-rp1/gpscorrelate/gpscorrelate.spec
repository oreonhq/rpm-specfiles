%global source0_hash 006ad389e3579b2e3ed3046902ed577ecc8253ab159f9d4034131dd38f827281
Name:           gpscorrelate
Version:        2.1
Release:        1%{?dist}
Summary:        A GPS photo correlation / geotagging tool
License:        GPL-2.0-or-later
URL:            https://dfandrich.github.io/gpscorrelate/
VCS:            https://github.com/dfandrich/gpscorrelate
Source0:        https://github.com/dfandrich/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
Gpscorrelate adds coordinates to the exif data of jpeg pictures based on a gpx
track file. The correlation is done by comparing the timestamp of the images
with the timestamp of the gps coordinates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build prefix=%{_prefix} CFLAGS="%{optflags}" OFLAGS="%{optflags}" docdir="%{_pkgdocdir}"
%install
%make_install prefix=%{_prefix}
make install-desktop-file DESTDIR=%{buildroot} prefix=%{_prefix}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
