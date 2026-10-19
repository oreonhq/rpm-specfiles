%global source0_hash 38f331139784362a97f46b56859612ca8e7805e398bfed926473f043f515eaaa
%global	githash	4cf339fa69652faa2d5a4153b94754aa05543731
%global	shorthash	%(c=%{githash}; echo ${c:0:10})
%global	gitdate	Sun Oct 21 23:43:15 2012 +0900
%global	gitdate_num	20121021
%global	gem_name	net-irc
Name:		rubygem-%{gem_name}
Version:	0.0.9
Release:        1%{?dist}
Summary:        Library for implementing IRC server and client
License:	Ruby OR GPL-2.0-only
URL:		https://github.com/cho45/net-irc
Source0:        https://github.com/cho45/%{gem_name}/archive/%{githash}/%{gem_name}-%{shorthash}.tar.gz
Source1:	rubygem-net-irc-GPLv2
Patch0:	net-irc-dup-string-for-force_encoding.patch
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/ping
BuildRequires:  ruby(release)
BuildRequires:  rubygem(ostruct)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(rdoc)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
library for implementing IRC server and client

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#gem unpack %%{SOURCE0}
#%%setup -q -D -T -n  %%{gem_name}-%%{version}
#gem spec %%{SOURCE0} -l --ruby > %%{gem_name}.gemspec

%setup -q -c -T -a 0
cd %{gem_name}-%{githash}
%patch -P0 -p1

# has_rdoc is removed in rubygems4_0
# https://github.com/ruby/ruby/commit/6f18898f4902b2717442f9bef4faa876d58f99de
sed -i Rakefile \
	-e '\@require.*\(shipit\|sshpublisher\)@d' \
	-e '\@Rake::ShipitTask@,\@end@d' \
	-e 's|rake/gempackagetask|rubygems/package_task|' \
	-e 's|rake/rdoctask|rdoc/task|' \
	-e 's|Rake::GemPackageTask|Gem::PackageTask|' \
	-e 's|git|true|' \
	-e '\@has_rdoc@d' \
	%{nil}
rake gem <<EOF

EOF
cd pkg/%{gem_name}-%{version}
sed -i lib/net/irc.rb \
	-e '\@^#!.*$@d' \
	%{nil}

# rspec2 -> rspec3
sed -i spec/net-irc_spec.rb \
	-e 's|be_true|be_truthy|' \
	%{nil}

# ruby 2.7 warning: Thread.exclusive is deprecated, use Thread::Mutex
# ruby 3.0: Thread.exclusive no longer available

gem specification -l --ruby ../%{gem_name}-%{version}.gem > %{gem_name}.gemspec

# From lib/net/irc.rb
%gemspec_add_dep -g ostruct -s ./%{gem_name}.gemspec

%build

cd %{gem_name}-%{githash}/pkg/%{gem_name}-%{version}
gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cd %{gem_name}-%{githash}/pkg/%{gem_name}-%{version}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
install -cpm 644 %{SOURCE1} \
	%{buildroot}%{gem_instdir}/GPLv2
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile AUTHORS.txt \
	spec/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

ping -w3 localhost || exit 0
cd %{gem_name}-%{githash}/pkg/%{gem_name}-%{version}
rspec spec/ 2>&1 | tee test.log
cat test.log | grep -q "27 examples, 2 failures"
%files -f %{oreon_filedir}/main.list
%files -n rubygem-net-irc-doc -f %{oreon_filedir}/rubygem-net-irc-doc.list

%changelog

%autochangelog
