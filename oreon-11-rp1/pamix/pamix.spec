%global source0_hash b63522889d70920d64229c66e2ab6929950476538443af297f6b242f7e9dc406
Name:           pamix
Version:        1.6
Release:        1%{?dist}
Summary:        PulseAudio terminal mixer
License:        MIT
URL:            https://github.com/patroclos/PAmix
Source0:        https://github.com/patroclos/PAmix/archive/%{version}.tar.gz
Patch0:         0001-src-pamix_ui.cpp-always-use-s-style-format-for-print.patch
Patch1:         0002-src-pamix_ui.cpp-fix-d-zu-printf-confusion.patch
Recommends:     pulseaudio
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
PAmix is a simple, terminal-based mixer for PulseAudio inspired by pavucontrol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir PAmix-%{version}
%oreon_prep
%build

%cmake -DCMAKE_BUILD_TYPE=RELEASE -DWITH_UNICODE=1
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
