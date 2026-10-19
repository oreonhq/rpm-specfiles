%global source0_hash ef81c240412a5b77b164ae6570857b7a0f347770031a697764ba5167389842d8
%bcond check 1
%global crt_name                cri-tools1.33
%global crt_ver                 1.37.0
%global goipath         sigs.k8s.io/cri-tools
%global forgeurl        https://github.com/kubernetes-sigs/cri-tools
Version:                %{crt_ver}
%gometa -L -f
%global common_description %{expand:
CLI and validation tools for Kubelet Container Runtime Interface (CRI) .}
Name:           %{crt_name}
Release:        1%{?dist}
Summary:        CLI and validation tools for Kubelet Container Runtime Interface (CRI)
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/cri-tools-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Provides:       cri-tools = %{version}
Conflicts:      cri-tools
# oreon:deps
BuildRequires:  go-md2man
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
# %%autopatch -p1

%build

export GO_BUILDTAGS="selinux seccomp"
export GO_LDFLAGS="-X %{goipath}/pkg/version.Version=%{version}"
%gobuild -o %{gobuilddir}/bin/crictl %{goipath}/cmd/crictl
go-md2man -in docs/crictl.md -out docs/crictl.1
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -dp %{buildroot}%{_mandir}/man1
install -p -m 644 docs/crictl.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
