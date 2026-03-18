Summary:          MirBSD enhanced version of the Korn Shell
Name:             mksh
Version:          59c
Release:          15%{?dist}
# ISC (strlcpy.c) and MirOS (the rest)
License:          MirOS AND ISC
URL:              https://www.mirbsd.org/mksh.htm
Source0:          https://www.mirbsd.org/MirOS/dist/mir/%{name}/%{name}-R%{version}.tgz
Source1:          dot-mkshrc
Source2:          rtchecks.expected
Provides:         /bin/ksh
Provides:         /bin/lksh
Provides:         /bin/mksh
%if 0%{?fedora} || 0%{?rhel} > 8
Provides:         /bin/rksh
%endif
Provides:         /bin/rlksh
Provides:         /bin/rmksh
Requires:         filesystem >= 3
Requires(post):   grep
Requires(post):   alternatives
Requires(preun):  alternatives
Requires(postun): sed
BuildRequires:    gcc
# script(1) comes from somewhere in the overall util-linux* package mess
BuildRequires:    %{_bindir}/script
BuildRequires:    ed
BuildRequires:    perl-interpreter
BuildRequires:    perl(Getopt::Std)
BuildRequires:    sed

%description
mksh is the MirBSD enhanced version of the Public Domain Korn shell (pdksh),
a bourne-compatible shell which is largely similar to the original AT&T Korn
shell. It includes bug fixes and feature improvements in order to produce a
modern, robust shell good for interactive and especially script use, being a
bourne shell replacement, pdksh successor and an alternative to the C shell.

%prep
%setup -q -n %{name}

# we'll need this later
cat > rtchecks <<'EOF'
typeset -i sari=0
typeset -Ui uari=0
typeset -i x=0
print -r -- $((x++)):$sari=$uari. #0
let --sari --uari
print -r -- $((x++)):$sari=$uari. #1
sari=2147483647 uari=2147483647
print -r -- $((x++)):$sari=$uari. #2
let ++sari ++uari
print -r -- $((x++)):$sari=$uari. #3
let --sari --uari
let 'sari *= 2' 'uari *= 2'
let ++sari ++uari
print -r -- $((x++)):$sari=$uari. #4
let ++sari ++uari
print -r -- $((x++)):$sari=$uari. #5
sari=-2147483648 uari=-2147483648
print -r -- $((x++)):$sari=$uari. #6
let --sari --uari
print -r -- $((x++)):$sari=$uari. #7
(( sari = -5 >> 1 ))
((# uari = -5 >> 1 ))
print -r -- $((x++)):$sari=$uari. #8
(( sari = -2 ))
((# uari = sari ))
print -r -- $((x++)):$sari=$uari. #9
EOF

%build
CFLAGS="$RPM_OPT_FLAGS -DMKSH_DISABLE_EXPERIMENTAL" LDFLAGS="$RPM_LD_FLAGS" sh Build.sh -r
cp -f test.sh test_mksh.sh
export HAVE_PERSISTENT_HISTORY=0
CFLAGS="$RPM_OPT_FLAGS -DMKSH_DISABLE_EXPERIMENTAL" LDFLAGS="$RPM_LD_FLAGS" sh Build.sh -L -r
cp -f test.sh test_lksh.sh
./mksh FAQ2HTML.sh

%install
install -D -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p -m 0755 lksh $RPM_BUILD_ROOT%{_bindir}/lksh
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -D -p -m 0644 lksh.1 $RPM_BUILD_ROOT%{_mandir}/man1/lksh.1
install -D -p -m 0644 dot.mkshrc $RPM_BUILD_ROOT%{_sysconfdir}/mkshrc
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.mkshrc
ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/rmksh
ln -s lksh $RPM_BUILD_ROOT%{_bindir}/rlksh
ln -s %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/rmksh.1
ln -s lksh.1 $RPM_BUILD_ROOT%{_mandir}/man1/rlksh.1
%if 0%{?fedora} || 0%{?rhel} > 8
touch $RPM_BUILD_ROOT{%{_bindir}/{ksh,rksh},%{_mandir}/man1/{ksh,rksh}.1}
%else
touch $RPM_BUILD_ROOT{%{_bindir}/ksh,%{_mandir}/man1/ksh.1}
%endif

%check
./mksh rtchecks > rtchecks.got 2>&1
if ! cmp --quiet rtchecks.got %{SOURCE2}; then
  echo "rtchecks failed"
  diff -Naurp %{SOURCE2} rtchecks.got
  exit 1
fi

for tf in test_mksh.sh test_lksh.sh; do
  echo > test.wait
  script -qc "./$tf"' -v; x=$?; rm -f test.wait; exit $x'
  maxwait=0
  while test -e test.wait; do
    sleep 1
    maxwait=$(expr $maxwait + 1)
    test $maxwait -lt 900 || break
  done
done

%post
for d in /bin %{_bindir}; do
%if 0%{?fedora} || 0%{?rhel} > 8
  for s in ksh %{name} rksh rmksh; do
%else
  for s in ksh %{name} rmksh; do
%endif
    grep -q '^'"$d/$s"'$' %{_sysconfdir}/shells 2>/dev/null || echo "$d/$s" >> /etc/shells
  done
done

alternatives --install %{_bindir}/ksh ksh %{_bindir}/%{name} 10 \
%if 0%{?fedora} || 0%{?rhel} > 8
  --slave %{_bindir}/rksh rksh %{_bindir}/%{name} \
%endif
  --slave %{_mandir}/man1/ksh.1.gz ksh-man %{_mandir}/man1/%{name}.1.gz \
%if 0%{?fedora} || 0%{?rhel} > 8
  --slave %{_mandir}/man1/rksh.1.gz rksh-man %{_mandir}/man1/%{name}.1.gz
%endif

%preun
if [ $1 -eq 0 ]; then
  alternatives --remove ksh %{_bindir}/%{name}
fi

%postun
for d in /bin %{_bindir}; do
  for s in ksh %{name} rksh rmksh; do
    if [ ! -x "$d/$s" ]
    then
      sed -e 's@^'"$d/$s"'$@POSTUNREMOVE@' -e '/^POSTUNREMOVE$/d' -i %{_sysconfdir}/shells
    fi
  done
done

%files
%doc dot.mkshrc FAQ.htm
%ghost %{_bindir}/ksh
%{_bindir}/lksh
%{_bindir}/%{name}
%if 0%{?fedora} || 0%{?rhel} > 8
%ghost %{_bindir}/rksh
%endif
%{_bindir}/rlksh
%{_bindir}/rmksh
%config(noreplace) %{_sysconfdir}/mkshrc
%config(noreplace) %{_sysconfdir}/skel/.mkshrc
%ghost %{_mandir}/man1/ksh.1*
%{_mandir}/man1/lksh.1*
%{_mandir}/man1/%{name}.1*
%if 0%{?fedora} || 0%{?rhel} > 8
%ghost %{_mandir}/man1/rksh.1*
%endif
%{_mandir}/man1/rlksh.1*
%{_mandir}/man1/rmksh.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 59c-15
- Prepare for Oreon 11 (RP1)
