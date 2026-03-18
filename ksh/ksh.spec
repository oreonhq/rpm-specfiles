Name:         ksh
Summary:      The Original ATT Korn Shell
URL:          http://www.kornshell.com/
License:      EPL-2.0
Epoch:        3
Version:      1.0.10
Release:      8%{?dist}
Source0:      https://github.com/ksh93/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:      kshcomp.conf
Source2:      kshrc.rhs
Source3:      dotkshrc

# https://github.com/ksh93/ksh/commit/caae9aa23e2851cadf55f858a8f38b9f0de74314
Patch1:       ksh-1.0.11-SHLVL.patch

# https://github.com/ksh93/ksh/commit/5def43983de3ecfa38c805c02a1f0d6f1581160c
Patch2:       ksh-1.0.11-redir.patch

# add delay to sigchld.sh test to fix failures on slower builders
# based on https://github.com/ksh93/ksh/pull/922
Patch3:       ksh-1.0.11-sigchld-delay.patch

Conflicts:    pdksh
Requires: coreutils, diffutils
BuildRequires: gcc
BuildRequires: bison

# regression test suite requirements
BuildRequires: glibc-langpack-ja
BuildRequires: ncurses
BuildRequires: procps
BuildRequires: tzdata
BuildRequires: util-linux-script

Requires(post): grep, coreutils, systemd
Requires(postun): sed

Provides: /bin/ksh
Provides: /bin/rksh

%description
KSH-93 is the most recent version of the KornShell by David Korn of
AT&T Bell Laboratories.
KornShell is a shell programming language, which is upward compatible
with "sh" (the Bourne Shell).

%prep
%autosetup -p1

# /dev/fd test does not work because of mock
sed -i 's|ls /dev/fd|ls /proc/self/fd|' src/cmd/ksh93/features/options

%build
XTRAFLAGS=""
for f in -Wno-unknown-pragmas -Wno-missing-braces -Wno-unused-result -Wno-return-type -Wno-int-to-pointer-cast -Wno-parentheses -Wno-unused -Wno-unused-but-set-variable -Wno-cpp -Wno-maybe-uninitialized -Wno-lto-type-mismatch
do
  $CC $f -E - </dev/null >/dev/null 2>&1 && XTRAFLAGS="$XTRAFLAGS $f"
done
export CCFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing $XTRAFLAGS"
export LDFLAGS="$RPM_LD_FLAGS"
bin/package make

%install
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
install -p -m 755 arch/*/bin/ksh %{buildroot}%{_bindir}/ksh93
install -p -m 755 arch/*/bin/shcomp %{buildroot}%{_bindir}/shcomp
install -p -m 644 arch/*/man/man1/sh.1 %{buildroot}%{_mandir}/man1/ksh93.1
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/skel/.kshrc
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/kshrc
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/binfmt.d/kshcomp.conf

touch %{buildroot}%{_bindir}/ksh
touch %{buildroot}%{_mandir}/man1/ksh.1.gz

touch %{buildroot}%{_bindir}/rksh
touch %{buildroot}%{_mandir}/man1/rksh.1.gz

%check
# script is needed for pty tests in mock
script -q -e -c "bin/package test"

%post
for s in /bin/ksh /bin/rksh /usr/bin/ksh /usr/bin/rksh
do
  if [ ! -f /etc/shells ]; then
        echo "$s" > /etc/shells
  else
        if ! grep -q '^'"$s"'$' /etc/shells ; then
                echo "$s" >> /etc/shells
        fi
  fi
done

%{_sbindir}/alternatives --install %{_bindir}/ksh ksh \
                %{_bindir}/ksh93 50 \
        --slave %{_bindir}/rksh rksh \
                %{_bindir}/ksh93 \
        --slave %{_mandir}/man1/rksh.1.gz rksh-man \
                %{_mandir}/man1/ksh93.1.gz \
        --slave %{_mandir}/man1/ksh.1.gz ksh-man \
                %{_mandir}/man1/ksh93.1.gz

#if not symlink we are updating ksh where there was no alternatives before
#so replace with symlink and set alternatives
if [ ! -L %{_bindir}/ksh ]; then
        %{_sbindir}/alternatives --auto ksh
        ln -sf /etc/alternatives/ksh %{_bindir}/ksh
        ln -sf /etc/alternatives/ksh-man %{_mandir}/man1/ksh.1.gz
fi

/bin/systemctl try-restart systemd-binfmt.service >/dev/null 2>&1 || :

%postun
for s in /bin/ksh /bin/rksh /usr/bin/ksh /usr/bin/rksh
do
  if [ ! -f $s ]; then
        sed -i '\|^'"$s"'$|d' /etc/shells
  fi
done

%preun
if [ $1 = 0 ]; then
        %{_sbindir}/alternatives --remove ksh %{_bindir}/ksh93
fi

%verifyscript
echo -n "Looking for ksh in /etc/shells... "
if ! grep '^/bin/ksh$' /etc/shells > /dev/null; then
    echo "missing"
    echo "ksh missing from /etc/shells" >&2
else
    echo "found"
fi

%files 
%doc src/cmd/ksh93/{COMPATIBILITY,RELEASE,TYPES,README}
%doc README.md NEWS
%license LICENSE.md
%{_bindir}/ksh93
%ghost %{_bindir}/ksh
%ghost %{_bindir}/rksh
%{_bindir}/shcomp
%{_mandir}/man1/ksh93.1*
%ghost %{_mandir}/man1/ksh.1*
%ghost %{_mandir}/man1/rksh.1*
%config(noreplace) %{_sysconfdir}/skel/.kshrc
%config(noreplace) %{_sysconfdir}/kshrc
%config(noreplace) %{_sysconfdir}/binfmt.d/kshcomp.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.10-8
- Prepare for Oreon 11 (RP1)
