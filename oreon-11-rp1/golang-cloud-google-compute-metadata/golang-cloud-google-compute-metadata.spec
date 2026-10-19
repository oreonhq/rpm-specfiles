%global source0_hash none
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%global module compute/metadata
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         cloud.google.com/go/%{module}
%global forgeurl        https://github.com/GoogleCloudPlatform/google-cloud-go
Version:                0.3.0
%global tag             %{module}/v%{version}
%global distprefix      %{nil}
%gometa -L
%global common_description %{expand:
Google Cloud Client Libraries for Go  for module %{module}.}
%global golicenses      LICENSE
%global godocs          CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md RELEASING.md SECURITY.md testing.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Google Cloud Client Libraries for Go for module compute/metadata
License:        Apache-2.0 AND BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{tag}/google-cloud-go-compute-metadata-v%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

%goprep -A
%autopatch -p1
# As this is a submodule, use "-name compute" rather than module as in other specs
find . ! \( -name compute -o -name "*.md" -o -name LICENSE -o -name _build \) -maxdepth 1 -exec rm -rvf {} \;
mv compute/metadata/* .
rm -rfv compute

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

ln -s /usr/share/gocode/src/cloud.google.com/go/internal _build/src/cloud.google.com/go/
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
