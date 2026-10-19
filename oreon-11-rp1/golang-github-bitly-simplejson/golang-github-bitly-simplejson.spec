%global source0_hash ef4c1cc5aa25a5d681b7cc22c6eac7d60efd705a1ac4da60e5d8fd7ab942db48
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/bitly/go-simplejson
Version:                0.5.1
%gometa
%global common_description %{expand:
A Go package to interact with arbitrary JSON.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A Go package to interact with arbitrary JSON
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-simplejson-%{version}.tar.gz
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
