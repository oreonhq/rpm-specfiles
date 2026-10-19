%global source0_hash 91e8643026017e3d0088a6710fb11c4f617477e826ebe4c5fe586aa63147fc92
%global debug_package %{nil}
Name:           tsung
Version:        1.8.0
Release:        8%{?dist}
Summary:        A distributed multi-protocol load testing tool
License:        GPL-2.0-only
URL:            http://tsung.erlang-projects.org/
Source0:        http://tsung.erlang-projects.org/dist/%{name}-%{version}.tar.gz
Requires:       erlang
Requires:       gnuplot
Requires:       perl-Template-Toolkit
# oreon:deps
BuildRequires:  doxygen-latex
BuildRequires:  erlang
BuildRequires:  latexmk
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  python2-devel
BuildRequires:  python2-sphinx
BuildRequires:  texlive-fncychap
BuildRequires:  texlive-framed
BuildRequires:  texlive-threeparttable
BuildRequires:  texlive-titlesec
BuildRequires:  texlive-wrapfig
# /oreon:deps
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
sed -i 's|/usr/bin/env python|/usr/bin/python|' src/tsung-plotter/tsplot.py.in
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
rm -frv %{buildroot}%{_docdir}
rm -frv examples/*.xml.in
sed -i 's|python27|python2|' %{buildroot}%{_bindir}/tsplot
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n tsung-doc -f %{oreon_filedir}/tsung-doc.list

%changelog

%autochangelog
