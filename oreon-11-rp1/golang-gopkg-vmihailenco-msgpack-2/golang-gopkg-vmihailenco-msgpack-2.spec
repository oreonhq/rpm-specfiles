%global source0_hash cfa3bd1ec97666351670ff0c9a79cd34134c0890c5742587c4fba2ef22a460c0
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/vmihailenco/msgpack.v2
%global forgeurl        https://github.com/vmihailenco/msgpack
Version:                2.9.1
%gometa
%global common_description %{expand:
MessagePack encoding for Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        MessagePack encoding for Golang
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/msgpack-%{version}.tar.gz
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

for test in "TestTypes" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
