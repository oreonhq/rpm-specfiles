%global source0_hash d9011a68a263eac8792b0cf1844188dd7a4468900d4413d87eeb80d2e679b7ff
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/lucasb-eyer/go-colorful
Version:                1.4.1
%gometa
%global common_description %{expand:
A library for playing with colors in Go.}
%global golicenses      LICENSE
%global godocs          doc README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Library for playing with colors in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-colorful-%{version}.tar.gz
%if %{with check}
%endif
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
