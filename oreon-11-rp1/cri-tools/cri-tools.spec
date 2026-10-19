%global source0_hash ef81c240412a5b77b164ae6570857b7a0f347770031a697764ba5167389842d8
%global with_debug 1
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif
%global provider github
%global provider_tld com
%global project kubernetes-sigs
%global repo %{name}
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path %{provider_prefix}
Name: cri-tools
Version: 1.37.0
Release:        1%{?dist}
Summary:        CLI and validation tools for Container Runtime Interface
License: Apache-2.0
URL: https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch: %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
Provides: crictl = %{version}-%{release}
# oreon:deps
BuildRequires:  compiler(go-compiler)
BuildRequires:  glibc-static
BuildRequires:  go-md2man
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%global gomodulesmode GO111MODULE=on
export %{gomodulesmode}
export GOFLAGS="-mod=vendor"
export BUILDTAGS="selinux seccomp"
export GO_LDFLAGS="-X %{import_path}/pkg/version.Version=%{version}"
%gobuild -o bin/crictl %{import_path}/cmd/crictl
go-md2man -in docs/crictl.md -out docs/crictl.1
%install
install -dp %{buildroot}%{_bindir}
install -p -m 755 ./bin/crictl %{buildroot}%{_bindir}
install -dp %{buildroot}%{_mandir}/man1
install -p -m 644 docs/crictl.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%check

%{!?_licensedir:%global license %doc}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
