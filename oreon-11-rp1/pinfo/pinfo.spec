%global source0_hash 9dc5e848a7a86cb665a885bc5f0fdf6d09ad60e814d75e78019ae3accb42c217
Name:    pinfo
Version: 0.6.13
Release:        10%{?dist}
Summary:        An info file viewer
License: GPL-2.0-only
URL:    https://github.com/baszoetekouw/pinfo
Source0:        https://github.com/baszoetekouw/pinfo/archive/refs/tags/v0.6.13.tar.gz#/pinfo-0.6.13.tar.gz
Patch1: pinfo-0.6.9-infopath.patch
Patch2: pinfo-0.6.9-xdg.patch
Patch3: pinfo-0.6.10-man.patch
Patch4: pinfo-0.6.13-fnocommon.patch
Patch5: pinfo-0.6.13-gccwarn.patch
Patch6: pinfo-0.6.13-nogroup.patch
Patch7: pinfo-0.6.13-stringop-overflow.patch
Patch8: pinfo-configure-c99.patch
Requires: xdg-utils
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  texinfo
# /oreon:deps
%description
Pinfo is an info file (or man page) viewer with a user interface
similar to the Lynx Web browser's interface.  Pinfo supports searching
using regular expressions, and is based on the ncurses library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure --without-readline
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.13-10
- Prepare for Oreon 11 (RP1)
