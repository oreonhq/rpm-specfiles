%global source0_hash 46ecd64142e0c7c2decac8df241b78ccae0d1b323929fb4d61aa1acc16a9ff96

%global pkgdate 20041208

Name:           sunwait
Summary:        Calculate sunrise, sunset, twilight
Version:        0.1
Release:        0.27.%{pkgdate}%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.risacher.org/sunwait/
Source0:        http://www.risacher.org/sunwait/sunwait-%{pkgdate}.tar.gz
Source1:        http://www.risacher.org/sunwait/index.html

# patch to include string.h header to avoid warning
Patch0:         sunwait-string.patch
Patch1:         sunwait-c99.patch

# As of 20-DEC-2014, the source code for the new fork sunwait4windows
# is not being provided in any archive format conducive for packaging,
# so I'm using the author's 2004 release, which still works fine.
# I'll contact Ian Craig, maintainer of the fork, about better source
# release packaging.

# Upstream notified of incorrect-fsf-address by email on 20-DEC-2014
# Requested man page of upstream by email on 25-FEB-2015

BuildRequires: make
BuildRequires:  gcc
%description
Sunwait is a small C program for calculating sunrise and sunset, as
well as civil, nautical, and astronomical twilights. It has features
that make it useful for home automation tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{pkgdate}
%patch -P0 -p1 -b .string
%patch -P1 -p1
cp -p %{SOURCE1} sunwait.html

%build
make %{?_smp_mflags} CFLAGS="${RPM_OPT_FLAGS}"

%install
install -d -m 755 ${RPM_BUILD_ROOT}/%{_bindir}
install -m 755 sunwait ${RPM_BUILD_ROOT}/%{_bindir}

%files
%license COPYING
%doc sunwait.html
%{_bindir}/sunwait

%changelog
%autochangelog
