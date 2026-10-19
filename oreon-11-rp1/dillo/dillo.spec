%global source0_hash 4282e4bc0de229d23cd3e36dda81bba9267709c76d59d592c429d4532cf1d451
%bcond_without tests
%define _legacy_common_support 1
Name:           dillo
Version:        3.3.0
Release:        1%{?dist}
Summary:        A multi-platform graphical web browser
License:        GPL-3.0-or-later
URL:            https://dillo-browser.github.io/
Source0:        https://github.com/%{name}-browser/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with tests}
%endif
Requires:       hicolor-icon-theme
Requires:       wget%{?_isa}
Provides:       webclient
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  cmake(NanoSVG)
BuildRequires:  cmake(WebP)
BuildRequires:  cmake(fltk)
BuildRequires:  cmake(libjpeg-turbo)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xwd
BuildRequires:  xwininfo
# /oreon:deps
%description
Dillo is a multi-platform graphical web browser, known for its speed and small
footprint, that is developed with a focus on personal security and privacy. It
is built with the FLTK 1.3 GUI toolkit.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
autoreconf -vif

%build

%configure \
    --disable-dependency-tracking \
    --enable-ipv6 \
    --enable-tls \
    %if %{with tests}
    --enable-html-tests \
    %endif
    %{nil}
%make_build
%install
%make_install
rm -f doc/Makefile*
rm -fr %{buildroot}%{_datadir}/doc/%{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
