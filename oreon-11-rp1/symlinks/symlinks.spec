Summary: A utility which maintains a system's symbolic links
Name: symlinks
URL: https://github.com/brandt/symlinks
Version: 1.7
Release: 14%{?dist}
License: Symlinks
# ibiblio mirror dead; local tarball matches Fedora dist-git (SHA512 verified)
Source0: %{name}-%{version}.tar.gz
# Taken from http://packages.debian.org/changelogs/pool/main/s/symlinks/symlinks_1.2-4.2/symlinks.copyright
Source1: symlinks-LICENSE.txt
BuildRequires: make
BuildRequires: gcc

%description
The symlinks utility performs maintenance on symbolic links.  Symlinks
checks for symlink problems, including dangling symlinks which point
to nonexistent files.  Symlinks can also automatically convert
absolute symlinks to relative symlinks.

Install the symlinks package if you need a program for maintaining
symlinks on your system.

%prep
%setup -q
cp %{SOURCE1} .

%build
make CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS) %{build_ldflags}" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 symlinks $RPM_BUILD_ROOT%{_bindir}
install -m 644 symlinks.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc symlinks-LICENSE.txt
%{_bindir}/symlinks
%{_mandir}/man1/symlinks.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7-14
- Prepare for Oreon 11 (RP1)
