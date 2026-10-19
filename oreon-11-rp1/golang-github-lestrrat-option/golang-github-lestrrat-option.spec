%global source0_hash aa5a15220481004a12841384feac3e130b3a4b93e0517b6c6c8305cf953f1b56
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/lestrrat-go/option
Version:                2.0.0
%gometa -f
%global common_description %{expand:
Base option type.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Base option type
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/option-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1
rm -rv cmd

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
