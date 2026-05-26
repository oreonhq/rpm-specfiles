# defining macros needed by SELinux
%global selinuxtype targeted
%global selinux_policyver 3.14.3-22
%global moduletype contrib
%global modulename tabrmd

Name: tpm2-abrmd-selinux
Version: 2.3.1
Release: 15%{?dist}
Summary: SELinux policies for tpm2-abrmd

License: BSD-2-Clause
URL:     https://github.com/tpm2-software/tpm2-abrmd
Source0: https://github.com/tpm2-software/tpm2-abrmd/archive/%{version}/tpm2-abrmd-%{version}.tar.gz

Patch0: selinux-allow-fwupd-to-communicate-with-tpm2-abrmd.patch
# oreon url source checksums begin
%global source0_sha256 dade3fffa441b75a0d2dc216ac8fbf8a392e5b85344bfb618bd6d02216177bb3
%global source0_file tpm2-abrmd-2.3.1.tar.gz
# oreon url source checksums end

BuildArch: noarch
Requires: selinux-policy >= %{selinux_policyver}
BuildRequires: make
BuildRequires: git
BuildRequires: pkgconfig(systemd)
BuildRequires: selinux-policy
BuildRequires: selinux-policy-devel
BuildRequires: selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-base >= %{selinux_policyver}
Requires(post): libselinux-utils
Requires(post): policycoreutils
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires(post): policycoreutils-python-utils
%else
Requires(post): policycoreutils-python
%endif

%description
SELinux policy modules for tpm2-abrmd.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/tpm2-abrmd-2.3.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "dade3fffa441b75a0d2dc216ac8fbf8a392e5b85344bfb618bd6d02216177bb3" || { echo "oreon: Source0 SHA256 mismatch for tpm2-abrmd-2.3.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n tpm2-abrmd-%{version}

%build
pushd selinux
make %{?_smp_mflags} TARGET="tabrmd" SHARE="%{_datadir}"
popd

%pre
%selinux_relabel_pre -s %{selinuxtype}

%install
# install policy modules
pushd selinux
install -d %{buildroot}%{_datadir}/selinux/packages
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -p -m 644 %{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages
popd

%check

%post
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp.bz2

%postun
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans
%selinux_relabel_post -s %{selinuxtype}

%files
%license LICENSE
%{_datadir}/selinux/*
%{_datadir}/selinux/packages/%{modulename}.pp.bz2
%{_datadir}/selinux/devel/include/%{moduletype}/%{modulename}.if

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.1-15
- Prepare for Oreon 11 (RP1)
