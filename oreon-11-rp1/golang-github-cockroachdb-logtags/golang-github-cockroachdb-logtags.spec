%global source0_hash 72bd0eb43bcd8e3614dc9ca6cf8e7ef7b1945aac6f497195de7e8da32b3ffe22
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/cockroachdb/logtags
%global commit          eb05cc24525fa45bcdbaaeec3e431a82099f9ad4
%gometa
%global common_description %{expand:
Key/value annotations for Go contexts.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Key/value annotations for Go contexts
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/logtags-%{commit}.tar.gz
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
