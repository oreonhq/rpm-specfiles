%global source0_hash b281350217322fb1ff5dcdef1d0f8f4d1daaa8d9ed656f2ed76d409d27d46455
%global octpkg control
Name:           octave-%{octpkg}
Version:        4.2.3
Release:        1%{?dist}
Summary:        Computer-Aided Control System Design (CACSD) Tools for Octave
License:        GPL-3.0-or-later
URL:            https://gnu-octave.github.io/packages/control/
Source0:        https://github.com/gnu-octave/pkg-%{octpkg}/releases/download/%{octpkg}-%{version}/%{octpkg}-%{version}.tar.gz
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
ExcludeArch: aarch64
# oreon:deps
BuildRequires:  octave-devel
# /oreon:deps
%description
The Octave control systems package contains functions for analyzing
and designing automatic control systems and algorithms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{octpkg}-%{version}

%build

%octave_pkg_build
%install
%octave_pkg_install
for i in %{octpkgdir}/doc/references.txt; do
  iconv -f iso8859-1 -t utf-8 %{buildroot}/$i > %{buildroot}/$i.conv && mv -f %{buildroot}/$i.conv %{buildroot}/$i
done;
%oreon_autofiles main

%check

%octave_pkg_check
%post

%octave_cmd pkg rebuild
%preun

%octave_pkg_preun
%postun

%octave_cmd pkg rebuild
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
