%global source0_hash 99ea568b59bf402793540cbd821dbf81ed12c22ab663433089e6a38d54248f27
%bcond check 0
%global debug_package %{nil}
%global goipath         bitbucket.org/ww/goautoneg
%global commit          75cd24fc2f2c2a2088577d12123ddee5f54e0675
%global scm             hg
%gometa
%global common_description %{expand:
HTTP Content-Type Autonegotiation.}
%global golicenses      LICENSE
%global godocs          README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        HTTP Content-Type Autonegotiation
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/get/%{commit}.tar.bz2#/ww-goautoneg-75cd24fc2f2c.tar.bz2
Source1:        glide.lock
Source2:        glide.yaml
Patch0:         move-license-to-LICENSE.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1
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
