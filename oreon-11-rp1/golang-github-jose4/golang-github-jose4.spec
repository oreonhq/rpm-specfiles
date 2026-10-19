%global source0_hash e4dfda530019fcdb4fc2525d31e810c753ecba264921c544d868cf71811209b3
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/go-jose/go-jose/v4
Version:                4.1.5
%gometa -L -f
%global common_description %{expand:
An implementation of JOSE standards (JWE, JWS, JWT) in Go.}
%global golicenses      LICENSE json-LICENSE
%global godocs          CHANGELOG.md CONTRIBUTING.md README.md SECURITY.md\\\
                        jose-util/README.md json-README.md
Name:           golang-github-jose4
Release:        1%{?dist}
Summary:        An implementation of JOSE standards (JWE, JWS, JWT) in Go
License:        BSD-3-Clause AND Apache-2.0
URL:            %{gourl}
Source0:        https://github.com/go-jose/go-jose/archive/v%{version}/go-jose-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

mv json/LICENSE json-LICENSE
mv json/README.md json-README.md
mv jose-util/README.md jose-util-README.md

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
