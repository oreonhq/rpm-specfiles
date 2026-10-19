%global source0_hash e919f59c2926ed19094b58833da80db3bddc1af8c623090475a86f8df7d655a1
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/opencontainers/go-digest
Version:                1.0.0
%global commit          bde1400a84bededaf764144a72cbd007a633196e
%gometa
%global common_description %{expand:
Package Digest provides a generalized type to opaquely represent message digests
and their operations within the registry. The Digest type is designed to serve
as a flexible identifier in a content-addressable system. More importantly, it
provides tools and wrappers to work with hash.Hash-based digests with little
effort.}
%global golicenses      LICENSE.docs LICENSE.code
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Common digest package used across the container ecosystem
License:        Apache-2.0 and CC-BY-SA-4.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-digest-%{commit}.tar.gz
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
