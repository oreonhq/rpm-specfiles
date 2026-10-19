%global source0_hash e7ae8e6a8ea214bcf8836ce2bbf8428833a44c81aa13793225b751cb9412f6f3
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%bcond_with bootstrap
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         cloud.google.com/go
%global forgeurl        https://github.com/GoogleCloudPlatform/google-cloud-go
Version:                0.123.0
%global distprefix      %{nil}
%gometa
%global common_description %{expand:
Google Cloud Client Libraries for Go.}
%global golicenses      LICENSE
%global godocs          CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md RELEASING.md SECURITY.md testing.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Google Cloud Client Libraries for Go
License:        Apache-2.0 AND BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/google-cloud-go-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

%goprep
%autopatch -p1

find . ! \( -name internal -o -name civil -o -name "*.md" -o -name LICENSE -o -name _build \) -maxdepth 1 -exec rm -rf {} \;
# Remove modules requiring extra deps
rm -rf internal/postprocessor internal/gapicgen
# Remove generated snippets
rm -rf internal/generated

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%ifarch i686
for test in "TestTimestamp" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%endif
for test in "TestRetryPreserveError" "TestGolden" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -d cloud.google.com/go/internal/godocfx -d cloud.google.com/go/internal/postprocessor
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
