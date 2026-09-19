%global source0_hash 8db618bcb8fb47d370a0ace6fad1760f7dcddbaf617c16944357fa4634af8383

# Generated from mustermann-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mustermann

# Circular dependency with rubygem-sinatra
%{?_with_bootstrap: %global bootstrap 1}

Name: rubygem-%{gem_name}
Version: 3.0.3
Release: 4%{?dist}
Summary: Your personal string matching expert
License: MIT
URL: https://github.com/sinatra/mustermann
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Support and mustermann-contrib routines required by test suite.
# git clone https://github.com/sinatra/mustermann.git && cd mustermann
# git checkout v3.0.3 && tar czvf mustermann-3.0.3-support.tgz support/
Source1: %{gem_name}-%{version}-support.tgz
# tar czvf mustermann-3.0.3-mustermann-contrib.tgz mustermann-contrib/
Source2: %{gem_name}-%{version}-mustermann-contrib.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.6.0
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rspec-its)
%if ! 0%{?bootstrap}
BuildRequires: rubygem(sinatra)
%endif
BuildArch: noarch

%description
A library implementing patterns that behave like regular expressions.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1 -b 2

# Drop ruby2_keywords dependency that is required by Ruby < 2.7.
%gemspec_remove_dep -g ruby2_keywords

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

%if ! 0%{?bootstrap}
# Run the test suite
%check
# We don't ship tool.
sed -i "/^require 'tool\/warning_filter'/ s/^/#/" \
  %{builddir}/support/lib/support/env.rb
# We don't test coverage.
sed -i "/^require 'support\/coverage'/ s/^/#/" \
  %{builddir}/support/lib/support.rb

pushd .%{gem_instdir}
rspec -I%{builddir}/{support,mustermann-contrib}/lib spec
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/bench
%{gem_instdir}/mustermann.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
