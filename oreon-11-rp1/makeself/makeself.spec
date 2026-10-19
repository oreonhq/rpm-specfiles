%global source0_hash 96843e5db70da71dcb3cb594a6899886043f115e9205c6b5ca2f26000389514e
Name:           makeself
Version:        2.7.1
Release:        1%{?dist}
BuildArch:      noarch
Summary:        Make self-extractable archives on Unix
License:        GPL-2.0-or-later
URL:            http://%{name}.io/
Source0:        https://github.com/megastep/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz
Requires:       gzip
Recommends:     gnupg
Recommends:     openssl
Suggests:       bzip2
Suggests:       gzip
Suggests:       lz4
Suggests:       pigz
Suggests:       xz
Suggests:       zstd
# oreon:deps
BuildRequires:  /usr/bin/iconv
BuildRequires:  sed
# /oreon:deps
%description
makeself.sh is a shell script that generates a self-extractable
tar.gz archive from a directory. The resulting file appears as a shell
script, and can be launched as is. The archive will then uncompress
itself to a temporary directory and an arbitrary command will be
executed (for example an installation script). This is pretty similar
to archives generated with WinZip Self-Extractor in the Windows world.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-release-%{version}
%oreon_prep
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
