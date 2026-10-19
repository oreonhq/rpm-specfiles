%global source0_hash 5ba2f612c9bb01dce7b53edc8a62b295b78a61c6562a11e29bde8de5d33faa81
%global octpkg ncarray
Name:           octave-%{octpkg}
Version:        1.0.6
Release:        8%{?dist}
Summary:        Access NetCDF files as a multi-dimensional array
License:        GPL-2.0-or-later
URL:            https://gnu-octave.github.io/packages/ncarray/
Source0:        https://downloads.sourceforge.net/octave/ncarray-%{version}.tar.gz
BuildArch:      noarch
Requires:       octave(api) = %{octave_api}
Requires:       octave-netcdf >= 1.0.2
Requires:       octave-statistics >= 1.0.6
Requires(post): octave
Requires(postun): octave
# oreon:deps
BuildRequires:  octave-devel
BuildRequires:  octave-netcdf
BuildRequires:  octave-statistics
# /oreon:deps
%description
Access a single or a collection of NetCDF files as a multi-dimensional array.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcT

%build

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
