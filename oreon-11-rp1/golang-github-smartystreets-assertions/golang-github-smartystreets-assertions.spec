%global source0_hash 88be7f12190d1ceba0d57edd18dc9a40e670ba38c9db8c541d8f4be5af7a2ee1
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/smartystreets/assertions
Version:                1.16.0
%gometa
%global common_description %{expand:
Package assertions contains the implementations for all assertions which are
referenced in goconvey's convey package and gunit for use with the So(...)
method. They can also be used in traditional Go test functions and even in
applications.}
%global golicenses      LICENSE.md
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Epoch:          1
Release:        1%{?dist}
Summary:        Fluent assertion-style functions used by goconvey and gunit
License:        Apache-2.0 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/assertions-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d internal/go-render/render
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
