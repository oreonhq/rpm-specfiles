%global source0_hash b75e9731e717cec1c261a27d06c4f7baa696cf2fd4e5e3158df5f8fd65107285
%define		mainver		0.996
%define		baserelease	15
%define		srcname		mecab-ruby
Name:		ruby-mecab
Version:	%{mainver}
Release:        15%{?dist}
Summary:        Ruby binding for MeCab
License:	BSD-3-Clause OR LGPL-2.1-or-later OR GPL-2.0-or-later
URL:		http://mecab.sourceforge.net/
Source0:        http://mecab.googlecode.com/files/%{srcname}-%{version}.tar.gz
Requires:	mecab = %{version}
Requires:	ruby
Provides:	ruby(mecab) = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mecab-devel
BuildRequires:  mecab-jumandic
BuildRequires:  ruby
BuildRequires:  ruby-devel
# /oreon:deps
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
%oreon_autofiles main

%check

ruby -I. test.rb
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
