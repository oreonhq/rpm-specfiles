%global source0_hash b965bdd43991f8e55bafb639f5939ad24a678c4e10a8d408413391cfc70ae54c
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/emersion/go-textwrapper
%global commit          65d896831594eccd3e87d83b845e25d3580e5a39
%gometa
%global common_description %{expand:
A writer that wraps long text lines to a specified length.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Writer that wraps long text lines to a specified length
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-textwrapper-%{commit}.tar.gz
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
