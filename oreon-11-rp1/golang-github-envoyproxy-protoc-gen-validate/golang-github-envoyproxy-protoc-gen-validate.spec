%global source0_hash 9e47ef41ec0e269a173a94b6766cc4be4e1a1098fcda040b2f0441c51bfb6ae2
%bcond check 0
%global goipath         github.com/envoyproxy/protoc-gen-validate
Version:                1.3.3
%gometa
%global common_description %{expand:
Protoc plugin to generate polyglot message validators.}
%global golicenses      LICENSE NOTICE
%global godocs          CODE_OF_CONDUCT.md requirements.txt\\\
                        rule_comparison.md README.md java/RELEASING.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Protoc plugin to generate polyglot message validators
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/protoc-gen-validate-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/protoc-gen-validate %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
