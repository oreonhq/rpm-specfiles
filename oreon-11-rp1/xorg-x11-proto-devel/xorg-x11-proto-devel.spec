%global source0_hash 56898c716c0578df8a2d828c9c3e5c528277705c0484381a81960fe1a67668e8
%global debug_package %{nil}
Summary:        X.Org X11 Protocol headers
Name: xorg-x11-proto-devel
Version: 2025.1
Release:        2%{?dist}
License: BSD-2-Clause AND HPND AND HPND-sell-variant AND ICU AND MIT AND MIT-open-group AND SGI-B-2.0 AND SMLNJ AND X11 AND X11-distribute-modifications-variant
URL: https://www.x.org
BuildArch: noarch
Source0:        https://www.x.org/pub/individual/proto/xorgproto-%{version}.tar.xz
Source40: make-git-snapshot.sh
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig
# /oreon:deps
%description
X.Org X11 Protocol headers

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir xorgproto-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
for i in apple windows trap ; do
    rm -f $RPM_BUILD_ROOT%{_includedir}/X11/extensions/*${i}*
    rm -f $RPM_BUILD_ROOT%{_datadir}/pkgconfig/*${i}*
done
rm -f $RPM_BUILD_ROOT%{_docdir}/*/*.{html,svg}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2025.1-2
- Prepare for Oreon 11 (RP1)
