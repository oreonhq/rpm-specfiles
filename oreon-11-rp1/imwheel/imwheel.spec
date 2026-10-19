%global source1_hash edaef632cbb643e4e7a221717a6c441a4c1a7c918e6e4d56debc3d8739b233f6
%global source0_hash 2320ed019c95ca4d922968e1e1cbf0c075a914e865e3965d2bd694ca3d57cfe3
%global pkgrel    1.0.0
%global extver    pre12
Name:           imwheel
Version:        %{pkgrel}
Release:        1%{?dist}
Summary:        Mouse Event to Key Event Mapper Daemon
License:        GPL-2.0-or-later
Url:            http://imwheel.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}%{extver}.tar.gz
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Patch1:         imwheel-intptr_t.patch
Patch2:         imwheel-fix_uninitialized_var.patch
Patch3:         imwheel-fix_destdir.patch
Patch4:         imwheel-config_file_path.patch
Requires:       xorg-x11-fonts-75dpi
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
