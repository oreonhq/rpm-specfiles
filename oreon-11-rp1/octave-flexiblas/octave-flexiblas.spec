%global source0_hash c46ca66f3342ef4b11aaae1e3db506b0a7c16e405889c7d1230c5a9d7baed82f

%global octpkg flexiblas
# Exclude .oct files from provides
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$

Name:           octave-%{octpkg}
Version:        3.4.1
Release:        %autorelease
Summary:        FlexiBLAS API Interface for Octave
License:        GPL-3.0-or-later
URL:            https://www.mpi-magdeburg.mpg.de/projects/%{octpkg}
Source0:        %{octpkg}-octave-%{version}.tar.gz
# Generated using create-oct-package.sh from:
# Source1:        https://github.com/mpimd-csc/%{octpkg}/archive/v%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  octave-devel >= 5.1.0
BuildRequires:  flexiblas-devel >= 3.0.0
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
FlexiBLAS is a BLAS wrapper library which allows to change the BLAS
without recompiling the programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{octpkg}-octave
sed -i 's/-std=c++11//' src/Makefile

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
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING

%changelog
%autochangelog
