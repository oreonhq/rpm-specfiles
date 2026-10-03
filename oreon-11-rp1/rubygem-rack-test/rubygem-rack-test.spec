%global source0_hash 005a36692c306ac0b4a9350355ee080fd09ddef1148a5f8b2ac636c720f5c463

%global gem_name rack-test

Name: rubygem-%{gem_name}
Version: 2.2.0
Release: %autorelease
Summary: Simple testing API built on Rack
License: MIT
URL: https://github.com/rack/rack-test
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rack/rack-test.git && cd rack-test
# git archive -v -o rack-test-2.2.0-spec.tar.gz v2.2.0 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.2
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-global_expectations)
BuildRequires: rubygem(rack)
BuildArch: noarch

%description
Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries
to build on.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n  %{gem_name}-%{version} -b 1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
( cd .%{gem_instdir}
cp -a %{builddir}/spec spec

ruby -Ispec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
