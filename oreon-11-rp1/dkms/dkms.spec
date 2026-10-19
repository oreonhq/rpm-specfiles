%global source0_hash a8032b3e4eb7cd86ae9b6ffd16fc4fda84c95fa47a0f5aa2010d872d0a5b0b5e
Summary:        Dynamic Kernel Module Support Framework
Name:           dkms
Version:        3.4.3
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/dkms-project/%{name}
BuildArch:      noarch
Source0:        https://github.com/%{name}-project/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       coreutils
Requires:       cpio
Requires:       elfutils-libelf-devel
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       gcc
Requires:       grep
Requires:       gzip
Requires:       kmod
Requires:       make
Requires:       patch
Requires:       sed
Requires:       tar
Requires:       which
Requires:       (kernel-64k-devel-matched if kernel-64k-core)
Requires:       (kernel-debug-devel-matched if kernel-debug-core)
Requires:       (kernel-devel-matched if kernel-core)
Requires:       (kernel-rt-devel if kernel-rt-core)
Requires:       (kernel-rt-debug-devel if kernel-rt-debug-core)
%{?systemd_ordering}
Recommends:     openssl
# oreon:deps
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This package contains the framework for the Dynamic Kernel Module Support (DKMS)
method for installing module RPMS as originally developed by Dell.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
make install-redhat \
    SBIN=%{_bindir} \
    DESTDIR=%{buildroot}
sed -i \
    -e 's/# modprobe_on_install.*/modprobe_on_install="true"/g' \
    -e 's/# post_transaction.*/post_transaction="dracut --regenerate-all --force"/g' \
    %{buildroot}%{_sysconfdir}/%{name}/framework.conf
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
