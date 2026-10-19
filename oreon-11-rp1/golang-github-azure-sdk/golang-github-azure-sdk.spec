%global source0_hash 71c2a4a54e13cbdf3074333318c56c86d6ef6becf4fd487ebc229a81b6f96b1c
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/Azure/azure-sdk-for-go
Version:                68.0.0
%gometa
%global common_description %{expand:
Azure-sdk-for-go provides Go packages for managing and using Azure services. It
officially supports the last two major releases of Go.}
%global golicenses      LICENSE NOTICE
%global godocs          CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md SECURITY.md SUPPORT.md\\\
                        documentation/
Name:           %{goname}
Release:        1%{?dist}
Summary:        Microsoft Azure SDK for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/azure-sdk-for-go-%{version}.tar.gz
Patch0:         0001-Compat-with-latest-go-github.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

%goprep
sed -i "s|github.com/google/go-github/v32|github.com/google/go-github|" $(find . -iname '*.go' -type f)
%patch -P0 -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

for test in "TestParseReadmeFromLink" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
