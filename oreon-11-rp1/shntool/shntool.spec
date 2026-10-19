%global source0_hash 74302eac477ca08fb2b42b9f154cc870593aec8beab308676e4373a5e4ca2102
Name:           shntool
Version:        3.0.10
Release:        1%{?dist}
Summary:        A multi-purpose WAVE data processing and reporting utility
License:        GPL-2.0-or-later
URL:            http://shnutils.freeshell.org/shntool/
Source0:        http://shnutils.freeshell.org/shntool/dist/src/%{name}-%{version}.tar.gz
Patch0:         large-size.patch
Patch1:         large-times.patch
Patch2:         no-cdquality-check.patch
Patch3:         https://github.com/max619/shntool/commit/cfd06e4edecdca2013e0fe04db135fd110a68203.patch
Patch4:         0001-fix-valid-wavepack-header-versions.patch
Patch5:         gcc-15-fixes.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
A multi-purpose WAVE data processing and reporting utility. File
formats are abstracted from its core, so it can process any file that contains
WAVE data, compressed or not - provided there exists a format module to handle
that particular file type. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fiv

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
