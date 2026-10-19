%global source0_hash e6fa7db2708320e66a1645bf6b234e524e73f4163ca0519b8608616e48f5d206
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/kr/pretty
Version:                0.3.1
%gometa
%global common_description %{expand:
Package pretty provides pretty-printing for go values. This is useful during
debugging, to avoid wrapping long output lines in the terminal.}
%global golicenses      License
%global godocs          Readme
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Pretty printing for go values
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pretty-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/kr/text)
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
