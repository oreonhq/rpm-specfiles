%global source0_hash 0b0cc956dec5b583f3e6d95c0172db7da4a4bebc2a51f0036c7257517c803dc2
Name:           WindowMaker-extra
Version:        0.1
Release:        1%{?dist}
Summary:        Extra icons and themes for WindowMaker
License:        GPL-2.0-only
URL:            http://www.windowmaker.org
Source0:        http://windowmaker.org/pub/source/release/WindowMaker-extra-0.1.tar.gz
BuildArch:      noarch
Requires:       WindowMaker
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
This is the extra data package for Window Maker. For now it only contains some
icons and a few themes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
