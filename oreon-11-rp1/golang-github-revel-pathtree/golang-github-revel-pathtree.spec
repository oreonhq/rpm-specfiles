%global source0_hash 0d83c0be26702a19bf4cb421bcb3258ad4d8d8bd108d4312e3564f3c8d9e4770
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/revel/pathtree
%global commit          41257a1839e945fce74afd070e02bab2ea2c776a
%gometa
%global common_description %{expand:
Pathtree implements a tree for fast path lookup.}
%global golicenses      LICENSE
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Tree for fast path lookup
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/pathtree-%{commit}.tar.gz
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
