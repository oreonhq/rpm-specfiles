%global source0_hash 59b30378127dde8e0af92de1a23ebcee706820a862581a603543a99c357bcecb
Name:           hardinfo2
Version:        2.3.1
Release:        1%{?dist}
Summary:        System Information and Benchmark for Linux Systems
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-only
URL:            https://github.com/hardinfo2/hardinfo2
Source0:        https://github.com/%{name}/%{name}/archive/release-%{version}/%{name}-release-%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/glslangValidator
BuildRequires:  /usr/bin/glslc
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libdecor-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-png)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(x11)
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
Hardinfo2 is based on hardinfo, which have not been released >10 years.
Hardinfo2 is the reboot that was needed.

Hardinfo2 offers System Information and Benchmark for Linux Systems. It is able
to obtain information from both hardware and basic software. It can benchmark
your system and compare to other machines online.

Features include:
- Report generation (in either HTML or plain text)
- Online Benchmarking - compare your machine against other machines

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir hardinfo2-release-%{version}
%oreon_prep
%build

%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
