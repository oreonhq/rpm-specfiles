%global source0_hash 477e796f5c18e8c0e61b5d88e1759c68249e8e0210c2f3de2b98680e2cc63e32
Name:           aoetools
Version:        37
Release:        1%{?dist}
Summary:        ATA over Ethernet Tools
License:        GPL-2.0-only
URL:            http://aoetools.sourceforge.net
%global git_tag %{name}-%{version}
Source0:        https://github.com/OpenAoE/%{name}/archive/%{git_tag}/%{name}-%{git_tag}.tar.gz
Source1:        60-aoe.rules
Patch0:         %{name}-makefile.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
The aoetools are programs that assist in using ATA over Ethernet on 
systems with version 2.6 and newer Linux kernels.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_tag}

%build

%make_build
%install
%{!?_udevrulesdir: %global _udevrulesdir %{_sysconfdir}/udev/rules.d}
%make_install SBINDIR="%{_bindir}"
mkdir -pm 755 %{buildroot}/%{_udevrulesdir}
install -pm 644 %{SOURCE1} %{buildroot}/%{_udevrulesdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
