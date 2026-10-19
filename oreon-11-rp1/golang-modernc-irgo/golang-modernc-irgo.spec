%global source0_hash cd297a126b6550c87dc5fbd42866632937d06e3fad3e7995cf4acc192882b2ba
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/irgo
%global forgeurl        https://gitlab.com/cznic/irgo
Version:                1.0.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Translates intermediate representations to Go.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Translates intermediate representations to Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/irgo-%{tag}.tar.bz2
Patch0001:      irgo-v1.0.0-include-internal-buffer.patch
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
