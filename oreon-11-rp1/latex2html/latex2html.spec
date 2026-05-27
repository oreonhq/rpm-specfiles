%global source0_hash 2a3f50621a71c9c0c425fb6709ae69bb2cf4df4bfe72ac661c2ea302e5aba185
%global source3_hash 86019c5ddc6b310126664adf00b5f906b6ebd3d1cf5a2d1a7b546ccd481fab6d

%define enable_japanese 1

Summary: Converts LaTeX documents to HTML
Name: latex2html
Version: 2023.2
Release: 9%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/latex2html/latex2html/releases
# main latex2html source
Source0: https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: cfgcache.pm
Source2: %{name}-manpages.tar.gz
# support for Japanese
# http://takeno.iee.niit.ac.jp/~shige/TeX/latex2html/
Source3: http://takeno.iee.niit.ac.jp/~shige/TeX/latex2html/data2/l2h-2023-jp3.2b1.37.tar.gz
Patch1: latex2html-2018.2-teTeX-l2h-config.patch
Patch2: latex2html-2002-2-1-SHLIB.patch
Requires: tex(latex), tex(dvips), tex(url.sty), tex(preview.sty), netpbm-progs, poppler-utils
BuildRequires: tex(latex), tex(dvips), tex(url.sty), tex(preview.sty), netpbm-progs, poppler-utils
BuildRequires: perl-interpreter >= 5.003, perl-generators, ghostscript >= 4.03
BuildRequires: perl(Carp), perl(Config), perl(Cwd), perl(DB), perl(Exporter),
BuildRequires: perl(File::Copy), perl(FindBin), perl(IO::File), perl(Sys::Hostname)
BuildRequires: perl(Unicode::Collate::Locale), perl(lib), perl(strict), perl(vars)
BuildRequires: make
BuildArch: noarch

%description
LATEX2HTML is a converter written in Perl that converts LATEX
documents to HTML. This way e.g. scientific papers - primarily typeset
for printing - can be put on the Web for online viewing.

LATEX2HTML does also a good job in rapid web site deployment. These
pages are generated from a single LATEX source.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; })
%setup -q -c -a 0

pushd %{name}-%{version}
# Patch from Oliver Paukstadt <oliver.paukstadt@millenux.com>
%patch -P1 -p2 -b .config

# fix SHLIBDIR
%patch -P2 -p1 -b .shlib

# remove all platforms we don't need
for i in Dos Mac OS2 Win32; do
  rm -f L2hos/${i}.pm
done
rm -rf cweb2html
rm -f readme.hthtml
popd

%if %{enable_japanese}
cp -a %{name}-%{version} %{name}-%{version}JA
pushd %{name}-%{version}JA
tar fxz %{SOURCE3}
popd
%endif

%build
pushd %{name}-%{version}
cp %{SOURCE1} cfgcache.pm
tar fxz %{SOURCE2}

./configure	--program-prefix=%{?_program_prefix} \
		--prefix=%{_prefix} \
		--exec-prefix=%{_exec_prefix} \
		--bindir=%{_bindir} \
		--sbindir=%{_sbindir} \
		--sysconfdir=%{_sysconfdir} \
		--datadir=%{_datadir} \
		--includedir=%{_includedir} \
		--libdir=%{_datadir}/latex2html \
		--libexecdir=%{_libexecdir} \
		--localstatedir=%{_localstatedir} \
		--sharedstatedir=%{_sharedstatedir} \
		--mandir=%{_mandir} \
		--infodir=%{_infodir} \
		--shlibdir=%{_datadir}/latex2html \
		--with-texpath=%{_datadir}/texmf/tex/latex/html

perl -pi -e "s,/usr/(share/)?lib,%{_datadir}," cfgcache.pm
make
popd

%if %{enable_japanese}
pushd %{name}-%{version}JA
sed s/latex2html/jlatex2html/g < %{SOURCE1} > cfgcache.pm
perl -pi -e "s,/usr/bin/dvips,/usr/bin/pdvips," cfgcache.pm
perl -pi -e "s,/usr/bin/latex,/usr/bin/platex," cfgcache.pm

./configure	--program-prefix=%{?_program_prefix} \
		--prefix=%{_prefix} \
		--exec-prefix=%{_exec_prefix} \
		--bindir=%{_bindir} \
		--sbindir=%{_sbindir} \
		--sysconfdir=%{_sysconfdir} \
		--datadir=%{_datadir} \
		--includedir=%{_includedir} \
		--libdir=%{_datadir}/jlatex2html \
		--libexecdir=%{_libexecdir} \
		--localstatedir=%{_localstatedir} \
		--sharedstatedir=%{_sharedstatedir} \
		--mandir=%{_mandir} \
		--infodir=%{_infodir} \
		--shlibdir=%{_datadir}/jlatex2html \
		--with-texpath=%{_datadir}/texmf/tex/latex/html

perl -pi -e "s,/usr/(share/)?lib,%{_datadir},;
	    s,%{_datadir}/latex2html,%{_datadir}/jlatex2html," cfgcache.pm
make
perl -pi -e "s,\\\$\{dd}pstoimg,\\\$\{dd}jpstoimg, ;
	    s,\\\$\{dd}texexpand,\\\$\{dd}jtexexpand," l2hconf.pm

for i in latex2html pstoimg texexpand ; do
	mv ${i} j${i}
done
popd
%endif

%install
pushd %{name}-%{version}
sed -i "s,%{_prefix},%{buildroot}%{_prefix}," cfgcache.pm
sed -i "s,%{buildroot},," l2hconf.pm

