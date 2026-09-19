%global source0_hash 33e76b7639d0181a46eaf1136b05f0e9043dfc5fc4b1a7b9fd8ae8bd437dd5e4

# Initially Generated from mechanize-0.8.5.gem by gem2rpm -*- rpm-spec -*-

%global	majorver		2.14.0
%undefine	preminorver	
%global	rpmminorver		.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver		%{majorver}%{?preminorver}

%global	baserelease		5

%global	gem_name		mechanize

%global	gem_instdir()	%{gem_dir}/gems/%{gem_name}-%{version}%{?preminorver}

Summary:	A handy web browsing ruby object
Name:		rubygem-%{gem_name}
Version:	%{majorver}
Release:	%{?preminorver:0.}%{baserelease}%{?preminorver:%{rpmminorver}}%{?dist}
# SPDX confirmed
License:	MIT
URL:		https://github.com/sparklemotion/mechanize
Source0:	https://rubygems.org/gems/%{gem_name}-%{fullver}.gem
# Kill ntlm-http support
# https://github.com/sparklemotion/mechanize/issues/282
Patch0:	rubygem-mechanize-2.8.0-disable-ntlm-http.patch
Patch1:	rubygem-mechanize-2.6.0-disable-ntlm-http-test.patch

BuildRequires:	ruby(release)
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
# For %%check
BuildRequires:	rubygem(addressable)
BuildRequires:	rubygem(domain_name)
BuildRequires:	rubygem(http-cookie)
BuildRequires:	rubygem(mime-types)
BuildRequires:	rubygem(net-http-digest_auth)
BuildRequires:	rubygem(net-http-persistent)
BuildRequires:	rubygem(nkf)
BuildRequires:	rubygem(nokogiri)
#BuildRequires:	rubygem(ntlm-http)
BuildRequires:	rubygem(webrobots)
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(webrick)
# For test suite for Japanese locale
BuildRequires:	glibc-all-langpacks

Requires:	ruby(release)
Requires:	ruby(rubygems)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
#Requires:	rubygem(hoe)

# For non-gem support, net-http-persistent (which this package depends on)
# must also create non-gem package. Let's kill it (at least for F-15)
Obsoletes:	ruby-%{gem_name} < 1.0.0-999

BuildArch:	noarch

%description
The Mechanize library is used for automating interaction with websites. 
Mechanize automatically stores and sends cookies, follows redirects, 
can follow links, and submit forms. Form fields can be populated and 
submitted. Mechanize also keeps track of the sites that you have 
visited as a history.

%package	doc
Summary:	Documentation for %{name}
# Directory ownership issue
Requires:	%{name} = %{version}-%{release}
Requires:	ruby(rubygems)

%description	doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

# Patches
%patch -P0 -p1 -b .ntlm
%patch -P1 -p1 -b .ntlmtest

sed -i -e '\@ntlm-http@d' %{gem_name}-%{version}.gemspec
# Kill also this for now
sed -i -e '\@rubyntlm@d' %{gem_name}-%{version}.gemspec
# Remove runtime dependency currently in ruby main lib
sed -i -e '\@nkf@d' %{gem_name}-%{version}.gemspec
sed -i -e '\@base64@d' %{gem_name}-%{version}.gemspec

# 2.12.0
# Skip brotli related test
sed -i test/test_mechanize_http_agent.rb \
	-e '\@def.*encoding_brotli@s|$| ;skip|' \
	-e '\@require.*brotli@s|require|#require|' \
	%{nil}
# 2.12.1
# skip zstd-ruby related test
sed -i test/test_mechanize_http_agent.rb \
	-e '\@def.*encoding_zstd@s|$| ;skip|' \
	-e '\@require.*zstd-ruby@s|require|#require|' \
	%{nil}

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}

# Clean up
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest \
	.gemtest \
	.gitignore \
	.github/ \
	.travis.yml \
	.yardopts \
	Gemfile \
	Rakefile \
	*.gemspec \
	test/ \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}

%check
# Explicitly use UTF-8
LANG=C.utf8
LC_ALL=C.utf8

pushd ./%{gem_instdir}

# http://pkgs.fedoraproject.org/cgit/openssl.git/tree/openssl-1.0.1e-no-md5-verify.patch
# TODO: need "correct" solution
export OPENSSL_ENABLE_MD5_VERIFY=yes

# Workaround. "rake test" invokes test with "ruby -w", i.e. "ruby -W2"
export RUBYLIB=$(pwd)/lib:$(pwd)
ruby -e 'Dir.glob("test/**/test*.rb").each {|f| require f}' || \
	ruby -W2 -e 'Dir.glob("test/**/test*.rb").each {|f| require f}'
popd

%files
%doc	%{gem_instdir}/[A-Z]*.rdoc
%doc	%{gem_instdir}/[A-Z]*.md
%license	%{gem_instdir}/LICENSE.txt
%dir	%{gem_instdir}
%{gem_libdir}/
%{gem_spec}

%files	doc
%{gem_dir}/doc/%{gem_name}-%{fullver}/
%{gem_instdir}/examples/

%changelog
%autochangelog
