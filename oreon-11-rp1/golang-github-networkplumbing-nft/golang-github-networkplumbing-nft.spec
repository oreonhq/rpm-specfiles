%global source0_hash f62b62631f0fd704161aa76ab94ebbccaefd39cab477061717712002ac911c05
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/networkplumbing/go-nft
Version:                0.4.0
%gometa
%global common_description %{expand:
Go bindings for nft utility.}
%global godevelheader %{expand:
Requires:       nftables-devel}
%global golicenses      LICENSE
%global godocs          README.md CONTRIBUTING.md CODE_OF_CONDUCT.md CHANGELOG
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go bindings for nft utility
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-nft-%{version}.tar.gz
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
