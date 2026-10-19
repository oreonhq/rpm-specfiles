%global source0_hash 078c3f5a9900e6a3f8fd49eb2305bd7d308ad64753fbd06c285fdaf7b9221fa1
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/kisielk/sqlstruct
%global commit          dae28ed3702399459ee08325d41622e4788d10f3
%gometa
%global common_description %{expand:
Sqlstruct provides some convenience functions for using structs with go's
database/sql package.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Convenience functions for using structs with Go's database/sql package
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/sqlstruct-%{commit}.tar.gz
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
