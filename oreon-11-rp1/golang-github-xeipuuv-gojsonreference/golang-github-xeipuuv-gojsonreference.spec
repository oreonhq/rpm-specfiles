%global source0_hash 641833c200235d14732c9705ab636d3ef33a52d924b0ab5702fe98a08cf6339e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xeipuuv/gojsonreference
%global commit          bd5ef7bd5415a7ac448318e64f11a24cd21e594b
%gometa
%global common_description %{expand:
An implementation of JSON Reference.}
%global golicenses      LICENSE-APACHE-2.0.txt
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        JSON Reference implementation in Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gojsonreference-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/xeipuuv/gojsonpointer)
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
