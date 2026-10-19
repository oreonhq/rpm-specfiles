%global source0_hash 8ea5979dfc5978c9690dc1dd533a830815441dd33617f4a61bcdff7d2c3c7e90
%global source1_hash none
%bcond check 1
%ifarch ppc64le
%global exp "-tags=exp.linuxppc64le"
%endif
%global goipath         github.com/go-delve/delve
Version:                1.27.2
%global common_description %{expand:
Delve is a debugger for the Go programming language. The goal of the project
is to provide a simple, full featured debugging tool for Go. Delve should be
easy to invoke and easy to use. Chances are if you're using a debugger, things
aren't going your way. With that in mind, Delve should stay out of your way as
much as possible.}
%global golang_arches x86_64 aarch64 ppc64le
%gometa
Name:           delve
Release:        1%{?dist}
Summary:        A debugger for the Go programming language
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://github.com/go-delve/delve/archive/refs/tags/v%{version}.tar.gz#/delve-%{version}.tar.gz
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  git
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  lsof
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%goprep -A
%global gomodulesmode GO111MODULE=on
GO111MODULE=on go mod vendor

%build

%gobuild %{?exp} -o %{gobuilddir}/bin/dlv %{goipath}/cmd/dlv
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
for d in $(go list %{?exp} ./... \
  | grep -v cmd \
  | grep -v scripts \
  | grep -v 'github.com/go-delve/delve/pkg/proc$' \
  | grep -v 'github.com/go-delve/delve/service/dap$' \
  | grep -v 'github.com/go-delve/delve/service/test$'); do
  go test %{?exp} ${d}
done
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.26.2-1
- Import
