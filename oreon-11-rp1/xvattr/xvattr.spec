%global source0_hash 1cedc0b4795e6f4234b1d52172f74d7163ecb8142fbb35dc86c905df5478d8fa

%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} > 36)
%global gxvattr 0
%else
%global gxvattr 1
%endif

Summary:    Utility for getting and setting Xv attributes
Name:       xvattr
Version:    1.3
Release:    54%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        http://www.dtek.chalmers.se/groups/dvd/
Source:     http://ajax.fedorapeople.org/%{name}/%{name}-%{version}.tar.gz
# Normalize documentation encoding
Patch0:     xvattr-1.3-Convert-documentation-to-UTF-8.patch
# Do not loose system CFLAGS for gxvattr
Patch1:     xvattr-1.3-Use-GTK_CFLAGS-properly.patch
# Allow to disable GTK tools
Patch2:     xvattr-1.3-Make-GTK-tools-optional.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
%if %{gxvattr}
BuildRequires:  gtk+-devel
%endif
BuildRequires:  libX11-devel
BuildRequires:  libXv-devel
BuildRequires:  make
BuildRequires:  perl-podlators

%description
This program is used for getting and setting Xv attributes such as
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY.

%package -n gxvattr
Summary: GTK1-based GUI for Xv attributes

%description -n gxvattr
GTK1-based GUI for inspecting and setting Xv attributes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf --install --force

%build
%configure \
%if %{gxvattr}
    --enable-gtk
%else
    --disable-gtk
%endif
%{make_build}

%install
%{make_install}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/xvattr
%{_mandir}/man1/*

%if %{gxvattr}
%files -n gxvattr
%license COPYING
%{_bindir}/gxvattr
%endif

%changelog
%autochangelog
