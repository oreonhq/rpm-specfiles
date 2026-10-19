%global source0_hash 52d9e193dfa26eb5206ab92189c15a11c51e6d6e44a4fdd18c2119534218b2a8
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/weppos/publicsuffix-go
Version:                0.40.2
%gometa -L
%global common_description %{expand:
Domain name parser for Go based on the Public Suffix List.}
%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md
Name:           golang-github-weppos-publicsuffix
Release:        1%{?dist}
Summary:        Domain name parser for Go based on the Public Suffix List
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/publicsuffix-go-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

# Package generator downloads an updated version of the PSL list and compiles it into go code.
# It is meant to be used by maintainers in conjunction with the go generate tool
# to update the list.
# Removes dependency on github.com/google/go-github
rm -rf publicsuffix/generator

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
