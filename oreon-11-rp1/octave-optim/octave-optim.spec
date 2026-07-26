%global source0_hash 554a8e18bb7195ae861f5059c14f1a557844265c1addb5bfbf3ab9885524787e

%global octpkg optim

Name:           octave-%{octpkg}
Version:        1.6.2
Release:        16%{?dist}
Summary:        A non-linear optimization tool kit for Octave
# C++ and .m are GPLv3+, documentation is GFDL
# Automatically converted from old format: GPLv3+ and GFDL - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
URL:            https://gnu-octave.github.io/packages/optim/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

# Fails to build with octave 10.  Patch is based on
# https://savannah.gnu.org/bugs/?func=detailitem&item_id=65526
Patch:          octave-optim-octave10.patch

BuildRequires:  octave-devel
BuildRequires:  octave-struct >= 1.0.12
BuildRequires:  octave-statistics >= 1.4.0 
BuildRequires:  tex(latex)
BuildRequires:  tex(dsfont.sty)
BuildRequires:  ghostscript

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
Requires:       octave-struct >= 1.0.10

%description
This package contains a non-linear optimization tool kit for Octave, containing
functions for curve fitting and the following minimization algorithms:
* Nead-Miller simplex
* Conjugate Gradients
* Memory limited BFGS
* Simulated Annealing

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install
rm -rf %{buildroot}/%{octpkgdir}/doc/.svnignore
chmod a-x %{buildroot}/%{octpkgdir}/*.m
rm -rf  %{buildroot}/%{octpkgdir}/doc

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
%{octpkgdir}/PKG_ADD
%{octpkgdir}/private/optim_problems_p_r_y.data
%{octpkgdir}/private/*.m
%{octpkgdir}/+__optim_checks__/*.m
%{_metainfodir}/octave-%{octpkg}.metainfo.xml
%doc doc/development/interfaces.txt

%changelog
%autochangelog
