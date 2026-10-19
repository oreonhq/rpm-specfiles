%global source0_hash 64c5309cb5831fa341b6e2d0b154105491df555e3de15423e77f434def151227
%bcond check 1
%global with_debug   0
%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif
%global service_name            kubernetes
%global k8s_name                kubernetes1.33
%global k8s_ver                 1.33.10
%global k8s_minver              1.33
%global k8s_nextver             1.34
%global k8s_tag                 v1.33.10
%global golangver               1.24.13
%global _buildshell  /bin/bash
%global _checkshell  /bin/bash
%global goipath         k8s.io/kubernetes
%global forgeurl        https://github.com/kubernetes/kubernetes
Version:                %{k8s_ver}
%global tag             %{k8s_tag}
%gometa -L -f
%global common_description %{expand:
Production-Grade Container Scheduling and Management.}
Name:           %{k8s_name}
Release:        1%{?dist}
Summary:        Open Source Production-Grade Container Scheduling And Management Platform
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-3-Clause-HP AND CC-BY-4.0 AND ISC AND MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{k8s_tag}/%{service_name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source101:      kube-proxy.service
Source102:      kube-apiserver.service
Source103:      kube-scheduler.service
Source104:      kube-controller-manager.service
Source105:      kubelet.service
Source106:      environ-apiserver
Source107:      environ-config
Source108:      environ-controller-manager
Source109:      environ-kubelet
Source110:      environ-kubelet.kubeconfig
Source111:      environ-proxy
Source112:      environ-scheduler
Source113:      kubernetes-accounting.conf
Source114:      10-kubeadm.conf
Source117:      kubelet.env
Requires:       kubernetes-cni
Requires:       iptables >= 1.4.21
Requires:       util-linux
Recommends:     (cri-o%{k8s_minver} or containerd)
Conflicts:      cri-o < %{k8s_minver}
Conflicts:      cri-o >= %{k8s_nextver}
Recommends:     %{name}-client = %{version}-%{release}
Recommends:     %{name}-kubeadm = %{version}-%{release}
Conflicts:      %{name}-kubeadm < %{version}-%{release}
Conflicts:      %{name}-kubeadm > %{version}-%{release}
Conflicts:      %{name}-client < %{version}-%{release}
Conflicts:      %{name}-client > %{version}-%{release}
Provides:       kubernetes
Conflicts:      kubernetes
# oreon:deps
BuildRequires:  go-md2man
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  golang-github-cpuguy83-md2man
BuildRequires:  make
BuildRequires:  rsync
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{common_description}
Installs kubelet, the kubernetes agent on each machine in a
cluster. The kubernetes-client sub-package,
containing kubectl, is recommended but not strictly required.
The kubernetes-client sub-package should be installed on
control plane machines.

##############################################
%package  kubeadm
Summary:  Kubernetes tool for standing up clusters
Requires:       %{name} = %{version}-%{release}
Requires:       kubernetes-cni
Recommends:     cri-tools
Conflicts:      cri-tools < %{k8s_minver}
Conflicts:      cri-tools >= %{k8s_nextver}
Conflicts:      %{name} < %{version}-%{release}
Conflicts:      %{name} > %{version}-%{release}
Provides:       kubernetes-kubeadm
Conflicts:      kubernetes-kubeadm
%description kubeadm
%{common_description}
Installs kubeadm, a Kubernetes tool for standing up clusters. Not mandatory.
If used, install on each machine in the cluster. Used to initialize
each node, and to join new machines to an existing cluster.

##############################################
%package client
Summary: Kubernetes client tools
Conflicts:      %{name} < %{version}-%{release}
Conflicts:      %{name} > %{version}-%{release}
Provides:       kubernetes-client
Conflicts:      kubernetes-client
%description client
%{common_description}
Installs kubectl, the Kubernetes command line client used to
interact with a Kubernetes cluster.

##############################################
%package systemd
Summary: Systemd services for control plane and/or node
Requires: %{name} = %{version}-%{release}
Provides:       kubernetes-systemd
Conflicts:      kubernetes-systemd
%description systemd
%{common_description}
Systemd services needed for manual installation of Kubernetes
on control plane or node machines. If kubeadm is used to bootstrap
a Kubernetes cluster then this rpm is not needed as kubeadm will install
these services as static pods in the cluster on nodes as needed.
If these systemd services are used, enable all services except
kube-proxy on each control plane. Enable kube-proxy on all machines
nodes that runs kubelet, including control plane machines with
kubelet.

##############################################
##############################################
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

export FORCE_HOST_GO=y
export KUBE_GOPATH=%{gobuilddir}
export KUBE_OUTPUT_SUBPATH=_build
export KUBE_GIT_VERSION=v%{version}
%global k8s_overrides kube-proxy kubeadm kube-apiserver kube-controller-manager kubelet kube-scheduler kubectl
export KUBE_CGO_OVERRIDES="%{k8s_overrides}"
%global k8s_goflags -buildmode=pie -compiler=gc -tags=rpm_crashtraceback${BUILDTAGS:+,}${BUILDTAGS:-}
export GOFLAGS="%{k8s_goflags}"
%global k8s_goldflags %{?currentgoldflags} -B 0x$(echo '%{name}-%{version}-%{release}-${SOURCE_DATE_EPOCH:-}' | sha1sum | cut -d ' ' -f1) -compressdwarf=false -linkmode=external -extldflags '%{build_ldflags} %{?__golang_extldflags}'
export GOLDFLAGS="%{k8s_goldflags}"
%make_build WHAT="cmd/kube-proxy"
%make_build WHAT="cmd/kube-apiserver"
%make_build WHAT="cmd/kube-controller-manager"
%make_build WHAT="cmd/kubelet"
%make_build WHAT="cmd/kubeadm"
%make_build WHAT="cmd/kube-scheduler"
%make_build WHAT="cmd/kubectl"
source hack/update-generated-docs.sh
%install
%go_vendor_license_install -c %{S:2}
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} %{gobuilddir}/bin/kube-proxy
install -p -m 755 -t %{buildroot}%{_bindir} %{gobuilddir}/bin/kube-apiserver
install -p -m 755 -t %{buildroot}%{_bindir} %{gobuilddir}/bin/kube-controller-manager
install -p -m 755 -t %{buildroot}%{_bindir} %{gobuilddir}/bin/kubelet
install -p -m 755 -t %{buildroot}%{_bindir} %{gobuilddir}/bin/kubeadm
install -p -m 755 -t %{buildroot}%{_bindir} %{gobuilddir}/bin/kube-scheduler
install -p -m 755 -t %{buildroot}%{_bindir} %{gobuilddir}/bin/kubectl
echo "+++ INSTALLING kubelet service config"
install -d -m 0755 %{buildroot}/%{_unitdir}/kubelet.service.d
install -p -m 0644 -t %{buildroot}/%{_unitdir}/kubelet.service.d %{SOURCE114}
echo "+++ INSTALLING shell completion"
install -dm 0755 %{buildroot}/%{bash_completions_dir}
%{buildroot}%{_bindir}/kubectl completion bash > %{buildroot}/%{bash_completions_dir}/kubectl
install -dm 0755 %{buildroot}/%{fish_completions_dir}
%{buildroot}%{_bindir}/kubectl completion fish > %{buildroot}/%{fish_completions_dir}/kubectl.fish
install -dm 0755 %{buildroot}/%{zsh_completions_dir}
%{buildroot}%{_bindir}/kubectl completion zsh > %{buildroot}/%{zsh_completions_dir}/_kubectl
echo "+++ INSTALLING config files"
%define remove_environ_prefix() %(echo -n %1|sed 's/.*environ-//g')
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{service_name}
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{service_name}/manifests
install -m 644 -T %{SOURCE106} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE106}}
install -m 644 -T %{SOURCE107} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE107}}
install -m 644 -T %{SOURCE108} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE108}}
install -m 644 -T %{SOURCE109} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE109}}
install -m 644 -T %{SOURCE110} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE110}}
install -m 644 -T %{SOURCE111} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE111}}
install -m 644 -T %{SOURCE112} %{buildroot}%{_sysconfdir}/%{service_name}/%{remove_environ_prefix %{SOURCE112}}
install -d -m 0755 %{buildroot}%{_sysconfdir}/systemd/system.conf.d
install -p -m 0644 -t %{buildroot}%{_sysconfdir}/systemd/system.conf.d %{SOURCE113}
install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig/
install -p -m 0644 -T %{SOURCE117} %{buildroot}%{_sysconfdir}/sysconfig/kubelet
echo "+++ INSTALLING service files"
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE101}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE102}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE103}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE104}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE105}
echo "+++ INSTALLING manpages"
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 docs/man/man1/*.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_sharedstatedir}/kubelet
mv CHANGELOG/CHANGELOG-*.md .
rm CHANGELOG.md
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%go_vendor_license_check -c %{S:2}
if [ 1 != 1 ]; then
echo "******Testing the commands*****"
hack/test-cmd.sh
echo "******Benchmarking kube********"
hack/benchmark-go.sh
echo "******Testing the go code******"
hack/test-go.sh
echo "******Testing integration******"
hack/test-integration.sh --use_go_build
fi
%post systemd

%systemd_post kube-apiserver kube-scheduler kube-controller-manager kube-proxy
%preun systemd

%systemd_preun kube-apiserver kube-scheduler kube-controller-manager kube-proxy
%postun systemd

%systemd_postun kube-apiserver kube-scheduler kube-controller-manager kube-proxy
%post

%systemd_post kubelet
if [[ `systemctl show kubelet | grep -q -e CPUAccounting=no -e MemoryAccounting=no; echo $?` -eq 0 ]]; then
  systemctl daemon-reexec
fi
%preun

%systemd_preun kubelet
%postun

%systemd_postun kubelet
%files -f %{oreon_filedir}/main.list
%files -n kubernetes1.33-kubeadm -f %{oreon_filedir}/kubernetes1.33-kubeadm.list
%files -n kubernetes1.33-client -f %{oreon_filedir}/kubernetes1.33-client.list
%files -n kubernetes1.33-systemd -f %{oreon_filedir}/kubernetes1.33-systemd.list

%changelog

%autochangelog
