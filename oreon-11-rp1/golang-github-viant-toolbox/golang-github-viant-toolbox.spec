%global source0_hash 31f271114d2d320a25fc0a7213178a932a9c19e91baa99daa913900ecf075437
%ifnarch %{arm} %{ix86}
%bcond check 0
%endif
%bcond_with    bootstrap
%global debug_package %{nil}
%global goipath         github.com/viant/toolbox
Version:                0.33.2
%gometa
%global goipaths0       github.com/viant/toolbox
%global goipathsex0     github.com/viant/toolbox/url github.com/viant/toolbox/secret github.com/viant/toolbox/data/udf
%if %{without bootstrap}
%global goipaths1       github.com/viant/toolbox/url github.com/viant/toolbox/secret github.com/viant/toolbox/data/udf
%endif
%global common_description %{expand:
Toolbox - Go utility library.}
%global golicenses      LICENSE.txt NOTICE.txt
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go utility library
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/toolbox-%{version}.tar.gz
%if %{with check}
%endif
Patch0001:  0001-typo-in-service.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(cloud.google.com/go/storage)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/kms)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/ssm)
BuildRequires:  golang(github.com/go-errors/errors)
BuildRequires:  golang(github.com/lunixbochs/vtclean)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/crypto/blowfish)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(golang.org/x/oauth2/jwt)
BuildRequires:  golang(google.golang.org/api/cloudkms/v1)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(gopkg.in/yaml.v2)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0001 -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck %{?with_bootstrap:-d url -d secret -d data/udf -d kms/gcp -t storage} \
         -d . -d data
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
