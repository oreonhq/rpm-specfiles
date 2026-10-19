%global source0_hash 7658fec509ad0360a6d8906c0c3f987821d61fc79b70f8a3d266d68a3c358487
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mattn/go-zglob
Version:                0.0.8
%gometa
%global common_description %{expand:
a globbing utility}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        None
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-zglob-%{version}.tar.gz
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
