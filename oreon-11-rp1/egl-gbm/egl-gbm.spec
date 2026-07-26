%global source0_hash 2669f59a22e1d41d73b02866f3ed35e55b50c6afc70f078bcff97bfef67736ad

%global commit0 b24587d4871a630d05e9e26da94c95e6ce4324f2
%global date 20240919
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

Name:           egl-gbm
Epoch:          2
Version:        1.1.3%{!?tag:^%{date}git%{shortcommit0}}
Release:        %autorelease
Summary:        Nvidia egl gbm libary
License:        MIT
URL:            https://github.com/NVIDIA/%{name}

%if 0%{?tag:1}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %url/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  eglexternalplatform-devel
BuildRequires:  libdrm-devel
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libgbm-devel

%description
The GBM EGL external platform library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

%build
%meson
%meson_build

%install
%meson_install
# Delete unversioned .so
rm %{buildroot}%{_libdir}/libnvidia-egl-gbm.so

%files
%license COPYING
%{_libdir}/libnvidia-egl-gbm.so.1*
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json

%changelog
%autochangelog
