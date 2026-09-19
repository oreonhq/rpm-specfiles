%global source0_hash f73d1ec1a962822e681c2eefa77d9843a02ee0c63196ba0c1181cc1da016a76c

Name:           radeontool
Version:        1.6.3
Release:        29%{?dist}
Summary:        Backlight and video output configuration tool for radeon cards

License:        zlib
URL:            http://people.freedesktop.org/~airlied/radeontool/
Source0:        http://people.freedesktop.org/~airlied/radeontool/radeontool-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libpciaccess-devel
# radeontool is included in (some of) these pm-utils releases
Conflicts:      pm-utils <= 0.99.3-11

%description
radeontool is used for debugging radeon related issues. In the past it has
been used for backlight control, but this should no longer be required.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/radeontool
%{_bindir}/avivotool
%{_bindir}/radeonreg

%changelog
%autochangelog
