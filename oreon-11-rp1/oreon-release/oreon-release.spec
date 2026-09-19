%global source0_hash none

%define release_pack RP1
%define dist_version 11

Summary:        Oreon release files
Name:           oreon-release
Version:        11
Release:        4%{?dist}
License:        MIT
URL:            https://oreonhq.com/oreon


Provides:       oreon-release = %{version}-%{release}
Provides:       oreon-release(%{version}) = %{release}
Provides:       system-release = 11-%{release}
Provides:       system-release(11) = %{release}
Provides:       base-module(platform:or%{version})
Requires:       oreon-repos(%{version})
BuildArch:      noarch
BuildRequires:  bash

Source0:        LICENSE
Source1:        85-display-manager.preset
Source2:        90-default.preset
Source3:        99-default-disable.preset

%description
Oreon release files including base system configuration and identification.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%build
cat > os-release << EOF
NAME="Oreon"
VERSION="%{version}"
ID=oreon
VERSION_ID=%{version}
VERSION_CODENAME="Horizon"
PLATFORM_ID="platform:or%{version}"
PRETTY_NAME="Oreon 11 (%{release_pack})"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=oreon-logo-icon
CPE_NAME="cpe:/o:oreonhq:oreon:%{version}"
HOME_URL="https://oreonhq.com/"
DOCUMENTATION_URL="https://wiki.oreonhq.com/"
SUPPORT_URL="https://oreonhq.com/help/"
BUG_REPORT_URL="https://community.oreonhq.com/"
PRIVACY_POLICY_URL="https://oreonhq.com/legal/"
EOF

cat > issue << EOF
Oreon 11 (%{release_pack})
Kernel \r on an \m (\l)

EOF

cat > issue.net << EOF
Oreon 11 (%{release_pack})
Kernel \r on an \m (\l)
EOF

%install
install -d -m 755 %{buildroot}/etc
install -d -m 755 %{buildroot}%{_prefix}/lib
install -d -m 755 %{buildroot}%{_rpmmacrodir}

# Defines %%oreon for specs (kernel/shim/grub2 secure boot branding). Builders
# should have oreon-release installed so mock/koji expands %%{?oreon}.
cat > %{buildroot}%{_rpmmacrodir}/macros.oreon-release << 'EOF'
%%oreon 11
%%python_wheel_pkg_prefix python3
EOF

# Install os-release
install -m 644 os-release %{buildroot}%{_prefix}/lib/os-release
ln -s ../usr/lib/os-release %{buildroot}/etc/os-release

# Install system-release files
echo "Oreon release 11 (%{release_pack})" > %{buildroot}/etc/system-release
ln -s system-release %{buildroot}/etc/oreon-release
echo "cpe:/o:oreonhq:oreon:%{version}" > %{buildroot}%{_prefix}/lib/system-release-cpe

# Install issue files
install -m 644 issue %{buildroot}/etc/issue
install -m 644 issue.net %{buildroot}/etc/issue.net

# Install systemd presets
install -d -m 755 %{buildroot}%{_prefix}/lib/systemd/system-preset
install -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 644 %{SOURCE2} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 644 %{SOURCE3} %{buildroot}%{_prefix}/lib/systemd/system-preset/

%files
%{_prefix}/lib/os-release
/etc/os-release
/etc/oreon-release
/etc/system-release
%{_prefix}/lib/system-release-cpe
%config(noreplace) /etc/issue
%config(noreplace) /etc/issue.net
%{_prefix}/lib/systemd/system-preset/*
%{_rpmmacrodir}/macros.oreon-release

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11-2
- Import
