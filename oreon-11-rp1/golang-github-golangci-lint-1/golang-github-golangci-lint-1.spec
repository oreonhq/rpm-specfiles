%global source0_hash a78e6aa0d62da377b65466cbbba708cec8290ca6c4a77b1c3d897d44043fe624
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/golangci/lint-1
%global commit          d2cdd8c0821928c61cb0903441f8b35457a98a61
%gometa
%global common_description %{expand:
Fork of the official Go linter with API enhancements}
%global golicenses      LICENSE
%global godocs          README.md CONTRIBUTING.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Fork of the official Go linter with API enhancements
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/lint-1-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/lint)
BuildRequires:  golang(golang.org/x/tools/go/ast/astutil)
BuildRequires:  golang(golang.org/x/tools/go/gcexportdata)
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
