%global source0_hash 9e841283b1eaec9c28e3b6c3ea8c3f26b4cb10d44fe6778cb4591d7aa1ef8c93
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/certificate-transparency-go
Version:                1.3.3
%gometa
%global common_description %{expand:
Auditing for TLS certificates (Go code).}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md CHANGELOG.md CONTRIBUTORS\\\
                        README.md examples
Name:           %{goname}
Release:        1%{?dist}
Summary:        Auditing for TLS certificates, Go code
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/certificate-transparency-go-%{version}.tar.gz
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

for test in "TestRateLimiterGoroutines" \
            "TestSECP192R1" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%if 0%{?__isa_bits} == 32
%gocheck -d client -d loglist -d x509
%else
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
