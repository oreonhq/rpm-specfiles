%global source0_hash 8eb492408ec5aafe4e196ec5bdbd2298e0ac068d2b754948f34b9082b9126b37
%global octpkg symbolic
%global _python_bytecompile_extra 0
Name:           octave-%{octpkg}
Version:        3.2.2
Release:        1%{?dist}
Summary:        Symbolic computations for Octave
License:        GPL-3.0-or-later AND FSFAP
URL:            https://gnu-octave.github.io/packages/%{octpkg}
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
Requires:       python%{python3_pkgversion}-sympy >= 1.5.1
# oreon:deps
BuildRequires:  octave-devel
BuildRequires:  octave-doctest
BuildRequires:  python3
BuildRequires:  python3-packaging
BuildRequires:  python3-sympy
# /oreon:deps
%description
Adds symbolic calculation features to GNU Octave.
These include common Computer Algebra System tools such as algebraic
operations, calculus, equation solving, Fourier and Laplace transforms,
variable precision arithmetic and other features.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{octpkg}-%{version}

%build

%octave_pkg_build
%install
%octave_pkg_install
%oreon_autofiles main

%check

pushd %{buildroot}/%{octpkgdir}
%octave_cmd r=octsympy_tests; if r, type fntests.log; end; exit(r)
rm -f fntests.log
%octave_cmd pkg load doctest; syms x; r=doctest("."); exit(~r)
popd
%post

%octave_cmd pkg rebuild
%preun

%octave_pkg_preun
%postun

%octave_cmd pkg rebuild
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
