%global source0_hash e17eeaba48ea8c1d5d127eaac3b753d24b8f00152253b5c2a0a43e3a5f83a46c
%global git_date 20251128
%global git_commit 19878fea4c5f62208655e32269842bce55c819b2
%{?git_commit:%global git_commit_hash %(c=%{git_commit}; echo ${c:0:7})}
%global _python_bytecompile_extra 0
%define rpmstatedir %{_localstatedir}/lib/rpm-state/%{name}
%define rpmstate_autopolicy %{rpmstatedir}/autopolicy-reapplication-needed
Name:           crypto-policies
Version:        %{git_date}
Release:        1%{?dist}
Summary:        System-wide crypto policies
License:        LGPL-2.1-or-later
URL:            https://gitlab.com/redhat-crypto/fedora-crypto-policies
Source0:        https://gitlab.com/redhat-crypto/fedora-%{name}/-/archive/19878fe/%{name}-git19878fe.tar.gz
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Conflicts: openssl-libs < 1:3.5.0-1
Conflicts: nss < 3.105
Conflicts: libreswan < 3.28
Conflicts: openssh < 9.9
Conflicts: gnutls < 3.8.10
Recommends: crypto-policies-scripts
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  bind
BuildRequires:  gnutls-utils
BuildRequires:  java-25-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  nss-tools
BuildRequires:  openssh-clients
BuildRequires:  openssl
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  sequoia-policy-config
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This package provides pre-built configuration files with
cryptographic policies for various cryptographic back-ends,
such as SSL/TLS libraries.

%package scripts
Summary: Tool to switch between crypto policies
Requires: %{name} = %{version}-%{release}
Recommends: (grubby if kernel)
%description scripts
This package provides a tool update-crypto-policies, which applies
the policies provided by the crypto-policies package. These can be
either the pre-built policies from the base package or custom policies
defined in simple policy definition files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n fedora-crypto-policies-%{git_commit_hash}-%{git_commit}

%build

%make_build \
  SEQUOIA_POLICY_CONFIG_CHECK_LOOSE=sequoia-policy-config-check \
  SEQUOIA_POLICY_CONFIG_CHECK_STRICT=
