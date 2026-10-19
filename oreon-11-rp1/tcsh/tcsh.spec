%global source0_hash 4208cf4630fb64d91d81987f854f9570a5a0e8a001a92827def37d0ed8f37364
%global _hardened_build 1
Name:             tcsh
Summary:        An enhanced version of csh, the C shell
Version:          6.24.16
Release:        1%{?dist}
License:          BSD-3-Clause
URL:              http://www.tcsh.org/
Source0:        https://astron.com/pub/tcsh/%{name}-%{version}.tar.gz
Provides:         csh = %{version}
Provides:         /bin/csh
Provides:         /bin/tcsh
Requires(post):   coreutils
Requires(post):   grep
Requires(postun): sed
Patch100: tcsh-6.24.07-manpage-memoryuse.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Tcsh is an enhanced but completely compatible version of csh, the C shell. Tcsh
is a command language interpreter which can be used both as an interactive login
shell and as a shell script command processor. Tcsh includes a command line
editor, programmable word completion, spelling correction, a history mechanism,
job control and a C language like syntax.

# === BUILD INSTRUCTIONS ======================================================

# Call the 'autosetup' macro to prepare the environment, but do not patch the
# source code yet -- we need to convert the 'Fixes' file first:
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -N -S git

# NOTE: If more files needs to be converted, add them here:
for file in Fixes; do
  iconv -f iso-8859-1 -t utf-8 "$file" > "${file}.converted" && \
  touch -r "$file" "${file}.converted" && \
  mv "${file}.converted" "$file"
done

# Also, rename the Copyright so we comply with more generally accepted name:
mv Copyright COPYING

# Amend the converted files to the initial commit, and patch the source code:
git add --all --force
git commit --all --amend --no-edit > /dev/null
%autopatch -p1

# ---------------

%build

%configure
%make_build all
%check

%make_build check
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 755 tcsh     %{buildroot}%{_bindir}/tcsh
install -p -m 644 tcsh.man %{buildroot}%{_mandir}/man1/tcsh.1
ln -sf tcsh                %{buildroot}%{_bindir}/csh
ln -sf tcsh.1              %{buildroot}%{_mandir}/man1/csh.1
while read lang language; do
  dest="%{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES"
  if [[ -f "nls/$language.cat" ]]; then
    mkdir -p "$dest"
    install -p -m 644 "nls/$language.cat" "$dest/tcsh"
    echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/tcsh"
  fi
done > %{name}.lang << _EOF
de german
el greek
en C
es spanish
et et
fi finnish
fr french
it italian
ja ja
pl pl
ru russian
uk ukrainian
_EOF
%oreon_autofiles main

%post

if [[ "$1" -eq 1 ]]; then
  if [[ ! -f %{_sysconfdir}/shells ]]; then
    echo "/bin/csh"        >> %{_sysconfdir}/shells
    echo "/bin/tcsh"       >> %{_sysconfdir}/shells
    echo "%{_bindir}/csh"  >> %{_sysconfdir}/shells
    echo "%{_bindir}/tcsh" >> %{_sysconfdir}/shells
  else
    grep -q "^/bin/csh$"        %{_sysconfdir}/shells || echo "/bin/csh"        >> %{_sysconfdir}/shells
    grep -q "^/bin/tcsh$"       %{_sysconfdir}/shells || echo "/bin/tcsh"       >> %{_sysconfdir}/shells
    grep -q "^%{_bindir}/csh$"  %{_sysconfdir}/shells || echo "%{_bindir}/csh"  >> %{_sysconfdir}/shells
    grep -q "^%{_bindir}/tcsh$" %{_sysconfdir}/shells || echo "%{_bindir}/tcsh" >> %{_sysconfdir}/shells
  fi
fi
%postun

if [[ "$1" -eq 0 && -f %{_sysconfdir}/shells ]]; then
  sed -i -e '\!^/bin/csh$!d'        %{_sysconfdir}/shells
  sed -i -e '\!^/bin/tcsh$!d'       %{_sysconfdir}/shells
  sed -i -e '\!^%{_bindir}/csh$!d'  %{_sysconfdir}/shells
  sed -i -e '\!^%{_bindir}/tcsh$!d' %{_sysconfdir}/shells
fi
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.16-1
- Prepare for Oreon 11 (RP1)
