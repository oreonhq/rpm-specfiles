%global source0_hash fa7ff29847b55010fbbb775b35382f97f29b7b97abe9a2f6fb3e22b36db5440a

#global pre_release .pre1

Name:		libva-utils
Version:	2.23.0
Release:	2%{?dist}
Summary:	Tools for VAAPI (including vainfo)
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:		https://github.com/intel/libva-utils
Source0:	%{url}/archive/%{version}%{?pre_release}/%{name}-%{version}%{?pre_release}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++

BuildRequires:	libXext-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libdrm-devel
BuildRequires:  libva-devel
%{!?_without_wayland:
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(wayland-client) >= 1
BuildRequires:  pkgconfig(wayland-scanner) >= 1
}

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

%files
%license COPYING
%doc CONTRIBUTING.md README.md
%{_bindir}/av1encode
%{_bindir}/vainfo
%{_bindir}/loadjpeg
%{_bindir}/jpegenc
%{_bindir}/avcenc
%{_bindir}/avcstreamoutdemo
%{_bindir}/h264encode
%{_bindir}/hevcencode
%{_bindir}/mpeg2vldemo
%{_bindir}/mpeg2vaenc
%{_bindir}/putsurface
%{_bindir}/sfcsample
%{?_with_tests:%{_bindir}/test_va_api}
%{_bindir}/vacopy
%{_bindir}/vavpp
%{_bindir}/vp8enc
%{_bindir}/vp9enc
%{_bindir}/vpp3dlut
%{_bindir}/vppblending
%{_bindir}/vppchromasitting
%{_bindir}/vppdenoise
%{_bindir}/vpphdr_tm
%{_bindir}/vppscaling_csc
%{_bindir}/vppscaling_n_out_usrptr
%{_bindir}/vppsharpness
%{!?_without_wayland:%{_bindir}/putsurface_wayland}

%changelog
%autochangelog
