%global source0_hash 35af35bdf0d4bb2439c5fb06891b9943da7a20e370d386039f920446e9876587
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/leodido/go-urn
Version:                1.5.0
%gometa
%global common_description %{expand:
Parser for uniform resource names as seen on RFC 2141.}
%global golicenses      LICENSE
%global godocs          docs README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Parser for uniform resource names as seen on RFC 2141
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-urn-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
