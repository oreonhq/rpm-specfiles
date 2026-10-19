%global source0_hash d8c77953bccf97b5983811e1bc79a528724307cb0c2509339f8da0b4af865888
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/ahmetb/go-linq/v3
Version:                3.2.0
%gometa -f
%global common_description %{expand:
.NET LINQ capabilities in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        .NET LINQ capabilities in Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://github.com/ahmetb/go-linq/archive/v%{version}/go-linq-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

rm -rfv example_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
