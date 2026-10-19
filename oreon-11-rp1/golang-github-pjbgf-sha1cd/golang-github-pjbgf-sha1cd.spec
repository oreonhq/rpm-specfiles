%global source0_hash dda27d0744ab0e561f24b799a7cc1239e4b5cc17fa7c98cc20101659a1557a47
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/pjbgf/sha1cd
Version:                0.6.0
%gometa -L -f
%global common_description %{expand:
SHA1 implementation with collision detection.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-pjbgf-sha1cd
Release:        1%{?dist}
Summary:        SHA1 implementation with collision detection
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/sha1cd-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
