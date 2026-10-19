%global source0_hash 56dc8d3883c765d9791a3698a55c66935b2978ac60e0e3c7c8799b182dd22bb5
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mitchellh/go-wordwrap
Version:                1.0.1
%gometa
%global common_description %{expand:
Go-wordwrap is a package for Go that automatically wraps words into multiple
lines. The primary use case for this is in formatting CLI output, but of course
word wrapping is a generally useful thing to do.}
%global golicenses      LICENSE.md
%global godocs          README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library for wrapping words in a string
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-wordwrap-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
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
