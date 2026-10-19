%global source0_hash 82b2d04549216f36a8c538a756010a90222e3942ab815596b86a62dbf766f2d2
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         golang.org/x/net
%global forgeurl        https://github.com/golang/net
Version:                0.43.0
%gometa
%global common_description %{expand:
This package holds supplementary Go networking libraries.}
%global golicenses      LICENSE PATENTS
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go supplementary network libraries
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/net-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
cp -rp publicsuffix/data %{buildroot}%{gopath}/src/%{goipath}/publicsuffix
echo '%{gopath}/src/%{goipath}/publicsuffix/data/' >> %{godevelfilelist0}
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
