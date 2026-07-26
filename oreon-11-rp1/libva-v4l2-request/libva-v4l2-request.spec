%global source0_hash 92b523050561d64f7b6016edb53ca00524805f9f31a8b566baf457bbb15716fa

%global commit0 a3c2476de19e6635458273ceeaeceff124fabd63
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20190517

Name:           libva-v4l2-request
Version:        1.0.0
Release:        18.%{?date0}git%{?shortcommit0}%{?dist}
Summary:        VA-API Backend using v4l2-request API

# Automatically converted from old format: LGPLv2+ and MIT - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:            https://github.com/bootlin/libva-v4l2-request
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# https://github.com/bootlin/libva-v4l2-request/pull/38
Patch3:         https://patch-diff.githubusercontent.com/raw/bootlin/libva-v4l2-request/pull/38.patch
Patch4:         0001-Add-missing-include.patch
Patch5:         0001-Drop-headers-from-pre-upstream-ctrls.patch

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  libva-devel
BuildRequires:  libdrm-devel

%description
This VA-API backend is designed to work with the Linux Video4Linux2
Request API that is used by a number of video codecs drivers, including
the Video Engine found in most Allwinner SoCs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}
# Not yet adapted to upstream kernel
rm -r src/h265.c
sed -i -e "/'h265.c'/d" src/meson.build

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING COPYING.LGPL COPYING.MIT
%doc AUTHORS CREDITS README.md
%{_libdir}/dri/v4l2_request_drv_video.so

%changelog
%autochangelog
