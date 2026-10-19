%global source0_hash 54e6583a00bcb75a5cc681c053dbdca4117f4425d62cea81c8dbafab5096e65a
%global gem_name slim
Name: rubygem-%{gem_name}
Version: 5.1.1
Release:        6%{?dist}
Summary:        Slim is a template language
License: MIT
URL: http://github.com/slim-template/slim/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-slim-5.1.1-Test-Rails-7.patch
Patch2: rubygem-slim-5.1.1-Literate-test-Update-name-of-Minitest-module.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activemodel)
BuildRequires:  rubygem(kramdown)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rails-controller-testing)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygem(sinatra)
BuildRequires:  rubygem(temple)
BuildRequires:  rubygem(tilt)
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n rubygem-slim-doc -f %{oreon_filedir}/rubygem-slim-doc.list

%changelog

%autochangelog
