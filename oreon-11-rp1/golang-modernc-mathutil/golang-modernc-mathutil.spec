%global source0_hash 602dc5b237cccc99cc0486dc63c2c6b694ed059425dc06869093c6a5ecbfa8e0
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/mathutil
%global forgeurl        https://gitlab.com/cznic/mathutil
Version:                1.4.1
%global tag             v1.4.1
%gometa -f
%global common_description %{expand:
Utilities supplemental to the Go standard "rand" and "math" packages.}
%global golicenses      LICENSE LICENSE-mersenne
%global godocs          example AUTHORS CONTRIBUTORS AUTHORS-mersenne\\\
                        CONTRIBUTORS-mersenne README-mersenne
Name:           %{goname}
Release:        1%{?dist}
Summary:        Utilities supplemental to the Go standard "rand" and "math" packages
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/mathutil-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
mv mersenne/LICENSE LICENSE-mersenne
mv mersenne/AUTHORS AUTHORS-mersenne
mv mersenne/CONTRIBUTORS CONTRIBUTORS-mersenne
mv mersenne/README README-mersenne

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%if 0%{?__isa_bits} == 32
%gocheck -d mersenne
%else
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
