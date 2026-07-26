%global source0_hash 4c2d4dd8f1d213f080519c6f9dfbbdca068087ee0411122b16e377e0f4641610

%global octpkg quaternion

Name:           octave-%{octpkg}
Version:        2.4.0
Release:        34%{?dist}
Summary:        Quaternion package for Octave
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://octave.sourceforge.io/quaternion/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# 6.1.0 support https://savannah.gnu.org/bugs/?func=detailitem&item_id=59163
Patch0:         https://hg.octave.org/mxe-octave/raw-file/tip/src/of-quaternion-2-dev-fixes.patch

BuildRequires:  octave-devel >= 6:3.8.0

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Package for the manipulation of Quaternions used for frame transformation

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{octpkg}
%patch -P0 -p1 -b .octave6.1

%build
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/@quaternion/*.m
%{octpkgdir}/@quaternion/private/*.m
%{octpkgdir}/packinfo
%doc %{octpkgdir}/packinfo/COPYING
%doc %{octpkgdir}/doc

%changelog
%autochangelog
