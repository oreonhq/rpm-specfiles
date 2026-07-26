%global source0_hash d321650865db848df67a7161e8f82b5d49ab01eb8db2d5b5cce2cfab3467cb0f

%global octpkg specfun

Name:           octave-%{octpkg}
Version:        1.1.0
Release:        45%{?dist}
Summary:        Special functions for Octave, including ellipitic functions
# announced on devel@lists.fedoraproject.org
# Message-ID: <1323949577.12740.9.camel@xbox360.hq.axsem.com>
# Automatically converted from old format: GPLv3+ and BSD - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://octave.sourceforge.io/specfun/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildArch:      noarch
# We remove functions moved into octave 6
BuildRequires:  octave-devel >= 6

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
This package contains special functions for Octave, including elliptic
functions, sine/cosine integral functions, complementary error functions
and exponential integrals, Heaviside and Dirac functions, the Riemann zeta
function and others.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{octpkg}
# Remove functions moved into octave main
rm inst/{ellipke,expint}.m src/{ellipj.cc,Makefile}

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
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/packinfo
%doc %{octpkgdir}/packinfo/COPYING

%changelog
%autochangelog
