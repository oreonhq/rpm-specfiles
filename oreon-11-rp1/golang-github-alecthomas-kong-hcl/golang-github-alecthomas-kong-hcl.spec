%global source0_hash 5908bcd949e2c6b4d668ae4878371eecb86232ac05ea632c2c86ee2871afde4d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/alecthomas/kong-hcl
Version:                1.0.1
%gometa
%global common_description %{expand:
A Kong configuration loader for HCL.}
%global golicenses      COPYING
%global godocs          README.md
Name:           %{goname}
Epoch:          1
Release:        1%{?dist}
Summary:        Kong configuration loader for HCL
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/kong-hcl-%{version}.tar.gz
Patch0:         0001-Don-t-use-Kong-group-for-paths-for-v2.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/alecthomas/kong)
BuildRequires:  golang(github.com/hashicorp/hcl)
BuildRequires:  golang(github.com/hashicorp/hcl/v2)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/gohcl)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/hclparse)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/hclsyntax)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/zclconf/go-cty/cty)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

for test in "TestHCL" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
