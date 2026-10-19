%global source0_hash f57dc468339505a0ce7f248cbec13af5fd492cd7a885c50af70d9786144f4f91
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/docker/libtrust
%global commit          aabc10ec26b754e797f9028f4589c5b7bd90dc20
%gometa
%global common_description %{expand:
Libtrust is library for managing authentication and authorization using public
key cryptography.
Authentication is handled using the identity attached to the public key.
Libtrust provides multiple methods to prove possession of the private key
associated with an identity:
 - TLS x509 certificates
 - Signature verification
 - Key Challenge
Authorization and access control is managed through a distributed trust graph.
Trust servers are used as the authorities of the trust graph and allow caching
portions of the graph for faster access.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Primitives for identity and authorization
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/libtrust-%{commit}.tar.gz
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
