%global source0_hash fccea7dd84c1104ed3babb47a28f05e0012a89c284f39ab094090450915294ce
%global octpkg struct
Name:           octave-%{octpkg}
Version:        1.0.18
Release:        12%{?dist}
Summary:        Structure handling for Octave
License:        GPL-3.0-or-later
URL:            https://octave.sourceforge.io/struct/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
# oreon:deps
BuildRequires:  octave-devel
# /oreon:deps
%description
Octave includes support for organizing data in structures. This package
contains additional data structure manipulation functions that are not
included in the octave core.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcT

%build

%octave_pkg_build -T
%install
%octave_pkg_install
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
