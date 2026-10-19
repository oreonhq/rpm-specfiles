%global source0_hash 54061d27e32b4529dba62f7dc81c72405388ad09a5b3d8d6860d69c7206bfd97
%global _clapperenhdir %{_libdir}/clapper-0.0/enhancers
Name:           clapper-enhancers
Version:        0.10.0
Release:        1%{?dist}
Summary:        Plugins enhancing Clapper library capabilities
License:        LGPL-2.1-or-later
URL:            https://github.com/Rafostar/clapper-enhancers
Source0:        https://github.com/Rafostar/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       clapper%{_isa} >= 0.9.0
Requires:       libpeas-loader-python%{_isa}
Requires:       python3dist(yt-dlp)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(clapper-0.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
This package contains the following plugins enhancing Clapper capabilities:

* control-hub
* lbry (odysee.com)
* media-scanner
* mpris
* parser-m3u
* peertube
* recall
* utils
* yt-dlp

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%py_byte_compile %{python3} %{buildroot}%{_clapperenhdir}/yt-dlp
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
