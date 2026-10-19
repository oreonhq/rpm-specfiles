%global source0_hash 8d97f26f393212abab99cd1a258bc338186df6686aa550c4830ac19e1658b855
%bcond check 0
%global debug_package %{nil}
%global goipath         gorm.io/gorm
%global forgeurl        https://github.com/go-gorm/gorm
Version:                1.20.11
%gometa
%global common_description %{expand:
The fantastic ORM library for Golang, aims to be developer friendly.}
%global golicenses      License
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        ORM library for Golang
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/gorm-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/jinzhu/inflection)
BuildRequires:  golang(github.com/jinzhu/now)
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
