%global source0_hash 4cb67c32e94749353e08ce5fefb831fefa3e7b49b863329489a84804df11449d

#%%global commit cf51167b55246b7f90ad4970d9686637e8bb0beb
#%%global commit_date 20180820
#%%global shortcommit %%(c=%%{commit};echo ${c:0:7})

Name:           grive2
Version:        0.5.3
Release:        13%{?dist}
#Release:        22.%%{commit_date}git%%{shortcommit}%%{?dist}
Summary:        Google Drive client

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://yourcmc.ru/wiki/Grive2
Source0:        https://github.com/vitalif/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
#Source0:        https://github.com/vitalif/%%{name}/archive/%%{commit}.tar.gz#/%%{name}-%%{commit}.tar.gz
# libgcrypt-config --libs or so returns the output with trailing newline, which now makes
# cmake 3.24 error. Remove traling newline using EXECUTE_PROCESS
Patch:          grive2-0.5.1-cmake-remove-newline.patch
# Add missing c++ include header
Patch:          grive2-0.5.1-cxx-missing-include.patch

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  expat-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  yajl-devel
BuildRequires:  zlib-devel
BuildRequires:  systemd
Requires(preun): systemd
Requires:       inotify-tools

%description
The purpose of this project is to provide an independent open source
implementation of Google Drive client for GNU/Linux. It uses Google Drive
REST API to talk to Google Drive service.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake3
%cmake_build

%install
%cmake_install

%preun
%systemd_user_preun grive-changes@.service
%systemd_user_preun grive-timer@.service
%systemd_user_preun grive-timer@.timer

%files
%license COPYING
%doc README.md
%{_bindir}/grive
%{_mandir}/man1/*
%{_userunitdir}/grive*
%{_libexecdir}/grive

%changelog
%autochangelog
