%global source0_hash d7bd7a700680486c419338972348b4c9cb3cb54384b3b2822e8c932d2b23e08b
%bcond check 1
%bcond bootstrap 1
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         google.golang.org/genproto
%global forgeurl        https://github.com/google/go-genproto
%global commit          ef581f913117b3bdd0edc13c9343ec2fc7db51d9
%gometa -L
%global common_description %{expand:
This package contains the generated Go packages for common protocol buffer
types, and the generated gRPC code necessary for interacting with Google's gRPC
APIs.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md\\\
                        RELEASING.md SECURITY.md example docs
%global gosupfiles      googleapis/example/library/v1/library.pb.go
Name:           golang-google-genproto
Version:        0
Release:        1%{?dist}
Summary:        Generated code for Google Cloud client libraries
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/go-genproto-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1
# These are managed with their own specs
rm -rf googleapis/api/apikeys googleapis/api/servicecontrol googleapis/api/servicemanagement googleapis/api/serviceusage

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
