%global source0_hash 5712117a25d31d1266003646a40e81e7d7427433c26366e426dffa9ab8abd648

%global octpkg miscellaneous

Name:           octave-%{octpkg}
Version:        1.3.1
Release:        5%{?dist}
Summary:        Miscellaneous functions for Octave
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://octave.sourceforge.io/miscellaneous/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Source1:        octave-miscellaneous-python.patch

BuildRequires:  octave-devel
BuildRequires:  dos2unix
BuildRequires:  units
BuildRequires:  python3-devel

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Miscellaneous tools that don't fit somewhere else. It includes
additional functions for manipulating cell arrays, computation of
Chebyshev, Hermite, Legendre and Laguerre polynomials, working with
CSV data and for Latex export.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install
chmod a-x %{buildroot}/%{octpkgdir}/*.m
dos2unix %{buildroot}/%{octpkgdir}/*.m
chmod a-x %{buildroot}/%{octpkgdir}/private/*.m
dos2unix %{buildroot}/%{octpkgdir}/private/*.m
pushd %{buildroot}%{octpkgdir}
/usr/bin/patch -p0 < %{SOURCE1}
popd
%py3_shebang_fix %{buildroot}%{octpkgdir}
rm -rf %{buildroot}/%{octpkgdir}/test

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
%{octpkgdir}/private/*.m
%{octpkgdir}/*.py*
%{octpkgdir}/packinfo
%exclude %{octpkgdir}/packinfo/COPYING
%license %{octpkgdir}/packinfo/COPYING

%changelog
%autochangelog
