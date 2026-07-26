%global source0_hash fccea7dd84c1104ed3babb47a28f05e0012a89c284f39ab094090450915294ce

%global octpkg struct

Name:           octave-%{octpkg}
Version:        1.0.18
Release:        12%{?dist}
Summary:        Structure handling for Octave
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://octave.sourceforge.io/struct/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel 

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Octave includes support for organizing data in structures. This package
contains additional data structure manipulation functions that are not
included in the octave core.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%{octpkglibdir}
%{_metainfodir}/octave-struct.metainfo.xml

%changelog
%autochangelog
