%global source0_hash 84afe297b4ad64a89d8c8a560322c4e262417772b17862015f4f5b9d1558d990
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/circonus-labs/circonus-gometrics
Version:                3.4.7
%gometa
%global common_description %{expand:
A Go implementation of metrics reporting for circonus.}
%global golicenses      LICENSE
%global godocs          OPTIONS.md README.md CHANGELOG.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation of metrics reporting for circonus
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/circonus-gometrics-%{version}.tar.gz
Source1:        glide.lock
Source2:        glide.yaml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/circonus-labs/circonusllhist)
BuildRequires:  golang(github.com/circonus-labs/go-apiclient)
BuildRequires:  golang(github.com/circonus-labs/go-apiclient/config)
BuildRequires:  golang(github.com/hashicorp/go-retryablehttp)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/tv42/httpunix)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
