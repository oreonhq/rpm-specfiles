%global source0_hash ea86535e167351f3214feea4d0524626d07e211d1e84d94cbf230d41b2e01bc1

%global octpkg parallel

Name:           octave-%{octpkg}
Version:        4.0.1
Release:        10%{?dist}
Summary:        Parallel execution package for cluster computers for Octave
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://octave.sourceforge.io/parallel/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# Fix build with octave 8.1 - https://savannah.gnu.org/bugs/?63922
Patch0:         octave-parallel-octave8.1.patch

BuildRequires:  octave-devel
BuildRequires:  gnutls-devel
BuildRequires:  tex(latex)
BuildRequires:  ghostscript
BuildRequires:  octave-struct
BuildRequires:  autoconf
BuildRequires:  automake

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

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
#octave_pkg_build -T
%octave_pkg_build

%install
%octave_pkg_install
chmod a-x %{buildroot}/%{octpkgdir}/*.m
rm -rf  %{buildroot}/%{octpkgdir}/doc

%check
#octave_pkg_check
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
%{octpkgdir}/private/*.m
%dir %{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/on_uninstall.m
%{octpkglibdir}
%{_metainfodir}/octave-%{octpkg}.metainfo.xml
%{octpkgdir}/bin/octave-pserver

%changelog
%autochangelog
