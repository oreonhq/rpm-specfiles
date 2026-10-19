%global source0_hash f40b63ae731d140158baad46df1a4c35f2aacff033633278a0dba7e61d23eb72
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xlzd/gotp
Version:                0.1.0
%gometa -L
%global common_description %{expand:
Golang OTP(One-Time Password) Library.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           golang-github-xlzd-gotp
Release:        1%{?dist}
Summary:        Golang OTP(One-Time Password) Library
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gotp-%{version}.tar.gz
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