%install
mkdir -p -m 755 %{buildroot}%{_datarootdir}/crypto-policies/
mkdir -p -m 755 %{buildroot}%{_datarootdir}/crypto-policies/back-ends/
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/back-ends/
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/state/
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/local.d/
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/policies/
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/crypto-policies/policies/modules/
mkdir -p -m 755 %{buildroot}%{_bindir}
make DESTDIR=%{buildroot} DIR=%{_datarootdir}/crypto-policies MANDIR=%{_mandir} %{?_smp_mflags} install
install -p -m 644 default-config %{buildroot}%{_sysconfdir}/crypto-policies/config
install -p -m 644 default-fips-config %{buildroot}%{_datarootdir}/crypto-policies/default-fips-config
touch %{buildroot}%{_sysconfdir}/crypto-policies/state/current
touch %{buildroot}%{_sysconfdir}/crypto-policies/state/CURRENT.pol
rm -rf %{buildroot}%{_datarootdir}/crypto-policies/GOST-ONLY
rm -rf %{buildroot}%{_datarootdir}/crypto-policies/BSI
rm -rf %{buildroot}%{_datarootdir}/crypto-policies/FEDORA42
rm -rf %{buildroot}%{_datarootdir}/crypto-policies/FEDORA43
for d in LEGACY DEFAULT FUTURE FIPS ; do
    mkdir -p -m 755 %{buildroot}%{_datarootdir}/crypto-policies/back-ends/$d
    for f in %{buildroot}%{_datarootdir}/crypto-policies/$d/* ; do
        ln $f %{buildroot}%{_datarootdir}/crypto-policies/back-ends/$d/$(basename $f .txt).config
    done
done
for f in %{buildroot}%{_datarootdir}/crypto-policies/DEFAULT/* ; do
    ln -sf %{_datarootdir}/crypto-policies/DEFAULT/$(basename $f) %{buildroot}%{_sysconfdir}/crypto-policies/back-ends/$(basename $f .txt).config
done
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/crypto-policies/python
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test %{?_smp_mflags} SKIP_LINTING=1 \
  SEQUOIA_POLICY_CONFIG_CHECK_LOOSE=sequoia-policy-config-check \
  SEQUOIA_POLICY_CONFIG_CHECK_STRICT=
%pretrans -p <lua>

if posix.access("%{_sysconfdir}/crypto-policies/config") then
    local cf = io.open("%{_sysconfdir}/crypto-policies/config", "r")
    if cf then
        local prev = cf:read()
        cf:close()
        local new
        if prev == "TEST-FEDORA41" or prev:sub(1, 14) == "TEST-FEDORA41:" then
            new = "DEFAULT" .. prev:sub(14)
        elseif prev == "FEDORA40" or prev:sub(1, 9) == "FEDORA40:" then
            new = "FEDORA42" .. prev:sub(9)
        else
            new = prev
        end
        if new ~= prev then
            cf = io.open("%{_sysconfdir}/crypto-policies/config", "w")
            if cf then
                cf:write(new)
                cf:close()
            end
        end
    end
end
if arg[2] == 2 then
    posix.unlink("%{rpmstate_autopolicy}")
    local mountinfo = io.open("/proc/self/mountinfo", "r");
    if mountinfo then
        local mountpoints = {}
        for mount in mountinfo:lines() do
            -- See proc_pid_mountinfo(5) for the format
            local pos, _, _, _, _, mountroot, mountpoint = string.find(mount, "^(%d+) (%d+) (%d+:%d+) ([^ ]+) ([^ ]+) ")
            if pos == nil then
                print("Failed to parse /proc/self/mountinfo line, ignoring:", mount)
            else
                mountpoints[mountpoint] = mountroot
            end
        end
        mountinfo:close()
        local expected_backend_suffix = "/%{name}/back-ends/FIPS"
        local expected_config_suffix = "/%{name}/default-fips-config"
        local backends_automount =
            mountpoints["%{_sysconfdir}/%{name}/back-ends"] and
            string.sub(mountpoints["%{_sysconfdir}/%{name}/back-ends"], string.len(expected_backend_suffix) * -1, -1) == expected_backend_suffix
        local config_automount =
            mountpoints["%{_sysconfdir}/%{name}/config"] and
            string.sub(mountpoints["%{_sysconfdir}/%{name}/config"], string.len(expected_config_suffix) * -1, -1) == expected_config_suffix
        if backends_automount and config_automount then
            if posix.access("%{_bindir}/umount", "x") then
                rpm.execute("%{_bindir}/umount", "%{_sysconfdir}/%{name}/config")
                rpm.execute("%{_bindir}/umount", "%{_sysconfdir}/%{name}/back-ends")
            end
            local res, msg, errno = posix.mkdir("%{rpmstatedir}")
            if res ~= 0 and errno ~= 17  then -- 17 is EEXIST
                print("Failed to create state directory: " .. msg)
            else
                local marker, err = io.open("%{rpmstate_autopolicy}", "w+")
                if not marker then
                    print("Failed to create marker file %{rpmstate_autopolicy} for automatic FIPS policy bind-mount: " .. err)
                else
                    marker:close()
                end
            end
        end
    end
end
%post -p <lua>

if not posix.access("%{_sysconfdir}/crypto-policies/config") then
    local policy = "DEFAULT"
    local cf = io.open("/proc/sys/crypto/fips_enabled", "r")
    if cf then
        if cf:read() == "1" then
            policy = "FIPS"
        end
        cf:close()
    end
    cf = io.open("%{_sysconfdir}/crypto-policies/config", "w")
    if cf then
        cf:write(policy.."\n")
        cf:close()
    end
    cf = io.open("%{_sysconfdir}/crypto-policies/state/current", "w")
    if cf then
        cf:write(policy.."\n")
        cf:close()
    end
    local policypath = "%{_datarootdir}/crypto-policies/"..policy
    for fn in posix.files(policypath) do
        if fn ~= "." and fn ~= ".." then
            local backend = fn:gsub(".*/", ""):gsub("%%..*", "")
            local cfgfn = "%{_sysconfdir}/crypto-policies/back-ends/"..backend..".config"
            posix.unlink(cfgfn)
            posix.symlink(policypath.."/"..fn, cfgfn)
        end
    end
else
    if posix.access("%{rpmstate_autopolicy}") then
        os.execute("%{_libexecdir}/fips-crypto-policy-overlay >/dev/null 2>/dev/null || :")
        posix.unlink("%{rpmstate_autopolicy}")
    end
end
%pre

rm -f "%{_sysconfdir}/crypto-policies/back-ends/javasystem.config" 2>/dev/null || :
rm -f "%{_sysconfdir}/crypto-policies/back-ends/openssl.config" 2>/dev/null || :
exit 0
%posttrans scripts

%{_bindir}/update-crypto-policies --no-check >/dev/null 2>/dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n crypto-policies-scripts -f %{oreon_filedir}/crypto-policies-scripts.list

%changelog

* Fri Apr 3 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{git_date}-3.git
- Remove autopatch with no Patch entries (prep failed in mock)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{git_date}-3.git
- Prepare for Oreon 11 (RP1)
