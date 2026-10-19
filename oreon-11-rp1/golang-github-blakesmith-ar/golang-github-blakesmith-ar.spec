%global source0_hash 4e16785340ed0d9987c8793198e70b1a544515be7a1f916a746fde9af49e5c94
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/blakesmith/ar
%global commit          809d4375e1fb5bb262c159fc3ec2e7a86a8bfd28
%gometa
%global common_description %{expand:
Golang ar archive file library.}
%global golicenses      COPYING
%global godocs          README.md fixtures/hello.txt fixtures/lamp.txt
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Golang ar archive file library
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/ar-%{commit}.tar.gz
Patch:          0001-Fix-non-constant-format-strings.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
