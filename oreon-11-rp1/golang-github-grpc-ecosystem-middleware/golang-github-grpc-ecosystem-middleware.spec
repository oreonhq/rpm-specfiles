%global source0_hash c0b837e6062f5e7fc289b34c68f133a76760bde82b190361c2c5fe64b520f62f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/grpc-ecosystem/go-grpc-middleware
Version:                2.3.4
%gometa
%global common_description %{expand:
gRPC Go recently acquired support for Interceptors, i.e. middleware that is
executed either on the gRPC Server before the request is passed onto the user's
application logic, or on the gRPC client either around the user call. It is a
perfect way to implement common patterns: auth, logging, message, validation,
retries or monitoring.
These are generic building blocks that make it easy to build multiple
microservices easily. The purpose of this repository is to act as a go-to point
for such reusable functionality. It contains some of them itself, but also will
link to useful external repos.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md DOC.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang gRPC Middlewares: interceptor chaining, auth, logging, retries and more
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-grpc-middleware-%{version}.tar.gz
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

%gocheck -d tags
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
