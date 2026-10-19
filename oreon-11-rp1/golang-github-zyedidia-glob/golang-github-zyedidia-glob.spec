%global source0_hash 120640d0ee8956d0a331f9ef444a05198636c48a7f154df3e1687262e2f2d98f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/zyedidia/glob
%global commit          dd4023a66dc351ae26e592d21cd133b5b143f3d8
%gometa
%global common_description %{expand:
This package adds support for globs in Go.
It simply converts glob expressions to regexps.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go package for glob matching
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/glob-%{commit}.tar.gz
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
