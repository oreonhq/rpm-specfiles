%global source0_hash 59fb3771a2d2a2313447532c59a2e000a6a7bb7a677f3ef8183fbaaab5493a14
%global octpkg optim
Name:           octave-%{octpkg}
Version:        1.6.3
Release:        1%{?dist}
Summary:        A non-linear optimization tool kit for Octave
License:        GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
URL:            https://gnu-octave.github.io/packages/optim/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Patch:          octave-optim-octave10.patch
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
Requires:       octave-struct >= 1.0.10
# oreon:deps
BuildRequires:  ghostscript
BuildRequires:  octave-devel
BuildRequires:  octave-statistics
BuildRequires:  octave-struct
BuildRequires:  tex(dsfont.sty)
BuildRequires:  tex(latex)
# /oreon:deps
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
%oreon_autofiles main

%post

%octave_cmd pkg rebuild
%preun

%octave_pkg_preun
%postun

%octave_cmd pkg rebuild
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
