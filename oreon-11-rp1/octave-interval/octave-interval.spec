%global source0_hash 38e526427375713229ab3d86a5fe3f5a08550747d8420541706fdea9093fdce8

%global octpkg interval

Name:           octave-%{octpkg}
Version:        3.2.1
Release:        15%{?dist}
Summary:        Interval arithmetic for Octave
# The source code is GPLv3+ except src/crlibm/ which is LGPLv2+
# Automatically converted from old format: GPLv3+ and LGPLv2+ - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://octave.sourceforge.io/%{octpkg}/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.8.0
BuildRequires:  mpfr-devel

Requires:       octave(api) = %{octave_api}
Requires:       mpfr >= 3.1.0
Requires(post): octave
Requires(postun): octave

%description
The Octave-forge Interval package for real-valued interval arithmetic
allows one to evaluate functions over subsets of their domain.  All
results are verified, because interval computations automatically keep
track of any errors.  These concepts can be used to handle
uncertainties, estimate arithmetic errors and produce reliable
results.  Also it can be applied to computer-assisted proofs,
constraint programming, and verified computing.  The implementation is
based on interval boundaries represented by binary64 numbers and is
conforming to IEEE Std 1788-2015, IEEE standard for interval
arithmetic.

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
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/@infsup
%{octpkgdir}/@infsupdec
%{octpkgdir}/test
%doc %{octpkgdir}/doc
%dir %{octpkgdir}/packinfo
%doc %{octpkgdir}/packinfo/doc-cache
%license %{octpkgdir}/packinfo/COPYING
%{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/CITATION
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/*.m
%{_metainfodir}/octave-%{octpkg}.metainfo.xml

%changelog
%autochangelog
