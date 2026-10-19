%global source0_hash e0914e2bce867bb6708e8ceb7ca7ece4c5a6473a873d0a5927943a932dbdd03e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/DATA-DOG/go-sqlmock
Version:                1.5.2
%gometa
%global goaltipaths     gopkg.in/DATA-DOG/go-sqlmock.v1
%global common_description %{expand:
Sqlmock is a mock library implementing sql/driver. Which has one and only
purpose - to simulate any sql driver behavior in tests, without needing a real
database connection. It helps to maintain correct TDD workflow.}
%global golicenses      LICENSE
%global godocs          examples README.md
%global gosupfiles      glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Sql mock driver for Golang to test database interactions
License:        BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-sqlmock-%{version}.tar.gz
Source1:        glide.lock
Source2:        glide.yaml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/kisielk/sqlstruct)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
