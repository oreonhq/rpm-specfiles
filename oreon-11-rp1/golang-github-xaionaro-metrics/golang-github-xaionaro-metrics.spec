%global source0_hash 3199fa430a3d2f6437540d85b6e25943d3380cd6f5456e7a014b54fc1213bbae
%ifarch i686 armv7hl
%bcond check 1
%else
%bcond check 0
%endif
%global goipath         github.com/xaionaro-go/metrics
%global commit          68050b33767320ae8ac5219ea8665a9af03c21ff
%gometa
%global common_description %{expand:
An implementation of fast metrics for high-load-ed services on Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        An implementation of fast metrics for high-load-ed services on Golang
License:        GPLv3
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/metrics-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/trafficstars/metrics)
BuildRequires:  golang(github.com/xaionaro-go/atomicmap)
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