perl -pi -e "s,/.*\\\$\{dd}texexpand,%{_bindir}/texexpand,;
	    s,/.*\\\$\{dd}pstoimg,%{_bindir}/pstoimg,;
	    s,/.*\\\$\{dd}*icons,\\\$\{LATEX2HTMLDIR}/icons,;
	    s,/.*\\\$\{dd}rgb.txt,\\\$\{LATEX2HTMLDIR}/styles/rgb.txt,;
	    s,/.*\\\$\{dd}styles\\\$\{dd}crayola.txt,\\\$\{LATEX2HTMLDIR}/styles/crayola.txt," latex2html

make install
rm -rf %{buildroot}%{_datadir}/latex2html/versions/table.pl.orig \
       %{buildroot}%{_datadir}/latex2html/docs/ \
       %{buildroot}%{_datadir}/latex2html/example/
sed -i "s,/usr/local/bin/perl,/usr/bin/perl," %{buildroot}%{_datadir}/latex2html/makeseg/makeseg
sed -i "s,/usr/local/bin/perl,/usr/bin/perl," %{buildroot}%{_datadir}/latex2html/makemap
sed -i "s,###\!.*,," %{buildroot}%{_datadir}/latex2html/makemap
sed -i "s,###\!.*,," %{buildroot}%{_datadir}/latex2html/makeseg/makeseg
sed -i "s,%{buildroot},," %{buildroot}%{_bindir}/pstoimg
sed -i "s,%{buildroot},," %{buildroot}%{_bindir}/texexpand
sed -i "s,%{buildroot},," cfgcache.pm
sed -i "s,$cfg{'srcdir'}.*,$cfg{'srcdir'} = q'%{name}-%{version}';," cfgcache.pm
perl -pi -e "s,$cfg{'GS_LIB'} = q'';,$cfg{'GS_LIB'} = q'%{_datadir}/ghostscript/`ghostscript --version`';," cfgcache.pm
install -m0644 *.pm %{buildroot}%{_datadir}/latex2html
chmod +x %{buildroot}%{_datadir}/latex2html/makeseg/makeseg %{buildroot}%{_datadir}/latex2html/makemap

# install man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -m0644 *.1 %{buildroot}%{_mandir}/man1
popd

# install japanese version
%if %{enable_japanese}
pushd %{name}-%{version}JA
sed -i "s,%{_prefix},%{buildroot}%{_prefix}," cfgcache.pm
perl -pi -e "s,latex2html pstoimg texexpand,jlatex2html jpstoimg jtexexpand," config/install.pl
perl -pi -e "s,/.*\\\$\{dd}texexpand,%{_bindir}/jtexexpand,;
	    s,/.*\\\$\{dd}pstoimg,%{_bindir}/jpstoimg,;
	    s,/.*\\\$\{dd}icons,\\\$\{LATEX2HTMLDIR}/icons,;
	    s,/.*\\\$\{dd}styles\\\$\{dd}rgb.txt,\\\$\{LATEX2HTMLDIR}/styles/rgb.txt,;
	    s,/.*\\\$\{dd}styles\\\$\{dd}crayola.txt,\\\$\{LATEX2HTMLDIR}/styles/crayola.txt," jlatex2html
sed -i "s,%{buildroot},," l2hconf.pm

make install
rm -rf %{buildroot}%{_datadir}/jlatex2html/versions/table.pl.orig \
       %{buildroot}%{_datadir}/jlatex2html/docs/ \
       %{buildroot}%{_datadir}/jlatex2html/example/
sed -i "s,/usr/local/bin/perl,/usr/bin/perl," %{buildroot}%{_datadir}/jlatex2html/makeseg/makeseg
sed -i "s,/usr/local/bin/perl,/usr/bin/perl," %{buildroot}%{_datadir}/jlatex2html/makemap
sed -i "s,###\!.*,," %{buildroot}%{_datadir}/jlatex2html/makemap 
sed -i "s,###\!.*,," %{buildroot}%{_datadir}/jlatex2html/makeseg/makeseg
sed -i "s,%{buildroot},," %{buildroot}%{_bindir}/jpstoimg
sed -i "s,%{buildroot},," %{buildroot}%{_bindir}/jtexexpand
sed -i "s,%{buildroot},," cfgcache.pm
sed -i "s,$cfg{'srcdir'}.*,$cfg{'srcdir'} = q'%{name}-%{version}JA';," cfgcache.pm
perl -pi -e "s,$cfg{'GS_LIB'} = q'';,$cfg{'GS_LIB'} = q'%{_datadir}/ghostscript/`ghostscript --version`';," cfgcache.pm
install -m0644 *.pm %{buildroot}%{_datadir}/jlatex2html
chmod +x %{buildroot}%{_datadir}/jlatex2html/makeseg/makeseg %{buildroot}%{_datadir}/jlatex2html/makemap
popd
%endif

# do not clash with texlive, prefer url.sty from texlive instead
rm -f %{buildroot}%{_datadir}/texmf/tex/latex/html/url.sty

%post
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%postun
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%check
make -C %{name}-%{version} check
%if %{enable_japanese}
make -C %{name}-%{version}JA check
%endif

%files
%doc latex2html-%{version}/{LICENSE,README.md,FAQ,BUGS,docs,example}
%{_bindir}/latex2html
%{_bindir}/pstoimg
%{_bindir}/texexpand
%dir %{_datadir}/latex2html
%{_datadir}/latex2html/*
%dir %{_datadir}/texmf/tex/latex/html
%{_datadir}/texmf/tex/latex/html/*

%if %{enable_japanese}
%{_bindir}/jlatex2html
%{_bindir}/jpstoimg
%{_bindir}/jtexexpand
%dir %{_datadir}/jlatex2html
%{_datadir}/jlatex2html/*
%endif

%{_mandir}/man1/latex2html.*
%{_mandir}/man1/texexpand.*
%{_mandir}/man1/pstoimg.*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2023.2-9
- Import
