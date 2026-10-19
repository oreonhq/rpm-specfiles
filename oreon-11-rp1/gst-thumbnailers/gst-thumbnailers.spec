%global source0_hash fdf3d96fa630ab1cd8b966ffabfd86e68548c005a6667772b7f00dd781c50ad3
%global upstream_version %%(echo %{version} | tr '~' '.')
Name:           gst-thumbnailers
Version:        1.1.0
Release:        1%{?dist}
Summary:        GStreamer Thumbnailers
SourceLicense:  GPL-3.0-or-later
License:        %{shrink:
    GPL-3.0-or-later
    AND Apache-2.0 WITH LLVM-exception
    AND MIT
    AND (Apache-2.0 OR MIT)
    AND (BSD-3-Clause OR Apache-2.0)
    AND (Unlicense OR MIT)
    AND (Zlib OR Apache-2.0 OR MIT)
}
URL:            https://gitlab.gnome.org/GNOME/gst-thumbnailers
Source0:        https://gitlab.gnome.org/GNOME/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          0001-meson-adapt-for-RPM-package-build-environment.patch
Patch:          0002-cargo-drop-benchmarks-and-benchmark-only-dependencie.patch
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  meson
BuildRequires:  pkgconfig(glycin-2)
BuildRequires:  pkgconfig(gstreamer-1.0)
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gst-thumbnailers-%{upstream_version} -p1

%build

%meson
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%meson_install
%oreon_autofiles main

%check

%ifnarch s390x
%meson_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
