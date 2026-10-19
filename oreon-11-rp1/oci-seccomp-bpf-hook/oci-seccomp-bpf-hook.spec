%global source0_hash f8518ff7c16481d63b9d6d305cf5d666889da4ee5d0a7950189933f2825704ff
%global with_debug 1
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif
%global gomodulesmode GO111MODULE=on
Name: oci-seccomp-bpf-hook
Version: 1.2.10
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and MIT
Release:        1%{?dist}
ExclusiveArch: x86_64 %{power64} aarch64 s390x armv7hl
Summary:        OCI Hook to generate seccomp json files based on EBF syscalls used by container
URL: https://github.com/containers/%{name}
Source0:        https://github.com/containers/oci-seccomp-bpf-hook/archive/refs/tags/v1.2.10.tar.gz#/oci-seccomp-bpf-hook-1.2.10.tar.gz
Requires: bcc
Enhances: podman
Enhances: cri-o
# oreon:deps
BuildRequires:  bcc-devel
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel
BuildRequires:  go-md2man
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  gpgme-devel
BuildRequires:  libseccomp-devel
BuildRequires:  make
# /oreon:deps
%description
%{summary}
%{name} provides a library for applications looking to use
the Container Pod concept popularized by Kubernetes.

%package tests
Summary: Tests for %{name}
Requires: %{name} = %{version}-%{release}
Requires: bats
Requires: podman
%description tests
%{summary}

This package contains system tests for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n %{name}-%{version}
sed -i 's;HOOK_BIN_DIR;%{_libexecdir}/oci/hooks.d;' %{name}.json
sed -i '/$(HOOK_DIR)\/%{name}.json/d' Makefile

%build

%set_build_flags
export CGO_CFLAGS=$CFLAGS
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')
%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif
export LDFLAGS="-X main.version=%{version}"
%gobuild -o bin/%{name} .
%{__make} docs
%install
%{__make} DESTDIR=%{buildroot} PREFIX=%{_prefix} install.docs-nobuild install-nobuild
install -d -p %{buildroot}/%{_datadir}/%{name}/test/system
cp -pav test/. %{buildroot}/%{_datadir}/%{name}/test/system
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%if ! 0%{?gotest:1}
%global gotest go test
%endif
%gotest %{import_path}/src/%{name}
%endif
%{!?_licensedir:%global license %doc}
%files -f %{oreon_filedir}/main.list
%files -n oci-seccomp-bpf-hook-tests -f %{oreon_filedir}/oci-seccomp-bpf-hook-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.10-1
- Prepare for Oreon 11 (RP1)
