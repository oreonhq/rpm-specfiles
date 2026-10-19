%global source0_hash a3f513e988a6b1c38182478d57f5e60dc6c7331217d22c05a73de33baa553de8
%bcond doc 0
%global swaggerui_version 5.21.0
%global swaggerui_source_baseurl https://github.com/swagger-api/swagger-ui/raw/v%{swaggerui_version}/dist/
%bcond check 1
%global goipath github.com/lxc/incus
Version:        6.19.1
%gometa
%global godocs AUTHORS CODE_OF_CONDUCT.md CONTRIBUTING.md README.md SECURITY.md
%global golicenses COPYING
%define gocompilerflags_static -compiler gc
%define gobuild_baseflags_static %{gocompilerflags_static} -tags="rpm_crashtraceback ${GO_BUILDTAGS-${BUILDTAGS-}}" -a -v
%define gobuild_ldflags_static ${GO_LDFLAGS-${LDFLAGS-}} %{?currentgoldflags} -B 0x$(echo "%{name}-%{version}-%{release}-${SOURCE_DATE_EPOCH:-}" | sha1sum | cut -d ' ' -f1) -compressdwarf=false
%define gobuildflags_static() %{expand:%{gobuild_baseflags_static} -ldflags "%{gobuild_ldflags_static}"}
%define gobuild_static(-) %{expand:
  %{?gobuilddir:GOPATH="%{gobuilddir}:${GOPATH:+${GOPATH}:}%{?gopath}"} %{?gomodulesmode} \\
  CGO_ENABLED=0 go build %{gobuildflags_static} %{?**};
}
Name:           incus
Release:        1%{?dist}
Summary:        Powerful system container and virtual machine manager
License:        Apache-2.0
URL:            https://linuxcontainers.org/incus
Source0:        https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.xz
Source101:      %{name}.socket
Source102:      %{name}.service
Source103:      %{name}-startup.service
Source104:      %{name}-user.socket
Source105:      %{name}-user.service
Source106:      %{name}-sysusers.conf
Source107:      %{name}-tmpfiles.conf
Source108:      %{name}-dnsmasq.conf
Source109:      %{name}-sysctl.conf
Source110:      shutdown
Source111:      %{name}.fc
Source201:      %{swaggerui_source_baseurl}/swagger-ui-bundle.js#/swagger-ui-%{swaggerui_version}-bundle.js
Source202:      %{swaggerui_source_baseurl}/swagger-ui-standalone-preset.js#/swagger-ui-%{swaggerui_version}-standalone-preset.js
Source203:      %{swaggerui_source_baseurl}/swagger-ui.css#/swagger-ui-%{swaggerui_version}.css
Patch1002:      incus-0.2-doc-Remove-downloads-from-sphinx-build.patch
%global bashcompletiondir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || :)
%global selinuxtype targeted
%{?sysusers_requires_compat}
Requires:       %{name}-client = %{version}-%{release}
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
Requires:       attr
Requires:       dnsmasq
Requires:       iptables, ebtables
Requires:       (nftables if iptables-nft)
Requires:       lxcfs
Requires:       rsync
Requires:       shadow-utils
Requires:       squashfs-tools
Requires:       tar
Requires:       xdelta
Requires:       xz
%{?systemd_requires}
%ifnarch %{ix86} %{arm32}
Requires:       skopeo
%endif
%if %{with check}
%endif
Recommends:     %{name}-agent = %{version}-%{release}
Suggests:       %{name}-doc
# oreon:deps
BuildRequires:  btrfs-progs
BuildRequires:  dnsmasq
BuildRequires:  gettext
BuildRequires:  glibc-static
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  help2man
BuildRequires:  nftables
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(cowsql)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(lxc)
BuildRequires:  pkgconfig(raft)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Container hypervisor based on LXC
Incus offers a REST API to remotely manage containers over the network,
using an image based work-flow and with support for live migration.

This package contains the Incus daemon.

%pre

%sysusers_create_package %{name} %{SOURCE106}
%tmpfiles_create_package %{name} %{SOURCE107}
%post

%systemd_post %{name}.socket
%systemd_post %{name}.service
%systemd_post %{name}-startup.service
%systemd_post %{name}-user.socket
%systemd_post %{name}-user.service
%preun

%systemd_preun %{name}.socket
%systemd_preun %{name}.service
%systemd_preun %{name}-startup.service
%systemd_preun %{name}-user.socket
%systemd_preun %{name}-user.service
%postun

%systemd_postun_with_restart %{name}.socket
%systemd_postun_with_restart %{name}.service
%systemd_postun_with_restart %{name}-user.socket
%systemd_postun_with_restart %{name}-user.service
%package selinux
Summary:        Container hypervisor based on LXC - SELinux policy
BuildArch:      noarch
Requires:       container-selinux
Requires(post): container-selinux
BuildRequires:  selinux-policy-devel
%{?selinux_requires}
%description selinux
Incus offers a REST API to remotely manage containers over the network,
using an image based work-flow and with support for live migration.

