%global source0_hash f88c2cee5cc29bb7d32b51412ec7ca6ebad94835b899e0db5619e5f4e2a0acb3
%bcond check 0
%global goipath         github.com/onsi/ginkgo/v2
Version:                2.33.0
%gometa -f
%global common_description %{expand:
A Modern Testing Framework for Go.}
%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md README.md CONTRIBUTING.md\\\
                        RELEASING.md
Name:           golang-github-onsi-ginkgo-2
Release:        1%{?dist}
Summary:        A Modern Testing Framework for Go
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/onsi/ginkgo/archive/v%{version}/ginkgo-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/ginkgo %{goipath}/ginkgo
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d integration
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
