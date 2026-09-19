%global source0_hash eaef1bc2cf4bd774021ab2da761fabe7599c1bea690ac8ccae18e1a0305b2759

%global gem_name spring

Name: rubygem-%{gem_name}
Version: 4.1.1
Release: 7%{?dist}
Summary: Rails application preloader
License: MIT
URL: https://github.com/rails/spring
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/spring.git && cd spring
# git archive -v -o spring-4.1.1-tests.tar.gz v4.1.1 test/
Source1: %{gem_name}-%{version}-tests.tar.gz
# Needed by `spring status`
Requires: %{_bindir}/ps
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.7.0
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(activesupport)
BuildArch: noarch
# OkJson is allowed to be bundled:
# https://fedorahosted.org/fpc/ticket/113
Provides: bundled(okjson) = 43

%description
Spring is a Rails application preloader. It speeds up development by keeping
your application running in the background so you don't need to boot it every
time you run a test, rake task or migration.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

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

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

# Run only unit test now, acceptance tests wants to compile gems extensions
ruby -Ilib -e 'Dir.glob "./test/unit/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/spring
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
