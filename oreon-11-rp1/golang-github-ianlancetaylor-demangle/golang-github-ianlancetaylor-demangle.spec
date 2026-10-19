%global source0_hash 16cdabfbf26e31f925e59471205b9c614ef00b0bf170eb46463a627bf6e24485
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/ianlancetaylor/demangle
%global commit          28f6c0f3b63983aaa99575ca3b693afff7996387
%gometa
%global common_description %{expand:
A Go package that can be used to demangle C++ symbol names.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        C++ symbol name demangler written in Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/demangle-%{commit}.tar.gz
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
