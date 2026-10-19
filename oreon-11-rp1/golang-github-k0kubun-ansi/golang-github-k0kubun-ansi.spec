%global source0_hash 698308ac5d4ee445bcb3bf56086ddaf7e55676df082f10e1218e3a7b142e3bf3
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/k0kubun/go-ansi
%global commit          3bf9e290321332340cd6915d2386f733fbf7233a
%gometa
%global common_description %{expand:
Windows-portable ANSI escape sequence utility for Go language.}
%global golicenses      LICENSE.txt
%global godocs          README.mdf
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Windows-portable ANSI escape sequence utility for Go language
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-ansi-%{commit}.tar.gz
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
