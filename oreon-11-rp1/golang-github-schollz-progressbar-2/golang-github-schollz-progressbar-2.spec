%global source0_hash 67825f1d650968d69d407c3b8a058df37a9887118b4c68f9acd744fa064b1ea1
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/schollz/progressbar/v2
%global forgeurl        https://github.com/schollz/progressbar
Version:                3.19.1
%gometa
%global common_description %{expand:
A very simple thread-safe progress bar which should work on every OS without
problems. I needed a progressbar for croc and everything I tried had problems,
so I made another one.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Basic thread-safe progress bar for Golang applications
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/progressbar-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/k0kubun/go-ansi)
BuildRequires:  golang(github.com/mitchellh/colorstring)
BuildRequires:  golang(github.com/stretchr/testify/assert)
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

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
