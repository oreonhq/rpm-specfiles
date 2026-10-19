%global source0_hash ab9fecc6048ba1e583fdeb348913c6a3ec32c1164e22d411ecd6bd20f2e189a2
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/scanner
%global forgeurl        https://gitlab.com/cznic/scanner
Version:                1.1.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Package scanner provides some common scanner stuff.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package scanner provides some common scanner stuff
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/scanner-%{tag}.tar.bz2
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
