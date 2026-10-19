%global source0_hash bf959a1ced3cde8176a7ff50ad358ee98e93301ac068581a8b2617c5b83afcb3
Name:		libva-utils
Version:	2.24.0
Release:        1%{?dist}
Summary:        Tools for VAAPI (including vainfo)
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:		https://github.com/intel/libva-utils
Source0:        https://github.com/intel/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%{!?_without_wayland:
}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  wayland-devel
# /oreon:deps
%description
The libva-utils package contains tools that are provided as part
of libva, including the vainfo tool for determining what (if any)
libva support is available on a system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?pre_release}

%build

%meson \
%{?_with_tests: -Dtests=true} \
%{?_without_wayland: -Dwayland=false}
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
