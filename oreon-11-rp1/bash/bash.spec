%global source0_hash 0d5cd86965f869a26cf64f4b71be7b96f90a3ba8b3d74e27e8e9d9d5550f31ba

#% define beta_tag rc2
%define patchlevel 9
%define baseversion 5.3
%bcond_without tests

Version: %{baseversion}.%{patchlevel}
Name: bash
Summary: The GNU Bourne Again shell
Release: 3%{?dist}
License: GPL-3.0-or-later
Url: https://www.gnu.org/software/bash
Source0:        https://ftp.gnu.org/gnu/bash/bash-5.3.tar.gz
# For now there isn't any doc
#Source2: ftp://ftp.gnu.org/gnu/bash/bash-doc-%%{version}.tar.gz

Source1: dot-bashrc
Source2: dot-bash_profile
Source3: dot-bash_logout
Source4:        https://ftp.gnu.org/gnu/bash/bash-5.3.tar.gz.sig
# Retreived from https://tiswww.cwru.edu/~chet/gpgkey.asc
# which is the https version of the link on http://tiswww.case.edu/php/chet/bash/bashtop.html
Source5: chet-gpgkey.asc

# Official upstream patches
# Patches are converted to apply with '-p1'
%{lua:for i=1,rpm.expand('%{patchlevel}') do
    print(string.format('Patch%u: bash-%s-patch-%u.patch\n', i, rpm.expand('%{baseversion}'), i))
end}

# Other patches
# Non-interactive shells beginning with argv[0][0] == '-' should run the startup files when not in posix mode.
Patch102: bash-2.03-profile.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=60870
Patch103: bash-2.05a-interpreter.patch
# Generate info for debuginfo files.
Patch104: bash-2.05b-debuginfo.patch
# Pid passed to setpgrp() can not be pid of a zombie process.
Patch105: bash-2.05b-pgrp_sync.patch
# Source bashrc file when bash is run under ssh.
Patch107: bash-3.2-ssh_source_bash.patch

# Try to pick up latest `--rpm-requires` patch from http://git.altlinux.org/gears/b/bash4.git
Patch109: bash-requires.patch
Patch110: bash-setlocale.patch
# Disable tty tests while doing bash builds
Patch111: bash-tty-tests.patch

# 484809, check if interp section is NOBITS
Patch116: bash-4.0-nobits.patch

# Do the same CFLAGS in generated Makefile in examples
Patch117: bash-4.1-examples.patch

# Builtins like echo and printf won't report errors
# when output does not succeed due to EPIPE
Patch118: bash-4.1-broken_pipe.patch

# Enable system-wide .bash_logout for login shells
Patch119: bash-4.2-rc2-logout.patch

# Static analyzis shows some issues in bash-2.05a-interpreter.patch
Patch120: bash-4.2-coverity.patch

# 799958, updated info about trap
# This patch should be upstreamed.
Patch122: bash-4.2-manpage_trap.patch

# 1112710 - mention ulimit -c and -f POSIX block size
# This patch should be upstreamed.
Patch124: bash-4.3-man-ulimit.patch

# 1102815 - fix double echoes in vi visual mode
Patch125: bash-4.3-noecho.patch

#1241533,1224855 - bash leaks memory when LC_ALL set
Patch126: bash-4.3-memleak-lc_all.patch

# bash-4.4 builds loadable builtin examples by default
# this patch disables it
Patch127: bash-4.4-no-loadable-builtins.patch

# 2020528 - Add a runtime option to enable history logging to syslog
# This option is undocumented in upstream and is documented by this patch
Patch128: bash-5.0-syslog-history.patch

# Enable audit logs
Patch131: bash-4.3-audit.patch

BuildRequires:  gcc
BuildRequires: texinfo bison
BuildRequires: ncurses-devel
BuildRequires: autoconf, gettext
BuildRequires: gnupg2
# Required for bash tests
BuildRequires: glibc-all-langpacks
BuildRequires: make
BuildRequires: audit-libs-devel
Requires: filesystem >= 3
Provides: /bin/sh
Provides: /bin/bash

