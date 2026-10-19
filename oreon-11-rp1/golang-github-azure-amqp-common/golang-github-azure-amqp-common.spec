%global source0_hash 859afe1db25a44bba1d3845aa5325ddfc14087f00dc3cd3f23d883b88fe55e19
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/Azure/azure-amqp-common-go
Version:                4.2.0
%gometa
%global goaltipaths     github.com/Azure/azure-amqp-common-go/v3
%global common_description %{expand:
Azure AMQP abstractions for Golang contains common types and interfaces for use
in Service Bus and Event Hubs.
This project contains reusable components for AMQP based services like Event Hub
and Service Bus. You will find abstractions over authentication, claims-based
security, connection string parsing and RPC for AMQP.}
%global golicenses      LICENSE
%global godocs          README.md changelog.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Common types and interfaces for Service Bus and Event Hubs
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/azure-amqp-common-go-%{version}.tar.gz
Patch0001:      0001-Fix-build-with-Go-1.24.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/Azure/go-amqp)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires:  golang(github.com/devigned/tab)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/crypto/pkcs12)
# /oreon:deps
%description
%{common_description}

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
