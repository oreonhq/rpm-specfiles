%global source0_hash be5de3591ed05d08ec2d31bd98e255a45fecb735c615fe4e46036f8be26070a8
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mr-tron/base58
Version:                1.2.0
%gometa
%global common_description %{expand:
Fast implementation of base58 encoding on golang.}
%global golicenses      LICENSE
%global godocs          examples README.md base58/DEPRECATED.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast implementation of base58 encoding on golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/base58-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
