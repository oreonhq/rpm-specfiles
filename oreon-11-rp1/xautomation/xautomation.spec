%global source0_hash ee8f2c61165da682f58371a51cfc263d6e54609b614e712320b0987779d95f0d

Name:           xautomation
Version:        1.09
Release:        15%{?dist}
Summary:        Tools to automate tasks in X, even detecting on screen images

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://hoopajoo.net/projects/xautomation.html
Source0:        http://hoopajoo.net/static/projects/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel

%description
Control X from the command line for scripts, and do "visual scraping" to find
things on the screen. The control interface allows mouse movement, clicking,
button up/down, key up/down, etc, and uses the XTest extension so you don't have
the annoying problems that xse has when apps ignore sent events. The visgrep
program find images inside of images and reports the coordinates, allowing
programs to find buttons, etc, on the screen to click on.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/pat2ppm
%{_bindir}/patextract
%{_bindir}/png2pat
%{_bindir}/rgb2pat
%{_bindir}/visgrep
%{_bindir}/xmousepos
%{_bindir}/xte
%{_mandir}/man1/*.1.*
%{_mandir}/man7/*.7.*

%changelog
%autochangelog
