%global source0_hash 89c2125e903edf6f6fe035137eceef79382fce43783e5da240fc4a34b0878934
%define		migemover	0.40
%define		emacsver	21.4
%define		xemacsver	21.4
%define		e_sitedir	%{_datadir}/emacs/site-lisp
%define		xe_sitedir	%{_datadir}/xemacs/site-lisp
%define		rubyabi		1.9.1
Name:		migemo
Version:	%{migemover}
Release:        1%{?dist}
Summary:        Japanese incremental search tool
License:	GPL-2.0-only AND GPL-2.0-or-later
URL:		http://0xcc.net/migemo/
Source0:        http://0xcc.net/migemo/%{name}-%{version}.tar.gz
Patch0:		migemo-ruby-1.9.patch
Patch1:		migemo-0.40-bz830559.patch
BuildArch:	noarch
Requires:	ruby(release)
Requires:	ruby(romkan)
Requires:	ruby(bsearch)
# oreon:deps
BuildRequires:  emacs
BuildRequires:  glibc-langpack-ja
BuildRequires:  make
BuildRequires:  ruby
BuildRequires:  ruby(bsearch)
BuildRequires:  ruby(release)
BuildRequires:  ruby(romkan)
BuildRequires:  ruby-devel
# /oreon:deps
%description
Ruby/Migemo is a tool for Japanese incremental search.

%package	emacs
Summary:	Emacs front-end of Migemo
Requires:	%{name} = %{version}-%{release}
Requires:	emacs(bin) >= %{emacsver}
Requires:	apel
%description	emacs
%{summary}.

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LANG=ja_JP.eucJP
cd tests
for f in *.sh ; do \
	sh ./$f || :
done
%files -f %{oreon_filedir}/main.list
%files -n migemo-emacs -f %{oreon_filedir}/migemo-emacs.list

%changelog

%autochangelog
