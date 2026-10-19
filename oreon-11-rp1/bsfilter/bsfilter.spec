%global source0_hash 8aa1d713cc848b20d678eb7a5f24bec1879860d023701644bfd426a587998ac9
%global	repoid		59804
%global	mainver	1.0.19
%undefine	prever
%global	baserelease	10
Name:		bsfilter
Version:	%{mainver}
Release:        10%{?dist}
Summary:        Bayesian spam filter
License:	GPL-2.0-or-later
URL:		http://sourceforge.jp/projects/bsfilter/
Source0:        http://dl.sourceforge.jp/%{name}/%{repoid}/%{name}-%{version}.tgz
Requires:		ruby(release)
BuildArch:		noarch
# oreon:deps
BuildRequires:  mecab-ipadic
BuildRequires:  ruby(mecab)
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
# /oreon:deps
%description
Bayesian spam filter.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{mainver}%{?prever:.%prever}
sed -i.shebang \
	-e '\@^#!@s|%{_bindir}/env ruby|%{_bindir}/ruby|' \
	bsfilter/bsfilter

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -cpm 0755 bsfilter/bsfilter %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

cd test
ruby ./test.rb || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
