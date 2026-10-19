%global source0_hash 40740483a7ff2070dd7957be7513498d7e4a080bea2128159fc3f160803dae41
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/lestrrat-go/httpcc
Version:                1.0.1
%gometa -f
%global common_description %{expand:
HTTP/1.1 Cache-Control Header Parser.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        HTTP/1.1 Cache-Control Header Parser
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/httpcc-%{version}.tar.gz
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
