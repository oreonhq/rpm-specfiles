%global source0_hash cff5f83b85a21e0c5c8c8eecbd552090bb75d8ac59e27b0bae48046f9cb5a44a
Name:		hsetroot
Version:	1.0.5
Release:        1%{?dist}
Summary:        Yet another wallpaper application
License:	GPL-2.0-only
URL:		https://github.com/himdel/hsetroot
Source0:        https://github.com/himdel/hsetroot/archive/refs/tags/%{version}.tar.gz
Patch0: 1.0.5-add-destdir.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
# /oreon:deps
%description
hsetroot is an imlib2-based wallpaper composer, which also works with
compositors like compton or picom. It has a lot of options
like rendering gradients, solids, images but it also allows you
to perform manipulations on those things, or chain them together.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Make sure that executables don't get stripped
sed -i -e 's/install -st/install -t/' Makefile

%build

%make_build
%install
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
