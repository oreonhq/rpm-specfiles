%global source0_hash 48a295f3b3a917cc851d1aa8b185c09fde3a1b1e741fc57d7fa96b3671271630
%bcond_without tests
%global appstream_id io.github.syllo.nvtop
Name:           nvtop
Version:        3.3.2
Release:        1%{?dist}
Summary:        GPU process monitoring for various devices
License:        GPL-3.0-or-later and BSD-3-Clause
URL:            https://github.com/Syllo/nvtop
Source0:        https://github.com/Syllo/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with tests}
%if 0%{?el8}
%else
%endif
%endif
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ncursesw)
# /oreon:deps
%description
Nvtop stands for Neat Videocard TOP, a (h)top like task monitor for various GPUs
including AMD, Apple, Huawei, Intel, NVIDIA and Qualcomm. It can handle multiple
GPUs and print information about them in a htop familiar way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with tests}
%cmake -DBUILD_TESTING=ON
%else
%cmake
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appstream_id}.metainfo.xml
%if %{with tests}
%ctest
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
