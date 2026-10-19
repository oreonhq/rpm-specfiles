%global source8_hash 028f99fc12cbd98784b732905d38fd263e74d7dfd1f38cfd36f1169d623b92ab
%global source7_hash 7d0e37d433d02859e3805c2c5524cd6063f81b046373d95c26d9b55225b74961
%global source6_hash 80269a7fa218b2f7bcc2a1ba7ebc3a127149813290a3cf5f61a7a27e16d3e0ed
%global source5_hash a9c730f17e65f84825c6b232f527c5147689150415d2dc0c39663eb09cb78497
%global source4_hash 6379b2115f6e3704e876416e48b81a5518b4362e1d9304cd977e91f889437d0d
%global source3_hash a8b882c269be073fffafc698cb3aa965ddf1c18e3aa19472f6468318a5506faa
%global source2_hash e122d290f94a76bb6d31a10599cf083181fc0cc78064a2e57ad6e7ee23c810b1
%global source1_hash 64a6465dc8fd5f6c2025cd4754416a4df1a4ea6c91b9f852af0441c011f3531a
%global source0_hash f234d86b99354169584b24094470065ff1c8cb388a52c84f1356ddbfe58f7f2f
Name:           cvs2cl
Version:        2.73
Release:        1%{?dist}
Summary:        Generate ChangeLogs from CVS working copies
License:        GPL-2.0-or-later
URL:            http://www.red-bean.com/cvs2cl/
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
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  perl-generators
BuildRequires:  perl-macros
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
