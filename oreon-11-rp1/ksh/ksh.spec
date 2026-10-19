%global source0_hash 9f4c7a9531cec6941d6a9fd7fb70a4aeda24ea32800f578fd4099083f98b4e8a
Name:         ksh
Summary:        The Original ATT Korn Shell
URL:          http://www.kornshell.com/
License:      EPL-2.0
Epoch:        3
Version:      1.0.10
Release:        8%{?dist}
Source0:        https://github.com/ksh93/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz#/ksh-1.0.10.tar.gz
Source1:      kshcomp.conf
Source2:      kshrc.rhs
Source3:      dotkshrc
Patch1:       ksh-1.0.11-SHLVL.patch
Patch2:       ksh-1.0.11-redir.patch
Patch3:       ksh-1.0.11-sigchld-delay.patch
Conflicts:    pdksh
Requires: coreutils, diffutils
Requires(post): grep, coreutils, systemd
Requires(postun): sed
Provides: /bin/ksh
Provides: /bin/rksh
# oreon:deps
BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  glibc-langpack-ja
BuildRequires:  ncurses
BuildRequires:  procps
BuildRequires:  tzdata
BuildRequires:  util-linux-script
# /oreon:deps
%description
KSH-93 is the most recent version of the KornShell by David Korn of
AT&T Bell Laboratories.
KornShell is a shell programming language, which is upward compatible
with "sh" (the Bourne Shell).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%check

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
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3:1.0.10-8
- Import
