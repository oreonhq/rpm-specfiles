%global source0_hash 0e31d981891ba8d4272276991665e025704f2533fa8e169ffb7e3dc9b7d0f22f

Summary: Bluecurve icon theme
Name: bluecurve-icon-theme
Version: 8.0.2
Release: 35%{?dist}
BuildArch: noarch
License: GPL-2.0-or-later
# There is no official upstream yet
Source0: %{name}-%{version}.tar.bz2
URL: http://www.redhat.com

Requires: system-logos
Requires: bluecurve-cursor-theme
Requires(post): coreutils

# we require XML::Parser for our in-tree intltool
BuildRequires: gcc
BuildRequires: perl(XML::Parser)
BuildRequires: perl(Getopt::Long)
BuildRequires: make

%description
This package contains Bluecurve style icons.

%package -n bluecurve-cursor-theme
Summary: Bluecurve cursor theme

%description -n bluecurve-cursor-theme
This package contains Bluecurve style cursors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
make

%install
%make_install

# These are empty
rm -f ChangeLog NEWS README

touch %{buildroot}%{_datadir}/icons/Bluecurve/icon-theme.cache

# The upstream packages may gain po files at some point in the near future
# %find_lang %{name} || touch %{name}.lang

%files
%doc AUTHORS
%license COPYING
%{_datadir}/icons/Bluecurve/index.theme
%{_datadir}/icons/Bluecurve/16x16
%{_datadir}/icons/Bluecurve/20x20
%{_datadir}/icons/Bluecurve/24x24
%{_datadir}/icons/Bluecurve/32x32
%{_datadir}/icons/Bluecurve/36x36
%{_datadir}/icons/Bluecurve/48x48
%{_datadir}/icons/Bluecurve/64x64
%{_datadir}/icons/Bluecurve/96x96
%ghost %{_datadir}/icons/Bluecurve/icon-theme.cache

%files -n bluecurve-cursor-theme
%doc AUTHORS
%license COPYING
%dir %{_datadir}/icons/Bluecurve
%{_datadir}/icons/Bluecurve/Bluecurve.cursortheme
%{_datadir}/icons/Bluecurve/cursors
%{_datadir}/icons/Bluecurve-inverse
%{_datadir}/icons/LBluecurve
%{_datadir}/icons/LBluecurve-inverse

%changelog
%autochangelog
