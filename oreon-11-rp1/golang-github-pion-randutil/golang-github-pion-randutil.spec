%global source0_hash 32bf89ea07eec2be1c74834a3a4d52b52b84e1b77004ae16799ace86c367b9dc
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/pion/randutil
Version:                0.1.0
%global commit          b2a37e259481c76bdeee4909c8657eb06df36d95
%gometa -L -f
%global common_description %{expand:
Helper library for cryptographic and mathmatical randoms.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-pion-randutil
Release:        1%{?dist}
Summary:        Helper library for cryptographic and mathmatical randoms
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/randutil-%{commit}.tar.gz
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
