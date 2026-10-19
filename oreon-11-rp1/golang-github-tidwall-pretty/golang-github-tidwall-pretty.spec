%global source0_hash 820d92d4bb31a9f5a03f4168a5c4ff4ca50d8fd4a72bdf24257b5e4a0acf0ee5
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/tidwall/pretty
Version:                1.0.2
%gometa
%global common_description %{expand:
Pretty is a Go package that provides fast methods for formatting JSON for human
readability, or to compact JSON for smaller payloads.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Efficient JSON beautifier and compactor for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pretty-%{version}.tar.gz
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
