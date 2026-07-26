%global source0_hash 3af5218dfb80d20a156d3c50fa0d510c7b244d9676813659f8d220bc95405f07

Name:           makeself
Version:        2.6.0
Release:        2%{?dist}
BuildArch:      noarch
Summary:        Make self-extractable archives on Unix

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://%{name}.io/
Source:         https://github.com/megastep/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  %{_bindir}/iconv
BuildRequires:  sed

Requires:       gzip

Recommends:     gnupg
Recommends:     openssl

Suggests:       bzip2
Suggests:       gzip
Suggests:       lz4
Suggests:       pigz
Suggests:       xz
Suggests:       zstd

%description
makeself.sh is a shell script that generates a self-extractable
tar.gz archive from a directory. The resulting file appears as a shell
script, and can be launched as is. The archive will then uncompress
itself to a temporary directory and an arbitrary command will be
executed (for example an installation script). This is pretty similar
to archives generated with WinZip Self-Extractor in the Windows world.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-release-%{version}

%build
iconv --from-code=ISO-8859-1 --to-code=UTF-8 %{name}.1 | gzip > %{name}.1.gz
sed -i 's:^HEADER=.*:HEADER=/usr/libexec/makeself-header.sh:' makeself.sh

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}
mkdir -p %{buildroot}%{_mandir}/man1

install -p -m755 %{name}.sh %{buildroot}%{_bindir}
install -p -m644 %{name}-header.sh %{buildroot}%{_libexecdir}
install -p -m644 %{name}.1.gz %{buildroot}%{_mandir}/man1
ln -s %{name}.sh %{buildroot}%{_bindir}/%{name}

%files
%doc README.md COPYING
%{_mandir}/man1/*
%{_libexecdir}/*
%{_bindir}/*

%changelog
%autochangelog
