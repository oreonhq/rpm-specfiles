%global source0_hash 4cb67c32e94749353e08ce5fefb831fefa3e7b49b863329489a84804df11449d
Name:           grive2
Version:        0.5.3
Release:        1%{?dist}
Summary:        Google Drive client
License:        GPL-2.0-only
URL:            http://yourcmc.ru/wiki/Grive2
Source0:        https://github.com/vitalif/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch:          grive2-0.5.1-cmake-remove-newline.patch
Patch:          grive2-0.5.1-cxx-missing-include.patch
Requires(preun): systemd
Requires:       inotify-tools
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  systemd
BuildRequires:  yajl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The purpose of this project is to provide an independent open source
implementation of Google Drive client for GNU/Linux. It uses Google Drive
REST API to talk to Google Drive service.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake3
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%preun

%systemd_user_preun grive-changes@.service
%systemd_user_preun grive-timer@.service
%systemd_user_preun grive-timer@.timer
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
