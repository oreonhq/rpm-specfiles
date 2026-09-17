%global source0_hash fbd09409950c8b95e02ccb3895ec78f52cc8589a08a65d8c512a7cacf567bb4a

%global octpkg general

Name:           octave-%{octpkg}
Version:        2.1.1
Release:        19%{?dist}
Summary:        General tools for Octave, string dictionary, parallel computing
# Automatically converted from old format: GPLv3+ and BSD and Public Domain - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Public-Domain
URL:            http://octave.sourceforge.net/general/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Source1:        octave-general.metainfo.xml

BuildRequires:  octave-devel >= 4.0
BuildRequires:  libappstream-glib

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

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

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/@dict/
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo
%{_metainfodir}/octave-%{octpkg}.metainfo.xml

%changelog
%autochangelog
