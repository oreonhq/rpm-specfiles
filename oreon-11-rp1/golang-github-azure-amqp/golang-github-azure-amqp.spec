%global source0_hash 215c3a84712b92519abd3e31fbcc9ee10fd8812cc86b1cb9249d620ea78d6693
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/Azure/go-amqp
Version:                1.7.0
%gometa
%global common_description %{expand:
github.com/Azure/go-amqp is an AMQP 1.0 client implementation for Go.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md\\\
                        SECURITY.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        AMQP 1.0 client library for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-amqp-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/fortytw2/leaktest)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(github.com/stretchr/testify)
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

%gocheck -d internal/encoding
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
