%global source0_hash 9e0baa665c86e7afdc86b59627a50e6f4f1f87cfa31f1fc1e56fb7b1dbd678bf
Name:           iio-sensor-proxy
Version:        3.9
Release:        1%{?dist}
Summary:        IIO accelerometer sensor to input device proxy
License:        GPL-3.0-or-later
URL:            https://gitlab.freedesktop.org/hadess/iio-sensor-proxy
Source0:        https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/-/archive/3.9/iio-sensor-proxy-3.8.tar.bz2
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  python3-dbusmock
BuildRequires:  systemd
BuildRequires:  umockdev
# /oreon:deps
%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
License:        GFDL-1.1-or-later
BuildArch:      noarch
%description docs
This package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir iio-sensor-proxy-%{version}-0085ddf8ecb173a1c5fcf2344aa40e561125354f
%oreon_prep
%build

%meson -Dgtk_doc=true -Dgtk-tests=false -Dssc=disabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n iio-sensor-proxy-docs -f %{oreon_filedir}/iio-sensor-proxy-docs.list

%changelog

%autochangelog
