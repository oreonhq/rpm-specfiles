%global source0_hash none
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/jcmturner/gokrb5.v7
%global forgeurl        https://github.com/jcmturner/gokrb5
Version:                7.5.0
%gometa
%global goipathsex0     gopkg.in/jcmturner/gokrb5.v7/v8
%global common_description %{expand:
Pure Go Kerberos library for clients and services.}
%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md README.md USAGE.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Pure Go Kerberos library for clients and services
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/gokrb5-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/hashicorp/go-uuid)
BuildRequires:  golang(github.com/jcmturner/gofork/encoding/asn1)
BuildRequires:  golang(github.com/jcmturner/gofork/x/crypto/pbkdf2)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/crypto/md4)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(gopkg.in/jcmturner/aescts.v1)
BuildRequires:  golang(gopkg.in/jcmturner/dnsutils.v1)
BuildRequires:  golang(gopkg.in/jcmturner/goidentity.v3)
BuildRequires:  golang(gopkg.in/jcmturner/rpc.v1/mstypes)
BuildRequires:  golang(gopkg.in/jcmturner/rpc.v1/ndr)
# /oreon:deps
%description
%{common_description}

%prep

%goprep
rm -rf v8/

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
