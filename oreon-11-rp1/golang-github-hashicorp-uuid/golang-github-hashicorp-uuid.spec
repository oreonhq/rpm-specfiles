%global source0_hash 13868e1f82015c5e2edd4fa34ea61990a60b4898bdd67a96cccfb0b799884ee1
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hashicorp/go-uuid
Version:                1.0.4
%gometa
%global common_description %{expand:
Generates UUID-format strings using high quality, purely random bytes. It is not
intended to be RFC compliant, merely to use a well-understood string
representation of a 128-bit value. It can also parse UUID-format strings into
their component bytes.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Generates uuid-format strings using purely high quality random bytes
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-uuid-%{version}.tar.gz
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
