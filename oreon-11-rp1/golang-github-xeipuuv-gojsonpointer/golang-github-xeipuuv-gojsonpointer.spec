%global source0_hash ac83000a2843d5ac25783b256dda3d12533bc860dafc4c35ba2f5d69dbf9556d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xeipuuv/gojsonpointer
%global commit          02993c407bfbf5f6dae44c4f4b1cf6a39b5fc5bb
%gometa
%global common_description %{expand:
An implementation of JSON Pointer.}
%global golicenses      LICENSE-APACHE-2.0.txt
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        JSON Pointer implementation in Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gojsonpointer-%{commit}.tar.gz
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
