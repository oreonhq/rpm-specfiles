%global source0_hash 662e46a93aba5ffe383e55597ce5749447e5c8e9409b1452f5790bfd6e1f8a11
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-git/gcfg
Version:                1.5.0
%gometa
%global common_description %{expand:
Go-gcfg/gcfg fork for usage in go-git/go-git.}
%global golicenses      LICENSE
%global godocs          README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go-gcfg/gcfg fork for usage in go-git/go-git
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gcfg-%{version}.tar.gz
Patch0:         https://github.com/go-gcfg/gcfg/commit/f52d3f482a436943be3dabf712d76d30cde3708b.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
