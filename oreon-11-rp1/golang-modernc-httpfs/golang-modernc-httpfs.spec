%global source0_hash 7663974ca5408894b4018428e6f42c6562e6316e09a92f008ef8bb97815fa389
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/httpfs
%global forgeurl        https://gitlab.com/cznic/httpfs
Version:                1.0.6
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Implements http.FileSystem on top of a map[string]string.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Implements http.FileSystem on top of a map[string]string
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/httpfs-%{tag}.tar.bz2
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
