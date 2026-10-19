%global source0_hash f85d81da7bea87f98eabd5753935fbf81501ca83d8c40f5f90dca2d29bbf2827
%bcond tests 1
%bcond docs 1
%bcond obs 0
Name:           mkosi
Version:        27
Release:        1%{?dist}
Summary:        Create bespoke OS images
License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/mkosi
Source0:        https://github.com/systemd/mkosi/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{without obs}
Patch:          0001-verity-do-not-copy-signing-cert-in-addons-portables-.patch
%endif
BuildArch:      noarch
%global __brp_compress true
%if %{with docs}
%endif
%if %{undefined suse_version}
Requires:       python3
Requires:       coreutils
%else
%define pythons python3
Requires:       python3 >= 3.9
%endif
%if %{with obs}
Requires:       %{name}-system-deps = %{version}-%{release}
%endif
%if %{defined suse_version}
%global bash_completions_dir %{_datadir}/bash-completion/completions
%global fish_completions_dir %{_datadir}/fish/completions
%global zsh_completions_dir %{_datadir}/zsh/site-functions
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkosi = %{version}-%{release}
# /oreon:deps
%package -n       python3-mkosi+bootable
Summary:        Metapackage for python3-mkosi bootable extras
Requires:       python3-mkosi = %{version}-%{release}
Requires:       python3dist(pefile) >= 2021.9.3
Provides:       python3dist(mkosi[bootable]) = %{version}-%{release}

%description -n python3-mkosi+bootable
Metapackage for python3-mkosi bootable extras.

%description
A fancy wrapper around "dnf --installroot", "apt", "pacman", and "zypper" that
generates disk images with a number of bells and whistles.

Generated images are tailored to the purpose: GPT partitions,
systemd-boot or grub2, images for containers, VMs, initrd, and extensions.

Mkosi can boot an image via QEMU or systemd-nspawn, or simply start a shell in
chroot, burn the image to a device, connect to a running VM via ssh, extract
logs and coredumps, serve an image over HTTP and more.

See https://mkosi.systemd.io/ for documentation.

%package initrd
Summary:       Build initrds locally using mkosi
Requires:      %{name} = %{version}-%{release}
Requires:      (dnf5 or dnf)
%description initrd
This package provides the CLI and the plugin for kernel-install to build
initrds with mkosi locally.

After the package is installed, the plugin can be enabled by writing
'initrd_generator=mkosi-initrd' to '/etc/kernel/install.conf'.

%package addon
Summary:       Build PE addons locally using mkosi
Requires:      %{name} = %{version}-%{release}
%description addon
This package provides the CLI and the plugin for kernel-install to build
PE addons for distribution-signed unified kernel images with mkosi locally.

After the package is installed, the plugin can be enabled by adding
configuration for the addon to `/etc/mkosi-addon` or `/run/mkosi-addon`.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%if %{undefined suse_version}
%build

%if %{with docs}
tools/make-man-page.sh
%endif
%pyproject_wheel
bin/mkosi completion bash >mkosi.bash
bin/mkosi completion fish >mkosi.fish
bin/mkosi completion zsh >mkosi.zsh
%install
%pyproject_install
%if %{undefined suse_version}
%endif
{
  bin/mkosi dependencies | sed -e 's/^/Recommends: /'
  echo "Recommends:    less"
  echo "%package system-deps"
  echo "Summary:       Pull in additional dependencies needed to build images"
  bin/mkosi dependencies | sed -e 's/^/Requires: /'
  echo "Requires:      efitools"
  echo "Requires:      jq"
  echo "Requires:      pesign"
  echo "%description system-deps"
  echo "This package pulls in all the dependencies needed to build images."
  echo "%files system-deps"
} >%{specpartsdir}/mkosi.specpart
%if %{defined suse_version}
export NO_BRP_STALE_LINK_ERROR=yes
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/mkosi
%endif
%if %{with docs}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man7
ln -s -t %{buildroot}%{_mandir}/man1/ \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi.1 \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi-sandbox.1 \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi-initrd.1 \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi-addon.1
ln -s -t %{buildroot}%{_mandir}/man7/ \
         ../../../..%{python3_sitelib}/mkosi/resources/man/mkosi.news.7
%endif
install -Dt %{buildroot}%{_prefix}/lib/kernel/install.d/ \
         kernel-install/50-mkosi.install
mkdir -p %{buildroot}%{_prefix}/lib/mkosi-initrd
mkdir -p %{buildroot}%{_sysconfdir}/mkosi-initrd
install -Dt %{buildroot}%{_prefix}/lib/kernel/install.d/ \
         kernel-install/51-mkosi-addon.install
mkdir -p %{buildroot}%{_prefix}/lib/mkosi-addon
mkdir -p %{buildroot}%{_sysconfdir}/mkosi-addon
install -m0644 -D mkosi.bash %{buildroot}%{bash_completions_dir}/mkosi
install -m0644 -D mkosi.fish %{buildroot}%{fish_completions_dir}/mkosi.fish
install -m0644 -D mkosi.zsh %{buildroot}%{zsh_completions_dir}/_mkosi
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{undefined suse_version}
%check

%if %{with tests}
%pytest tests/ -v
%if %{undefined suse_version}
%py3_test_envvars %{buildroot}%{_bindir}/mkosi --help >/dev/null
%endif
%endif
%clean
rm -rf \
    $RPM_BUILD_ROOT \
    mkosi.bash \
    mkosi.zsh \
    mkosi.fish \
    mkosi/resources/man/*.1 \
    mkosi/resources/man/*.7
%files
%files -n mkosi-initrd -f %{oreon_filedir}/mkosi-initrd.list
%files -n mkosi-addon -f %{oreon_filedir}/mkosi-addon.list

%changelog

%autochangelog
%endif
%endif
