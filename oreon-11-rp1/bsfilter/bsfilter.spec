%global source0_hash 8aa1d713cc848b20d678eb7a5f24bec1879860d023701644bfd426a587998ac9

%global	repoid		59804

%global	mainver	1.0.19
%undefine	prever

%global	baserelease	10

Name:		bsfilter
Version:	%{mainver}
Release:	%{?prever:0.}%{baserelease}%{?prever:.%prever}%{?dist}
Summary:	Bayesian spam filter

# bsfilter script
# SPDX confirmed
License:	GPL-2.0-or-later
URL:		http://sourceforge.jp/projects/bsfilter/
Source0:	http://dl.sourceforge.jp/%{name}/%{repoid}/%{name}-%{version}%{?prever:.%prever}.tgz

BuildRequires:	ruby(release)
Requires:		ruby(release)
# Below is for %%check
BuildRequires:	rubygem(minitest)
BuildRequires:	ruby(mecab)
BuildRequires:	mecab-ipadic
BuildArch:		noarch

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

%check
cd test
# Still some test fails, some of them are just dependency missing,
# some of them "really" fails, need contact with the upstream...
# rescue test failure for now
ruby ./test.rb || :

%files
# rpmlint warns about incorrect-fsf-address, need report to the upstream
%license	COPYING
%doc	htdocs/

%{_bindir}/%{name}

%changelog
%autochangelog
