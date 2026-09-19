%global source0_hash b75e9731e717cec1c261a27d06c4f7baa696cf2fd4e5e3158df5f8fd65107285

%define		mainver		0.996
#%%define		betaver		pre3
%define		baserelease	15
%define		srcname		mecab-ruby

Name:		ruby-mecab
Version:	%{mainver}
Release:	%{?betaver:0.}%{baserelease}%{?betaver:.%betaver}%{?dist}
Summary:	Ruby binding for MeCab

# License is the same as MeCab
# SPDX confirmed
License:	BSD-3-Clause OR LGPL-2.1-or-later OR GPL-2.0-or-later
URL:		http://mecab.sourceforge.net/
Source0:	http://mecab.googlecode.com/files/%{srcname}-%{mainver}%{?betaver}.tar.gz

BuildRequires:	make
BuildRequires:	gcc-c++
# This is not release number specific
BuildRequires:	mecab-devel = %{version}
# ruby-devel requires ruby-libs and not require ruby
BuildRequires:	ruby
BuildRequires:	ruby-devel
# %%check
BuildRequires:	mecab-jumandic

Requires:	mecab = %{version}
Requires:	ruby

Provides:	ruby(mecab) = %{version}-%{release}

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}%{?betaver}

%build
ruby extconf.rb
%{__make} %{?_smp_mflags} \
	CXXFLAGS="$RPM_OPT_FLAGS -fPIC"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="%{__install} -c -p" \
	RUBYARCHDIR=${RPM_BUILD_ROOT}%{ruby_vendorarchdir}
 
%check
ruby -I. test.rb

%files
%doc bindings.html
%doc AUTHORS
%license	COPYING
%license	BSD
%license	GPL
%license	LGPL

%{ruby_vendorarchdir}/*MeCab*

%changelog
%autochangelog
