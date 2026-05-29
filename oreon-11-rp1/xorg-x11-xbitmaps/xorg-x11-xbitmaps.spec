%global source0_hash ad6cad54887832a17d86c2ccfc5e52a1dfab090f8307b152c78b0e1529cd0f7a

%global pkgname xbitmaps

%global debug_package %{nil}

Summary: X.Org X11 application bitmaps
Name: xorg-x11-%{pkgname}
Version: 1.1.3
Release: 6%{?dist}
License: HPND AND ICU
URL: http://www.x.org
BuildArch: noarch

Source0:        https://www.x.org/pub/individual/data/xbitmaps-%{version}.tar.xz

BuildRequires: make
BuildRequires: automake gcc
Requires: pkgconfig

%description
X.Org X11 application bitmaps

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n xbitmaps-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING
%{_includedir}/X11
%{_datadir}/pkgconfig/xbitmaps.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-6
- Import
