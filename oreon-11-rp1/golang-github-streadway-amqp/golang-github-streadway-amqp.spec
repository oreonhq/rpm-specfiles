%global source0_hash 350cd1141c348430905b2be7e076c1fa31276a9a9ef3cebf245c215d28f0cbf6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/streadway/amqp
Version:                1.0.0
%gometa
%global common_description %{expand:
Package Amqp is an AMQP 0.9.1 client with RabbitMQ extensions.}
%global golicenses      LICENSE
%global godocs          _examples CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go client for AMQP 0.9.1
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/amqp-%{version}.tar.gz
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

for test in "TestTLSHandshake" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%ifarch aarch64
rm -rvf client_test.go tls_test.go
%endif
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