This package contains the SELinux policy.

%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi
%posttrans selinux

%selinux_relabel_post -s %{selinuxtype}
%package client
Summary:        Container hypervisor based on LXC - Client
License:        Apache-2.0
Requires:       gettext
%description client
Incus offers a REST API to remotely manage containers over the network,
using an image based work-flow and with support for live migration.

This package contains the command line client.

%package tools
Summary:        Container hypervisor based on LXC - Extra Tools
License:        Apache-2.0
Requires:       incus%{?_isa} = %{version}-%{release}
Conflicts:      lxd-tools
%description tools
Incus offers a REST API to remotely manage containers over the network,
using an image based work-flow and with support for live migration.

This package contains extra tools provided with Incus.
 - fuidshift - A tool to map/unmap filesystem uids/gids
 - lxc-to-incus - A tool to migrate LXC containers to Incus
 - lxd-to-incus - A tool to migrate an existing LXD environment to Incus
 - incus-benchmark - A Incus benchmark utility
 - incus-migrate - A physical to container migration tool

%package agent
Summary:        Incus guest agent
License:        Apache-2.0
Requires:       incus%{?_isa} = %{version}-%{release}
Recommends:     edk2-ovmf
Recommends:     xorriso
Recommends:     qemu-char-spice
Recommends:     qemu-device-display-virtio-vga
Recommends:     qemu-device-display-virtio-gpu
Recommends:     qemu-device-usb-redirect
Recommends:     qemu-img
Recommends:     qemu-kvm-core
%description agent
This packages provides an agent to run inside Incus virtual machine guests.

It has to be installed on the Incus host if you want to allow agent
injection capability when creating a virtual machine.

%package doc
Summary:        Container hypervisor based on LXC - Documentation
License:        Apache-2.0 AND BSD-2-Clause AND MIT
BuildArch:      noarch
BuildRequires:  python3-furo
BuildRequires:  python3-linkify-it-py
BuildRequires:  python3-lxd-sphinx-extensions
BuildRequires:  python3-myst-parser
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-copybutton
BuildRequires:  python3-sphinx-design
BuildRequires:  python3-sphinx-notfound-page
BuildRequires:  python3-sphinx-remove-toctrees
BuildRequires:  python3-sphinx-reredirects
BuildRequires:  python3-sphinx-tabs
BuildRequires:  python3-sphinxcontrib-devhelp
BuildRequires:  python3-sphinxext-opengraph
%description doc
Incus offers a REST API to remotely manage containers over the network,
using an image based work-flow and with support for live migration.

This package contains user documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -k
%autopatch -v -p1

%build

export CGO_LDFLAGS_ALLOW="(-Wl,-wrap,pthread_create)|(-Wl,-z,now)"
for cmd in incusd incus-user; do
    BUILDTAGS="libsqlite3" %gobuild -o %{gobuilddir}/lib/$cmd %{goipath}/cmd/$cmd
done
for cmd in incus fuidshift incus-benchmark lxc-to-incus lxd-to-incus; do
    BUILDTAGS="libsqlite3" %gobuild -o %{gobuilddir}/bin/$cmd %{goipath}/cmd/$cmd
