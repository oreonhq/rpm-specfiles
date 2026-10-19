%global source0_hash 4246cfa5aa2c6a48c82e0401969f976ebf92aabfddfb3cb4d31984ea2c140c8e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/RaveNoX/go-jsonmerge
Version:                1.0.0
%global commit          0828c736138271f2395cda9396066feb8f91c9d6
%gometa -f
%global common_description %{expand:
Merge JSON objects to one (replaces only existent values).}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Merge JSON objects to one (replaces only existent values)
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-jsonmerge-%{commit}.tar.gz
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
