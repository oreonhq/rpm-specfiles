%global source0_hash 0e31d981891ba8d4272276991665e025704f2533fa8e169ffb7e3dc9b7d0f22f
Summary:        Bluecurve icon theme
Name: bluecurve-icon-theme
Version: 8.0.2
Release:        35%{?dist}
BuildArch: noarch
License: GPL-2.0-or-later
Source0:        %{name}-%{version}.tar.bz2
URL: http://www.redhat.com
Requires: system-logos
Requires: bluecurve-cursor-theme
Requires(post): coreutils
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(XML::Parser)
# /oreon:deps
%description
This package contains Bluecurve style icons.

%package -n bluecurve-cursor-theme
Summary: Bluecurve cursor theme
%description -n bluecurve-cursor-theme
This package contains Bluecurve style cursors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
make
%install
%make_install
rm -f ChangeLog NEWS README
touch %{buildroot}%{_datadir}/icons/Bluecurve/icon-theme.cache
%oreon_autofiles bluecurve-cursor-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bluecurve-cursor-theme -f %{oreon_filedir}/bluecurve-cursor-theme.list

%changelog

%autochangelog
