%global source0_hash 9d433b45c4bf4401354f2a8194d2d48565f6b84f5c0ea30f493855946aacee7f
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/pkg/sftp
Version:                1.13.11
%gometa -L -f
%global common_description %{expand:
SFTP support for the go.crypto/ssh package.}
%global golicenses      LICENSE
%global godocs          examples CONTRIBUTORS README.md request-readme.md
Name:           golang-github-pkg-sftp
Release:        1%{?dist}
Summary:        SFTP support for the go.crypto/ssh package
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/sftp-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
