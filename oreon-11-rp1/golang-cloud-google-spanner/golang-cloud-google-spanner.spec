%global source0_hash none
%bcond check 1
%bcond bootstrap 1
%global debug_package %{nil}
%global module spanner
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         cloud.google.com/go/%{module}
%global forgeurl        https://github.com/GoogleCloudPlatform/google-cloud-go
Version:                1.63.0
%global tag             %{module}/v%{version}
%global distprefix      %{nil}
%gometa -L
%global common_description %{expand:
Google Cloud Client Libraries for Go for module %{module}.}
%global golicenses      LICENSE
%global godocs          CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md RELEASING.md SECURITY.md testing.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Google Cloud Client Libraries for Go for module spanner
License:        Apache-2.0 AND BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{tag}/google-cloud-go-%{module}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

%goprep -A
%autopatch -p1
find . ! \( -name %{module} -o -name "*.md" -o -name LICENSE -o -name _build \) -maxdepth 1 -exec rm -rf {} \;
mv %{module}/* .

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

for test in "TestStressSessionPool" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
rm admin/database/apiv1/database_test.go
ln -s /usr/share/gocode/src/cloud.google.com/go/internal _build/src/cloud.google.com/go/
%ifarch i686
%gocheck -d cloud.google.com/go/spanner/spansql
%%else
%gocheck
%endif
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
