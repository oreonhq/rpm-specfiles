%global source0_hash 86aef8eddb8f39025cc32a6a385157dc8adbc83417ca25b1e95681c7dae08b47
%global octpkg datatypes
Name:           octave-%{octpkg}
Version:        1.4.2
Release:        1%{?dist}
Summary:        Extra data types for GNU Octave
License:        GPL-3.0-or-later AND CC-BY-SA-4.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://gnu-octave.github.io/packages/datatypes/
Source0:        https://github.com/pr0m1th3as/datatypes/releases/download/release-%{version}/datatypes-%{version}.tar.gz
Patch:          octave-datatypes-tz.patch
Requires(post): octave
Requires(postun): octave
# oreon:deps
BuildRequires:  date-devel
BuildRequires:  gcc-c++
BuildRequires:  octave-devel
# /oreon:deps
%description
Extra data types for GNU Octave.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{octpkg}-release-%{version}
rm -r src/date src/tz.cpp

%build

%octave_pkg_build
%install
%octave_pkg_install
%oreon_autofiles main

%check

export TZ=UTC
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
