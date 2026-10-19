%global source0_hash 136b36bd1087c38bb3202bb3b0421c241bde06f4aa6325da4d5dc03a23e68d1d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/opencontainers/runtime-spec
Version:                1.3.0
%gometa
%global common_description %{expand:
OCI Runtime Specification.}
%global golicenses      LICENSE
%global godocs          ChangeLog GOVERNANCE.md README.md RELEASES.md\\\
                        bundle.md config-linux.md config-solaris.md config-\\\
                        vm.md config-windows.md config-zos.md config.md\\\
                        features-linux.md features.md glossary.md\\\
                        implementations.md principles.md runtime-linux.md\\\
                        runtime.md spec.md style.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        OCI Runtime Specification
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/runtime-spec-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