%description
The GNU Bourne Again shell (Bash) is a shell or command language
interpreter that is compatible with the Bourne shell (sh). Bash
incorporates useful features from the Korn shell (ksh) and the C shell
(csh). Most sh scripts can be run by bash without modification.

%package devel
Summary: Development headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development headers for %{name}.

%package doc
Summary: Documentation files for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation files for %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE5}' --signature='%{SOURCE4}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{baseversion} -p1

echo %{version} > _distribution
echo %{release} > _patchlevel

# force refreshing the generated files
rm y.tab.*

%build
# GCC 15 defaults to `-std=gnu23` which breaks compilation
export CFLAGS+="-std=gnu17"

autoconf
%configure --with-bash-malloc=no --with-afs

# Recycles pids is neccessary. When bash's last fork's pid was X
# and new fork's pid is also X, bash has to wait for this same pid.
# Without Recycles pids bash will not wait.
MFLAGS="CPPFLAGS=-D_GNU_SOURCE -DRECYCLES_PIDS -DDEFAULT_PATH_VALUE='\"/usr/local/bin:/usr/bin\"' -DSTANDARD_UTILS_PATH='\"/bin:/usr/bin:/usr/sbin:/sbin\"' `getconf LFS_CFLAGS` -DSYSLOG_HISTORY -DSYSLOG_SHOPT=0"

# work around missing deps in Makefiles
make "$MFLAGS" version.h
make "$MFLAGS" %{?_smp_mflags} -C builtins
make "$MFLAGS" %{?_smp_mflags}

%install
if [ -e autoconf ]; then
  # Yuck. We're using autoconf 2.1x.
  export PATH=.:$PATH
fi

# Fix bug #83776
sed -i -e 's,bashref\.info,bash.info,' doc/bashref.info

%make_install install-headers

mkdir -p %{buildroot}/%{_sysconfdir}

# make manpages for bash builtins as per suggestion in DOC/README
pushd doc
sed -e '
/^\.SH NAME/, /\\- bash built-in commands, see \\fBbash\\fR(1)$/{
/^\.SH NAME/d
s/^bash, //
s/\\- bash built-in commands, see \\fBbash\\fR(1)$//
s/,//g
b
}
d
' builtins.1 > man.pages
for i in echo pwd test kill; do
  sed -i -e "s,$i,,g" man.pages
  sed -i -e "s,  , ,g" man.pages
done

install -p -m 644 builtins.1 %{buildroot}%{_mandir}/man1/builtins.1

for i in `cat man.pages` ; do
  echo .so man1/builtins.1 > %{buildroot}%{_mandir}/man1/$i.1
  chmod 0644 %{buildroot}%{_mandir}/man1/$i.1
done
popd

# Link bash man page to sh so that man sh works.
ln -s bash.1 %{buildroot}%{_mandir}/man1/sh.1

# Not for printf, true and false (conflict with coreutils)
rm -f %{buildroot}/%{_mandir}/man1/printf.1
rm -f %{buildroot}/%{_mandir}/man1/true.1
rm -f %{buildroot}/%{_mandir}/man1/false.1

ln -sf bash %{buildroot}%{_bindir}/sh
rm -f %{buildroot}%{_infodir}/dir
mkdir -p %{buildroot}%{_sysconfdir}/skel
install -p -m644 %SOURCE1 %{buildroot}/etc/skel/.bashrc
install -p -m644 %SOURCE2 %{buildroot}/etc/skel/.bash_profile
install -p -m644 %SOURCE3 %{buildroot}/etc/skel/.bash_logout
LONG_BIT=$(getconf LONG_BIT)
mv %{buildroot}%{_bindir}/bashbug \
   %{buildroot}%{_bindir}/bashbug-"${LONG_BIT}"
