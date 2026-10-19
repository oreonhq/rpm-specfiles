%global source0_hash 510b220a406a93f1a7fb2858e7a30fde15d5c3258c6f94e8f72b1ce2ec4b8793
Name: sane-frontends
Version: 1.0.14
Release:        1%{?dist}
Summary:        Graphical frontend to SANE
URL: http://www.sane-project.org
Source0:        https://gitlab.com/sane-project/frontends/-/archive/%{version}/frontends-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:        sane-frontends-1.0.14-array-out-of-bounds.patch
Patch1:        sane-frontends-1.0.14-sane-backends-1.0.20.patch
Patch2:        sane-frontends-1.0.14-xcam-man.patch
Patch3:        frontends-scanadf-segv.patch
Patch4:        sane-frontends-configure-c99.patch
Patch5:        sane-frontends-c99.patch
Patch6:        0001-src-scanadf.c-Fix-segfault-when-scanadf-h-d-device.patch
License: GPL-2.0-or-later AND GPL-2.0-or-later WITH SANE-exception
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  sane-backends-devel
# /oreon:deps
%description
This packages includes the scanadf and xcam programs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n frontends-%{version}
rm -f lstat.c lstat.h mkdir.c mkdir.h readlink.c readlink.h

%build

autoconf
%configure --with-gnu-ld --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --mandir=%{_mandir} --disable-gimp
%make_build
%install
%make_install
rm -f %{buildroot}%{_bindir}/xscanimage
rm -f %{buildroot}%{_mandir}/man1/xscanimage*
rm -f %{buildroot}%{_datadir}/sane/sane-style.rc
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.14-54
- Import
