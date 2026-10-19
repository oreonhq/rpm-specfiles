%global source0_hash b4b6865e7f65ee5b9c254a69128bf10e93b38bc27f5bc5b973fef300217fc725
%global octpkg image
Name:           octave-%{octpkg}
Version:        2.20.1
Release:        1%{?dist}
Summary:        Image processing for Octave
License:        GPL-2.0-or-later
URL:            http://octave.sourceforge.net/image/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
# oreon:deps
BuildRequires:  octave-devel
# /oreon:deps
%description
The Octave-forge Image package provides functions for processing images.
The package also provides functions for feature extraction, image
statistics, spatial and geometric transformations, morphological
operations, linear filtering, and much more.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcT

%build

export XTRA_CXXFLAGS="-fPIC"
%octave_pkg_build -T
%install
%octave_pkg_install
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
