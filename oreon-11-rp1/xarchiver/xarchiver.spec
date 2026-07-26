%global source0_hash 58e4fb2c1fb8421573a31cf3b4dfec301076d61f48ac5720df632986c87e9573

Name:           xarchiver
Version:        0.5.4.26
Release:        2%{?dist}
Summary:        Archive manager for Xfce

License:        GPL-2.0-or-later AND BSD-4-Clause-UC AND (LGPL-2.1-or-later OR AFL-2.0)
URL:            https://github.com/ib/xarchiver
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libxml2-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk-doc
BuildRequires:  desktop-file-utils

# Using Debian's list of recommendations vs suggestions:
# https://salsa.debian.org/debian/xarchiver/blob/master/debian/control
%if 0%{?rhel} && 0%{?rhel} < 8
Requires:       arj, binutils, bzip2, cpio, gzip, xdg-utils, tar, unzip, zip
%else
Recommends:     bzip2, p7zip-plugins, unzip, xdg-utils, xz
Suggests:       arj, binutils, cpio, lz4, lzop, ncompress, unar, zstd, zip
%endif

%description
Xarchiver is a lightweight GTK frontend for manipulating 7z, arj, bzip2,
gzip, iso, rar, lha, tar, zip, RPM and deb files. It allows you to create
archives and add, extract, and delete files from them. Password protected
archives in the arj, 7z, rar, and zip formats are supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# remove useless docs
rm %{buildroot}%{_docdir}/%{name}/ChangeLog

%files -f %{name}.lang
%license COPYING
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/%{name}/
%{_libexecdir}/thunar-archive-plugin/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
