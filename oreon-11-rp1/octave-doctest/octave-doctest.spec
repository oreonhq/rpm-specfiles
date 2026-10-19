%global source0_hash a2526d8f83f8b2fbabfab35611cff240a88f7fef701387d6924cb53571a3283a
%global octpkg doctest
Name:           octave-%{octpkg}
Version:        0.8.2
Release:        1%{?dist}
Summary:        Documentation tests for Octave
License:        BSD-3-Clause AND FSFAP
URL:            https://octave.sourceforge.io/%{octpkg}/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
Requires:       octave(api) = %{octave_api}
Requires:       texinfo >= 6.0
Requires(post): octave
Requires(postun): octave
# oreon:deps
BuildRequires:  octave-devel
BuildRequires:  texinfo
# /oreon:deps
%description
The Octave-forge Doctest package finds specially-formatted blocks of
example code within documentation files.  It then executes the code
and confirms the output is correct.  This can be useful as part of a
testing framework or simply to ensure that documentation stays
up-to-date during software development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{octpkg}-%{version}

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
