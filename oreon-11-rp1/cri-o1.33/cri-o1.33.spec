%global source0_hash f83a60924cac7b78ac180181aac7c7e3e8ac2be74d9eb52632b28a155ef34916
%bcond check 1
%global crio_spec_name  cri-o1.33
%global crio_spec_ver   1.37.1
%global crio_tag        v1.33.10
%global golangver       1.24.3
%global build_timestamp %(date -u +'%Y-%m-%dT%H:%M:%SZ')_Release:%{release}
%{?crio_commit:%global commit0 %{crio_commit}}
%global goipath           github.com/cri-o/cri-o
Version:                  %{crio_spec_ver}
%{!?commit0:%global tag   %{crio_tag}}
%gometa -L -f
%global common_description %{expand:
Open Container Initiative-based implementation of Kubernetes Container Runtime
Interface.}
Name:           %{crio_spec_name}
Release:        1%{?dist}
Summary:        Open Container Initiative-based implementation of Kubernetes Container Runtime Interface
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND Unlicense
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{crio_tag}/cri-o-1.33.10.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires(pre):  container-selinux
Requires:       containers-common >= 1:0.1.31-14
Recommends:     crun
Suggests:       containernetworking-plugins >= 1.0.0-1
Requires:       conmon >= 2.0.2-1
Requires:       socat
Requires:       iptables
Obsoletes:      ocid <= 0.3
Provides:       ocid = %{version}-%{release}
Provides:       crio = %{version}-%{release}
Conflicts:      crio
# oreon:deps
BuildRequires:  btrfs-progs-devel
BuildRequires:  conmon
BuildRequires:  crun
BuildRequires:  device-mapper-devel
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  glibc-static
BuildRequires:  go-md2man
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  gpgme-devel
BuildRequires:  iptables
BuildRequires:  libassuan-devel
BuildRequires:  libseccomp-devel
BuildRequires:  make
BuildRequires:  marshalparser
BuildRequires:  runc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description %{common_description}

# **********************************
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
# %%autopatch -p1

%build

%global __golang_extldflags -Wl,-z,undefs -Wl,-z,notext
%global buildtags  $(hack/btrfs_installed_tag.sh) $(hack/btrfs_tag.sh) $(hack/seccomp_tag.sh) $(hack/selinux_tag.sh) $(hack/libsubid_tag.sh) exclude_graphdriver_devicemapper
export GO_BUILDTAGS="%{buildtags}"
export GO_LDFLAGS=" -X  %{goipath}/internal/version.buildDate=%{build_timestamp} "
%global currentgoldflags   %{nil}
%gobuild -o %{gobuilddir}/bin/crio %{goipath}/cmd/crio
export CFLAGS="$CFLAGS -std=c99"
%make_build bin/pinns
GO_MD2MAN=go-md2man %make_build docs
%install
sed -i 's/\/local//' contrib/systemd/crio.service
%{gobuilddir}/bin/crio \
      --selinux \
      --cni-plugin-dir /opt/cni/bin \
      --cni-plugin-dir "%{_libexecdir}/cni" \
      --enable-metrics \
      --metrics-port 9537 \
      config > crio.conf
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                        %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/crio %{buildroot}%{_bindir}/
install -m 0755 -vp ./bin/pinns            %{buildroot}%{_bindir}/
install -m 0755 -vd                %{buildroot}%{_libexecdir}/crio
install -m 0755 -vd                %{buildroot}%{_sharedstatedir}/containers
echo "+++ INSTALLING shell completion"
install -d -m 0755    %{buildroot}%{bash_completions_dir}
install -D -m 0644 -t %{buildroot}%{bash_completions_dir} ./completions/bash/crio
install -d -m 0755    %{buildroot}%{fish_completions_dir}
install -D -m 0644 -t %{buildroot}%{fish_completions_dir} ./completions/fish/crio.fish
install -d -m 0755    %{buildroot}%{zsh_completions_dir}
install -D -m 0644 -t %{buildroot}%{zsh_completions_dir} ./completions/zsh/_crio
echo "+++ INSTALLING config files"
install -d -m 0755    %{buildroot}%{_sysconfdir}
install -D -m 0644 -t %{buildroot}%{_sysconfdir}  crictl.yaml
install -dp %{buildroot}%{_sysconfdir}/cni/net.d
install -p -m 0644 contrib/cni/10-crio-bridge.conflist %{buildroot}%{_sysconfdir}/cni/net.d/100-crio-bridge.conflist
install -p -m 0644 contrib/cni/99-loopback.conflist %{buildroot}%{_sysconfdir}/cni/net.d/200-loopback.conflist
echo "+++ INSTALLING service files"
install -d -m 0755 %{buildroot}%{_sysconfdir}/crio
install -dp %{buildroot}%{_datadir}/containers/oci/hooks.d
install -dp %{buildroot}%{_datadir}/oci-umount/oci-umount.d
install -p -m 0644 crio.conf %{buildroot}%{_sysconfdir}/crio
install -p -m 0644 crio-umount.conf %{buildroot}%{_datadir}/oci-umount/oci-umount.d/crio-umount.conf
echo "+++ INSTALLING systemd files"
install -d -m 0755 %{buildroot}%{_unitdir}
install -p -m 0644 contrib/systemd/crio.service %{buildroot}%{_unitdir}/crio.service
install -p -m 0644 contrib/systemd/crio-wipe.service %{buildroot}%{_unitdir}/crio-wipe.service
echo "+++ INSTALLING manpages"
install -d -m 0755 %{buildroot}%{_mandir}/man5
install -p -m 0644 docs/*.5 %{buildroot}%{_mandir}/man5
install -d -m 0755 %{buildroot}%{_mandir}/man8
install -p -m 0644 docs/*.8 %{buildroot}%{_mandir}/man8
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
TEST_TAGS=$((echo "test rpm_crashtraceback %{buildtags}") | sed -e 's/\s\+/,/g')
%global gotestflags     %{gocompilerflags} -tags $TEST_TAGS${GO_MOD_VENDOR:+,$GO_MOD_VENDOR}
%gocheck -t test/nri -t internal/factory/container -t internal/oci -t server
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
