%global source0_hash cb181bba1015c6b0bb478c2d4507809e76f405dcde23793c14c8ecb347c58353
%if 0%{?el8}
%global python3 /usr/libexec/platform-python
%endif
Name:       mock-core-configs
Version:    44.2
Release:        1%{?dist}
Summary:        Mock core config files basic chroots
License:    GPL-2.0-or-later
URL:        https://github.com/rpm-software-management/mock/
Source0:        https://github.com/rpm-software-management/mock/releases/download/%{name}-%{version}-1/%{name}-%{version}.tar.gz
BuildArch:  noarch
Provides: mock-configs
Requires:   distribution-gpg-keys >= 1.117
Requires:   mock >= 6.1.test
Requires:   mock-filesystem
Requires(post): coreutils
Requires(post): python3-dnf
Requires(post): python3-hawkey
Requires(post): system-release
Requires(post): python3
Requires(post): sed
# oreon:deps

# /oreon:deps
%description
Mock configuration files which allow you to create chroots for Alma Linux,
Amazon Linux, CentOS, CentOS Stream, Circle Linux, EuroLinux, Fedora, Fedora EPEL, Mageia,
Navy Linux, OpenMandriva Lx, openSUSE, Oracle Linux, Red Hat Enterprise Linux,
Rocky Linux and various other specific or combined chroots.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/mock/eol/templates
mkdir -p %{buildroot}%{_sysconfdir}/mock/templates
cp -a etc/mock/*.cfg %{buildroot}%{_sysconfdir}/mock
cp -a etc/mock/templates/*.tpl %{buildroot}%{_sysconfdir}/mock/templates
cp -a etc/mock/eol/*cfg %{buildroot}%{_sysconfdir}/mock/eol
cp -a etc/mock/eol/templates/*.tpl %{buildroot}%{_sysconfdir}/mock/eol/templates
find %{buildroot}%{_sysconfdir}/mock -name "*.cfg" -o -name '*.tpl' \
    | grep -v chroot-aliases \
    | sed -e "s|^%{buildroot}|%%config(noreplace) |" >> %{name}.cfgs
echo "%%config %{_sysconfdir}/mock/chroot-aliases.cfg" >> %{name}.cfgs
ln -s fedora-rawhide-x86_64.cfg %{buildroot}%{_sysconfdir}/mock/default.cfg
if [ -d %{buildroot}%{_datadir}/bash-completion ]; then
    echo %{_datadir}/bash-completion/completions/mock >> %{name}.cfgs
    echo %{_datadir}/bash-completion/completions/mockchain >> %{name}.cfgs
elif [ -d %{buildroot}%{_sysconfdir}/bash_completion.d ]; then
    echo %{_sysconfdir}/bash_completion.d/mock >> %{name}.cfgs
fi
mock_docs=%{_pkgdocdir}
mock_docs=${mock_docs//mock-core-configs/mock}
mock_docs=${mock_docs//-%version/-*}
sed -i "s~@MOCK_DOCS@~$mock_docs~" %{buildroot}%{_sysconfdir}/mock/site-defaults.cfg
%oreon_autofiles main

%post

if [ -s /etc/os-release ]; then
    if grep -Fiq Rawhide /etc/os-release; then
        ver=rawhide
    elif [ -s /etc/mageia-release ]; then
        if grep -Fiq Cauldron /etc/mageia-release; then
           ver=cauldron
        fi
    else
        ver=$(source /etc/os-release && echo $VERSION_ID | cut -d. -f1 | grep -o '[0-9]\+')
    fi
else
    ver=%{?rhel}%{?fedora}%{?mageia}
fi
if [ -s /etc/mageia-release ]; then
    mock_arch=$(sed -n '/^$/!{$ s/.* \(\w*\)$/\1/p}' /etc/mageia-release)
else
    mock_arch=$(%{python3} -c "import dnf.rpm; import hawkey; print(dnf.rpm.basearch(hawkey.detect_arch()))")
fi
cfg=unknown-distro
%if 0%{?eln}
cfg=fedora-eln-$mock_arch.cfg
%endif
%if 0%{?mageia}
cfg=mageia-$ver-$mock_arch.cfg
%endif
if [ -e %{_sysconfdir}/mock/$cfg ]; then
    if [ "$(readlink %{_sysconfdir}/mock/default.cfg)" != "$cfg" ]; then
        ln -s $cfg %{_sysconfdir}/mock/default.cfg 2>/dev/null || ln -s -f $cfg %{_sysconfdir}/mock/default.cfg.rpmnew
    fi
else
    echo "Warning: file %{_sysconfdir}/mock/$cfg does not exist."
    echo "         unable to update %{_sysconfdir}/mock/default.cfg"
fi
:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
