%global source0_hash f745c5636d3fb59bffab5f9d2a745a94a9608166c20c90936fc66848a5e816e6
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/cheggaaa/pb.v1
%global forgeurl        https://github.com/cheggaaa/pb
Version:                1.0.28
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-cheggaaa-pb-devel < 1.0.26-3
Obsoletes:      golang-gopkg-cheggaaa-pb-1-devel < 1.0.26-3
}
%global common_description %{expand:
Simple progress bar for console programs.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Console progress bar for Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/pb-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/fatih/color)
BuildRequires:  golang(github.com/mattn/go-colorable)
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
