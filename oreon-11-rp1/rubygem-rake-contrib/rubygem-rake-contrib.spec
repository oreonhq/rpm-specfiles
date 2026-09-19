%global source0_hash f15669c886a01361fb0a1aec4137e72b11168015afea766aa90386cba98b2cca

%global gem_name rake-contrib

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 21%{?dist}
Summary: Additional libraries for Rake
License: MIT
URL: https://github.com/ruby/rake-contrib
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ruby/rake-contrib.git
# HEAD = a587db7f45dc1d24c7c
# cd rake-contrib; tar -czf rake-contrib-tests.tar.gz test
Source1: %{gem_name}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(net-ftp)
BuildRequires: ruby
BuildArch: noarch

%description
Additional libraries for Rake.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}

tar -xzf %{SOURCE1}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rake-contrib.gemspec

%changelog
%autochangelog
