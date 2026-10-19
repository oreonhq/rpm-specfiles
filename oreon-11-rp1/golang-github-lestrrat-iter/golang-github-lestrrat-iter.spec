%global source0_hash 7f9469449fb1f267f7284ca3e8da7b957153dd1963bf5b6def4a71aec1da0770
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/lestrrat-go/iter
Version:                1.0.2
%gometa -f
%global common_description %{expand:
Iterator tools.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Iterator tools
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/iter-%{version}.tar.gz
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
