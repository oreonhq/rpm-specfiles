%global source0_hash 891d72bf6aab64d5debe474f29df0f4812a4c9d04216ef441a917cc4370985b3
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/nsf/termbox-go
Version:                1.1.2
%gometa
%global common_description %{expand:
Termbox is a library that provides a minimalistic API which allows the
programmer to write text-based user interfaces. The library is crossplatform and
has both terminal-based implementations on *nix operating systems and a winapi
console based implementation for windows operating systems. The basic idea is an
abstraction of the greatest common subset of features available on all major
terminals and other terminal-like APIs in a minimalistic fashion. Small API
means it is easy to implement, test, maintain and learn it, that's what makes
the termbox a distinct library in its area.}
%global golicenses      LICENSE
%global godocs          AUTHORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Pure Go termbox implementation
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/termbox-go-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/mattn/go-runewidth)
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
