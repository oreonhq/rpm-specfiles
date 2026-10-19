%global source0_hash 3e97e2bb7be3fa658cf68394a0f9c56a3f39b9c2e14b01efddb1c028e5376423
%global goipath         github.com/cri-o/cri-o
%global service_name    crio
%global build_timestamp %(date -u +'%Y-%m-%dT%H:%M:%SZ')
%global git_tree_state  clean
%global criocli_path    ""
Version:        1.37.1
%gometa
%bcond check 0
%global commit0 b7f3c240bcbda6fae8d43561694d18317e09e167
Name:           cri-o
Epoch:          0
Release:        1%{?dist}
Summary:        Open Container Initiative-based implementation of Kubernetes Container Runtime Interface
License:        Apache-2.0
URL:            https://github.com/cri-o/cri-o
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       container-selinux
Requires:       containers-common >= 1:0.1.31-14
Recommends:     runc >= 1.0.0-16
Suggests:       containernetworking-plugins >= 1.0.0-1
Requires:       conmon >= 2.0.2-1
Requires:       socat
Obsoletes:      ocid <= 0.3
Provides:       ocid = %{epoch}:%{version}-%{release}
Provides:       %{service_name} = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  glibc-static
BuildRequires:  go-md2man
BuildRequires:  go-rpm-macros
BuildRequires:  gpgme-devel
BuildRequires:  libassuan-devel
BuildRequires:  libseccomp-devel
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Open Container Initiative-based implementation of Kubernetes Container Runtime
Interface.

%prep

%goprep -k

sed -i 's/install.config: crio.conf/install.config:/' Makefile
sed -i 's/install.bin: binaries/install.bin:/' Makefile
sed -i 's/install.man: $(MANPAGES)/install.man:/' Makefile
sed -i 's/\.gopathok //' Makefile
sed -i 's/module_/module-/' internal/version/version.go
sed -i 's/\/local//' contrib/systemd/%{service_name}.service
sed -i 's/\/local//' contrib/systemd/%{service_name}-wipe.service

%build

%global __golang_extldflags -Wl,-z,undefs
export GO111MODULE=on
export GOFLAGS=-mod=vendor
export BUILDTAGS="containers_image_ostree_stub
$(hack/btrfs_installed_tag.sh)
$(hack/btrfs_tag.sh) $(hack/openpgp_tag.sh)
$(hack/seccomp_tag.sh) $(hack/selinux_tag.sh)
$(hack/libsubid_tag.sh) exclude_graphdriver_devicemapper"
export BASE_LDFLAGS="-X %{goipath}/internal/pkg/criocli.DefaultsPath=%{criocli_path}
-X  %{goipath}/internal/version.buildDate=%{build_timestamp}
-X  %{goipath}/internal/version.gitCommit=%{commit0}
-X  %{goipath}/internal/version.version=%{version}
-X  %{goipath}/internal/version.gitTreeState=%{git_tree_state} "
for cmd in cmd/* ; do
  %gobuild -o bin/$(basename $cmd) %{goipath}/$cmd
done
export CFLAGS="$CFLAGS -std=c99"
%make_build bin/pinns
GO_MD2MAN=go-md2man make docs
%install
sed -i 's/\/local//' contrib/systemd/%{service_name}.service
bin/%{service_name} \
      --selinux \
      --cni-plugin-dir /opt/cni/bin \
      --cni-plugin-dir "%{_libexecdir}/cni" \
      --enable-metrics \
      --metrics-port 9537 \
      config > %{service_name}.conf
install -dp %{buildroot}{%{_bindir},%{_libexecdir}/%{service_name}}
install -p -m 755 bin/%{service_name} %{buildroot}%{_bindir}
install -dp %{buildroot}%{_sysconfdir}/cni/net.d
install -p -m 644 contrib/cni/10-crio-bridge.conflist %{buildroot}%{_sysconfdir}/cni/net.d/100-crio-bridge.conflist
install -p -m 644 contrib/cni/99-loopback.conflist %{buildroot}%{_sysconfdir}/cni/net.d/200-loopback.conflist
install -dp %{buildroot}%{_sysconfdir}/%{service_name}
install -dp %{buildroot}%{_datadir}/containers/oci/hooks.d
install -dp %{buildroot}%{_datadir}/oci-umount/oci-umount.d
install -p -m 644 crio.conf %{buildroot}%{_sysconfdir}/%{service_name}
install -p -m 644 crio-umount.conf %{buildroot}%{_datadir}/oci-umount/oci-umount.d/%{service_name}-umount.conf
install -p -m 644 crictl.yaml %{buildroot}%{_sysconfdir}
%make_install PREFIX=%{buildroot}%{_prefix} \
            install.bin \
            install.completions \
            install.config \
            install.man \
            install.systemd
install -dp %{buildroot}%{_sharedstatedir}/containers
%oreon_autofiles main

%post

%systemd_post %{service_name}
%preun

%systemd_preun %{service_name}
%postun

%systemd_postun_with_restart %{service_name}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
