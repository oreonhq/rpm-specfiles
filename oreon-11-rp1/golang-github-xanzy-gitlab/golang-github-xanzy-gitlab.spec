%global source0_hash f97741ea51d34a61077fad0ebe4ba82e6966ebf89024410626f34a5785839042
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xanzy/go-gitlab
Version:                0.114.0
%gometa -L -f
%global common_description %{expand:
GitLab Go SDK.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-xanzy-gitlab
Release:        1%{?dist}
Summary:        GitLab Go SDK
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-gitlab-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
