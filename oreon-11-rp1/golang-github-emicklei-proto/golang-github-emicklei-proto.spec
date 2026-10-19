%global source0_hash 95e76593e9d0577a30c04621807ca70265bc3aa507ac045e760a7c1933705963
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/emicklei/proto
Version:                1.14.3
%gometa -f
%global common_description %{expand:
Parser for Google ProtocolBuffers definition.}
%global golicenses      LICENSE
%global godocs          CHANGES.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Parser for Google ProtocolBuffers definition
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/proto-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
