%global source0_hash a52db2697f433621346dc4af59952728192878471e29f46b4b4221b7d5623a86
Name:           xarchiver
Version:        0.5.4.27
Release:        1%{?dist}
Summary:        Archive manager for Xfce
License:        GPL-2.0-or-later AND BSD-4-Clause-UC AND (LGPL-2.1-or-later OR AFL-2.0)
URL:            https://github.com/ib/xarchiver
Source0:        https://github.com/ib/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Recommends:     bzip2, p7zip-plugins, unzip, xdg-utils, xz
Suggests:       arj, binutils, cpio, lz4, lzop, ncompress, unar, zstd, zip
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%description
Xarchiver is a lightweight GTK frontend for manipulating 7z, arj, bzip2,
gzip, iso, rar, lha, tar, zip, RPM and deb files. It allows you to create
archives and add, extract, and delete files from them. Password protected
archives in the arj, 7z, rar, and zip formats are supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
rm %{buildroot}%{_docdir}/%{name}/ChangeLog
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
