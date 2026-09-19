%global source0_hash 2320ed019c95ca4d922968e1e1cbf0c075a914e865e3965d2bd694ca3d57cfe3

%global pkgrel    1.0.0
%global extver    pre12

Name:           imwheel
Version:        %{pkgrel}
Release:        0.19.%{extver}%{?dist}
Summary:        Mouse Event to Key Event Mapper Daemon
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Url:            http://imwheel.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{pkgrel}%{extver}.tar.gz
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
# PATCH-FIX-UPSTREAM to prevent compiler warnings
# "cast from pointer to integer of different size"
Patch1:         imwheel-intptr_t.patch
# PATCH-FIX-UPSTREAM to fix uninitialized variable hsi.
Patch2:         imwheel-fix_uninitialized_var.patch
# PATCH-FIX-OPENSUSE not to install to root only.
Patch3:         imwheel-fix_destdir.patch
# PATCH-FEATURE-OPENSUSE to put configs to /etc/ instead of /etc/X11.
Patch4:         imwheel-config_file_path.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires: make
# https://bugzilla.redhat.com/show_bug.cgi?id=1823983
Requires:       xorg-x11-fonts-75dpi

%description
A daemon for X11, which watches for mouse wheel actions and outputs them as
key presses. It can be configured separately for different windows. It also
allows input from it's own (included) gpm, or from jamd, or from XFree86 ZAxis
mouse wheel conversion.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{pkgrel}%{extver}
iconv -f iso88591 -t utf8 ChangeLog > ChangeLog
sed -i 's|AM_CONFIG_HEADER|AC_CONFIG_HEADERS|' configure.in
mv %{S:1} COPYING

%build
autoreconf -fiv
%configure --with-x
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog EMACS
%doc FREEBSD NEWS README
%license COPYING
%config(noreplace) %{_sysconfdir}/imwheelrc
%{_bindir}/imwheel
%{_mandir}/man1/imwheel.1*

%changelog
%autochangelog
