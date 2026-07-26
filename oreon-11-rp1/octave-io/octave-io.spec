%global source0_hash 4aa48468b3697934bf8c854e27dbab8827605e9dd4fe37e56834265e6130ba6f

%global octpkg io

Name:           octave-%{octpkg}
Version:        2.7.0
Release:        4%{?dist}
Summary:        Input/Output in external formats
# Automatically converted from old format: GPLv3+ and BSD - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD
URL:            http://octave.sourceforge.net/%{octpkg}/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 6:4.0
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Input/Output in external formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{_metainfodir}/io.sourceforge.octave.io.metainfo.xml
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/PKG_ADD
%{octpkgdir}/PKG_DEL
%doc %{octpkgdir}/doc/
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo
%{octpkgdir}/private/
%{octpkgdir}/templates/

%changelog
%autochangelog
