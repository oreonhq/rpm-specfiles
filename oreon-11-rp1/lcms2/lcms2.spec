%global source0_hash bfc54f7bab59fbc921012014a8032e4cba4abd46db47d46b76416a8c0b2815c8
Name:           lcms2
Version:        2.19.1
Release:        1%{?dist}
Summary:        Color Management Engine
License:        MIT AND GPL-3.0-or-later
URL:            https://github.com/mm2/Little-CMS
%global lcms2_gh_tag lcms2.%(echo %{version} | cut -d. -f2)
Source0:        http://www.littlecms.com/lcms2-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  meson
BuildRequires:  zlib-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dutils=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n lcms2-utils -f %{oreon_filedir}/lcms2-utils.list
%files -n lcms2-devel -f %{oreon_filedir}/lcms2-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.16-1
- Prepare for Oreon 11 (RP1)
