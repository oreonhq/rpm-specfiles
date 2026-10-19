%global source0_hash 536af4ea7422e4cc2baaf053ca29b919f2c77d9016ad73196f6de1db4f2eb58a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mattn/go-tty
Version:                2.0.2
%gometa
%global common_description %{expand:
Simple tty utility.}
%global golicenses      LICENSE
%global godocs          _example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple tty utility
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-tty-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/mattn/go-colorable)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(golang.org/x/sys/unix)
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
