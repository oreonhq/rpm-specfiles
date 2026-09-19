%global source0_hash d028c52579e251c3f21ebfdf065dffab3ad7893434efda33b501225ef1ea6ed3

%global octpkg gsl

Name:		octave-%{octpkg}
Version:	2.1.1
Release:	22%{?dist}
Summary:	Octave bindings to the GNU Scientific Library
# Some test files are GPLv3+ but they're not shipped.
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://octave.sourceforge.net/gsl/
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:	octave-devel
BuildRequires:	gsl-devel

Requires:	octave(api) = %{octave_api}
Requires(post):	octave
Requires(postun): octave

%description
The octave-gsl package provides an Octave binding to functions
in the Gnu Scientific Library, such as
* Airy functions
* Bessel functions
* Conical functions
* Debye functions
* Riemann Beta and Gamma functions
* Sine and cosine integrals
* Wigner coefficients 3-j, 6-j and 9-j coefficients

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install
# The are no docs, so there really shouldn't be a doc-cache. 9.1 doesn't preduce one, but earlier versions do
rm -f %{buildroot}%{octpkgdir}/doc-cache

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%dir %{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/on_uninstall.m

%changelog
%autochangelog
