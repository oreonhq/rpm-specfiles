%global source0_hash abd13286b717c71b420591201255be9c295b77731f94c5eb591cb7d488f5f247

%global octpkg control

Name:           octave-%{octpkg}
Version:        4.2.1
Release:        1%{?dist}
Summary:        Computer-Aided Control System Design (CACSD) Tools for Octave
License:        GPL-3.0-or-later
URL:            https://gnu-octave.github.io/packages/control/
Source0:        https://github.com/gnu-octave/pkg-%{octpkg}/releases/download/%{octpkg}-%{version}/%{octpkg}-%{version}.tar.gz
BuildRequires:  octave-devel >= 4.0.0

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

# compiler crash on aarch64:
#during GIMPLE pass: ifcvt
#MB04DL.f: In function ‘mb04dl_’:
#MB04DL.f:4:7: internal compiler error: in predicate_rhs_code, at tree-if-conv.cc:2908
#    4 |       SUBROUTINE MB04DL( JOB, N, THRESH, A, LDA, B, LDB, ILO, IHI,
#      |       ^~~~~~~~~~~~~~~~~
ExcludeArch: aarch64

%description
The Octave control systems package contains functions for analyzing
and designing automatic control systems and algorithms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install
for i in %{octpkgdir}/doc/references.txt; do
  iconv -f iso8859-1 -t utf-8 %{buildroot}/$i > %{buildroot}/$i.conv && mv -f %{buildroot}/$i.conv %{buildroot}/$i
done;

%check
%octave_pkg_check

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
%{octpkgdir}/packinfo
%exclude %{octpkgdir}/packinfo/COPYING
%license %{octpkgdir}/packinfo/COPYING
%{octpkgdir}/@lti
%{octpkgdir}/@ss
%{octpkgdir}/@tf
%{octpkgdir}/@tfpoly
%{octpkgdir}/@frd
%{octpkgdir}/@iddata
%doc %{octpkgdir}/doc
%{_metainfodir}/io.github.gnu_octave.pkg-control.metainfo.xml

%changelog
%autochangelog
