%global source0_hash 4e4d209a038c252a2833eeaac18a53c5f19141e88e35a32d4d1c7bb42239d96a
Name:       spectre-meltdown-checker
Version:    26.36.0913490
Release:        1%{?dist}
Summary:        Spectre & Meltdown vulnerability/mitigation checker for Linux
License:    GPL-3.0-only
URL:        https://github.com/speed47/spectre-meltdown-checker
Source0:        https://github.com/speed47/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
# oreon:deps
BuildRequires:  help2man
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%install
install -D --preserve-timestamps %{name}.sh %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/%{name} -n "Spectre and Meltdown mitigation detection tool" \
    --no-info --output=%{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
