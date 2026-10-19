%global source0_hash 5afc8e77308451ee45ee919efee5a154ca3c153a90e2a1b58cebf7827ab88ad0
%global libhandy_version 1.5.0
%global tarball_version %(echo %{version} | tr '~' '.')
Name:          yelp
Epoch:         2
Version:       49.2
Release:        1%{?dist}
Summary:        Help browser for the GNOME desktop
License:       LicenseRef-Callaway-LGPLv2+ AND Apache-2.0 AND GPL-2.0-or-later
URL:           https://wiki.gnome.org/Apps/Yelp
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{version}.tar.xz
Requires:      yelp-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:      yelp-xsl
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(yelp-xsl)
# /oreon:deps
%description
Yelp is the help browser for the GNOME desktop. It is designed
to help you browse all the documentation on your system in
one central tool, including traditional man pages, info pages and
documentation written in DocBook.

%package libs
Summary: Libraries for yelp
%description libs
This package contains libraries used by the yelp help browser.

%package devel
Summary: Development files for yelp-libs
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
This package contains header files for the libraries in the yelp-libs package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Yelp.desktop
%files -f %{oreon_filedir}/main.list
%files -n yelp-libs -f %{oreon_filedir}/yelp-libs.list
%files -n yelp-devel -f %{oreon_filedir}/yelp-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 49.0-1
- Prepare for Oreon 11 (RP1)
