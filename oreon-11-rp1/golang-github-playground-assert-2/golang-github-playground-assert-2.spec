%global source0_hash ca447aee4aa30f4284443d8fe4cd99b4b9cba62b8ed14f5dc4e289c74d90d748
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-playground/assert/v2
Version:                2.0.1
%gometa
%global goaltipaths     gopkg.in/go-playground/assert.v2
%global common_description %{expand:
Basic Assertion Library used along side native go testing, with building blocks
for custom assertions.}
Name:           %{goname}
Release:        1%{?dist}
Summary:        Basic Assertion Library used along side native go testing
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/go-playground/assert/archive/v%{version}/assert-%{version}.tar.gz
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
