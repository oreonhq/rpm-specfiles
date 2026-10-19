%global source0_hash 98903a1993617c8692bc35cdbd1ed9577f1ea044fa476b0f378566ba8e52e56c
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with bootstrap
%if %{without bootstrap}
%bcond check 0
%else
%bcond check 1
%endif
%global goipath         github.com/containernetworking/cni
Version:                1.3.1
%gometa
%if %{without bootstrap}
%global goipaths0       %{goipath}
%global goipathsex0    %{goipath}/plugins/debug
%global godevelheader0  %{expand:
Obsoletes:      golang-github-containernetworking-cni-devel < 1.1.0-1}
%endif
%global goipaths1       %{goipath}/plugins/debug
%global godevelheader1  %{expand:
Obsoletes:      golang-github-containernetworking-cni-devel < 1.1.0-1}
%global common_description %{expand:
Container Network Interface - networking for Linux containers.}
%global golicenses      LICENSE
%global godocs          GOVERNANCE.md README.md CONTRIBUTING.md CODE-OF-\\\
                        CONDUCT.md CONVENTIONS.md RELEASING.md SPEC.md\\\
                        ROADMAP.md cnitool-README.md Documentation/cnitool.md\\\
                        Documentation/spec-upgrades.md\\\
                        plugins-debug-README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Container Network Interface - networking for Linux containers
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cni-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/cnitool %{goipath}/cnitool
%install
%gopkginstall
install -m 0755 -vd                           %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/cnitool %{buildroot}%{_bindir}/
mv plugins/debug/README.md plugins-debug-README.md
mv cnitool/README.md cnitool-README.md
%oreon_autofiles main
%if %{with check}
%check

rm -vf libcni/backwards_compatibility_test.go pkg/invoke/get_version_integration_test.go
%gocheck -d pkg/version/testhelpers
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
