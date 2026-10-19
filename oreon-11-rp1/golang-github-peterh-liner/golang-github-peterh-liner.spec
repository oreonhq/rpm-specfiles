%global source0_hash 3c14c4eea1be82f4182bf7b0c6f064847333f3afbcfb8b8c1d1c0bb8b7ed65d9
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/peterh/liner
Version:                1.2.2
%gometa
%global common_description %{expand:
Liner is a command line editor with history. It was inspired by linenoise;
everything Unix-like is a VT100 (or is trying very hard to be). If your terminal
is not pretending to be a VT100, change it. Liner also support Windows.}
%global golicenses      COPYING
%global godocs          README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Pure go line editor with history, inspired by linenoise
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/liner-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/mattn/go-runewidth)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
