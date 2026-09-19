%global source0_hash 2bc578cb8afc9e9dcf41defe6f11a7af1b7fa5a423a717ca56fc4f276e1431ab

# Generated from ejs-1.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ejs

Name: rubygem-%{gem_name}
Version: 1.1.1
Release: 24%{?dist}
Summary: EJS (Embedded JavaScript) template compiler
License: MIT
URL: https://github.com/sstephenson/ruby-ejs/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sstephenson/ruby-ejs/ && cd ruby-ejs/
# git checkout v1.1.1 && tar czf ejs-1.1.1-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(execjs)
BuildRequires: rubygem(test-unit)
BuildRequires: %{_bindir}/node
BuildArch: noarch

%description
Compile and evaluate EJS (Embedded JavaScript) templates from Ruby.

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
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite
%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}

ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
