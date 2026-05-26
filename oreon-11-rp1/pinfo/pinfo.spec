# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 9dc5e848a7a86cb665a885bc5f0fdf6d09ad60e814d75e78019ae3accb42c217
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:    pinfo
Version: 0.6.13
Release: 10%{?dist}
Summary: An info file viewer
License: GPL-2.0-only

URL:    https://github.com/baszoetekouw/pinfo
Source:        https://github.com/baszoetekouw/pinfo/archive/refs/tags/v0.6.13.tar.gz

Patch1: pinfo-0.6.9-infopath.patch
Patch2: pinfo-0.6.9-xdg.patch
Patch3: pinfo-0.6.10-man.patch
Patch4: pinfo-0.6.13-fnocommon.patch
Patch5: pinfo-0.6.13-gccwarn.patch
Patch6: pinfo-0.6.13-nogroup.patch
Patch7: pinfo-0.6.13-stringop-overflow.patch
Patch8: pinfo-configure-c99.patch

BuildRequires: automake
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: texinfo

Requires: xdg-utils

%description
Pinfo is an info file (or man page) viewer with a user interface
similar to the Lynx Web browser's interface.  Pinfo supports searching
using regular expressions, and is based on the ncurses library.

%prep
%oreon_verify_sources
%autosetup -p1

%build
./autogen.sh
%configure --without-readline
%make_build

%install
%make_install

# This file should not be packaged
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md TECHSTUFF
%config(noreplace) %{_sysconfdir}/pinforc
%{_bindir}/pinfo
%{_infodir}/pinfo.info*
%{_mandir}/man1/pinfo.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.13-10
- Prepare for Oreon 11 (RP1)
