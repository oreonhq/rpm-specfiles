%global source0_hash 48a295f3b3a917cc851d1aa8b185c09fde3a1b1e741fc57d7fa96b3671271630

%bcond_without tests

%global appstream_id io.github.syllo.nvtop

Name:           nvtop
Version:        3.3.2
Release:        %autorelease
Summary:        GPU process monitoring for various devices

# BSD-3-Clause: include/ini.h, src/ini.c
# LGPL-2.1-or-later: include/list.h - this combines into GPL-3.0-or-later
# some cmake modules are BSD-3-Clause or MIT but those are not shipped out
License:        GPL-3.0-or-later and BSD-3-Clause
URL:            https://github.com/Syllo/nvtop
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.10
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ncursesw)
%if %{with tests}
%if 0%{?el8}
# EL8 gtest doesn't ship pkgconfig
BuildRequires:  gtest-devel
%else
BuildRequires:  pkgconfig(gtest)
%endif
%endif
Requires:       hicolor-icon-theme

%description
Nvtop stands for Neat Videocard TOP, a (h)top like task monitor for various GPUs
including AMD, Apple, Huawei, Intel, NVIDIA and Qualcomm. It can handle multiple
GPUs and print information about them in a htop familiar way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%if %{with tests}
%cmake -DBUILD_TESTING=ON
%else
%cmake
%endif
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appstream_id}.metainfo.xml
%if %{with tests}
%ctest
%endif

%files
%license COPYING
%doc README.markdown
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{appstream_id}.metainfo.xml

%changelog
%autochangelog
