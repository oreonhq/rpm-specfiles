%global source0_hash 8790d7a22c37cce00c9c9ed6b7ef00ca8f3a5c8d5b294d432d6339e794992a99
%bcond check 0
%global debug_package %{nil}
%global goipath         gitlab.com/yawning/edwards25519-extra.git
%global forgeurl        https://gitlab.com/yawning/edwards25519-extra
%global commit          def713fd18e464864613d2b55ef41a21df2c9493
%gometa -f
%global common_description %{expand:
This package provides extensions to the Go standard library's Ed25519 and
curve25519 implementations, primarily extracted from curve25519-voi.
This package is intended for interoperability with the standard library
and the edwards25519 package as much as possible.
}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Extensions to the Go standard library's Ed25519 and curve25519 implementations
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{commit}/edwards25519-extra-%{commit}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
