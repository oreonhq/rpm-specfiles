%global source0_hash 174222e155b19cda0f60c481a954524b849e5c74bffdc3a164f919dd3b72de40
%bcond check 0
%global debug_package %{nil}
%global goipath         sourcegraph.com/sourcegraph/appdash-data
%global forgeurl        https://github.com/sourcegraph/appdash-data
%global commit          73f23eafcf67cad684fba328dd545a116ac273ff
%gometa
%global common_description %{expand:
This repository holds binary and external asset files (images, CSS, JS etc) that
Appdash relies on.}
%global golicenses      data/Caged/d3-tip/LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Binary and external asset files for Appdash
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/appdash-data-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

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
