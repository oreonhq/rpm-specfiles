%global source0_hash 4208cf4630fb64d91d81987f854f9570a5a0e8a001a92827def37d0ed8f37364

# === GLOBAL MACROS ===========================================================

# According to Fedora Package Guidelines, it is advised that packages that can
# process untrusted input are build with position-independent code (PIC).
#
# Koji should override the compilation flags and add the -fPIC or -fPIE flags by
# default. This is here just in case this wouldn't happen for some reason.
# For more info: https://fedoraproject.org/wiki/Packaging:Guidelines#PIE
%global _hardened_build 1

# =============================================================================

Name:             tcsh
Summary:          An enhanced version of csh, the C shell
Version:          6.24.16
Release:          1%{?dist}
License:          BSD-3-Clause

URL:              http://www.tcsh.org/
Source:        https://astron.com/pub/tcsh/%{name}-%{version}.tar.gz

Provides:         csh = %{version}
Provides:         /bin/csh
Provides:         /bin/tcsh

Requires(post):   coreutils
Requires(post):   grep
Requires(postun): sed

BuildRequires:    make
BuildRequires:    gcc
BuildRequires:    git
BuildRequires:    autoconf
BuildRequires:    gettext-devel
BuildRequires:    libxcrypt-devel
BuildRequires:    ncurses-devel

# =============================================================================

# NOTE: 'autosetup' macro (below) uses 'git' for applying the patches:
#       ->> All the patches should be provided in 'git format-patch' format.
#       ->> Auxiliary repository will be created during 'fedpkg prep', you
#           can see all the applied patches there via 'git log'.

# Upstream patches -- official upstream patches released by upstream since the
# ----------------    last rebase that are necessary for any reason:


# Downstream patches -- these should be always included when doing rebase:
# ------------------
Patch100: tcsh-6.24.07-manpage-memoryuse.patch


# Downstream patches for RHEL -- patches that we keep only in RHEL for various
# ---------------------------    reasons, but are not enabled in Fedora:
%if %{defined rhel} || %{defined centos}
Patch200: tcsh-6.20.00-tcsh-posix-status.patch
%endif


# Patches to be removed -- deprecated functionality which shall be removed at
# ---------------------    some point in the future:


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

# ---------------

%check
%make_build check

# ---------------

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 755 tcsh     %{buildroot}%{_bindir}/tcsh
install -p -m 644 tcsh.man %{buildroot}%{_mandir}/man1/tcsh.1
ln -sf tcsh                %{buildroot}%{_bindir}/csh
ln -sf tcsh.1              %{buildroot}%{_mandir}/man1/csh.1

# NOTE: We have to construct tcsh.lang by ourselves, since upstream does not use
#       standard naming/placing of localization files for the gettext...
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

# ---------------

%post
# Add login shell entries to /etc/shells only when installing the package
# for the first time (see 'man 5 SHELLS' for more info):
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

# ---------------

%postun
# Remove the login shell lines from /etc/shells only when uninstalling:
if [[ "$1" -eq 0 && -f %{_sysconfdir}/shells ]]; then
  sed -i -e '\!^/bin/csh$!d'        %{_sysconfdir}/shells
  sed -i -e '\!^/bin/tcsh$!d'       %{_sysconfdir}/shells
  sed -i -e '\!^%{_bindir}/csh$!d'  %{_sysconfdir}/shells
  sed -i -e '\!^%{_bindir}/tcsh$!d' %{_sysconfdir}/shells
fi

# === PACKAGING INSTRUCTIONS ==================================================

%files -f %{name}.lang
%doc FAQ Fixes README.md complete.tcsh
%license COPYING
%{_bindir}/tcsh
%{_bindir}/csh
%{_mandir}/man1/*.1*

# =============================================================================

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.16-1
- Prepare for Oreon 11 (RP1)
