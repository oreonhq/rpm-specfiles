%global source0_hash 3aad74e13db23da34c248f99fd87e9b193e00aad2b68bc9f578ce0241cb9db7f

Name:       spectre-meltdown-checker
Version:    0.46
Release:    8%{?dist}

Summary:    Spectre & Meltdown vulnerability/mitigation checker for Linux
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:    GPL-3.0-only
URL:        https://github.com/speed47/spectre-meltdown-checker
Source0:    https://github.com/speed47/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:     pr495-Fix-Retpoline-detection-for-Linux-6.9+-issue-490.patch

BuildArch:  noarch

Requires:   /bin/sh
Requires:   binutils
Requires:   bzip2
Requires:   coreutils
Requires:   findutils
Requires:   gawk
Requires:   grep
Requires:   kmod
Requires:   sed
Requires:   util-linux

%if !0%{?rhel} == 7
Requires:   zstd
Suggests:   iucode-tool
Suggests:   procps-ng
Suggests:   sqlite
Suggests:   unzip
Suggests:   wget
%endif

BuildRequires: help2man

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build

%install
install -D --preserve-timestamps %{name}.sh %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/%{name} -n "Spectre and Meltdown mitigation detection tool" \
    --no-info --output=%{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README.md
%{_bindir}/*
%{_mandir}/man1/%{name}*

%changelog
%autochangelog
