%global source0_hash 74302eac477ca08fb2b42b9f154cc870593aec8beab308676e4373a5e4ca2102

Name:           shntool
Version:        3.0.10
Release:        %autorelease
Summary:        A multi-purpose WAVE data processing and reporting utility

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://shnutils.freeshell.org/shntool/
Source0:        http://shnutils.freeshell.org/shntool/dist/src/%{name}-%{version}.tar.gz

# Patches are from Debian
# https://sources.debian.org/patches/shntool/3.0.10-1/
Patch0:         large-size.patch
Patch1:         large-times.patch
Patch2:         no-cdquality-check.patch
Patch3:         https://github.com/max619/shntool/commit/cfd06e4edecdca2013e0fe04db135fd110a68203.patch
Patch4:         0001-fix-valid-wavepack-header-versions.patch
Patch5:         gcc-15-fixes.patch

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc

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

%files
%doc AUTHORS ChangeLog NEWS README
%doc doc/*
%license COPYING
%{_bindir}/shn*
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
