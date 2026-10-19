%global source0_hash 9e1dcd513e28fac99e7b47fec38ce4f1969a9a9693b80619e9009286e2d0d584
%global source1_hash bf03f6a824e0079e8046916484f50d5b1a7fc92f95b8eae5d0840641a25496e4
%bcond check 1
%global goipath github.com/opencontainers/runc
Epoch:          2
Version:        1.4.2
%global tag     v%{gsub %{version} ~ -}
%gometa -L -f
Name:           runc
Release:        1%{?dist}
Summary:        CLI tool for spawning and running containers according to the OCI specification
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://github.com/opencontainers/runc/archive/refs/tags/v%{version}.tar.gz#/runc-%{version}.tar.gz
Source1:        runc-%{version}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Provides:       oci-runtime
Recommends:     container-selinux >= 2:2.85-1
%ifnarch s390x
Recommends:     criu
%endif
# oreon:deps
BuildRequires:  go-md2man
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  pkgconfig(libseccomp)
# /oreon:deps
%description
CLI tool for spawning and running containers according to the OCI
specification.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%goprep -p1
tar -xf %{SOURCE1}

%build

%global gomodulesmode GO111MODULE=on
export  GO_BUILDTAGS="seccomp urfave_cli_no_docs"
%gobuild -o %{gobuilddir}/bin/runc %{goipath}
man/md2man-all.sh
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -d -p                           %{buildroot}%{_mandir}/man8
install -m 0644 -vp man/man8/*.8        %{buildroot}%{_mandir}/man8/.
install -m 0755 -vd                     %{buildroot}/%{bash_completions_dir}
install -m 0644 -vp contrib/completions/bash/%{name} %{buildroot}/%{bash_completions_dir}
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck2 -t libcontainer/integration -t libcontainer/nsenter
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2:1.4.2-1
- Import
