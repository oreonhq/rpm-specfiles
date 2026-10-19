%global source0_hash 596fa828d6425c47aa1a11418139cc572dae07a96c87eb1b9c70acf0c1836cd3
Summary:        A utility which maintains a system's symbolic links
Name: symlinks
URL: https://github.com/brandt/symlinks
Version: 1.7
Release:        1%{?dist}
License: Symlinks
Source0:        http://ibiblio.org/pub/Linux/utils/file/%{name}-%{version}.tar.gz
Source1: symlinks-LICENSE.txt
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The symlinks utility performs maintenance on symbolic links.  Symlinks
checks for symlink problems, including dangling symlinks which point
to nonexistent files.  Symlinks can also automatically convert
absolute symlinks to relative symlinks.

Install the symlinks package if you need a program for maintaining
symlinks on your system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7-14
- Prepare for Oreon 11 (RP1)
