%global source0_hash 37d975b280d884ca0d55a800bc6e47314b6e86268e56254f9d15d19ca9404eb8
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-logr/stdr
Version:                1.2.2
%gometa -f
%global common_description %{expand:
Logr implementation against the stdlib log package.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Logr implementation against the stdlib log package
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/stdr-%{version}.tar.gz
Patch:          stdr-fix-expected-output.diff
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