ln -s bashbug-"${LONG_BIT}" %{buildroot}%{_bindir}/bashbug
ln -s bashbug.1 %{buildroot}/%{_mandir}/man1/bashbug-"$LONG_BIT".1

# Fix missing sh-bangs in example scripts (bug #225609).
for script in \
  examples/scripts/shprompt
# I don't know why these are gone in 4.3
  #examples/scripts/krand.bash \
  #examples/scripts/bcsh.sh \
  #examples/scripts/precedence \
do
  cp "$script" "$script"-orig
  echo '#!/bin/bash' > "$script"
  cat "$script"-orig >> "$script"
  rm -f "$script"-orig
done

# bug #820192, need to add execable alternatives for regular built-ins
for ea in alias bg cd command fc fg getopts hash jobs read type ulimit umask unalias wait
do
  cat <<EOF > "%{buildroot}"/%{_bindir}/"$ea"
#!/bin/sh
builtin $ea "\$@"
EOF
chmod +x "%{buildroot}"/%{_bindir}/"$ea"
done

%find_lang %{name}

# copy doc to /usr/share/doc
cat /dev/null > %{name}-doc.files
mkdir -p %{buildroot}/%{_pkgdocdir}/doc
# loadables aren't buildable
rm -rf examples/loadables
for file in CHANGES COMPAT NEWS NOTES POSIX RBASH README examples
do
  cp -rp "$file" %{buildroot}%{_pkgdocdir}/"$file"
  echo "%%doc %{_pkgdocdir}/$file" >> %{name}-doc.files
done
echo "%%doc %{_pkgdocdir}/doc" >> %{name}-doc.files



%if %{with tests}
%check
make check
%endif

# post is in lua so that we can run it without any external deps.  Helps
# for bootstrapping a new install.
# Jesse Keating 2009-01-29 (code from Ignacio Vazquez-Abrams)
# Roman Rakus 2011-11-07 (code from Sergey Romanov) #740611
%post -p <lua>
nl        = '\n'
sh        = '/bin/sh'..nl
bash      = '/bin/bash'..nl
f = io.open('/etc/shells', 'a+')
if f then
  local shells = nl..f:read('*all')..nl
  if not shells:find(nl..sh) then f:write(sh) end
  if not shells:find(nl..bash) then f:write(bash) end
  f:close()
end

%postun -p <lua>
-- Run it only if we are uninstalling
if arg[2] == 0
then
  t={}
  for line in io.lines("/etc/shells")
  do
    if line ~= "/bin/bash" and line ~= "/bin/sh"
    then
      table.insert(t,line)
    end
  end

  f = io.open("/etc/shells", "w+")
  for n,line in pairs(t)
  do
    f:write(line.."\n")
  end
  f:close()
end

%files -f %{name}.lang
%config(noreplace) /etc/skel/.b*
%{_bindir}/sh
%{_bindir}/bash
%{_bindir}/alias
%{_bindir}/bg
%{_bindir}/cd
%{_bindir}/command
%{_bindir}/fc
%{_bindir}/fg
%{_bindir}/hash
%{_bindir}/getopts
%{_bindir}/jobs
%{_bindir}/read
%{_bindir}/type
%{_bindir}/ulimit
%{_bindir}/umask
%{_bindir}/unalias
%{_bindir}/wait
%dir %{_pkgdocdir}/
%license COPYING
%attr(0755,root,root) %{_bindir}/bashbug[-.]*
%{_bindir}/bashbug
%{_infodir}/bash.info*
%{_mandir}/*/*
%{_mandir}/*/..1*
%doc RBASH README
%doc doc/{FAQ,INTRO,README,bash{,ref}.html}

%files doc -f %{name}-doc.files
%doc doc/*.ps doc/*.0 doc/*.html doc/article.txt

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{baseversion}.%{patchlevel}-3
- Prepare for Oreon 11 (RP1)
