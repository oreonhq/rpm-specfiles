%global source0_hash none

Name:           cvs2cl
Version:        2.73
Release:        34%{?dist}
Summary:        Generate ChangeLogs from CVS working copies

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.red-bean.com/cvs2cl/
# To update the sources:
# spectool -g -f cvs2cl.spec
# md5sum -c sources
# fedpkg upload (all the sources which don't match)
# (remove the old ones from 'sources')
Source0:        http://www.red-bean.com/cvs2cl/cvs2cl.pl
Source1:        http://www.red-bean.com/cvs2cl/changelog.dtd
Source2:        http://www.red-bean.com/cvs2cl/changelog-xml-schema.xdr
Source3:        http://www.red-bean.com/cvs2cl/cl2html.xslt
Source4:        http://www.red-bean.com/cvs2cl/cl2html-ciaglia.xslt
Source5:        http://www.red-bean.com/cvs2cl/filter-cvs2cl.xslt
Source6:        http://www.red-bean.com/cvs2cl/cvs2cl_ruether.xslt
Source7:        http://www.red-bean.com/cvs2cl/cl2html_rss-karaguezian.xslt
Source8:        http://www.red-bean.com/cvs2cl/ChangeLog.xsd
Patch0:         %{name}-2.69-perldeps.patch

BuildArch:      noarch
BuildRequires:  %{_bindir}/pod2man
# HACK: Pull-in perl-filter macros
BuildRequires:  perl-generators
BuildRequires:  perl-macros
Requires:       xml-common

%if 0%{?perl_default_filter_revision} > 2
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(CVS::Utils::ChangeLog::.*\\)
%else
%{?filter_setup:
%filter_from_requires /^perl(CVS::Utils::ChangeLog::.*)/d
%{?perl_default_filter}
}
%endif

%description
cvs2cl generates GNU-style ChangeLogs for a CVS working copy using the
output of the "cvs log" command.  The script originally came from the
open source CVS book at http://cvsbook.red-bean.com/.

%prep
%setup -c -T
sed -e 's/cvs2cl\.pl/cvs2cl/' %{SOURCE0} > cvs2cl
%patch -P0

%build
%{_bindir}/pod2man \
  --section=1 \
  --release=%{version} \
  --center="CVS-log-message-to-ChangeLog conversion script" \
  cvs2cl > cvs2cl.1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xml/cvs2cl,%{_mandir}/man1}
install -p -m 755 cvs2cl $RPM_BUILD_ROOT%{_bindir}/cvs2cl
install -p -m 644 \
  %{SOURCE1} \
  %{SOURCE2} \
  %{SOURCE3} \
  %{SOURCE4} \
  %{SOURCE5} \
  %{SOURCE6} \
  %{SOURCE7} \
  %{SOURCE8} \
  $RPM_BUILD_ROOT%{_datadir}/xml/cvs2cl
install -p -m 644 cvs2cl.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/cvs2cl
%{_datadir}/xml/cvs2cl/
%{_mandir}/man1/cvs2cl.1*

%changelog
%autochangelog
