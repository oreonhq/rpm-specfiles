%global source0_hash 5c155dc08511b522b1b972d278ae2017c4ae25405e961a62cd29864054f3d1b5
%global octpkg statistics
Name:           octave-%{octpkg}
Version:        1.9.3
Release:        1%{?dist}
Summary:        Additional statistics functions for Octave
License:        GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/gnu-octave/%{octpkg}
Source0:        https://github.com/gnu-octave/%{octpkg}/archive/refs/tags/release-%{version}/%{octpkg}-%{version}.tar.gz
Requires:       octave(api) = %{octave_api}
Requires:       octave-io
Requires(post): octave
Requires(postun): octave
%undefine _debugsource_packages
# oreon:deps
BuildRequires:  octave-devel
BuildRequires:  octave-io
# /oreon:deps
%description
Additional statistics functions for Octave.

%package        demos
Summary:        Demo files for using %{name}
Requires:       %{name} = %{version}-%{release}
%description    demos
Demo files for using %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcT

%build

%octave_pkg_build -T
%install
%octave_pkg_install
chmod a-x %{buildroot}/%{octpkgdir}/*.m
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%octave_pkg_check
%post

%octave_cmd pkg rebuild
%preun

%octave_pkg_preun
%postun

%octave_cmd pkg rebuild
%files -f %{oreon_filedir}/main.list
%files -n octave-statistics-demos -f %{oreon_filedir}/octave-statistics-demos.list

%changelog

%autochangelog
