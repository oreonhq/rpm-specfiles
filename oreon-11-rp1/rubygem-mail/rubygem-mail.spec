%global source0_hash ec3b9fadcf2b3755c78785cb17bc9a0ca9ee9857108a64b6f5cfc9c0b5bfc9ad

# Generated from mail-2.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mail

Name: rubygem-%{gem_name}
Version: 2.8.1
Release: 7%{?dist}
Summary: Mail provides a nice Ruby DSL for making, sending and reading emails
License: MIT
URL: https://github.com/mikel/mail
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Specs are not shipped with the gem. You can get them like so:
# git clone https://github.com/mikel/mail.git --no-checkout
# cd mail && git archive -v -o mail-2.8.1-specs.txz 2.8.1 spec/
Source1: %{gem_name}-%{version}-specs.txz
BuildRequires: rubygem(net-smtp)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(mini_mime)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
A really Ruby Mail handler.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%gemspec_add_file 'lib/mail/yaml.rb'

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec .

# We don't want benchmarks
sed -i -e '/require..rspec.benchmark/ s/^/#/' \
       -e '/include.RSpec..Benchmark/ s/^/#/' \
  spec/spec_helper.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
