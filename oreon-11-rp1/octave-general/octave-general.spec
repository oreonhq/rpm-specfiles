%global source0_hash b13777d4f5932e6891f2aac13da17f22b8c9b8b4ff8ed0179659ebd19124148f
%global octpkg general
Name:           octave-%{octpkg}
Version:        2.1.4
Release:        1%{?dist}
Summary:        General tools for Octave, string dictionary, parallel computing
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Public-Domain
URL:            http://octave.sourceforge.net/general/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Source1:        octave-general.metainfo.xml
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
# oreon:deps
BuildRequires:  libappstream-glib
BuildRequires:  octave-devel
# /oreon:deps
%description
The Octave-forge General package provides functions for parallel computing,
string dictionaries and other general utility functions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcT

%build

%octave_pkg_build -T
%install
%octave_pkg_install
mkdir -p %{buildroot}%{_metainfodir}
install -p -m 0644 %SOURCE1 %{buildroot}%{_metainfodir}/
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
