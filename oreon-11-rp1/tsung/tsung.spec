%global source0_hash 91e8643026017e3d0088a6710fb11c4f617477e826ebe4c5fe586aa63147fc92

# Avoid installing arch-independent data into arch-dependent directory
# MUST for Erlang packages.
%global debug_package %{nil}

Name:           tsung
Version:        1.8.0
Release:        8%{?dist}
Summary:        A distributed multi-protocol load testing tool
License:        GPL-2.0-only
URL:            http://tsung.erlang-projects.org/
Source0:        http://tsung.erlang-projects.org/dist/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  erlang
BuildRequires:  perl-generators
# Just for expanding %%{__python3} macro
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
%else
BuildRequires:  python2-devel
BuildRequires:  python2-sphinx
%endif
BuildRequires:  doxygen-latex
BuildRequires:  latexmk
BuildRequires:  texlive-titlesec
BuildRequires:  texlive-framed
BuildRequires:  texlive-threeparttable
BuildRequires:  texlive-wrapfig
BuildRequires:  texlive-fncychap
Requires:       erlang
Requires:       gnuplot
Requires:       perl-Template-Toolkit

%description
tsung is a distributed load testing tool. It is protocol-independent and can 
currently be used to stress and benchmark HTTP, Jabber/XMPP, PostgreSQL, 
MySQL and LDAP servers.

It simulates user behavior using an XML description file, reports many 
measurements in real time (statistics can be customized with transactions, 
and graphics generated using GnuPlot).

For HTTP, it supports 1.0 and 1.1, has a proxy mode to record sessions, 
supports GET and POST methods, Cookies, and Basic WWW-authentication.
 
It also has support for SSL.

%package doc
BuildArch:      noarch
Summary:        Documentation files for tsung

%description doc
Documentation files for tsung

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}

# Fix bogus shebangs.
sed -i 's|/usr/bin/env bash|/bin/bash|' *.sh.in
%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i 's|/usr/bin/env python|/usr/bin/python|' src/tsung-plotter/tsplot.py.in
%else
sed -i 's|/usr/bin/env python|/usr/bin/python|' src/tsung-plotter/tsplot.py.in
%endif
sed -i '/SPHINXBUILD/ s|sphinx-build|sphinx-build-3|' docs/Makefile
sed -i 's|/usr/bin/env perl|/usr/bin/perl|' src/log2tsung.pl.in
# Switch to UTF-8
for file in LISEZMOI
do
    iconv -f ISO-8859-1 -t UTF-8 $file > $file.utf8
    touch -r $file $file.utf8
    mv -f $file.utf8 $file
done

%build
%configure --prefix=/usr
%make_build
cd docs
for target in html dirhtml singlehtml pickle json htmlhelp qthelp devhelp \
              epub latex latexpdf text man texinfo info gettext changes
do
    make $target ||:
done

%install
%make_install

for i in `ls %{buildroot}%{_libdir}/%{name}/bin | grep .pl$ | cut -d"." -f1`
do
  ln -sf ../%{_lib}/%{name}/bin/$i.pl %{buildroot}%{_bindir}/$i
done

# Fix versioned/unversioned docdir
rm -frv %{buildroot}%{_docdir}
rm -frv examples/*.xml.in

# Fix bogus shebang again
%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i 's|python33|python3|' %{buildroot}%{_bindir}/tsplot
%else
sed -i 's|python27|python2|' %{buildroot}%{_bindir}/tsplot
%endif

%files
%doc CHANGELOG.md CONTRIBUTORS COPYING LISEZMOI README.md TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-rrd
%{_bindir}/%{name}_percentile
%{_bindir}/%{name}_stats
%{_bindir}/%{name}-recorder
%{_bindir}/log2%{name}
%{_bindir}/tsplot
%{_datadir}/%{name}
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-recorder.1*
%{_mandir}/man1/tsplot.1*

%files doc
%doc docs examples

%changelog
%autochangelog
