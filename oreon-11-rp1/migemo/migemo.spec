%global source0_hash 89c2125e903edf6f6fe035137eceef79382fce43783e5da240fc4a34b0878934

%define		migemover	0.40

%define		emacsver	21.4
%define		xemacsver	21.4
%define		e_sitedir	%{_datadir}/emacs/site-lisp
%define		xe_sitedir	%{_datadir}/xemacs/site-lisp
%define		rubyabi		1.9.1

Name:		migemo
Version:	%{migemover}
Release:	47%{?dist}
Summary:	Japanese incremental search tool

# migemo-dict	GPL-2.0-or-later
# migemo.el.in	GPL-2.0-or-later
# Otherwise	GPL-2.0-only
# SPDX confirmed
License:	GPL-2.0-only AND GPL-2.0-or-later
URL:		http://0xcc.net/migemo/
Source0:	http://0xcc.net/migemo/%{name}-%{version}.tar.gz
# patch taken and modified from http://d.hatena.ne.jp/yshl/20090814/1250197679
Patch0:		migemo-ruby-1.9.patch
# See bug 830559
Patch1:		migemo-0.40-bz830559.patch

BuildArch:	noarch

BuildRequires:  make
BuildRequires:  glibc-langpack-ja
Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	ruby
BuildRequires:	ruby-devel

BuildRequires:	ruby(romkan)
BuildRequires:	ruby(bsearch)
BuildRequires:	emacs >= %{emacsver}
%if 0%{?fedora} < 36
BuildRequires:	xemacs >= %{xemacsver}
%endif
Requires:	ruby(romkan)
Requires:	ruby(bsearch)

%if 0%{?fedora} >= 36
Obsoletes:	%{name}-xemacs < 0.40-36
%endif

%description
Ruby/Migemo is a tool for Japanese incremental search.

%package	emacs
Summary:	Emacs front-end of Migemo
Requires:	%{name} = %{version}-%{release}
Requires:	emacs(bin) >= %{emacsver}
Requires:	apel

%description	emacs
%{summary}.

%if 0%{?fedora} < 36
%package	xemacs
Summary:	XEmacs front-end of Migemo
Requires:	%{name} = %{version}-%{release}
Requires:	xemacs(bin) >= %{emacsver}
Requires:	apel

%description	xemacs
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
sed -i '18d' migemo-convert.rb # patching is failing probably because of the special chars, so do this by sed
%patch -P1 -p1

%build
%configure \
	--with-rubydir=%{ruby_vendorlibdir}
%{__make} %{?_smp_mflags} migemo.elc

%install
%{__rm} -rf $RPM_BUILD_ROOT
export LANG=ja_JP.eucJP
%{__make} INSTALL="%{__install} -c -p" DESTDIR=$RPM_BUILD_ROOT install

%if 0%{?fedora} < 36
# For xemacs
%{__rm} -f migemo.elc
%configure \
	--with-rubydir=%{ruby_sitelib} \
	--with-emacs=xemacs \
	--with-lispdir=%{xe_sitedir}
%{__make} INSTALL="%{__install} -c -p" DESTDIR=%{buildroot} install-lispLISP
%endif

%check
export LANG=ja_JP.eucJP
cd tests
for f in *.sh ; do \
	sh ./$f || :
done

%files
%defattr(-,root,root,-)
%doc AUTHORS
%doc ChangeLog
%license COPYING
%doc README

%{_bindir}/migemo*
%{_datadir}/migemo/
%{ruby_vendorlibdir}/migemo*

%files	emacs
%defattr(-,root,root,-)
%{e_sitedir}/migemo.el*

%if 0%{?fedora} < 36
%files	xemacs
%defattr(-,root,root,-)
%{xe_sitedir}/migemo.el*
%endif

%changelog
%autochangelog
