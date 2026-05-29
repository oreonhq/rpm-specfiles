%global source0_hash none

Name:           lcms2
Version:        2.16
Release:        %autorelease
Summary:        Color Management Engine
# part of src/cmssm.c is softsurf (no SPDX yet) see https://gitlab.com/fedora/legal/fedora-license-data/-/issues/469
# utils/samples/mkcmy.c is libtiff - but it is not used
# plugins/threaded/src/ is GPL-3.0-or-later
License:        MIT AND GPL-3.0-or-later
URL:            https://github.com/mm2/Little-CMS
# Upstream moved tarballs off littlecms.com; GitHub release tag is lcms2.<minor> (e.g. 2.16 -> lcms2.16).
%global lcms2_gh_tag lcms2.%(echo %{version} | cut -d. -f2)
Source0:        https://github.com/mm2/Little-CMS/releases/download/lcms2.%(echo/lcms2-2.16.tar.gz

BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  zlib-devel
BuildRequires:  meson

%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form. LCMS2 is the current version of LCMS, and can be
parallel installed with the original (deprecated) lcms.

%package        utils
Summary:        Utility applications for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains utility applications for %{name}.

%package        devel
Summary:        Development files for LittleCMS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       littlecms-devel = %{version}-%{release}

%description    devel
Development files for LittleCMS.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%meson -Dutils=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc AUTHORS
%doc ChangeLog
%doc README*
%license LICENSE
%{_libdir}/liblcms2.so.2*

%files utils
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%{_includedir}/lcms2*.h
%{_libdir}/liblcms2.so
%{_libdir}/pkgconfig/lcms2.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.16-1
- Prepare for Oreon 11 (RP1)
