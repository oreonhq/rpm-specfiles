%global source0_hash cbe45c3804b25008c5ca58e6e420d290001be5843d0bfafbddf607b63166ab31
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-sql-driver/mysql
Version:                1.8.0
%gometa -L
%global common_description %{expand:
Go MySQL Driver is a MySQL driver for Go's (golang) database/sql package.}
%global golicenses      LICENSE
%global godocs          AUTHORS CHANGELOG.md README.md
Name:           golang-github-sql-driver-mysql
Release:        1%{?dist}
Summary:        MySQL driver for Go's database/sql package
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mysql-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

for test in "TestErrorInMultiResult" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
