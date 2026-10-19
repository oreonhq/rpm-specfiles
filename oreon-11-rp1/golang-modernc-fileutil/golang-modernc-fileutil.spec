%global source0_hash ff80e68546da1a47bdb9ebfb72cda8aafd1e425e2e204a4a3abefb37b2cb8756
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/fileutil
%global forgeurl        https://gitlab.com/cznic/fileutil
Version:                1.3.0
%global tag             v1.3.0
%gometa
%global common_description %{expand:
Package fileutil collects some file utility functions.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README
Name:           %{goname}
Release:        1%{?dist}
Summary:        File utility functions in Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/fileutil-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
