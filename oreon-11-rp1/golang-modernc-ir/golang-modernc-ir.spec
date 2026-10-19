%global source0_hash 764b8f75f89ecfd3f2c7ed2f8721ac53a68d18703d382f531d5a8f6890be62a0
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/ir
%global forgeurl        https://gitlab.com/cznic/ir
Version:                1.0.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Implements intermediate representation of compiled programs.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Implements intermediate representation of compiled programs
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/ir-%{tag}.tar.bz2
Patch0001:      ir-v1.0.0.0-include-internal-buffer.patch
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

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
