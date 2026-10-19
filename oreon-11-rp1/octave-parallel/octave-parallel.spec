%global source0_hash ea86535e167351f3214feea4d0524626d07e211d1e84d94cbf230d41b2e01bc1
%global octpkg parallel
Name:           octave-%{octpkg}
Version:        4.0.1
Release:        1%{?dist}
Summary:        Parallel execution package for cluster computers for Octave
License:        GPL-3.0-or-later
URL:            https://octave.sourceforge.io/parallel/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Patch0:         octave-parallel-octave8.1.patch
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ghostscript
BuildRequires:  gnutls-devel
BuildRequires:  octave-devel
BuildRequires:  octave-struct
BuildRequires:  tex(latex)
# /oreon:deps
%description
Parallel execution package for cluster computers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#setup -qcT
%autosetup -p1 -n %{octpkg}-%{version}
cd src
# For patch of configure.ac
./bootstrap

%build

export CXXFLAGS="%{optflags}"
%octave_pkg_build
%install
%octave_pkg_install
chmod a-x %{buildroot}/%{octpkgdir}/*.m
rm -rf  %{buildroot}/%{octpkgdir}/doc
%oreon_autofiles main

%check

rm -rf  %{buildroot}/%{octpkgdir}/doc
%post

%octave_cmd pkg rebuild
%preun

%octave_pkg_preun
%postun

%octave_cmd pkg rebuild
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
