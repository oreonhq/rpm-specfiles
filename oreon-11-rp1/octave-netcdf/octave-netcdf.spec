%global source0_hash ab54b69ceb2b38fff12dd74ff3b33b819428b5c7896e28aebb0216594a032d49
%global octpkg netcdf
Name:           octave-%{octpkg}
Version:        1.0.20
Release:        1%{?dist}
Summary:        A MATLAB compatible NetCDF interface for Octave
License:        GPL-2.0-or-later
URL:            https://gnu-octave.githun.io/packages/%{octpkg}/
Source0:        https://github.com/gnu-octave/%{name}/releases/download/v%{version}/%{octpkg}-%{version}.tar.gz
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
# oreon:deps
BuildRequires:  automake
BuildRequires:  netcdf-devel
BuildRequires:  octave-devel
# /oreon:deps
%description
A MATLAB compatible NetCDF interface for Octave.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{octpkg}-%{version}

%conf
cd src
# Needed to fix C++ flag detection
autoreconf -f

%build

%octave_pkg_build
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
