%global source0_hash 54e6583a00bcb75a5cc681c053dbdca4117f4425d62cea81c8dbafab5096e65a

# Generated from slim-1.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name slim

Name: rubygem-%{gem_name}
Version: 5.1.1
Release: 6%{?dist}
Summary: Slim is a template language
License: MIT
URL: http://github.com/slim-template/slim/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix Rails 7 test compatibility.
Patch0: rubygem-slim-5.1.1-Test-Rails-7.patch
# Minitest 5.19 puts `MiniTest` class behind environment variable.
# https://github.com/slim-template/slim/commit/7c42d101853126ff0ec1c9e7b544bdfb55820817
Patch2: rubygem-slim-5.1.1-Literate-test-Update-name-of-Minitest-module.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(activemodel)
BuildRequires: rubygem(rails-controller-testing)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(kramdown)
BuildRequires: rubygem(temple)
BuildRequires: rubygem(tilt)
BuildArch: noarch

%description
Slim is a template language whose goal is reduce the syntax to the essential
parts without becoming cryptic.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1
%patch 2 -p1

# Relax the Tilt dependency. We have just Tilt 2.0.11 in Fedora while the bump
# does not seem to have any justification.
# https://github.com/slim-template/slim/commit/a9db8474696752590b1c5d182dc67383d5a74813
%gemspec_remove_dep -g tilt '>= 2.1.0'
%gemspec_add_dep -g tilt '>= 2.0.6'

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
ruby -Ilib:test/core -rostruct -e 'Dir.glob "./test/core/**/test_*.rb", &method(:require)'
ruby -Ilib:test/literate test/literate/run.rb
ruby -Ilib:test/core -e 'Dir.glob "./test/logic_less/**/test_*.rb", &method(:require)'
ruby -Ilib:test/core -e 'Dir.glob "./test/translator/**/test_*.rb", &method(:require)'
ruby -Ilib:test/core -e 'Dir.glob "./test/smart/**/test_*.rb", &method(:require)'
ruby -Ilib:test/core -e 'Dir.glob "./test/include/**/test_*.rb", &method(:require)'
ruby -Ilib -e 'Dir.glob "./test/rails/**/test_*.rb", &method(:require)'
ruby -Ilib -e 'Dir.glob "./test/sinatra/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/slimrb
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%{gem_instdir}/Gemfile
%lang(ja) %doc %{gem_instdir}/README.jp.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%dir %{gem_instdir}/doc
%doc %{gem_instdir}/doc/*.md
%lang(ja) %doc %{gem_instdir}/doc/jp
%{gem_instdir}/slim.gemspec
%{gem_instdir}/test

%changelog
%autochangelog
