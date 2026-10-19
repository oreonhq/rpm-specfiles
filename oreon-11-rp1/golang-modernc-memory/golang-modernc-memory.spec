%global source0_hash 59e562eb1e28aaa9dec53f3f5747470077fbfa42311baa8c4a4fe64c721bb968
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/memory
%global forgeurl        https://gitlab.com/cznic/memory
Version:                1.8.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
A memory allocator.}
%global golicenses      LICENSE LICENSE-GO LICENSE-MMAP-GO
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A memory allocator
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/memory-%{tag}.tar.bz2
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