done
BUILDTAGS="netgo" %gobuild_static -o %{gobuilddir}/bin/incus-migrate %{goipath}/cmd/incus-migrate
BUILDTAGS="agent netgo" %gobuild_static -o %{gobuilddir}/bin/incus-agent %{goipath}/cmd/incus-agent
mkdir %{gobuilddir}/completions
%{gobuilddir}/bin/%{name} completion bash > %{gobuilddir}/completions/%{name}.bash
%{gobuilddir}/bin/%{name} completion fish > %{gobuilddir}/completions/%{name}.fish
%{gobuilddir}/bin/%{name} completion zsh > %{gobuilddir}/completions/%{name}.zsh
%if %{with docs}
mkdir -p doc/.sphinx/_static/swagger-ui
install -pm 0644 %{SOURCE201} doc/.sphinx/_static/swagger-ui/swagger-ui-bundle.js
install -pm 0644 %{SOURCE202} doc/.sphinx/_static/swagger-ui/swagger-ui-standalone-preset.js
install -pm 0644 %{SOURCE203} doc/.sphinx/_static/swagger-ui//swagger-ui.css
sed -i 's|^path.*$|path = "%{gobuilddir}"|' doc/conf.py
sphinx-build -c doc/ -b dirhtml doc/ doc/html/
rm -vrf doc/html/{.buildinfo,.doctrees}
rm -vrf doc/html/{_sources,_sphinx_design_static}
%endif
rm -f po/zh_Hans.po po/zh_Hant.po    # remove invalid locales
make %{?_smp_mflags} build-mo
mkdir %{gobuilddir}/man
%{gobuilddir}/bin/incus manpage %{gobuilddir}/man/
%{gobuilddir}/lib/incusd manpage %{gobuilddir}/man/
help2man %{gobuilddir}/bin/fuidshift -n "uid/gid shifter" --no-info --no-discard-stderr > %{gobuilddir}/man/fuidshift.1
help2man %{gobuilddir}/bin/incus-benchmark -n "The container lightervisor - benchmark" --no-info --no-discard-stderr > %{gobuilddir}/man/incus-benchmark.1
help2man %{gobuilddir}/bin/incus-migrate -n "Physical to container migration tool" --no-info --no-discard-stderr > %{gobuilddir}/man/incus-migrate.1
help2man %{gobuilddir}/bin/lxc-to-incus -n "Convert LXC containers to Incus" --no-info --no-discard-stderr > %{gobuilddir}/man/lxc-to-incus.1
help2man %{gobuilddir}/bin/lxd-to-incus -n "LXD to Incus migration tool" --no-info --no-discard-stderr > %{gobuilddir}/man/lxd-to-incus.1
help2man %{gobuilddir}/bin/incus-agent -n "Incus virtual machine guest agent" --no-info --no-discard-stderr > %{gobuilddir}/man/incus-agent.1
mkdir selinux
cp -p %{SOURCE111} selinux/
pushd selinux
echo 'policy_module(%{name},1.0)' >%{name}.te
%{__make} NAME=%{selinuxtype} -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 %{name}.pp
popd
%install
install -d %{buildroot}%{_bindir}
install -m0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -d %{buildroot}%{_unitdir}
install -m0644 -vp %{SOURCE101} %{buildroot}%{_unitdir}/
install -m0644 -vp %{SOURCE102} %{buildroot}%{_unitdir}/
install -m0644 -vp %{SOURCE103} %{buildroot}%{_unitdir}/
install -m0644 -vp %{SOURCE104} %{buildroot}%{_unitdir}/
install -m0644 -vp %{SOURCE105} %{buildroot}%{_unitdir}/
install -D -m0644 -vp %{SOURCE106} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m0644 -vp %{SOURCE107} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -m0644 -vp %{SOURCE108} %{buildroot}%{_sysconfdir}/dnsmasq.d/%{name}.conf
install -D -m0644 -vp %{SOURCE109} %{buildroot}%{_sysctldir}/10-incus-inotify.conf
install -D -m0644 -vp selinux/%{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -d %{buildroot}%{_libexecdir}/%{name}
install -m0755 -vp %{SOURCE110} %{buildroot}%{_libexecdir}/%{name}/
install -m0755 -vp %{gobuilddir}/lib/* %{buildroot}%{_libexecdir}/%{name}/
install -d %{buildroot}%{_mandir}/man1
cp -p %{gobuilddir}/man/*.1 %{buildroot}%{_mandir}/man1/
install -D -m0644 -vp %{gobuilddir}/completions/%{name}.bash %{buildroot}%{bashcompletiondir}/%{name}
install -D -m0644 -vp %{gobuilddir}/completions/%{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -D -m0644 -vp %{gobuilddir}/completions/%{name}.zsh %{buildroot}%{zsh_completions_dir}/_%{name}
install -d -m0700 %{buildroot}%{_localstatedir}/cache/%{name}
install -d -m0700 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0711 %{buildroot}%{_localstatedir}/lib/%{name}
for mofile in po/*.mo ; do
    install -D -m0644 -vp ${mofile} %{buildroot}%{_datadir}/locale/$(basename ${mofile%%.mo})/LC_MESSAGES/%{name}.mo
done
%find_lang incus
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

export GOPATH=%{buildroot}/%{gopath}:%{gopath}
export CGO_LDFLAGS_ALLOW="(-Wl,-wrap,pthread_create)|(-Wl,-z,now)"
%define gotestflags -buildmode pie -compiler gc -v -tags libsqlite3
%gocheck -v -t %{goipath}/test \
    -d %{goipath}/cmd/lxc-to-incus  # lxc-to-incus test fails, see ganto/copr-lxc4#23
%endif
%files -f %{oreon_filedir}/main.list
%files -n incus-selinux -f %{oreon_filedir}/incus-selinux.list
%files -n incus-client -f %{oreon_filedir}/incus-client.list
%files -n incus-tools -f %{oreon_filedir}/incus-tools.list
%files -n incus-agent -f %{oreon_filedir}/incus-agent.list

%changelog

%autochangelog
