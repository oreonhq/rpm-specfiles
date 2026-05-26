# PASST - Plug A Simple Socket Transport
#  for qemu/UNIX domain socket mode
#
# PASTA - Pack A Subtle Tap Abstraction
#  for network namespace/tap device mode
#
# Copyright (c) 2022 Red Hat GmbH
# Author: Stefano Brivio <sbrivio@redhat.com>

%global git_hash 386b5f5472b89769c025f5d5056348532a823b93
%global selinuxtype targeted
%global selinux_policy_version 41.41

Name:		passt
Version:	0^20260120.g386b5f5
Release:	1%{?dist}
Summary:	User-mode networking daemons for virtual machines and namespaces
License:	GPL-2.0-or-later AND BSD-3-Clause
Group:		System Environment/Daemons
URL:		https://passt.top/
Source:		https://passt.top/passt/snapshot/passt-%{git_hash}.tar.xz
# oreon url source checksums begin
%global source0_sha256 8a1452f19ebf7644baa29dbe07bfd7a264409afbc33fd759536f3a5c70973885
%global source0_file passt-386b5f5472b89769c025f5d5056348532a823b93.tar.xz
# oreon url source checksums end

BuildRequires:	gcc, make, checkpolicy, selinux-policy-devel
Requires:	(%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})

%description
passt implements a translation layer between a Layer-2 network interface and
native Layer-4 sockets (TCP, UDP, ICMP/ICMPv6 echo) on a host. It doesn't
require any capabilities or privileges, and it can be used as a simple
replacement for Slirp.

pasta (same binary as passt, different command) offers equivalent functionality,
for network namespaces: traffic is forwarded using a tap interface inside the
namespace, without the need to create further interfaces on the host, hence not
requiring any capabilities or privileges.

%package		    selinux
BuildArch:		    noarch
Summary:		    SELinux support for passt and pasta
%if 0%{?fedora} > 43
BuildRequires:      selinux-policy-devel
%selinux_requires_min
%else
BuildRequires:      pkgconfig(systemd)
Requires(post):     libselinux-utils
Requires(post):     policycoreutils
%endif
Requires:		    container-selinux
Requires:		    selinux-policy-%{selinuxtype}
Requires(post):		container-selinux
Requires(post):		selinux-policy-%{selinuxtype}

%description selinux
This package adds SELinux enforcement to passt(1), pasta(1), passt-repair(1).

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/passt-386b5f5472b89769c025f5d5056348532a823b93.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8a1452f19ebf7644baa29dbe07bfd7a264409afbc33fd759536f3a5c70973885" || { echo "oreon: Source0 SHA256 mismatch for passt-386b5f5472b89769c025f5d5056348532a823b93.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n passt-%{git_hash}

%build
%set_build_flags
# The Makefile creates symbolic links for pasta, but we need actual copies for
# SELinux file contexts to work as intended. Same with pasta.avx2 if present.
# Build twice, changing the version string, to avoid duplicate Build-IDs.
%make_build VERSION="%{version}-%{release}.%{_arch}-pasta"
mv -f passt pasta
%ifarch x86_64
mv -f passt.avx2 pasta.avx2
%make_build passt passt.avx2 VERSION="%{version}-%{release}.%{_arch}"
%else
%make_build passt VERSION="%{version}-%{release}.%{_arch}"
%endif

%install
# Already built (not as symbolic links), see above
touch pasta
%ifarch x86_64
touch pasta.avx2
%endif

%make_install DESTDIR=%{buildroot} prefix=%{_prefix} bindir=%{_bindir} mandir=%{_mandir} docdir=%{_docdir}/%{name}
%ifarch x86_64
ln -sr %{buildroot}%{_mandir}/man1/passt.1 %{buildroot}%{_mandir}/man1/passt.avx2.1
ln -sr %{buildroot}%{_mandir}/man1/pasta.1 %{buildroot}%{_mandir}/man1/pasta.avx2.1
install -p -m 755 %{buildroot}%{_bindir}/passt.avx2 %{buildroot}%{_bindir}/pasta.avx2
%endif

pushd contrib/selinux
make -f %{_datadir}/selinux/devel/Makefile
install -p -m 644 -D passt.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/passt.pp
install -p -m 644 -D passt.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/passt.if
install -p -m 644 -D pasta.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/pasta.pp
install -p -m 644 -D passt-repair.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/passt-repair.pp
popd

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/passt.pp %{_datadir}/selinux/packages/%{selinuxtype}/pasta.pp %{_datadir}/selinux/packages/%{selinuxtype}/passt-repair.pp

%postun selinux
if [ $1 -eq 0 ]; then
	%selinux_modules_uninstall -s %{selinuxtype} passt pasta passt-repair
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%files
%license LICENSES/{GPL-2.0-or-later.txt,BSD-3-Clause.txt}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/demo.sh
%{_bindir}/passt
%{_bindir}/pasta
%{_bindir}/qrap
%{_bindir}/passt-repair
%{_mandir}/man1/passt.1*
%{_mandir}/man1/pasta.1*
%{_mandir}/man1/qrap.1*
%{_mandir}/man1/passt-repair.1*
%ifarch x86_64
%{_bindir}/passt.avx2
%{_mandir}/man1/passt.avx2.1*
%{_bindir}/pasta.avx2
%{_mandir}/man1/pasta.avx2.1*
%endif

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/passt.pp
%{_datadir}/selinux/devel/include/distributed/passt.if
%{_datadir}/selinux/packages/%{selinuxtype}/pasta.pp
%{_datadir}/selinux/packages/%{selinuxtype}/passt-repair.pp

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0^20260120.g386b5f5-1
- Prepare for Oreon 11 (RP1)
