%global source0_hash 053a61c4b0d78e6978600c99562f04d053993c428d549a20b627151cf1aabbae
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/Masterminds/goutils
Version:                1.1.0
%gometa
%global common_description %{expand:
GoUtils is a Go implementation of some string manipulation libraries of Apache
Commons. This is an open source project aimed at providing Go users with
utility functions to manipulate strings in various ways.}
%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        String manipulation libraries of Apache Commons
License:        ASL 2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/goutils-%{version}.tar.gz
Patch0:         0001-Explicitly-convert-digits-to-runes-before-strings.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

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
