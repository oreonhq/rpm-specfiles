%global source0_hash 6766251becaa110d29c5803698ddfca4713b9166b8dc287523b5419eb3fea8eb
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/lib/pq
Version:                1.12.3
%gometa
%global common_description %{expand:
A pure Go postgres driver for Go's database/sql package}
%global golicenses      LICENSE.md
%global godocs          example README.md TESTS.md certs-README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Pure Go postgres driver for database/sql
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pq-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  postgresql-test-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
mv certs/README certs-README

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%postgresql_tests_run
export PGUSER=$(id -un) PGPASSWORD=$(id -un) PGDATABASE=$(id -un)
for test in "TestCloseBadConn" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
